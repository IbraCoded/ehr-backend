from django.urls import path
from .views import ObtainTokenPairView, TokenRefreshView, TokenBlacklistView

urlpatterns = [
    path('token/', ObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]