from django.db import models
from django.utils.translation import gettext_lazy as _

from .utils import model_error_messages


class Sponsors(models.Model):
    class SponsorType(models.TextChoices):
        PRIMARY = "primary", _("Primary")
        SECONDARY = "secondary", _("Secondary")
        ADDITIONAL = "additional", _("Additional")

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
    sponsor_type = models.CharField(
        max_length=10,
        choices=SponsorType,
        default=SponsorType.ADDITIONAL,
        error_messages=model_error_messages["sponsors"]["sponsor_type"],
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = "Sponsor"
        verbose_name_plural = "Sponsors"

    def __str__(self) -> str:
        return self.name
