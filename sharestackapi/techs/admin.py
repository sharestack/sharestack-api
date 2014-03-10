from django.contrib import admin

from .models import TechType, Tech, Component


class TechTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class TechAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")


class ComponentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "version", "tech")

admin.site.register(TechType, TechTypeAdmin)
admin.site.register(Tech, TechAdmin)
admin.site.register(Component, ComponentAdmin)
