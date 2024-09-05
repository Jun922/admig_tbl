from django.contrib import admin
from .models import Student, Lesson


class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'times',
        'progress',
    )

    def get_name(self, obj):
        return obj.name


admin.site.register(Student)
admin.site.register(Lesson, LessonAdmin)