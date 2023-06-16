# Generated by Django 4.2.2 on 2023-06-15 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('channels', '0001_initial'),
        ('pictures', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video_info',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('date_create', models.DateField()),
                ('thumbnail_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pictures.thumbnail')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('video_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='video.video_info')),
                ('channel_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='channels.channels')),
                ('genre_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='services.genres')),
            ],
        ),
    ]
