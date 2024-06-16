# admin_urls.py
from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="index"),
    path('custom-page/', views.custom_admin_view, name='custom_admin_page'),
]
