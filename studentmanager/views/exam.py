from django.views import generic


class ExamView(generic.TemplateView):
    template_name = 'studentmanager/coming-soon.html'
