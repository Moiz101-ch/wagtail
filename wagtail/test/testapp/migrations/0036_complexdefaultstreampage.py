# Generated by Django 5.0.3 on 2024-04-15 22:12

import django.db.models.deletion
from django.db import migrations, models

import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("tests", "0035_modelwithcustommanager"),
        ("wagtailcore", "0093_uploadedfile"),
    ]

    operations = [
        migrations.CreateModel(
            name="ComplexDefaultStreamPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            ("text", wagtail.blocks.CharBlock()),
                            ("rich_text", wagtail.blocks.RichTextBlock()),
                            (
                                "books",
                                wagtail.blocks.StreamBlock(
                                    [
                                        ("title", wagtail.blocks.CharBlock()),
                                        ("author", wagtail.blocks.CharBlock()),
                                    ]
                                ),
                            ),
                        ],
                        default=[
                            ("rich_text", "<p>My <i>lovely</i> books</p>"),
                            (
                                "books",
                                [
                                    ("title", "The Great Gatsby"),
                                    ("author", "F. Scott Fitzgerald"),
                                ],
                            ),
                        ],
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
