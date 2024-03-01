from django.urls import path

from .views import SponsorsListView

app_name = "sponsors"
urlpatterns = [
    path("", SponsorsListView.as_view(), name="index"),
]
