from django.contrib import admin
from django.urls import path, include
from .views import MapView

urlpatterns = [
    path('', MapView.as_view()),
    path('admin/', admin.site.urls),
    path('api/v1/', include('dispatch.urls')),
    path('api/v1/auth/', include('rest_auth.urls')),
    path('api/v1/auth/registration/', include('rest_auth.registration.urls'))
]
