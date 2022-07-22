# Generated by Django 3.2.10 on 2022-07-21 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='like_user',
        ),
        migrations.AddField(
            model_name='building',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='building',
            name='long',
            field=models.FloatField(blank=True, null=True),
        ),
    ]