from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.filter(author__username__icontains="Pancho")
    return render(request, 'blog/post_list.html', {'posts':posts})
