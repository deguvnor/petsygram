# Generated by Django 2.1.2 on 2018-10-08 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo_blog', '0004_auto_20181008_0708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='comment',
        ),
    ]
