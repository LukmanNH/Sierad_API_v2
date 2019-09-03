# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from .models import SieradProduce, User, Kandang, Lantai, SieradProduce_MI
from rest_framework.response import Response
from .serializers import (
    SieradSerializers,
    UserLoginSerializers, 
    UserRegisterSerializers, 
    UserViewSerializers,
    KandangSerializers,
    LantaiSerializers,
    SieradSerializers_MI

) 
from rest_framework.permissions import AllowAny
# from rest_framework.decorators import action
# from django.contrib.auth import get_user_model
from rest_framework.views import APIView

from rest_framework.generics import CreateAPIView

class SieradViewSet_MI(viewsets.ModelViewSet):
    queryset = SieradProduce_MI.objects.all()
    serializer_class = SieradSerializers_MI

    permission_classes = (AllowAny, )

class KandangViewSet(viewsets.ModelViewSet):
    queryset = Kandang.objects.all()
    serializer_class = KandangSerializers

    permission_classes = (AllowAny, )


class LantaiViewSet(viewsets.ModelViewSet):
    queryset = Lantai.objects.all()
    serializer_class = LantaiSerializers

    permission_classes = (AllowAny, )


class SieradViewSet(viewsets.ModelViewSet):
    queryset = SieradProduce.objects.all()
    serializer_class = SieradSerializers

    permission_classes = (AllowAny, )


class UserRegisterViewSet(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializers
    permission_classes = (AllowAny, )

    def post(self, req, *args, **kwargs):
        data = req.data
        serializer = UserRegisterSerializers(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            success_message = ({
                'code': 201,
                'Message': 'Registrasi Berhasil',
                'data': data
            })
            return Response(success_message, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_409_CONFLICT)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserViewSerializers
    permission_classes = (AllowAny, )


class UserLoginViewSet(APIView):
    permission_classes = (AllowAny, )
    serializer_class = UserLoginSerializers

    def post(self, req, *args, **kwargs):
        data = req.data
        success_message = ({
            'code': 200,
            'Message': 'Login Berhasil',
            'data': data
        })
        serializer = UserLoginSerializers(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(success_message, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)