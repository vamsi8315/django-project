# Generated by Django 3.0.8 on 2020-07-23 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emp',
            old_name='des',
            new_name='coursename',
        ),
        migrations.RemoveField(
            model_name='emp',
            name='salary',
        ),
    ]
