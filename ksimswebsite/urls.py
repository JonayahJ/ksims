# ksimswebsite URL Configuration

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')), # main website links
    path('publications/', include('publications.urls')), # publication list, article view, etc.
    path('contact/', include('contact.urls')), # contact form links and thank you page
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # allows us to grab images uploaded from admin side

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # add static file URL to django urlpatterns
