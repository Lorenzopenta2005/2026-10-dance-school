from django.urls import reverse_lazy
from django.views import generic

from school.models import Classroom, Course, DayOfTheWeek


class DayOfTheWeekListView(generic.ListView):
    model = DayOfTheWeek


class DayOfTheWeekDetailView(generic.DetailView):
    model = DayOfTheWeek


class ClassroomListView(generic.ListView):
    model = Classroom


class ClassroomDetailView(generic.DetailView):
    model = Classroom


class CourseListView(generic.ListView):
    model = Course


class CourseDetailView(generic.DetailView):
    model = Course


class CourseCreateView(generic.CreateView):
    model = Course
    fields = ["subject", "starting_hour", "day_of_the_week", "classroom", "school"]
    success_url = reverse_lazy("course_list")


class CourseUpdateView(generic.UpdateView):
    model = Course
    fields = ["subject", "starting_hour", "day_of_the_week", "classroom", "school"]

    def get_success_url(self):
        return reverse_lazy("course_detail", kwargs={"pk": self.object.pk})
