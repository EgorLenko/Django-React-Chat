# Generated by Django 4.1.7 on 2023-03-27 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("ChatnGo", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="r_messages",
                to="ChatnGo.chatroom",
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="u_messages",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]