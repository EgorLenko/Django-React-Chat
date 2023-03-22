from django.db import models


class Base(models.Model):
    """Base Abstract model for inheritance"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
