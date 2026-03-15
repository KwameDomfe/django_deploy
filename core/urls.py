from django.contrib import admin
from django.contrib.staticfiles.views import serve as staticfiles_serve
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path
from django.views.static import serve

from .views import (hello_world, health_check)

urlpatterns = [
    path(
        'admin/',
        admin.site.urls),

    path(
        '',
        hello_world, 
        name='hello_world'),

    path('health/',
        health_check, 
        name='health_check'),
    # deploy/
    path('deploy/',
        include('apps.deploy.urls')),
    path('accounts/',
        include('apps.accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
elif getattr(settings, 'SERVE_MEDIA', False):
    urlpatterns += [
        re_path(
            r'^media/(?P<path>.*)$',
            serve,
            {'document_root': settings.MEDIA_ROOT},
        ),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
elif getattr(settings, 'SERVE_STATIC', False):
    urlpatterns += [
        re_path(
            r'^static/(?P<path>.*)$',
            staticfiles_serve,
            {'insecure': True},
        ),
    ]
