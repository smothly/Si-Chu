# Generated by Django 3.0.2 on 2020-02-07 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20200207_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='category',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='class_code',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='score',
            field=models.CharField(max_length=15),
        ),
    ]
