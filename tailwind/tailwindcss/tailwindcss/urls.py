
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.serve_tailwind, name='alychi_tea'),

    path('__reload__/', include('django_browser_reload.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
