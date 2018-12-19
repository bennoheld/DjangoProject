from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse_lazy

from studentmanager.forms import CreateResultForm
from studentmanager.models import Result


class ResultView(generic.ListView):
    queryset = Result.objects.order_by('exam_id')
    template_name = 'studentmanager/result/result_list.html'


class ResultCreateView(generic.CreateView):
    form_class = CreateResultForm
    template_name = 'studentmanager/result/result_create_form.html'
    success_url = reverse_lazy('studentmanager:result')


class ResultDeleteView(generic.DeleteView):
    model = Result
    template_name = 'studentmanager/result/result_confirm_delete.html'
    success_url = reverse_lazy('studentmanager:result')

    def get_object(self):
        _exam_id = self.kwargs.get('exam_id')
        _matriculation_number = self.kwargs.get('student_id')
        return get_object_or_404(Result, exam_id=_exam_id, matriculation_number = _matriculation_number)
