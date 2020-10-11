# Generated by Django 3.1.2 on 2020-10-11 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crops', '0004_auto_20201011_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedata',
            name='city',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='savedata',
            name='desc',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='savedata',
            name='humidity',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='savedata',
            name='lat',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='savedata',
            name='lon',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='savedata',
            name='temp',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='savedata',
            name='wind',
            field=models.CharField(max_length=30),
        ),
    ]
