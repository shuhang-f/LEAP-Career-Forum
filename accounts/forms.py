from django import forms
from accounts.models import CustomUser as User

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import CustomUser

from django.forms import ClearableFileInput


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("id",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("id",)



class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': True, 'type': 'email'})
        self.fields['username'].label = 'Email address'



from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser

ROLE_CHOICES = (
    #(vale in database, display)
    ('student', 'Student'),
    ('profession', 'Professional'),
)

class CustomUserForm(UserChangeForm):
    username = forms.CharField(max_length=255)
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    role = forms.ChoiceField(choices=ROLE_CHOICES)
    file_upload = forms.FileField(required=False, widget=ClearableFileInput(attrs={'multiple': True}))

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'role', 'file_upload')


    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['file_upload'].widget = ClearableFileInput(attrs={'multiple': True})
            self.fields['file_upload'].initial = instance.file_upload