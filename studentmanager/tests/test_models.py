from django.test import TestCase

from studentmanager.models import Student, Exam, Result


class StudentModelTest(TestCase):

    def test_string_representation(self):
        student = Student(matriculation_number=1001)
        self.assertEqual(str(student), '1001')


class ExamModelTest(TestCase):

    def test_string_representation(self):
        exam = Exam(exam_id=1001)
        self.assertEqual(str(exam), '1001')


class ResultModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create Student and Exam for the Result
        Student.objects.create(matriculation_number=1005, name='John Doe', birthday='1995-10-16')
        Exam.objects.create(exam_id=1007, title='Test Exam', date='2019-02-13')

    def test_string_representation(self):
        result = Result(matriculation_number=Student.objects.get(matriculation_number=1005),
                        exam_id=Exam.objects.get(exam_id=1007))
        self.assertEqual(str(result), '1007 - 1005')
