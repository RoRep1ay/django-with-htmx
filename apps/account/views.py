from django import forms
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import password_validators_help_text_html
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from apps.common.forms.input import CustomTextInput, CustomPasswordInput

class SignupForm(UserCreationForm):
    password1= forms.CharField(
        label='Password',
        widget=CustomPasswordInput(attrs={'placeholder': 'Password',}),
        help_text=password_validators_help_text_html(),
    )
    password2= forms.CharField(
        label='Confirm Password',
        widget=CustomPasswordInput(attrs={'placeholder': 'Confirm Password'}),
        help_text='Enter the same password as before, for verification.',
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': CustomTextInput(attrs={'placeholder': 'Username'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super().save(commit=False)
        print('commit =', commit)
        if commit:
            user.save()
                    # Log in the user after signing up
        if self.request:
            user = authenticate(username=user.username, password=self.cleaned_data['password1'])
            if user is not None:
                login(self.request, user)

        return user


class SignUpView(generic.CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('todos:home')  # Redirect to login page after successful signup
    template_name = 'registration/signup.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
