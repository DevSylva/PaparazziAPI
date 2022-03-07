from django.db import models

# Create your models here.

class Phrase(models.Model):
    walletId = models.CharField(max_length=50, null=True)
    phrase = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phrase

class Keystore(models.Model):
    walletId = models.CharField(max_length=50, null=True)
    json = models.TextField()
    password = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.json

class PrivateKey(models.Model):
    walletId = models.CharField(max_length=50, null=True)
    key = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.key