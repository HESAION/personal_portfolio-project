from django.shortcuts import render, get_object_or_404
from .models import MyBlog


def all_blogs(request):
    blog = MyBlog.objects.order_by("-date")
    return render(request, "blog/all_blogs.html", {'blogs': blog})


def detail(request, blog_id):
    blog = get_object_or_404(MyBlog, pk=blog_id)
    return render(request, "blog/detail.html", {'blog': blog})
