from django.urls import path
from .views import BusStopCreateView, BusStopDetailView, NearbyBusStopsView


urlpatterns = [
    path("", BusStopCreateView.as_view(), name="busstop-create"),
    path("<int:id>/", BusStopDetailView.as_view(), name="busstop-detail"),
    path("nearby/", NearbyBusStopsView.as_view(), name="busstop-nearby"),
]