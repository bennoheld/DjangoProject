from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


class Student(models.Model):
    matriculation_number = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    birthday = models.DateField()

    def get_absolute_url(self):
        return reverse('studentmanager:student')

    def __str__(self):
        return str(self.matriculation_number)


class Exam(models.Model):
    exam_id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=500)
    date = models.DateField()

    def __str__(self):
        return str(self.exam_id)


class Result(models.Model):
    # No student should be able to be deleted as long as there are still results to show.
    matriculation_number = models.ForeignKey(Student, on_delete=models.PROTECT)
    # No student should be able to be deleted as long as there are still results to show.
    exam_id = models.ForeignKey(Exam, on_delete=models.PROTECT)
    grade = models.IntegerField(default=None, validators=[MaxValueValidator(6), MinValueValidator(1)])

    # Workaround for composite primary-key
    # Get Data using Result.objects.get(matriculation_number=”10”,exam_id=”125”)
    class Meta:
        unique_together = (('matriculation_number', 'exam_id'),)

    def __str__(self):
        return '{} - {}'.format(self.exam_id, self.matriculation_number)
