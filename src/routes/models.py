from django.db import models


class Route(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.code