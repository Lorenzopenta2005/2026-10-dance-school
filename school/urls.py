from django.urls import path

from school import views

urlpatterns = [
    path(
        "corsi/",
        views.CourseListView.as_view(),
        name="course_list",
    ),
    path(
        "corsi/<int:pk>/",
        views.CourseDetailView.as_view(),
        name="course_detail",
    ),
    path(
        "classi/",
        views.ClassroomListView.as_view(),
        name="classroom_list",
    ),
    path(
        "classi/<int:pk>/",
        views.ClassroomDetailView.as_view(),
        name="classroom_detail",
    ),
    path(
        "giorni/",
        views.DayOfTheWeekListView.as_view(),
        name="dayoftheweek_list",
    ),
    path(
        "giorni/<int:pk>/",
        views.DayOfTheWeekDetailView.as_view(),
        name="dayoftheweek_detail",
    ),
]
