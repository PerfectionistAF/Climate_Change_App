##STEP 2: create views for api, rest framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import csv
from rest_framework import viewsets
from .serializers import EmissionsSerializer
from ..models import Emissions

class EmissionsViewSet(viewsets.ModelViewSet):
    queryset = Emissions.objects.all()
    serializer_class = EmissionsSerializer  ##handle all cloud operations 

class UploadCSV(APIView):
    def post(self, request, format=None):
        file = request.FILES['file']
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        for row in reader:
            serializer = EmissionsSerializer(data=row)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)