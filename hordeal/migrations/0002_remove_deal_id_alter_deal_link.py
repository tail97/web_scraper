# Generated by Django 4.1.3 on 2022-12-06 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hordeal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deal',
            name='id',
        ),
        migrations.AlterField(
            model_name='deal',
            name='link',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
