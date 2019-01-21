"""
Collection of all custom created Forms to use in the Create and Delete View
"""

from django import forms

from .models import Student, Exam, Result


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student  # model to create
        fields = ['matriculation_number', 'name', 'birthday']  # visible form fields, use model attributes

        # specify the input types for each field to use form validation
        # use attrs to store css class for bootstrap
        widgets = {
            'matriculation_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control'})
        }


class CreateExamForm(forms.ModelForm):
    class Meta:
        model = Exam  # model to create
        fields = ['exam_id', 'title', 'date']  # visible form fields, use model attributes

        # specify the input types for each field to use form validation
        # use attrs to store css class for bootstrap
        widgets = {
            'exam_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'})
        }


class CreateResultForm(forms.ModelForm):
    class Meta:
        model = Result  # model to create
        fields = ['exam_id', 'matriculation_number', 'grade']  # visible form fields, use model attributes

        # specify the input types for each field to use form validation
        # use attrs to store css class for bootstrap
        widgets = {
            'exam_id': forms.Select(choices=Exam.objects.all(), attrs={'class': 'form-control'}),
            'matriculation_number': forms.Select(choices=Student.objects.all(), attrs={'class': 'form-control'}),
            'grade': forms.NumberInput(attrs={'class': 'form-control'})
        }
