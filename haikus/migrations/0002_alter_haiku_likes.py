# Generated by Django 3.2.16 on 2022-11-04 13:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('haikus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='haiku',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='haiku_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
