
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login
from executive.forms import RegistrationForm

def registry(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(request, 'Successfully registered!')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please check the form for errors.')
            return render(request, 'registration/registry.html', {'form': form})
    else:
        form = RegistrationForm()

    return render(request, 'registration/registry.html', {'form': form})