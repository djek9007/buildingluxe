# Generated by Django 3.2.15 on 2022-08-15 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Url'),
        ),
    ]
