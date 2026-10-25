
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.serve_tailwind, name='alychi_tea'),



    path('__reload__/', include('django_browser_reload.urls'))
]
