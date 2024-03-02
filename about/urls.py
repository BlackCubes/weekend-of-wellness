from django.urls import path

from .views import ContactTemplateView, DirectionsTemplateView, FaqListView

app_name = "about"
urlpatterns = [
    path("faq/", FaqListView.as_view(), name="faq"),
    path("directions/", DirectionsTemplateView.as_view(), name="directions"),
    path("contact/", ContactTemplateView.as_view(), name="contact"),
]
