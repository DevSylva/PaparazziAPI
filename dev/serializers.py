from rest_framework import serializers
from .models import *

class DevPhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevPhrase
        fields = '__all__'


class DevKeystoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevKeystore
        fields = '__all__'


class DevPrivateKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = DevPrivateKey
        fields = '__all__'