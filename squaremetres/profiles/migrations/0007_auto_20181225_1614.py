# Generated by Django 2.1.4 on 2018-12-25 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20181225_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/media/defaults/default_pic.png', null=True, upload_to='user_pic/'),
        ),
    ]