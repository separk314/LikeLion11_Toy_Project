# Generated by Django 4.1.7 on 2023-05-10 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("visits", "0003_rename_visit_id2_visit_visit_id"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="visit", options={"ordering": ["created_at"]},
        ),
    ]
