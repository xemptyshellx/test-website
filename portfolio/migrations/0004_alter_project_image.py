# Generated by Django 4.1.5 on 2023-01-16 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0003_project_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]