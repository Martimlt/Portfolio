from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view, name='home_page_view'),
    path('ucsd', views.ucsd_page_view, name='ucsd'),
    path('lusofona', views.lusofona_page_view, name='lusofona'),
]
