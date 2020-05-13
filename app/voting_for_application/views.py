from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .decorators import sensors_only
from .forms import VotingForm, ConfirmingForm, RefusingForm
from application_for_participation.models import Application, SceneSlot
from django.contrib import messages


@sensors_only
@login_required
def voting_list(request):
    applications = Application.objects.all()
    apps = applications.count()
    pending = applications.filter(applications_condition='PD')
    voted = applications.exclude(applications_condition='PD')
    applications = {'pending': pending, 'voted': voted}

    context = {'applications': applications, 'apps': apps}
    return render(request, 'voting_for_application/voting_view_list.html', context)


@sensors_only
@login_required
def voting_detail(request, user):
    application = Application.objects.filter(user__username=user).first()
    form = VotingForm()

    if request.method == 'POST':
        form = VotingForm(request.POST)
        if form.is_valid():
            if application.voted_sensors is None:
                application.voted_sensors = [request.user.username]
                application.rating += int(form.cleaned_data['decision'])
                application.save()
                messages.success(request, 'Ваш голос учтен')
                return redirect('voting_for_application:voting_list')
            elif request.user.username not in application.voted_sensors:
                application.voted_sensors.append(request.user.username)
                application.rating += int(form.cleaned_data['decision'])
                application.save()
                messages.success(request, 'Ваш голос учтен')
                return redirect('voting_for_application:voting_list')
            else:
                messages.warning(request, 'Вы уже оценили эту заявку')
                return redirect('voting_for_application:voting_list')
    context = {'application': application, 'form': form, 'verdict_form': None}
    if application.can_be_voted() and application.applications_condition == 'PD':
        if application.rating >= 3:
            verdict_form = ConfirmingForm()
            if request.method == 'POST':
                form = ConfirmingForm(request.POST)
                if form.is_valid():
                    application.applications_condition = 'CF'
                    application.desired_scene_and_time_slot = form.cleaned_data['scene_slot']
                    application.save()
                    messages.info(request, 'Вы одобрили участвие пользователю ' + application.user.username)
                    return redirect('voting_for_application:voting_list')
        else:
            verdict_form = RefusingForm()
            if request.method == 'POST':
                form = RefusingForm(request.POST)
                if form.is_valid():
                    application.applications_condition = 'RF'
                    application.save()
                    messages.info(request, 'Вы отказали ' + application.user.username + ' в участвии.')
                    return redirect('voting_for_application:voting_list')
        context = {'application': application, 'form': form, 'verdict_form': verdict_form}

    if application.applications_condition != 'PD':
        return redirect('voting_for_application:voting_list')

    return render(request, 'voting_for_application/voting_view_detail.html', context)
