from django.urls import path

from .views import FaqListView

app_name = "about"
urlpatterns = [
    path("faq", FaqListView.as_view(), name="faq"),
]
