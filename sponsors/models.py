from django.db import models

from .utils import model_error_messages


class Sponsors(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        error_messages=model_error_messages["sponsors"]["name"],
    )
    website = models.URLField(
        max_length=200,
        error_messages=model_error_messages["sponsors"]["website"],
        null=True,
        blank=True,
        default=None,
    )
    image = models.ImageField(
        upload_to="sponsors",
        error_messages=model_error_messages["sponsors"]["image"],
        null=True,
        blank=True,
        default=None,
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Sponsors"

    def __str__(self) -> str:
        return self.name
