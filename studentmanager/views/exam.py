from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from studentmanager.forms import CreateExamForm
from studentmanager.models import Exam


class ExamView(generic.ListView):
    queryset = Exam.objects.all()


class ExamCreateView(generic.CreateView):
    form_class = CreateExamForm
    template_name = 'studentmanager/create_exam_form.html'
    success_url = reverse_lazy('studentmanager:exam')


class ExamDeleteView(generic.DeleteView):
    model = Exam
    success_url = reverse_lazy('studentmanager:exam')

    def get_object(self):
        _exam_id = self.kwargs.get('id')
        return get_object_or_404(Exam, exam_id=_exam_id)
