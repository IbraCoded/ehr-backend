from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import ConsentLog
from .serializers import ConsentLogSerializer
import uuid
from datetime import datetime, timedelta

class ConsentLogViewSet(viewsets.ModelViewSet):
    queryset = ConsentLog.objects.all()
    serializer_class = ConsentLogSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def create_consent(self, request):
        patient_id = request.data.get('patient_id')
        hospital_id = request.data.get('hospital_id')
        token = str(uuid.uuid4())
        expiry_date = datetime.now() + timedelta(days=7)  # Consent valid for 7 days
        consent = ConsentLog.objects.create(
            patient_id=patient_id,
            hospital_id=hospital_id,
            token=token,
            expiry_date=expiry_date,
            status='active'
        )
        serializer = self.get_serializer(consent)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def revoke_consent(self, request, pk=None):
        consent = self.get_object()
        if consent.status == 'active':
            consent.status = 'revoked'
            consent.save()
            return Response({'message': 'Consent revoked'})
        return Response({'error': 'Consent already revoked or invalid'}, status=400)