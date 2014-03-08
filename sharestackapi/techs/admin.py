from django.contrib import admin

from .models import TechType, Tech


class TechTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class TechAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")


admin.site.register(TechType, TechTypeAdmin)
admin.site.register(Tech, TechAdmin)
