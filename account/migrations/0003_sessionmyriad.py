# Generated by Django 3.1.7 on 2022-02-04 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_sessioncbio'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionMyriad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servername', models.CharField(max_length=120)),
                ('serverIP', models.CharField(max_length=60)),
                ('serverUsername', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=120)),
            ],
        ),
    ]