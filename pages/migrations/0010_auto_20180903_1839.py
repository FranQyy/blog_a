# Generated by Django 2.1.1 on 2018-09-03 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20180903_1830'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='swiadczone_uslugi',
            options={'ordering': ('nazwa_uslugi',), 'verbose_name_plural': 'Świadczone usługi'},
        ),
    ]