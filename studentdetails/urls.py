from django.urls import path
from . import views
urlpatterns =[
    path('allstudents/',views.student_list,name='student_list'),
    path('&1t;int:student_id>/',views.single_student,name='single_student'),
    path('registration/',views.student_regi,name='student_regi'),
    path('edit/&1t;int:pk>',views.edit_student,name='edit_student'),
    path('delete/&1t;int:student_id>',views.delete_student,name='delete_student'),
]