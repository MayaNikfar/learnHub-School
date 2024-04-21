from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('careers/', views.careers, name='careers'),
path('blog/', views.blog, name='blog'),
path('login/', views.login, name='login'),
]