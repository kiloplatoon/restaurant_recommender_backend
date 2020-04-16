# Generated by Django 3.0.4 on 2020-04-14 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dinnr_app', '0006_auto_20200414_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendrequest',
            name='from_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friendrequest',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='UserProfile', to='dinnr_app.UserProfile'),
        ),
    ]
