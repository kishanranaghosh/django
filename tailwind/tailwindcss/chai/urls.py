from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_chai, name='alychi_tea'),
    path('store/',views.chai_stores_view, name='chai_stores'),

]
