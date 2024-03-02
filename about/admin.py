from typing import Any

from django.contrib import admin
from django.http import HttpRequest

from .forms import FaqForm
from .models import Faq


class FaqAdmin(admin.ModelAdmin):
    model = Faq
    form = FaqForm

    list_display = (
        "question",
        "created_at",
        "updated_at",
    )
    list_display_links = ("question",)
    search_fields = ("question",)
    ordering = (
        "question",
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Q&A",
            {
                "fields": (
                    "question",
                    "answer",
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
        "created_at",
        "updated_at",
    )

    add_fieldset = (
        (
            None,
            {
                "fields": (
                    "question",
                    "answer",
                )
            },
        ),
    )

    def get_fieldsets(
        self, request: HttpRequest, obj: Faq | None = None
    ) -> list[tuple[str | None, dict[str, Any]]]:
        if not obj:
            return self.add_fieldset

        return super(FaqAdmin, self).get_fieldsets(request, obj)


admin.site.register(Faq, FaqAdmin)
