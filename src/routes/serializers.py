from .models import Route
from rest_framework.serializers import ModelSerializer


class RouteSerializer(ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'code', 'description']