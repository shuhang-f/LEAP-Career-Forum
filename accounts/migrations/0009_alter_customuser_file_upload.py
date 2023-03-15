# Generated by Django 4.1.7 on 2023-03-14 23:19

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='file_upload',
            field=models.FileField(blank=True, null=True, upload_to=accounts.models.user_directory_path),
        ),
    ]