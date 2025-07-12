from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicalRecordViewSet, PrescriptionViewSet, LabResultViewSet

router = DefaultRouter()
router.register(r'records', MedicalRecordViewSet)
router.register(r'prescriptions', PrescriptionViewSet)
router.register(r'lab_results', LabResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
]