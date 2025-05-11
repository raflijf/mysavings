from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView
from django.views.generic.edit import FormView
from .forms import CustomUserCreationForm, EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from django.contrib import messages

class RedirectAuthenticatedUserMixin : 
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated : 
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)
    

class CustomLoginView(RedirectAuthenticatedUserMixin, LoginView) :
    template_name = 'account/login.html'
    next_page = '/'


class CustomLogoutView(LogoutView) :
    success_url = 'account/login/'


class RegisterUserView(RedirectAuthenticatedUserMixin, CreateView) :
    form_class = CustomUserCreationForm
    template_name = 'account/register.html'

    def get_success_url(self):
        self.success_url = reverse_lazy('account:login')
        return super().get_success_url()
    

class EditProfileView(UpdateView) :
    form_class = EditProfileForm
    template_name = 'account/profile.html'
    success_url = reverse_lazy('main:home')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Profil berhasil di perbarui')
        return super().form_valid(form)
    

class ChangePasswordView(LoginRequiredMixin, FormView):
    form_class = PasswordChangeForm
    template_name = 'account/change_password.html'
    success_url = reverse_lazy('account:login')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  
        return kwargs

    def form_valid(self, form):
        form.save()
        print('pacak')
        return super().form_valid(form)
    











