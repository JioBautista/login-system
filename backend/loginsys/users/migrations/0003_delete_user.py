# Generated by Django 5.0.4 on 2024-04-24 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_password_alter_user_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]