from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("balo", views.balo, name="balo"),
    path("<str:name>", views.greet, name="greet")
]
