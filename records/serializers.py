from rest_framework import serializers
from .models import MedicalRecord, Prescription, LabResult

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = ['id', 'patient', 'diagnosis', 'treatment', 'created_at', 'updated_at']

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ['id', 'patient', 'medication', 'dosage', 'created_at', 'updated_at']

class LabResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabResult
        fields = ['id', 'patient', 'test_type', 'result', 'created_at', 'updated_at']