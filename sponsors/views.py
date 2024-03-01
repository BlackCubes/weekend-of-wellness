from django.views.generic import ListView

from .models import Sponsors


class SponsorsListView(ListView):
    model = Sponsors
    context_object_name = "sponsors"
    template_name = "sponsors/index.html"
