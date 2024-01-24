from django.shortcuts import render

from .models import Post

# Create your views here.


def index(request):
    posts = Post.objects.all()
    return render(request=request, template_name="posts/index.html", context={"posts":posts})