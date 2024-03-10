from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Event, EventOrganization, Organization


class EventOrganizationInLine(admin.TabularInline):
    model = EventOrganization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'address', 'postcode')
    search_fields = ('title', 'description', 'address', 'postcode')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description')
    search_fields = ('title', 'description')
    inlines = (EventOrganizationInLine,)
    list_filter = ('organizations__title',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src={obj.image.url} width="100" height="100">')
        return None

    get_image.short_description = 'Превью изображения'
