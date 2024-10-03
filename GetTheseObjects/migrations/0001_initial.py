# Generated by Django 5.1.1 on 2024-10-03 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=200)),
                ('file_url', models.CharField(max_length=300)),
                ('original_file_name', models.CharField(max_length=200)),
                ('date_last_modified', models.DateTimeField()),
                ('file_type', models.CharField(max_length=50)),
            ],
        ),
    ]
