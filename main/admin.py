from django.contrib import admin

from .models import (
    Course,
    CourseAccess,
    Lesson,
    LessonView,
)

admin.site.register(Course)
admin.site.register(CourseAccess)
admin.site.register(Lesson)
admin.site.register(LessonView)
