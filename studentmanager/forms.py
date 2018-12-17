from django import forms

from .models import Student


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['matriculation_number', 'name', 'birthday']
        widgets = {
            'matriculation_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control'})
        }
