from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from config import settings
from rest_framework.authtoken import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('book/', include('book.urls')),
                  path('api-auth/', include('rest_framework.urls')),
                  path('olcha/', include('olcha.urls')),
                  path('api-token-auth/', views.obtain_auth_token),
                  path('user/', include('user.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
