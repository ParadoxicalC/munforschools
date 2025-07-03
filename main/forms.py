from django import forms
from .models import Signup, ResourceLink

class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ['name', 'email', 'school']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input input-bordered w-full'}),
            'email': forms.EmailInput(attrs={'class': 'input input-bordered w-full'}),
            'school': forms.TextInput(attrs={'class': 'input input-bordered w-full'}),
        }

class ResourceLinkForm(forms.ModelForm):
    class Meta:
        model = ResourceLink
        fields = ['title', 'url', 'description', 'pdf']
