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
    duration = models.PositiveIntegerField(default=0)  # time in seconds
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

    watch_time = models.PositiveIntegerField(default=0)  # time in seconds
    watched_at = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False)  # view status

    def save(self, *args, **kwargs):
        percentage = (self.watch_time / self.lesson.duration) * 100

        if percentage >= 80:
            self.status = True

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "User Lesson View"
        verbose_name_plural = "User Lesson Views"
