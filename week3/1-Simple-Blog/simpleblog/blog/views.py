from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html', locals())


def create_blog_post(request):
    return render(request, 'blog/create.html', locals())
