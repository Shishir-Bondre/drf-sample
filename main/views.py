from rest_framework import viewsets

from .models import Thing
from .serializers import ThingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ThingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Thing instances
    to be viewed or edited.
    """
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer

class UserViewSet(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.headers)
        return Response(status=200)