from django.urls import path
from core.views import( HomePageView, TeacherCreateView, TeacherListView, TeacherDeleteView,TeacherDetailView,TeacherUpdateView,
StudentCreateView, StudentListView)

urlpatterns = [ 
    #path('', views.home, name='home'),
    path('', HomePageView.as_view(), name='home'),

    
    path('teacher/list/', TeacherListView.as_view(), name='teacher.index'),
    path('teacher/create/', TeacherCreateView.as_view(), name='teacher.create'),
    path('teacher/<int:pk>/detail/', TeacherDetailView.as_view(), name='teacher.detail'),
    path('teacher/<int:pk>/edit/', TeacherUpdateView.as_view(), name='teacher.edit'),
    path('teacher/<int:pk>/detete/', TeacherDeleteView.as_view(), name='teacher.delete'),


    path('student/list/', StudentListView.as_view(), name='student.index'),
    path('student/create/', StudentCreateView.as_view(), name='student.create')
]