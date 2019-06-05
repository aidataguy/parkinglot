from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

class User(AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    username = models.CharField(_('username'),max_length=20, default=True)


class Parking(models.Model):
    address = models.TextField()
    availability = models.BooleanField()
    address_lang = models.CharField(max_length=255)
    address_long = models.CharField(max_length=255)
    reserved = models.BooleanField()
    booked_by = models.OneToOneField(to=User, on_delete=None, default=None)
  
