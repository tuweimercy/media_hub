from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, PasswordResetForm

from .models import User
# registration form
class UserRegistrationForm(UserCreationForm):
    # customizing our inputs for registration form
    email = forms.EmailField(required=True,
    widget =forms.EmailInput(attrs={'class' : 'form-control',
    'placeholder' : 'Email'}))
    user_type = forms.ChoiceField(choices=User.USER_TYPE_ROLES,
    widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('username','email','user_type', 'password1',
                  'password2')
        widgets = {
            'username' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Username'
            })
        }# here customizing our input fields if not overriden
        #meta
        # password matching check
        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['password1'].widget.attrs.update(
                {
                    'class':'form-control',
                    'placeholder' : 'password'
                }
            )
            self.fields['password2'].widget.attrs.update(
                {
                    'class':'form-control',
                    'placeholder' : 'Confirm password'
                }
            )


# override for user authentication form
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'username'
        }
    )) 
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control',
            'placeholder':'password'

        }
    ))   
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','bio','profile_image')
        widget ={
            'username':forms.TextInput(attrs={
                'class':'form-control'
            }),
             'email':forms.TextInput(attrs={
                'class':'form-control'
            }),
             'bio':forms.TextInput(attrs={
                'class':'form-control'
            }),
        }            