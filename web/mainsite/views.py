from django.template.loader import get_template
from django.http import HttpResponse
from datetime import datetime
from typing import Any

from .models import Post
from django.shortcuts import render


# Create your views here.


def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())  # type: Any
    return HttpResponse(html)


def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post is not None:
            html = template.render(locals())
            return HttpResponse(html)

    except:
        return redirect('/')
