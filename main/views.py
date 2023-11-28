from django.db.models import Count, Sum, F, Subquery
from django.db.models.functions import Coalesce

from rest_framework import generics
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from .serializers import (
    CourseSerializer,
    CourseAccessSerializer,
    LessonSerializer,
    LessonViewSerializer,
    CourseStatisticsSerializer,
)
from .models import (
    Course,
    CourseAccess,
    Lesson,
    LessonView,
)

User = get_user_model()


class CourseListView(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        current_user = self.request.user
        queryset = Course.objects.filter(courseaccess__user=current_user).distinct()
        return queryset


course_list_view = CourseListView.as_view()


class CourseDetailView(generics.RetrieveAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        current_user = self.request.user
        queryset = Course.objects.filter(courseaccess__user=current_user).distinct()
        return queryset


course_detail_view = CourseDetailView.as_view()


class StatisticsView(generics.ListAPIView):
    serializer_class = CourseStatisticsSerializer

    def get_queryset(self):
        queryset = Course.objects.all().annotate(
            course_participants=Count(
                "courseaccess__user",
                distinct=True,
            ),
            total_watch_time=(
                Coalesce(
                    Sum("courseaccess__user__lessonview__watch_time"),
                    0,
                )
            ),
            access_percentage=(
                Count("courseaccess__user", distinct=True) / User.objects.count()
            )
            * 100,
        )
        return queryset


statistics_view = StatisticsView.as_view()
