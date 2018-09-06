# Generated by Django 2.1.1 on 2018-09-01 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20180901_1422'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pracownik',
            options={'ordering': ('-publish',), 'verbose_name_plural': 'Pracownicy'},
        ),
        migrations.RenameField(
            model_name='pracownik',
            old_name='body',
            new_name='doswiadczenie',
        ),
        migrations.AddField(
            model_name='pracownik',
            name='jezyki',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pracownik',
            name='wyksztalcenie',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
