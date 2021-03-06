from django.conf import settings
from django.conf.urls import patterns, include, url, static
from django.contrib import admin



admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
) + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
