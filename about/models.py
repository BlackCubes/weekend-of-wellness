from django.db import models

from .utils import model_error_messages


class Faq(models.Model):
    question = models.CharField(
        max_length=100, error_messages=model_error_messages["faq"]["question"]
    )
    answer = models.CharField(
        max_length=300, error_messages=model_error_messages["faq"]["answer"]
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self) -> str:
        return self.question
