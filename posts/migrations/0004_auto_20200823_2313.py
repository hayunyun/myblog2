# Generated by Django 3.1 on 2020-08-23 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200722_2045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='writer',
        ),
    ]
