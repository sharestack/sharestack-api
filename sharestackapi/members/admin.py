from django.contrib import admin

from .models import User
from .models import Company


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "first_name", "last_name", "email")

class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(User, UserAdmin)
admin.site.register(Company, CompanyAdmin)
