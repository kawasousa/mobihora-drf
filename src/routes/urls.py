from django.urls import path
from .views import RouteListView, RouteDetailView


urlpatterns = [
    path('', RouteListView.as_view(), name='routes-list'),
    path('<int:id>/', RouteDetailView.as_view(), name='route-details')
]