# Generated by Django 3.0.4 on 2020-04-15 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinnr_app', '0009_restaurantswipes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantswipes',
            name='user_one_id',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='restaurantswipes',
            name='user_two_id',
            field=models.CharField(max_length=20),
        ),
    ]
