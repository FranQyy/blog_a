# Generated by Django 2.1.1 on 2018-09-05 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_wpis_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wpis',
            name='slug',
            field=models.SlugField(max_length=100, unique_for_date='date_added'),
        ),
    ]
