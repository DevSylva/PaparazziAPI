from django.contrib import admin
from .models import *

# Register your models here.

class PhraseAdmin(admin.ModelAdmin):
  list_display = ['walletId', 'phrase', 'created_at']

admin.site.register(Phrase, PhraseAdmin)


class KeystoreAdmin(admin.ModelAdmin):
  list_display = ['walletId', 'json', 'password', 'created_at']

admin.site.register(Keystore, KeystoreAdmin)


class PrivateKeyAdmin(admin.ModelAdmin):
  list_display = ['walletId', 'key', 'created_at']

admin.site.register(PrivateKey, PrivateKeyAdmin)
