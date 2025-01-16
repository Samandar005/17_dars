from django.contrib import admin
from .models import Group
from students.models import Student


class StudentInline(admin.StackedInline):
    model = Student
    extra = 1
    classes = ('collapse',)
    fieldsets = (
        ('Personal Information', {
            'fields': (
                ('first_name', 'last_name'),
                'birth_date',
                'images'
            )
        }),
        ('Contact Details', {
            'fields': (
                'phone_number',
                'address'
            )
        })
    )


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [StudentInline]
    list_display = ('group_name', 'class_leader', 'get_student_count')
    list_filter = ('class_leader',)
    search_fields = ('group_name', 'class_leader__first_name', 'class_leader__last_name')
    raw_id_fields = ('class_leader',)

    def get_student_count(self, obj):
        return obj.students.count()

    get_student_count.short_description = 'Number of Students'
