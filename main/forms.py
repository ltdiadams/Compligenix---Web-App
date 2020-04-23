from django import forms
from phone_field import PhoneField
from main.models import Phone

class Post(forms.ModelForm):
    # phone = PhoneField()
    class Meta:
        model=Phone
        fields = ('content',)