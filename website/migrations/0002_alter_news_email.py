# Generated by Django 4.2.10 on 2024-04-19 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]