from django import forms

from .models import Faq
from .utils import model_error_messages


class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq

        fields = (
            "question",
            "answer",
        )

        labels = {
            "question": "*Question",
            "answer": "*Answer",
        }

        widgets = {
            "question": forms.TextInput(attrs={"placeholder": "A most asked question"}),
            "answer": forms.Textarea(
                attrs={"placeholder": "An answer to the question"}
            ),
        }

        error_messages = {
            "question": model_error_messages["faq"]["question"],
            "answer": model_error_messages["faq"]["answer"],
        }
