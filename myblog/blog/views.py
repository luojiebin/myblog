from django.shortcuts import render

from .models import Post, About


def index(request):
    return render(request, 'blog/index.html', {
        'posts': Post.published.recent_posts(5),
    })


def detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/detail.html', {
        'post': post,
    })


def year_archive(request):
    return render(request, 'blog/year_archive.html', {
        'year_posts': Post.published.year_carchive(),
    })


def about(request):
    about = About.objects.first().content
    return render(request, 'blog/about.html', {'about': about})
