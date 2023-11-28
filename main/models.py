from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=255)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class CourseAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    granted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "User Course Access"
        verbose_name_plural = "User Course Access"


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    duration = models.PositiveIntegerField(default=0)
    video_link = models.URLField()

    course = models.ManyToManyField(
        Course,
        related_name="lessons",
    )

    def __str__(self):
        return self.title


class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="lesson_progress",
    )

    watched_at = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False)  # view status_

    class Meta:
        verbose_name = "User Lesson View"
        verbose_name_plural = "User Lesson Views"
