from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from studentmanager.forms import CreateExamForm
from studentmanager.models import Exam


class ExamView(generic.ListView):
    queryset = Exam.objects.all()
    template_name = 'studentmanager/exam/exam_list.html'


class ExamCreateView(generic.CreateView):
    form_class = CreateExamForm
    template_name = 'studentmanager/exam/exam_create_form.html'
    success_url = reverse_lazy('studentmanager:exam')


class ExamDeleteView(generic.DeleteView):
    model = Exam
    template_name = 'studentmanager/exam/exam_confirm_delete.html'
    success_url = reverse_lazy('studentmanager:exam')

    def get_object(self):
        _exam_id = self.kwargs.get('id')
        return get_object_or_404(Exam, exam_id=_exam_id)
