from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('project',views.project),
    path('postProject',views.postProject),
    path('viewProfile',views.viewProfile, name = 'viewProfile'),
    path('signup', views.sign_up),
]