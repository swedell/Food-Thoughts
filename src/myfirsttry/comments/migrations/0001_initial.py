# Generated by Django 3.0.7 on 2020-07-24 13:47

import comments.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('forums', '0007_auto_20200724_1917'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=400)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forums.ForumPost')),
                ('user', models.ForeignKey(on_delete=models.SET(comments.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated', '-timestamp'],
            },
        ),
    ]
