from django import forms

from .models import Sponsors
from .utils import model_error_messages


class SponsorsForm(forms.ModelForm):
    class Meta:
        model = Sponsors

        fields = (
            "name",
            "website",
            "image",
        )

        labels = {"name": "*Name", "website": "Website", "image": "Image"}

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Sponsor's name"}),
            "website": forms.TextInput(attrs={"placeholder": "Sponsor's website"}),
        }

        error_messages = {
            "name": model_error_messages["sponsors"]["name"],
            "website": model_error_messages["sponsors"]["website"],
            "image": model_error_messages["sponsors"]["image"],
        }
