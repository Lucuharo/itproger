from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('catalog', views.catalog),
    path('cabinet', views.cabinet),
]