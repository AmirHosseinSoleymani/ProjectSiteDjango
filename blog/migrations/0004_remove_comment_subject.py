# Generated by Django 4.2.10 on 2024-04-24 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_notifemail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='subject',
        ),
    ]
