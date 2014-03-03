from django.contrib import admin

from .models import Stack


class StackAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "owner")


admin.site.register(Stack, StackAdmin)