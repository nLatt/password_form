from django.urls import path
from . import views

urlpatterns = [
    path("", views.form, name="form"),
    path("logged_in/", views.logged_in, name="logged_in")
]
