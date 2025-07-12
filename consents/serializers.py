from rest_framework import serializers
from .models import ConsentLog

class ConsentLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsentLog
        fields = ['id', 'patient_id', 'hospital_id', 'token', 'expiry_date', 'status', 'created_at', 'updated_at']