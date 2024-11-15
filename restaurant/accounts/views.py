from django.shortcuts import render, redirect
from .forms import RegistrationForm, ProfileForm
from django.views import View
from django.contrib.auth import login, authenticate
from django.contrib import messages



class Register(View):
    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            messages.success(request, _("რეგისტრაცია წარმატებულია!"))
            # return redirect('accounts:profile')
        else:
            messages.error(request, form.errors)
        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})


    def get(self, request):
        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})

