from rest_framework import serializers
from .models import SieradProduce, User, Kandang, Lantai, SieradProduce_MI
from django.core.exceptions import ValidationError
# from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework.serializers import (
    ValidationError,
)

class KandangSerializers(serializers.ModelSerializer):
    class Meta:
        model = Kandang
        fields = '__all__'



class LantaiSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lantai
        fields = '__all__'

class SieradSerializers(serializers.ModelSerializer):
    class Meta:
        model = SieradProduce
        fields = '__all__'

class SieradSerializers_MI(serializers.ModelSerializer):
    class Meta:
        model = SieradProduce_MI
        fields = '__all__'


class UserRegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name',
                  'phone',
                  'jabatan',
                  ]

    def validate(self, data):
        user_obj = None
        phone = data.get("phone", None)

        user = User.objects.filter(
            Q(phone=phone)
        ).distinct()
        if user.exists() and user.count() == 1:
            raise ValidationError("Akun ini sudah ada")
        else:
            user_obj = user.first()
        return data


class UserViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name',
                  'phone',
                  'posisi',
                  ]


class UserLoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'phone',
        ]

    def validate(self, data):
        user_obj = None
        phone = data.get("phone", None)

        user = User.objects.filter(
            Q(phone=phone)
        ).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("Phone number is wrong.")
        return data


        # respData = {
        #     'user': data,
        #     'messages': 'Berhasil Login',
        #     'code': 200,
        # }
        # return data

