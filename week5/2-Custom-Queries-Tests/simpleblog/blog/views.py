from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import BlogPost, Tag
from .forms import BlogPostCreateModelForm, LoginForm
from . import services
from .decorators import anonymous_required


def index(request):
    if not request.session.get('counter'):
        request.session['counter'] = 0

    request.session['counter'] += 1

    posts = BlogPost.objects.all()

    return render(request, 'blog/index.html', locals())

@login_required(login_url=reverse_lazy('blog:login'))
def create_blog_post(request):
    form = BlogPostCreateModelForm()

    if request.method == 'POST':
        form = BlogPostCreateModelForm(data=request.POST)

        if form.is_valid():
            services.create_blog_post(**form.cleaned_data)
            return redirect(reverse('blog:index'))

    return render(request, 'blog/create.html', locals())


@anonymous_required(profile_url=reverse_lazy('blog:profile'))
def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            user = authenticate(**form.cleaned_data)

            if user is None:
                form.add_error(field='', error='No such user')
            else:
                login(request, user)

    return render(request, 'blog/login.html', locals())


@login_required(login_url=reverse_lazy('blog:index'))
def profile_view(request):
    return render(request, 'blog/profile.html', locals())



# login_required_views = [profile_view]


# for view in login_required_views:
#     fname = view.__name__
#     local_definitions = locals()

#     f = local_definitions.get(fname)

#     f = login_required(f)

#     local_definitions[fname] = f
