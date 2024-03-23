
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from listings.views import listing_list, listing_retrieve, linsting_create, linsting_update, listing_delete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('listings/', listing_list),
    path('listings/<pk>/', listing_retrieve),
    path('listings/<pk>/edit/', linsting_update),
    path('listings/<pk>/delete/', listing_delete),
    path('add-listing/', linsting_create),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)