# Generated by Django 2.1.1 on 2018-09-05 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_auto_20180905_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='wpis',
            name='slug',
            field=models.SlugField(default=1, max_length=100, unique_for_date='publish'),
            preserve_default=False,
        ),
    ]