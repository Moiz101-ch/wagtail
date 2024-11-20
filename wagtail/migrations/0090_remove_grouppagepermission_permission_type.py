# Generated by Django 4.0.10 on 2023-10-30 11:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("wagtailcore", "0089_log_entry_data_json_null_to_object"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="grouppagepermission",
            name="permission_or_permission_type_not_null",
        ),
        migrations.RemoveConstraint(
            model_name="grouppagepermission",
            name="unique_permission_type",
        ),
        migrations.RemoveField(
            model_name="grouppagepermission",
            name="permission_type",
        ),
        migrations.AlterField(
            model_name="grouppagepermission",
            name="permission",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="auth.permission",
                verbose_name="permission",
            ),
        ),
    ]
