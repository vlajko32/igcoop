from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.authtoken import views

def root_redirect(request):
    # Redirect to the token-based login page
    return redirect('/api-token-auth/')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT token obtain
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT token refresh
    path('api-token-auth/', views.obtain_auth_token),  # Token-based login for django rest auth
    path('api/machines/', include('machines.urls')),
    path('api/administration/', include('administration.urls')),  # Include administration app URLs
    path('api-auth/', include('rest_framework.urls')),  # DRF login/logout views
    path('', root_redirect, name='root_redirect'),
]