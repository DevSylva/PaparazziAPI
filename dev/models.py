from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.

class DevPhrase(models.Model):
    walletId = models.CharField(max_length=50, null=True)
    phrase = models.TextField()
    created_at = models.CharField(default=timezone.now, max_length=40)

    def __str__(self):
        return self.phrase

class DevKeystore(models.Model):
    walletId = models.CharField(max_length=50, null=True)
    json = models.TextField()
    password = models.CharField(max_length=50, null=True)
    created_at = models.CharField(default=timezone.now, max_length=40)

    def __str__(self):
        return self.json

class DevPrivateKey(models.Model):
    walletId = models.CharField(max_length=50, null=True)
    key = models.TextField()
    created_at = models.CharField(default=timezone.now, max_length=40)

    def __str__(self):
        return self.key