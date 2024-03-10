from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'username', 'first_name', 'last_name',
                    'phone_number')
    search_fields = (
        'username', 'email', 'first_name', 'last_name', 'phone_number')
    # list_filter = ('username', 'email')


admin.site.register(User, UserAdmin)
