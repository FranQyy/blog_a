# Generated by Django 2.1.1 on 2018-09-03 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20180901_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usluga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('galaz_prawa', models.CharField(max_length=250)),
                ('swiadczone_uslugi', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Usługi',
            },
        ),
    ]