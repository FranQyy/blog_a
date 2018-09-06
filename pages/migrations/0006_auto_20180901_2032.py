# Generated by Django 2.1.1 on 2018-09-01 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_pracownik_kontakt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pracownik',
            name='kontakt',
        ),
        migrations.AddField(
            model_name='pracownik',
            name='email',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pracownik',
            name='phone',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
