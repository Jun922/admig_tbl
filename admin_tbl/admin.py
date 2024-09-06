from django.contrib import admin
from .models import Student, Lesson


class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'times',
        'progress',
    )

    def get_name(self, obj):
        return obj.student


admin.site.register(Student)
admin.site.register(Lesson, LessonAdmin)