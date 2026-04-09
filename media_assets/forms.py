from django import forms
from .models import MediaAssets

class MediaAssetsForm(forms.ModelForm):
    '''define our form fields for the media upload'''
    class Meta:
        model= MediaAssets
        fields = ('title','description','category','media_file','is_public')
        widget = {
            'title' : forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class':'form-control',
                'rows': 3
            }),
            'category': forms.Select(attrs={
                'class':'form-control'
            }),
            'is_public': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }