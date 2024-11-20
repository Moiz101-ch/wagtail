# Generated by Django 2.2.10 on 2020-07-13 10:17

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0056_page_locale_fields_populate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="page",
            name="locale",
            field=models.ForeignKey(
                editable=False,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="wagtailcore.Locale",
            ),
        ),
        migrations.AlterField(
            model_name="page",
            name="translation_key",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
