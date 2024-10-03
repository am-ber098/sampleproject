
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'age', 'weight', 'psychological_condition']
        widgets = {
            'psychological_condition':  forms.Select(),
        }
