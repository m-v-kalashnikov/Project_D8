from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AccountForm
from .models import Account


@login_required
def account_view(request):
    account = Account.objects.filter(user=request.user).first()
    form = AccountForm()
    if account is None:
        if request.method == 'POST':
            form = AccountForm(request.POST)
            if form.is_valid():
                account = Account(user=request.user,
                                  name=form.cleaned_data['name'],
                                  musician_or_sensor=form.cleaned_data['musician_or_sensor']
                                  )
                account.save()
                return redirect('account_creation:account_profile')
        context = {'form': form}
        return render(request, 'account_creation/account_view_form.html', context)
    else:
        context = {'account': account}
        return render(request, 'account_creation/account_view.html', context)
