# Generated by Django 4.2.6 on 2023-12-04 10:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("data_analysis", "0029_alter_dataconnectionmodel_created_at_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dataconnectionmodel",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="dataconnectionmodel",
            name="updated_at",
        ),
    ]