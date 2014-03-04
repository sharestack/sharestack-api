from django.contrib import admin

from .models import Stack, Instance


class StackAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "owner")


class InstanceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "stack")


admin.site.register(Stack, StackAdmin)
admin.site.register(Instance, InstanceAdmin)