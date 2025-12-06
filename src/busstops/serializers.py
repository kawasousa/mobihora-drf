from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import BusStop


class BusStopSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BusStop
        geo_field = "location"
        fields = ["id", "name", "location"]