# Generated by Django 2.1.2 on 2018-11-30 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20181120_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='description',
            field=models.TextField(max_length=140),
        ),
    ]