from django.urls import path
from blog import views #You could also write from . import views as we are in the same directory

app_name='blog'

urlpatterns=[
    path('blog/',views.all_blogs,name='all_blogs'),
    path('<int:blog_id>/',views.detail,name='detail'),
    
]