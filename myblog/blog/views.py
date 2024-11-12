from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all()

    return render(request,
                  'blog/post/list.html',
                  {'posts': posts}
                  )


def post_detail(request, id):
    try:
        post = Post.objects.get(id=id)

    except Post.DoesNotExist:
        raise Http404("<h2> Пост не найден </h2>")

    return render(request,
        'blog/post/detail.html',
        {'post': post}
    )
