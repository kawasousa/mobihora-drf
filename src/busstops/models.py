from django.contrib.gis.db import models


class BusStop(models.Model):
    name = models.CharField(max_length=255)
    location = models.PointField(srid=4326)

    def __str__(self):
        return self.name