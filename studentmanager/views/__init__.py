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
                    'best': self.get_best_student(),
                    'worst': self.get_worst_student()
                    }
        exams = {'label': Exam._meta.verbose_name_plural,
                 'count': Exam.objects.count(),
                 'average': Result.objects.values('exam_id').annotate(averageGrade=Avg('grade')).aggregate(
                     Avg('averageGrade')).get('averageGrade__avg', 0.00),
                 'best': self.get_best_exam(),
                 'worst': self.get_worst_exam()
                 }
        results = {'label': Result._meta.verbose_name_plural,
                   'count': Result.objects.count(),
                   'average': Result.objects.all().aggregate(Avg('grade')).get('grade__avg', 0.00),
                   'best': self.get_best_result(),
                   'worst': self.get_worst_result()
                   }
        context['data'] = [students, exams, results]
        return context

    @staticmethod
    def get_best_student():
        """ try to get the best grade of all students"""
        best_grade = 0
        try:
            best_grade = Result.objects.values('matriculation_number').annotate(averageGrade=Avg('grade')).order_by(
                'averageGrade')[:1].first().get('averageGrade', 0.00)
        except AttributeError:
            pass
        return best_grade

    @staticmethod
    def get_worst_student():
        """ try to get the worst grade of all students"""
        worst_grade = 0
        try:
            worst_grade = best_grade = Result.objects.values('matriculation_number').annotate(averageGrade=Avg('grade')).order_by(
                '-averageGrade')[:1].first().get('averageGrade', 0.00)
        except AttributeError:
            pass
        return worst_grade

    @staticmethod
    def get_best_exam():
        """ try to get the best grade of all exams"""
        best_grade = 0
        try:
            best_grade = Result.objects.values('exam_id').annotate(averageGrade=Avg('grade')).order_by('averageGrade')[
                         :1].first().get('averageGrade', 0.00)
        except AttributeError:
            pass
        return best_grade

    @staticmethod
    def get_worst_exam():
        """ try to get the worst grade of all students"""
        worst_grade = 0
        try:
            worst_grade = Result.objects.values('exam_id').annotate(averageGrade=Avg('grade')).order_by(
                '-averageGrade')[:1].first().get('averageGrade', 0.00)
        except AttributeError:
            pass
        return worst_grade

    @staticmethod
    def get_best_result():
        """ try to get the best grade of all results"""
        best_grade = 0
        try:
            best_grade = Result.objects.values('grade').order_by('grade').first().get('grade', 0.00)
        except AttributeError:
            pass
        return best_grade

    @staticmethod
    def get_worst_result():
        """ try to get the worst grade of all students"""
        worst_grade = 0
        try:
            worst_grade = Result.objects.values('grade').order_by('grade').last().get('grade', 0.00)
        except AttributeError:
            pass
        return worst_grade
