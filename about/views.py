from django.views.generic import ListView

from .models import Faq


class FaqListView(ListView):
    model = Faq
    context_object_name = "faqs"
    template_name = "sponsors/faq.html"
