# Generated by Django 4.2.1 on 2023-05-11 15:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_article_title"),
    ]

    operations = [
        migrations.RenameField(
            model_name="article",
            old_name="date_posted",
            new_name="timestamp",
        ),
    ]
