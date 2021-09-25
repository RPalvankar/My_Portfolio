from blog.models import Blog
from django.shortcuts import render,get_object_or_404
from blog.models import Blog

def all_blogs(request):
    blogs_Ritvik=Blog.objects.order_by('-date')
    return render(request,'blog/all_blogs.html',{'blogs_Ritvik':blogs_Ritvik})

def detail(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':blog})

