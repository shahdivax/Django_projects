from django.urls import path
from . import urls
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about.html',views.about,name='about'),
    path('index.html',views.index,name='index'),
    path('projects.html',views.projects,name='proj'),
    path('blog.html',views.blog,name='blog'),
    path('contact.html',views.contact,name='contact')
    
]
