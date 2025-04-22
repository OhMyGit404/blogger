from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now log in, {username}.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'Users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'Users/profile.html')





































