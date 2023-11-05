from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

from utils.error_views import error_400, error_403, error_500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('service.urls')),
    path('api/account/', include('account.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view())
]



handler404 = 'utils.error_views.error_404'
handler403 = 'utils.error_views.error_403'
handler400 = 'utils.error_views.error_400'
handler500 = 'utils.error_views.error_500'
