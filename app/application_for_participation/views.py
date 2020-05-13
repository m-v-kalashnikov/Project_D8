from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .decorators import musician_only
from .forms import ApplicationForm
from .models import Application


@musician_only
@login_required
def application_view(request):
    application = Application.objects.filter(user=request.user).first()
    form = ApplicationForm()
    if application is None:
        if request.method == 'POST':
            form = ApplicationForm(request.POST)
            if form.is_valid():
                application = Application(user=request.user,
                                          name=form.cleaned_data['name'],
                                          text=form.cleaned_data['text'],
                                          presentation_format=form.cleaned_data['presentation_format'],
                                          desired_scene_and_time_slot=form.cleaned_data['desired_scene_and_time_slot'],
                                          comment=form.cleaned_data['comment'],
                                          applications_condition='PD'
                                          )
                application.save()
                return redirect('application_for_participation:application')
        context = {'form': form}
        return render(request, 'application_for_participation/application_view_form.html', context)
    else:
        context = {'application': application}
        return render(request, 'application_for_participation/application_view.html', context)
