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
            "sponsor_type",
        )

        labels = {
            "name": "*Name",
            "website": "Website",
            "image": "Image",
            "sponsor_type": "*Sponsor Type",
        }

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Sponsor's name"}),
            "website": forms.TextInput(attrs={"placeholder": "Sponsor's website"}),
        }

        error_messages = {
            "name": model_error_messages["sponsors"]["name"],
            "website": model_error_messages["sponsors"]["website"],
            "image": model_error_messages["sponsors"]["image"],
            "sponsor_type": model_error_messages["sponsors"]["sponsor_type"],
        }
