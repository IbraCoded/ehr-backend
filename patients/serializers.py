from rest_framework import serializers
from .models import Patient, PatientUser

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'patient_id', 'first_name', 'last_name', 'date_of_birth', 'gender', 'created_at', 'updated_at']

class PatientUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientUser
        fields = ['id', 'patient_id', 'user', 'created_at', 'updated_at']