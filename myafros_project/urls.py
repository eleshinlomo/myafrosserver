
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('test.urls')),
    path('api/', include('api.urls')),
    path('spanishagent/', include('spanishagent.urls')),
    path('api-auth/', include('rest_framework.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


