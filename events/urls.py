from django.urls import path

from .views import (
    EventsTemplateView,
    FarmersMarketTemplateView,
    FitnessClassesTemplateView,
    HealthFairTemplateView,
    MobileHealthClinicsTemplateView,
    PickleballTournamentTemplateView,
    WorkshopsTemplateView,
)

app_name = "events"
urlpatterns = [
    path("", EventsTemplateView.as_view(), name="index"),
    path(
        "fitness-classes/", FitnessClassesTemplateView.as_view(), name="fitness-classes"
    ),
    path("health-fair/", HealthFairTemplateView.as_view(), name="health-fair"),
    path("farmers-market/", FarmersMarketTemplateView.as_view(), name="farmers-market"),
    path(
        "mobile-health-clinics/",
        MobileHealthClinicsTemplateView.as_view(),
        name="mobile-health-clinics",
    ),
    path(
        "pickleball-tournament/",
        PickleballTournamentTemplateView.as_view(),
        name="pickleball-tournament",
    ),
    path("workshops/", WorkshopsTemplateView.as_view(), name="workshops"),
]
