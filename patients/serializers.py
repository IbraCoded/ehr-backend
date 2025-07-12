from rest_framework import viewsets
from .models import Patient, PatientUser
from .serializers import PatientSerializer, PatientUserSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientUserViewSet(viewsets.ModelViewSet):
    queryset = PatientUser.objects.all()
    serializer_class = PatientUserSerializer