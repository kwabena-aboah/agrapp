from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static


# Doorstep apps urls
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('products.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^sales/', include('sales.urls')),
    url(r'^payments/', include('payments.urls')),
    url(r'^pages/', include('pages.urls')),
    url(r'^tellme/', include('tellme.urls')),
]


# In Debug mode we need to serve media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
