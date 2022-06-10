from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

from .settings import STATICFILES_DIRS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('vencimientos/', include('vencimientos.urls')),
    
    # Serve the favicon
    path('favicon.ico', serve, {
            'path': 'favicon.ico',
            'document_root': STATICFILES_DIRS[0],
        }
    ),
]
