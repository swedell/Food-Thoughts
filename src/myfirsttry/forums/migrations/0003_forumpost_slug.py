# Generated by Django 3.0.7 on 2020-07-12 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0002_auto_20200709_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumpost',
            name='slug',
            field=models.SlugField(default='hello-world'),
            preserve_default=False,
        ),
    ]
