from django.db import models


class NatureImage(models.Model):
    url = models.CharField(max_length=80, default=None)
    height = models.CharField(max_length=80, default=None)
    width = models.CharField(max_length=80, default=None)
    comment = models.CharField(max_length=80, default=None)

    def __str__(self) -> str:
        return f"{self.height}"
