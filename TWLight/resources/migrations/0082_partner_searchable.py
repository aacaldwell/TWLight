# Generated by Django 3.2.7 on 2021-10-05 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resources", "0081_auto_20210928_1820"),
    ]

    operations = [
        migrations.AddField(
            model_name="partner",
            name="searchable",
            field=models.IntegerField(
                choices=[
                    (0, "Searchable"),
                    (1, "Not searchable"),
                    (2, "Partially searchable"),
                ],
                default=1,
                help_text="Indicates whether a partner is searchable in EDS or not.",
            ),
        ),
    ]
