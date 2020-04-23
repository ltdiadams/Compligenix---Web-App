# from django.db import models
# from phone_field import PhoneField
# from django.contrib.auth.models import User


# class Post(models.Model):
#     phone = PhoneField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE,)

# class Post(models.Model):
#     content = models.TextField()

from django.db import models
import re
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# def phone_regex(val):
#     reg = re.compile('^\+?1?\d{9,15}$')
#     if not reg.match(val):
#         raise ValidationError('Phone number must be entered in the format: +999999999. Up to 15 digits allowed.')

# Create your models here.
class Phone(models.Model):
    phone_regex = RegexValidator(
        regex= r'^\+?1?\d{9,15}$',
        message= ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."),
        code='invalid_regex',
    )
    content = models.CharField(max_length=17, validators=[phone_regex], blank=False) # validators should be a list
    # content = models.TextField()