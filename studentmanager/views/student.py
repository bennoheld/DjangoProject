from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from studentmanager.forms import CreateStudentForm
from studentmanager.models import Student


class StudentView(generic.ListView):
    queryset = Student.objects.all()


class StudentCreate(generic.CreateView):
    form_class = CreateStudentForm
    template_name = 'studentmanager/student_form.html'
    success_url = reverse_lazy('studentmanager:student')


class StudentDelete(generic.DeleteView):
    model = Student
    success_url = reverse_lazy('studentmanager:student')

    def get_object(self):
        _matriculation_number = self.kwargs.get('id')
        return get_object_or_404(Student, matriculation_number=_matriculation_number)
