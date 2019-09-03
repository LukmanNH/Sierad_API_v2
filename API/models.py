from django.db import models
from django.core.validators import MinValueValidator
from phone_field import PhoneField


class Kandang(models.Model):
    nama_kandang = models.CharField(max_length=50)
    

class Lantai(models.Model):
    nama_lantai = models.CharField(max_length=50)
    kandang = models.ManyToManyField(Kandang)


class SieradProduce_MI(models.Model):
    awal_populasi = models.IntegerField(validators=[MinValueValidator(0)], null=False)
    catatan = models.CharField(max_length=300, blank=True)
    

class SieradProduce(models.Model):
    dead = models.IntegerField(validators=[MinValueValidator(0)], null=False)
    execution = models.IntegerField(validators=[MinValueValidator(0)], null=False)
    afkir = models.IntegerField(validators=[MinValueValidator(0)], null=False)
    panen = models.IntegerField(validators=[MinValueValidator(0)], null=False)
    lantai = models.ManyToManyField(Lantai)
    
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Sierad Produce ID =  {}".format(self.id)


class User(models.Model):
    name = models.CharField(max_length=100,  null=False)
    jabatan = models.CharField(max_length=50,  null=False)
    phone = models.BigIntegerField(null=False, help_text='Phone Number')

    def __str__(self):
        return "{}".format(self.phone)
