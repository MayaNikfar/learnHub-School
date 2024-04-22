from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('careers/', views.careers, name='careers'),
path('students/', views.students_index, name='index'),
path('students/<int:student_id>/', views.students_detail, name='detail'),
path('students/create/', views.StudentCreate.as_view(), name='students_create'),
path('students/<int:pk>/update/', views.StudentUpdate.as_view(), name='students_update'),
path('students/<int:pk>/delete/', views.StudentDelete.as_view(), name='students_delete'),
path('students/<int:student_id>/add_photo/', views.add_photo, name='add_photo'),
path('students/<int:student_id>/assoc_class/<int:class_id>/', views.assoc_class, name='assoc_class'),
path('students/<int:student_id>/unassoc_class/<int:class_id>/', views.unassoc_class, name='unassoc_class'),
path('classes/', views.ClassList.as_view(), name='classes_index'),
path('classes/<int:pk>/', views.ClassDetail.as_view(), name='classes_detail'),
path('classes/create/', views.ClassCreate.as_view(), name='classes_create'),
path('classes/<int:pk>/update/', views.ClassUpdate.as_view(), name='classes_update'),
path('classes/<int:pk>/delete/', views.ClassDelete.as_view(), name='classes_delete'),
path('accounts/signup/', views.signup, name='signup'),
]