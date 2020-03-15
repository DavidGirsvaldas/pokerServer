from django.urls import path
from pokerApp import views

app_name = "pokerApp"
urlpatterns = [
    path("get_settings", views.get_settings, name="get_settings")
]
