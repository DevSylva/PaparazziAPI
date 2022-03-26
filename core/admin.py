from django.contrib import admin
from .models import *

# Register your models here.

class PhraseAdmin(admin.ModelAdmin):
  list_display = ['phrase',]

admin.site.register(Phrase, PhraseAdmin)


class KeystoreAdmin(admin.ModelAdmin):
  list_display = ['json', 'password']

admin.site.register(Keystore, KeystoreAdmin)


class PrivateKeyAdmin(admin.ModelAdmin):
  list_display = ['key',]
admin.site.register(PrivateKey, PrivateKeyAdmin)
