from django.urls import path
from Converter import views

urlpatterns = [
    path("", views.home, name="home"),
    path("converterResult/<int:pk>/", views.converterResult, name="converterResult"),
]