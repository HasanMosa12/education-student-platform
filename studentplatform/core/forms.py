from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupStudent(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class SignupParent(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
