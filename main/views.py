from django.db.models import Prefetch
from django.http import QueryDict

from rest_framework import generics

from .serializers import (
    CourseSerializer,
    LessonSerializer,
)
from .models import (
    Course,
    CourseAccess,
    Lesson,
    LessonView,
)


class LessonListView(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        current_user = self.request.user
        queryset = Lesson.objects.filter(
            course__courseaccess__user=current_user
        ).distinct()
        return queryset


lesson_list_view = LessonListView.as_view()
