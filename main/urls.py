from django.urls import path
from . import views

urlpatterns = [
    path("course/", views.course_list_view, name="course-list"),
    path("course/<int:pk>", views.course_detail_view, name="course-detail"),
]
