from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
from qrateApp import views
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns = [
        path("admin/", admin.site.urls),
        path('', views.home, name='home'),
        path('code/<slug:slug>/', views.view_code, name='view_code'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
      + [re_path(r'^.*$', views.handle_unknown_routes)]
else:
    urlpatterns = [
      path('', views.home, name='home'),
      path('code/<slug:slug>/', views.view_code, name='view_code'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    + [re_path(r'^.*$', views.handle_unknown_routes)]

