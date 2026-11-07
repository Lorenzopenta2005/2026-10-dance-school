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
