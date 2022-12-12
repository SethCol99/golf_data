from django.urls import path

from . import views

urlpatterns = [
    path("", views.landing, name = "landing"),
    path("round/", views.round.as_view(), name = "round")
]