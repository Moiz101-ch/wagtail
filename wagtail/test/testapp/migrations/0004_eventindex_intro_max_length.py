# Generated by Django 4.0.4 on 2022-07-08 14:53

from django.db import migrations

import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("tests", "0003_draftstatemodel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventindex",
            name="intro",
            field=wagtail.fields.RichTextField(blank=True, max_length=50),
        ),
    ]
