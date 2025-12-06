from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import BusStop
from .serializers import BusStopSerializer


class BusStopCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = BusStopSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BusStopDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, id):
        try:
            bus_stop = BusStop.objects.get(id=id)
        except BusStop.DoesNotExist:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = BusStopSerializer(bus_stop)
        return Response(serializer.data)

class   NearbyBusStopsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        lat = float(request.query_params.get("lat"))
        lng = float(request.query_params.get("lng"))
        limit = int(request.query_params.get("limit", 10))

        user_location = Point(lng, lat, srid=4326)

        bus_stops = (
        BusStop.objects
        .annotate(distance=Distance("location", user_location))
        .order_by("distance")[:limit]
        )

        serializer = BusStopSerializer(bus_stops, many=True)
        return Response(serializer.data)