# Generated by Django 4.2.2 on 2023-06-19 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_users_chat_id_users_country_id_users_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='chat_id',
            field=models.CharField(max_length=20),
        ),
    ]