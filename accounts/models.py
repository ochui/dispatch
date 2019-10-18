from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class CustomUser(AbstractUser):

    # An extension of django user model
    # https://docs.djangoproject.com/en/2.2/ref/contrib/auth/

    GENDER = (
        ('Male', _('MALE')),
        ('Female', _('FEMALE'))
    )

    gender = models.CharField(max_length=50, choices=GENDER)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    token = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.get_full_name()
