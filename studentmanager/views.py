from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .models import Student


class IndexView(generic.TemplateView):
    template_name = 'studentmanager/mainmenu.html'


class ResultView(generic.TemplateView):
    template_name = 'studentmanager/coming-soon.html'


class ExamView(generic.TemplateView):
    template_name = 'studentmanager/coming-soon.html'


class StudentView(generic.ListView):
    queryset = Student.objects.all()


class StudentCreate(generic.CreateView):
    model = Student
    fields = ['matriculation_number', 'name', 'birthday']


class StudentDelete(generic.DeleteView):
    model = Student
    success_url = reverse_lazy('studentmanager:student')

    def get_object(self):
        _matriculation_number = self.kwargs.get('id')
        return get_object_or_404(Student, matriculation_number=_matriculation_number)


def student(request):
    return HttpResponse('/student')


def exam(request):
    return HttpResponse('/exam')


def result(request):
    return HttpResponse('/result')
