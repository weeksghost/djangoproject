from django.shortcuts import render

from homepage.models import FeaturedText, FeaturedVideo
from blog.models import Post

def homepage(request):
    featured = FeaturedText.objects.all().filter(active=True).order_by('created')

    try:
        featured
    except:
        pass

    posts = Post.objects.all().filter(published=True).order_by('created')
    extvideo = FeaturedVideo.objects.all().filter(active=True).order_by('created')

    template = 'homepage.html'

    context = {
        'featured':featured,
        'posts': posts,
        'embed':extvideo,
    }
    return render(request, template, context)
