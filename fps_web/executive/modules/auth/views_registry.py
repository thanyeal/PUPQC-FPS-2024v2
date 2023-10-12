
from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import login
from executive.forms import CustomRegistrationForm

class RegistryView(View):
    def get(self, request):
        form = CustomRegistrationForm()
        return render(request, 'registration/registry.html', {'form': form})

    def post(self, request):
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(request, 'Successfully registered!')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please check the form for errors.')
            return render(request, 'registration/registry.html', {'form': form})
