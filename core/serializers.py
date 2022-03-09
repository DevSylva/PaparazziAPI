from rest_framework import serializers
from .models import *

class PhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phrase
        fields = '__all__'


class KeystoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keystore
        fields = '__all__'


class PrivateKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateKey
        fields = '__all__'