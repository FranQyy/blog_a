# Generated by Django 2.1.1 on 2018-09-05 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20180905_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='wpis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=250)),
                ('tekst', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'wpisy',
            },
        ),
    ]
