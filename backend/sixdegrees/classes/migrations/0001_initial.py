# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 11:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camp_id', models.SmallIntegerField(default=0)),
                ('title', models.CharField(max_length=200)),
                ('story_tell', models.TextField(max_length=256)),
                ('action1', models.CharField(max_length=200)),
                ('action2', models.CharField(max_length=200)),
                ('action3', models.CharField(max_length=200)),
                ('user_1', models.CharField(blank=True, max_length=200, null=True)),
                ('user_2', models.CharField(blank=True, max_length=200, null=True)),
                ('user_3', models.CharField(blank=True, max_length=200, null=True)),
                ('user_4', models.CharField(blank=True, max_length=200, null=True)),
                ('user_5', models.CharField(blank=True, max_length=200, null=True)),
                ('user_6', models.CharField(blank=True, max_length=200, null=True)),
                ('catalyst', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catalyst', to=settings.AUTH_USER_MODEL)),
                ('npo_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='npo_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NPOProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camp_id', models.SmallIntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
