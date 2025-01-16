from django.contrib import admin
from .models import Subject
from teachers.models import Teacher


class TeacherInline(admin.StackedInline):
    model = Teacher
    extra = 1
    classes = ('collapse',)
    fieldsets = (
        ('Personal Information', {
            'fields': (
                ('first_name', 'last_name'),
                'images'
            )
        }),
        ('Professional Details', {
            'fields': (
                'email',
                'phone_number',
                'work_experience'
            )
        })
    )


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    inlines = [TeacherInline]
    list_display = ('name', 'get_teachers_count')
    search_fields = ('name',)

    def get_teachers_count(self, obj):
        return obj.teachers.count()

    get_teachers_count.short_description = 'Number of Teachers'
