from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('devadmin/', admin.site.urls),
    path('', include('apps.authentication.urls')),
    path('accounts/', include('allauth.urls')),
    re_path('djga/', include('google_analytics.urls')),
    path("pages", include("apps.pages.urls", namespace='pages')),
]
