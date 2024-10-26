from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'email', 'date_creation', 'is_active', 'is_staff', 'is_superuser']

