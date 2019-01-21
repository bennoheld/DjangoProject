"""
Views related to Result
"""

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from studentmanager.forms import CreateResultForm
from studentmanager.models import Result


class ResultListView(generic.ListView):
    queryset = Result.objects.order_by('exam_id')  # get data for table
    template_name = 'studentmanager/result/result_list.html'  # template to render


class ResultCreateView(generic.CreateView):
    form_class = CreateResultForm  # form class to render in template
    template_name = 'studentmanager/result/result_create_form.html'  # template to render
    success_url = reverse_lazy('studentmanager:result')  # redirect to url after creation


class ResultDeleteView(generic.DeleteView):
    model = Result  # set model to delete
    template_name = 'studentmanager/result/result_confirm_delete.html'  # template to render
    success_url = reverse_lazy('studentmanager:result')  # redirect to url after creation

    def get_object(self):
        """get result by exam_id and matriculation using the exam_id and student_id URL parameter"""

        # extract the exam_id and student_id from the keyword-arguments to use them as query parameters
        _exam_id = self.kwargs.get('exam_id')
        _matriculation_number = self.kwargs.get('student_id')

        # try to get the result by exam_id and matriculation_number or raise Error 404.
        return get_object_or_404(Result, exam_id=_exam_id, matriculation_number=_matriculation_number)
