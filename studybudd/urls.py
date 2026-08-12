"""
URL configuration for studybudd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import path, include
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve as serve_media

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Google & GitHub OAuth callbacks
    path('', include('base.urls')),
    path('api/', include('base.api.urls')),
]

# Serve uploaded media (avatars).
# - Development: Django's built-in static() helper.
# - Production: served from MEDIA_ROOT behind gunicorn. For real-world scale,
#   move uploads to object storage (e.g. Cloudinary, S3) instead.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        re_path(r'^images/(?P<path>.*)$', serve_media, {'document_root': settings.MEDIA_ROOT}),
    ]
