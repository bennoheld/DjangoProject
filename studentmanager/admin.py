"""
Configure which models should be visible in the admin panel
"""

from django.contrib import admin

from .models import Student, Exam, Result

admin.site.register(Student)
admin.site.register(Exam)
admin.site.register(Result)
