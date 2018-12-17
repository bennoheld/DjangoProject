from django.urls import path

from . import views

app_name = 'studentmanager'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('student/', views.StudentView.as_view(), name='student'),
    path('student/<int:id>/delete/', views.StudentDelete.as_view(), name='student-delete'),
    path('student/add/', views.StudentCreate.as_view(), name='add'),
    path('exam/', views.ExamView.as_view(), name='exam'),
    path('exam/add/', views.ExamCreateView.as_view(), name='exam-add'),
    path('exam/<int:id>/delete/', views.ExamDeleteView.as_view(), name='exam-delete'),
    path('result/', views.ResultView.as_view(), name='result'),
]
