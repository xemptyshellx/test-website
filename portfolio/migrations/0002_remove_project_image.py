# Generated by Django 4.1.5 on 2023-01-14 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="project", name="image",),
    ]
