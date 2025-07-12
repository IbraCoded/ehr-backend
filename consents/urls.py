from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConsentLogViewSet

router = DefaultRouter()
router.register(r'consents', ConsentLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]