
from .forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from django.views import View

class RegisterView(View):
    def get(self, request):
        return render(request, 'registration/signup.html', { 'register_form': RegistrationForm() })
    
    def post(self, request):
        context = {}
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            context['message'] = 'Registration Successful'
            
            # return redirect(reverse('login'))
        context['register_form'] = form
        return render(request, 'registration/signup.html', context)
