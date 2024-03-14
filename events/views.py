from django.views.generic import TemplateView


class EventsTemplateView(TemplateView):
    template_name = "events/index.html"


class FitnessClassesTemplateView(TemplateView):
    template_name = "events/fitness-classes.html"


class HealthFairTemplateView(TemplateView):
    template_name = "events/health-fair.html"


class FarmersMarketTemplateView(TemplateView):
    template_name = "events/farmers-market.html"


class MobileHealthClinicsTemplateView(TemplateView):
    template_name = "events/mobile-health-clinics.html"


class PickleballTournamentTemplateView(TemplateView):
    template_name = "events/pickleball-tournament.html"


class WorkshopsTemplateView(TemplateView):
    template_name = "events/workshops.html"
