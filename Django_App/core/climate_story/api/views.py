##STEP 2: create views for api, rest framework
from rest_framework import viewsets
from .serializers import EmissionsSerializer
from ..models import Emissions

class EmissionsViewSet(viewsets.ModelViewSet):
    queryset = Emissions.objects.all()
    serializer_class = EmissionsSerializer  ##handle all cloud operations 