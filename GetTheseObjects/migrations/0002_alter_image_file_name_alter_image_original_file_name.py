# Generated by Django 5.1.1 on 2024-10-03 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GetTheseObjects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file_name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='image',
            name='original_file_name',
            field=models.CharField(max_length=300),
        ),
    ]
