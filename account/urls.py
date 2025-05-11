from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    CustomLoginView, 
    RegisterUserView, 
    CustomLogoutView, 
    EditProfileView, 
    ChangePasswordView
)
from django.views.generic import TemplateView


app_name = 'account'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path("profil/", EditProfileView.as_view(), name='edit_profile'),
    path('c/', ChangePasswordView.as_view(template_name = 'account/change_password.html'), name='change_password'),
]
