# Generated by Django 2.0.7 on 2018-07-18 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soup', '0007_auto_20180712_1304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='page_id',
            new_name='page',
        ),
        migrations.RenameField(
            model_name='content',
            old_name='site_id',
            new_name='site',
        ),
    ]
