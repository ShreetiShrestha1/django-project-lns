from django.urls import path
from lmsapi.views import TeacherApiView,TeacherApiListCreateView,StudentApiView, StudentApiListCreateView  

urlpatterns = [

    # teacher API: for detail, update, delete, edit
    path('teacher/<int:pk>/detail/', TeacherApiView.as_view(), name='api.teacher.detail'),
    path('teacher/<int:pk>/update/', TeacherApiView.as_view(), name='api.teacher.update'),
    path('teacher/<int:pk>/delete/', TeacherApiView.as_view(), name='api.teacher.delete'), 
    path('teacher/<int:pk>/edit/', TeacherApiView.as_view(), name='api.teacher.edit'),
    
    # teacher api: for list and create
    path('teacher/list/', TeacherApiListCreateView.as_view(), name='api.teacher.list'),
    path('teacher/create/', TeacherApiListCreateView.as_view(), name='api.teacher.create'),

    # student API: for detail, update, delete, edit
    path('student/<int:pk>/detail/', StudentApiView.as_view(), name='api.student.detail'),
    path('student/<int:pk>/update/', StudentApiView.as_view(), name='api.student.update'),  
    path('student/<int:pk>/delete/', StudentApiView.as_view(), name='api.student.delete'),
    path('student/<int:pk>/edit/', StudentApiView.as_view(), name='api.student.edit'),

    # student api: for list and create
    path('student/list/', StudentApiListCreateView.as_view(), name='api.student.list'), 
    path('student/create/', StudentApiListCreateView.as_view(), name='api.student.create'),
]