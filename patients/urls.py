from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, PatientUserViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'patient-users', PatientUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]