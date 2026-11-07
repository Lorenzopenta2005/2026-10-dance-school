from django.views import generic

from schoolmanagement.models import School


class SchoolListView(generic.ListView):
    model = School


class SchoolDetailView(generic.DetailView):
    model = School
