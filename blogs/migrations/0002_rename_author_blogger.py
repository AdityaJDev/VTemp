# Generated by Django 4.1.1 on 2022-09-12 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Author",
            new_name="Blogger",
        ),
    ]