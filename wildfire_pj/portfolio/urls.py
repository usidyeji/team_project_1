from django.urls import path
from . import views

urlpatterns = [
  path('pj/', views.Portfolio),
]