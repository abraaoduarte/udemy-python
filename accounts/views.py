from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, EditAccountForm

def register(request):
    template_name = 'accounts/register.html'

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username,
                password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('core:home')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }

    return render(request, template_name, context)

@login_required
def dashboard(request):
    template_name='accounts/dashboard.html'
    return render(request, template_name)

@login_required
def edit(request):
    template_name='accounts/edit.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user)
            context['success'] = True
    else:
        form = EditAccountForm(instance=request.user)
    context['form'] = form

    return render(request, template_name, context)