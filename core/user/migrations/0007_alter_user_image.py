# Generated by Django 4.0.2 on 2024-03-01 23:47

import core.security.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=core.security.fields.CustomImageField(blank=True, null=True, upload_to=core.security.fields.CustomImageField.get_upload_path, verbose_name='Imagen'),
        ),
    ]
