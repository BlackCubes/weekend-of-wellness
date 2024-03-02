from django.urls import path

from .views import (
    AboutTemplateView,
    ContactTemplateView,
    DirectionsTemplateView,
    EventTeamTemplateView,
    FaqListView,
)

app_name = "about"
urlpatterns = [
    path("", AboutTemplateView.as_view(), name="index"),
    path("faq/", FaqListView.as_view(), name="faq"),
    path("directions/", DirectionsTemplateView.as_view(), name="directions"),
    path("contact/", ContactTemplateView.as_view(), name="contact"),
    path("event-team/", EventTeamTemplateView.as_view(), name="event-team"),
]
