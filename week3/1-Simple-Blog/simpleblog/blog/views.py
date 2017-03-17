from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import BlogPost, Tag
from .forms import BlogPostCreateModelForm
from . import services


def index(request):
    posts = BlogPost.objects.all()

    return render(request, 'blog/index.html', locals())


def create_blog_post(request):
    form = BlogPostCreateModelForm()

    if request.method == 'POST':
        form = BlogPostCreateModelForm(data=request.POST)

        if form.is_valid():
            services.create_blog_post(**form.cleaned_data)
            return redirect(reverse('blog:index'))

    return render(request, 'blog/create.html', locals())
