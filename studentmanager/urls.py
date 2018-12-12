from django.urls import path

from . import views

app_name = 'studentmanager'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('student/', views.StudentView.as_view(), name='student'),
    path('student/<int:id>/delete/', views.StudentDelete.as_view(), name='student-delete'),
    path('add/', views.StudentCreate.as_view(), name='add'),
    path('exam/', views.ExamView.as_view(), name='exam'),
    path('result/', views.ResultView.as_view(), name='result'),
]
