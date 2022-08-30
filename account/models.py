from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'

class SessionCbio(models.Model):
    servername = models.CharField(max_length=120)
    serverIP = models.CharField(max_length=60)
    serverUsername = models.CharField(max_length=60)
    password = models.CharField(max_length=120)

    def __str__(self):
        return f'{self.servername}'

class SessionMyriad(models.Model):
    servername = models.CharField(max_length=120)
    serverIP = models.CharField(max_length=60)
    serverUsername = models.CharField(max_length=60)
    password = models.CharField(max_length=120)

    def __str__(self):
        return f'{self.servername}'

class SessionSmsc(models.Model):
    servername = models.CharField(max_length=120)
    serverIP = models.CharField(max_length=60)
    serverUsername = models.CharField(max_length=60)
    password = models.CharField(max_length=120)

    def __str__(self):
        return f'{self.servername}'