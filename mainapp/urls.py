from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


manager = views.PageManager()


urlpatterns = [
    path('', manager.get),
    url(r'^bio/\w+$', manager.get_bio),
    path('repertoire/', manager.get_repertoire),
    path('events/', manager.get_events),
    path('contacts/', manager.get_contacts),
    path('media/', manager.get_media),
    path('feedback/', manager.feedback),
    path('publications/', manager.get_publications)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
