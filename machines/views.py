from rest_framework import viewsets
from .models import Machine, ExpertReport, Registration, Location, MachineValue
from .serializers import *

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class ExpertReportViewSet(viewsets.ModelViewSet):
    queryset = ExpertReport.objects.all()
    serializer_class = ExpertReportSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class MachineValueViewSet(viewsets.ModelViewSet):
    queryset = MachineValue.objects.all()
    serializer_class = MachineValueSerializer