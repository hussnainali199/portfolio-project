# Generated by Django 2.0.2 on 2018-06-20 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20180620_0533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='imagesuper',
            new_name='image',
        ),
    ]
