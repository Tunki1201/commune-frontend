# Generated by Django 4.2.6 on 2023-11-20 05:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data_analysis", "0021_remove_project_project_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="workspace",
            name="workspace_name",
        ),
        migrations.AddField(
            model_name="workspace",
            name="encrypted_workspace_name",
            field=models.BinaryField(default=b""),
        ),
    ]