from django.views.generic import ListView, TemplateView

from .models import Faq


class AboutTemplateView(TemplateView):
    template_name = "about/index.html"


class FaqListView(ListView):
    model = Faq
    context_object_name = "faqs"
    template_name = "about/faq.html"


class DirectionsTemplateView(TemplateView):
    template_name = "about/directions.html"


class ContactTemplateView(TemplateView):
    template_name = "about/contact.html"


class EventTeamTemplateView(TemplateView):
    template_name = "about/event-team.html"
