from django.contrib import admin

from .models import TechType


class TechTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(TechType, TechTypeAdmin)
