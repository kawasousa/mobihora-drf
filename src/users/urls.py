from django.urls import path
from .views import UserRegisterView, UserDetailView


urlpatterns = [
    path('', UserRegisterView.as_view(), name='user-register'),
    path('me/', UserDetailView.as_view(), name='user-detail'),
    
]