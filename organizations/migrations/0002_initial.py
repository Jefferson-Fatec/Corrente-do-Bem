# Generated by Django 4.0.4 on 2024-03-30 20:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='organization_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
