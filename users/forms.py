
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta():
        model = User
        # fields = '__all__'
        # fields = ('username', 'email', 'password1', 'password2', 'bio', 'profile_pic', 'first_name', 'last_name')
        fields = ('username','email', 'password1', 'password2', )