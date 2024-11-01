# Generated by Django 5.1.2 on 2024-10-30 17:47

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("crowdprinter", "0003_rename_render_printjob_file_render_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Printer",
            fields=[
                ("slug", models.SlugField(primary_key=True, serialize=False)),
                ("name", models.TextField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name="printjob",
            name="file_stl",
            field=models.FileField(null=True, upload_to=""),
        ),
        migrations.CreateModel(
            name="PrintJobFile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file_3mf", models.FileField(upload_to="")),
                ("file_gcode", models.FileField(upload_to="")),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crowdprinter.printjob",
                    ),
                ),
                (
                    "printer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="crowdprinter.printer",
                    ),
                ),
            ],
        ),
    ]