from rest_framework import generics

from .serializers import CourseSerializer
from .models import (
    Course,
    CourseAccess,
    Lesson,
    LessonView,
)


class CourseListView(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        current_user = self.request.user
        queryset = Course.objects.filter(courseaccess__user=current_user).distinct()
        return queryset


course_list_view = CourseListView.as_view()
