"""
Import barrel for all views
"""
from django.db.models import Avg

from .exam import *
from .result import *
from .student import *


class IndexView(generic.TemplateView):
    template_name = 'studentmanager/landingpage.html'

    def get_context_data(self, **kwargs):
        """ add data for dashboardview to the context object"""
        context = super(IndexView, self).get_context_data(**kwargs)
        students = {'label': Student._meta.verbose_name_plural,
                    'count': Student.objects.count(),
                    'average': Result.objects.values('matriculation_number').annotate(
                        averageGrade=Avg('grade')).aggregate(Avg('averageGrade')).get('averageGrade__avg', 0.00),
                    'best': Result.objects.values('matriculation_number').annotate(averageGrade=Avg('grade')).order_by(
                        'averageGrade')[:1].first().get('averageGrade', 0.00),
                    'worst': Result.objects.values('matriculation_number').annotate(averageGrade=Avg('grade')).order_by(
                        '-averageGrade')[:1].first().get('averageGrade', 0.00)
                    }
        exams = {'label': Exam._meta.verbose_name_plural,
                 'count': Exam.objects.count(),
                 'average': Result.objects.values('exam_id').annotate(averageGrade=Avg('grade')).aggregate(
                     Avg('averageGrade')).get('averageGrade__avg', 0.00),
                 'best': Result.objects.values('exam_id').annotate(averageGrade=Avg('grade')).order_by('averageGrade')[
                         :1].first().get('averageGrade', 0.00),
                 'worst': Result.objects.values('exam_id').annotate(averageGrade=Avg('grade')).order_by(
                     '-averageGrade')[:1].first().get('averageGrade', 0.00)
                 }
        results = {'label': Result._meta.verbose_name_plural,
                   'count': Result.objects.count(),
                   'average': Result.objects.all().aggregate(Avg('grade')).get('grade__avg', 0.00),
                   'best': Result.objects.values('grade').order_by('grade').first().get('grade', 0.00),
                   'worst': Result.objects.values('grade').order_by('grade').last().get('grade', 0.00)
                   }
        context['data'] = [students, exams, results]
        return context
