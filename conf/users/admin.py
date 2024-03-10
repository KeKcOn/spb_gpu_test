from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'email',
        'username',
        'first_name',
        'last_name',
        'phone_number',
        'organization',
    )
    search_fields = (
        'username', 'email', 'first_name', 'last_name', 'phone_number')
    list_filter = ('organization',)
