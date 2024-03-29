from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("results", views.results, name="Results")
]