from django.urls import path

from .views import SubscribeTemplateView

app_name = "subscribe"
urlpatterns = [
    path("", SubscribeTemplateView.as_view(), name="index"),
]
