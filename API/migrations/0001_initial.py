# Generated by Django 2.2.4 on 2019-09-02 18:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kandang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_kandang', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Lantai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lantai', models.CharField(max_length=50)),
                ('kandang', models.ManyToManyField(to='API.Kandang')),
            ],
        ),
        migrations.CreateModel(
            name='SieradProduce_MI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('awal_populasi', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('catatan', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('jabatan', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField(help_text='Phone Number')),
            ],
        ),
        migrations.CreateModel(
            name='SieradProduce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dead', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('execution', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('afkir', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('panen', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('lantai', models.ManyToManyField(to='API.Lantai')),
            ],
        ),
    ]