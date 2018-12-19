from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from . import views

app_name = 'studentmanager'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('student/', login_required(views.StudentView.as_view()), name='student'),
    path('student/<int:id>/delete/', login_required(views.StudentDelete.as_view()), name='student-delete'),
    path('student/add/', login_required(views.StudentCreate.as_view()), name='add'),
    path('exam/', login_required(views.ExamView.as_view()), name='exam'),
    path('exam/add/', login_required(views.ExamCreateView.as_view()), name='exam-add'),
    path('exam/<int:id>/delete/', login_required(views.ExamDeleteView.as_view()), name='exam-delete'),
    path('result/', login_required(views.ResultView.as_view()), name='result'),
    path('result/add', login_required(views.ResultCreateView.as_view()), name='result-add'),
    path('result/<int:exam_id>/<int:student_id>/delete', login_required(views.ResultDeleteView.as_view()),
         name='result-delete'),
    path('login/', LoginView.as_view(), {'next_page': settings.LOGIN_REDIRECT_URL}, name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]
