# Generated by Django 4.1.7 on 2023-03-27 22:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ChatnGo", "0002_alter_message_room_alter_message_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="photo",
            field=models.URLField(blank=True, null=True),
        ),
    ]
