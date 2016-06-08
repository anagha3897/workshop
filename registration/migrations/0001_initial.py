# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-07 10:25
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_first_name', models.CharField(blank=True, max_length=32, null=True, validators=[django.core.validators.RegexValidator(regex='^[A-Za-z]*$')], verbose_name='First Name')),
                ('user_last_name', models.CharField(blank=True, max_length=32, null=True, validators=[django.core.validators.RegexValidator(regex='^[A-Za-z]*$')], verbose_name='Last Name')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='Email')),
                ('user_dob', models.DateField(blank=True, null=True, verbose_name='Birth Date')),
                ('user_gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True, verbose_name='Gender')),
                ('user_github', models.CharField(blank=True, max_length=100, verbose_name='Github Profile')),
                ('user_linkedin', models.CharField(blank=True, max_length=100, verbose_name='Linkedin Profile')),
                ('user_bio', models.CharField(blank=True, max_length=1000, verbose_name='Short Bio')),
                ('user_occupation', models.CharField(blank=True, max_length=100, verbose_name='Occupation')),
                ('user_nationality', models.CharField(blank=True, max_length=100, verbose_name='Nationality')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=32, unique=True, verbose_name='username')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Chocolate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Chocolate Name')),
                ('description', models.CharField(blank=True, max_length=1000, verbose_name='Chocolate Description')),
                ('manufacturer', models.CharField(blank=True, max_length=100, verbose_name='Chocolate Manufacturer')),
                ('price', models.IntegerField(blank=True, help_text='4 digits maximum', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)], verbose_name='Chocolate Price')),
            ],
        ),
    ]
