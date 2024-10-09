from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from .models import Blog
# Create your views here.

def index(request):
    blogs=Blog.objects.raw("SELECT * FROM posts_blog")
    print(blogs)
    return render(request, 'index.html',{'posts':blogs})  



def post(request, pk):
    blogs = Blog.objects.get(id=pk)
    return render(request, 'post.html', {'posts': blogs})

