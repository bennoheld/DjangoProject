from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from studentmanager.forms import CreateStudentForm
from studentmanager.models import Student


class StudentView(generic.ListView):
    queryset = Student.objects.order_by('matriculation_number')
    template_name = 'studentmanager/student/student_list.html'


class StudentCreateView(generic.CreateView):
    form_class = CreateStudentForm
    template_name = 'studentmanager/student/student_form.html'
    success_url = reverse_lazy('studentmanager:student')


class StudentDeleteView(generic.DeleteView):
    model = Student
    template_name = 'studentmanager/student/student_confirm_delete.html'
    success_url = reverse_lazy('studentmanager:student')

    def get_object(self):
        _matriculation_number = self.kwargs.get('id')
        return get_object_or_404(Student, matriculation_number=_matriculation_number)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
            # Redirect to success_url
            return HttpResponseRedirect(success_url)
        except ProtectedError:
            context = self.get_context_data(
                object=self.object,
                error='Student konnte nicht gelöscht werden, da noch Ergebnisse für ihn eingetragen sind!'
            )
            return self.render_to_response(context)
