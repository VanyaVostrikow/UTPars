# Generated by Django 4.2.2 on 2023-06-15 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('channels', '0001_initial'),
        ('users', '0003_alter_userdetail_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('user_rating', models.IntegerField(null=True)),
                ('channel_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='channel_id', to='channels.channels')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='users.users')),
            ],
        ),
    ]
