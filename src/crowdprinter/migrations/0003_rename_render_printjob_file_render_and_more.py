# Generated by Django 5.1.2 on 2024-10-30 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("crowdprinter", "0002_auto_20190129_1354"),
    ]

    operations = [
        migrations.RenameField(
            model_name="printjob",
            old_name="render",
            new_name="file_render",
        ),
        migrations.RenameField(
            model_name="printjob",
            old_name="stl",
            new_name="file_stl",
        ),
    ]
