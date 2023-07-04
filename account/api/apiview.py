from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.parsers import MultiPartParser
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

class Register(APIView):
    serializer_class = AccountSerializer
    parser_classes = (MultiPartParser ,)
    def post(self , request):
        data = request.data
        serializer = AccountSerializer(data=data)
        if serializer.is_valid():
            username = data['username']
            password = data['password']
            User.objects.get_or_create(username=username , password=password)
            user = User.objects.get(username=username)
            Token.objects.get_or_create(user=user)
            serializer.save()
            return Response({'Response' : 'add'} , status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class LoginApiView(APIView):
    serializer_class = AccountSerializer 
    parser_classes = (MultiPartParser ,)
    def post(self, request):
        data = request.data
        serializer = AccountSerializer(data=data)
        if serializer.is_valid():
            username = data['username']
            password = data['password']
            user = User.objects.get(username=username)
            if user is not None:
                return Response(data={
                    'Token': str(Token.objects.get(user=user)),
                })
            return Response(data={
                'otp_error': 'otp is wrong'
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)