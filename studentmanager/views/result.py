from django.views import generic


class ResultView(generic.TemplateView):
    template_name = 'studentmanager/coming-soon.html'
