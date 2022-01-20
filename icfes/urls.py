from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='main.html')),
    path('admin/', admin.site.urls),
    path('colegios/', include('saber11.urls')),
    path('saber11/', include('visor.urls')),
    path('blog/', include('blog.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'visor.views.handle_page_not_found'
