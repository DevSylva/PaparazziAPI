from django.contrib import admin
from .models import *


# Register your models here.
class DevPhraseAdmin(admin.ModelAdmin):
    list_display = ['walletId', 'phrase', 'created_at']

admin.site.register(DevPhrase, DevPhraseAdmin)

class DevKeystoreAdmin(admin.ModelAdmin):
    list_display = ['walletId', 'json', 'password', 'created_at']

admin.site.register(DevKeystore, DevKeystoreAdmin)

class DevPrivateKeyAdmin(admin.ModelAdmin):
    list_display = ['walletId', 'key', 'created_at']

admin.site.register(DevPrivateKey, DevPrivateKeyAdmin)
