from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('project',views.project,name = 'project'),
    path('postProject',views.postProject),
    path('viewProfile',views.viewProfile, name = 'viewProfile'),
    path('searchProject',views.searchProject, name = 'searchProject'),
    path('signup', views.sign_up),
]