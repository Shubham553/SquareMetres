# Generated by Django 2.1.4 on 2018-12-21 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20181221_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/static/images/default_pic.png', null=True, upload_to='user_pic/'),
        ),
    ]
