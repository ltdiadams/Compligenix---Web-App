from django import forms
from phone_field import PhoneField
from main.models import Todo

class Post(forms.ModelForm):
    # phone = PhoneField()
    class Meta:
        model=Todo
        fields = ('content',)