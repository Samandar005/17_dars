from django.contrib import admin
from django.utils.html import format_html
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'group', 'birth_date', 'show_image')
    list_filter = ('group', 'birth_date')
    search_fields = ('first_name', 'last_name', 'phone_number')
    ordering = ('first_name', 'last_name')

    fieldsets = (
        ('Personal Information', {
            'fields': (
                ('first_name', 'last_name'),
                'birth_date',
                'images'
            )
        }),
        ('Group Information', {
            'fields': ('group',)
        }),
        ('Contact Information', {
            'fields': (
                'phone_number',
                'address'
            )
        })
    )

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    get_full_name.short_description = 'Full Name'

    def show_image(self, obj):
        if obj.images:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.images.url)
        return "No Image"

    show_image.short_description = 'Photo'
