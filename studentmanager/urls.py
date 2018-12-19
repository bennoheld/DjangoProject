from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'studentmanager'
urlpatterns = [
    path('', login_required(views.IndexView.as_view()), name='index'),
    path('student/',login_required( views.StudentView.as_view()), name='student'),
    path('student/<int:id>/delete/', views.StudentDelete.as_view(), name='student-delete'),
    path('student/add/', views.StudentCreate.as_view(), name='add'),
    path('exam/', views.ExamView.as_view(), name='exam'),
    path('exam/add/', views.ExamCreateView.as_view(), name='exam-add'),
    path('exam/<int:id>/delete/', views.ExamDeleteView.as_view(), name='exam-delete'),
    path('result/', views.ResultView.as_view(), name='result'),
    path('result/add', views.ResultCreateView.as_view(), name='result-add'),
    path('result/<int:exam_id>/<int:student_id>/delete', views.ResultDeleteView.as_view(), name='result-delete'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout')
]
