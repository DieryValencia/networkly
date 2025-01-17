from django.db import models
from django.contrib.auth.models import User  ###

##
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experiencia_profesional = models.TextField(blank=True, null=True)
    estudios = models.TextField(blank=True, null=True)
    hobbies = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
##
# Create your models here.
