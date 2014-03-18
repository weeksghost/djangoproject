from django.shortcuts import render

from homepage.models import FeaturedText, FeaturedVideo
from blog.models import Post

def homepage(request):
    featured = FeaturedText.objects.all().filter(active=True)

    try:
        featured
    except:
        pass

    posts = Post.objects.all().filter(published=True)
    extvideo = FeaturedVideo.objects.all().filter(active=True)

    template = 'homepage.html'

    context = {
        'featured':featured,
        'posts': posts,
        'embed':extvideo,
    }
    return render(request, template, context)
