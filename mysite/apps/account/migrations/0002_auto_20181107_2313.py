# Generated by Django 2.1.2 on 2018-11-08 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='course',
            new_name='group',
        ),
    ]