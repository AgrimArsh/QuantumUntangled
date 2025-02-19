from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .decorators import login_required_message_and_redirect

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, you can now log in with your new account!')
            return redirect('users-login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required_message_and_redirect
def profile(request):
    return render(request, 'users/profile.html')