from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, Context

from blog.models import Post


def blog_list(request):
    template_name = 'blog_list.html'
    posts = Post.objects.filter(published=True)
    return render(request, template_name, {'posts': posts})

def post(request, slug):
    template_post = 'post.html'
    post = get_object_or_404(Post, slug=slug)
    return render(request, template_post, {'post': post})
