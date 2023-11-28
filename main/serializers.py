from rest_framework import serializers

from .models import (
    Course,
    CourseAccess,
    Lesson,
    LessonView,
)


class CourseAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseAccess
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonView
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
