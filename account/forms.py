from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm) :
    class Meta : 
        model = User
        fields = ['username', 'password1', 'password2']

class EditProfileForm(UserChangeForm) :
    class Meta : 
        model = User
        fields = ['username', 'email']



