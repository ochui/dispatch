# Generated by Django 2.2.6 on 2019-10-18 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191017_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='location',
        ),
    ]
