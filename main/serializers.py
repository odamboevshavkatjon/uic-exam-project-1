from rest_framework import serializers

from .models import (
    Course,
    CourseAccess,
    Lesson,
    LessonView,
)


class LessonViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonView
        fields = (
            "watch_time",
            "watched_at",
            "status",
        )


class LessonSerializer(serializers.ModelSerializer):
    lesson_progress = LessonViewSerializer(many=True)

    class Meta:
        model = Lesson
        fields = (
            "id",
            "title",
            "lesson_progress",
        )


class CourseAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseAccess
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Course
        fields = (
            "id",
            "owner",
            "lessons",
        )


class CourseStatisticsSerializer(serializers.ModelSerializer):
    course_participants = serializers.IntegerField()
    total_watch_time = serializers.IntegerField()
    access_percentage = serializers.IntegerField()

    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "owner",
            "course_participants",
            "total_watch_time",
            "access_percentage",
        )
