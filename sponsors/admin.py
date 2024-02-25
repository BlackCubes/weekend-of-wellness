from typing import Any

from django.contrib import admin
from django.http import HttpRequest
from django.utils.html import format_html

from .forms import SponsorsForm
from .models import Sponsors


class SponsorsAdmin(admin.ModelAdmin):
    model = Sponsors
    form = SponsorsForm

    list_display = (
        "name",
        "image_thumbnail_tag",
        "created_at",
        "updated_at",
    )
    list_display_links = (
        "name",
        "image_thumbnail_tag",
    )
    list_filter = ("name",)
    search_fields = ("name",)
    ordering = (
        "name",
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Info",
            {
                "fields": (
                    "name",
                    "website",
                )
            },
        ),
        (
            "Image",
            {
                "fields": (
                    "image",
                    "image_large_tag",
                )
            },
        ),
        (
            "Additional Info",
            {
                "fields": (
                    "id",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )
    readonly_fields = (
        "id",
        "image_large_tag",
        "created_at",
        "updated_at",
    )

    add_fieldset = (
        (
            None,
            {
                "fields": (
                    "name",
                    "website",
                )
            },
        ),
    )

    def get_fieldsets(
        self, request: HttpRequest, obj: Sponsors | None = None
    ) -> list[tuple[str | None, dict[str, Any]]]:
        if not obj:
            return self.add_fieldset

        return super(SponsorsAdmin, self).get_fieldsets(request, obj)

    @admin.display(description="Preview")
    def image_large_tag(self, obj: Sponsors):
        if obj.image:
            return format_html(
                '<img src="{0}" style="width: 320px; height: auto;" />'.format(
                    obj.image.url
                )
            )

        return format_html("<b>(No image)</b>")

    @admin.display(description="Image")
    def image_thumbnail_tag(self, obj: Sponsors):
        if obj.image:
            return format_html(
                '<img src="{0}" style="width: 100px; height: auto;" />'.format(
                    obj.image.url
                )
            )

        return format_html("<b>(No image)</b>")


admin.site.register(Sponsors, SponsorsAdmin)
