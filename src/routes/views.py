from .serializers import RouteSerializer
from .models import Route
from rest_framework.views import APIView
from rest_framework.response import Response
import rest_framework.status as status
from rest_framework.permissions import IsAuthenticated, AllowAny


class RouteListView(APIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return [AllowAny()]

    def post(self, request) -> Response:
        serializer = RouteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request) -> Response:
        routes = Route.objects.all()
        serializer = RouteSerializer(routes, many=True)

        return Response(serializer.data)

class RouteDetailView(APIView):
    def get_permissions(self):
        if self.request.method == 'PATCH':
            return [IsAuthenticated()]
        return [AllowAny()]

    def patch(self, request, id) -> Response:
        try:
            route = Route.objects.get(id=id)

            serializer = RouteSerializer(route, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except Route.DoesNotExist:
            return Response({"detail": "Linha não encontrada"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get(self, request, id) -> Response:
        try:
            route = Route.objects.get(id=id)
            serializer = RouteSerializer(route)
            
            return Response(serializer.data)
        except Route.DoesNotExist:
            return Response({"detail": "Linha não encontrada"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)