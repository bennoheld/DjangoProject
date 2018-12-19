from django import forms

from .models import Student, Exam, Result


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['matriculation_number', 'name', 'birthday']
        widgets = {
            'matriculation_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control'})
        }


class CreateExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['exam_id', 'title', 'date']
        widgets = {
            'exam_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'})
        }


class CreateResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['exam_id', 'matriculation_number', 'grade']
        widgets = {
            'exam_id': forms.Select(choices=Exam.objects.all(), attrs={'class': 'form-control'}),
            'matriculation_number': forms.Select(choices=Student.objects.all(), attrs={'class': 'form-control'}),
            'grade': forms.NumberInput(attrs={'class': 'form-control'})
        }
