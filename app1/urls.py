from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('student', views.student, name='student'),
   path('course', views.course, name='course'),
   path('create', views.create, name='create'),
   path('trainer', views.trainer, name='trainer'),
   path('',views.dashboard,name='dashboard'),
   path('dashboard',views.dashboard,name='dashboard'),
   path('trainerlo',views.trainerlo,name='trainerlo'),
   path('studentlo',views.studentlo,name='studentlo'),
   path('trainerlog',views.trainerlog,name='trainerlog'),
   path('studentlog',views.studentlog,name='studentlog'),
   
]

