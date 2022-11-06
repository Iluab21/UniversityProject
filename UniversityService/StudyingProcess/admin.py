from .models import Direction, Discipline, StudyGroup, Curator, Student
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('direction', )
        })
    )


admin.site.register(Curator, CustomUserAdmin)
admin.site.register(Direction)
admin.site.register(Discipline)
admin.site.register(StudyGroup)
admin.site.register(Student)

