from django.shortcuts import render

from homepage.models import FeaturedText, FeaturedVideo
from blog.models import Post

def homepage(request):
    featured = FeaturedText.objects.all().order_by('featured_title', 'featured_subtitle', 'content', 'call_to_action').filter(active=True)

    try:
        featured
    except:
        pass

    posts = Post.objects.all().filter(published=True)
    extvideo = FeaturedVideo.objects.all().order_by('title', 'embed_url').filter(active=True)

    template = 'homepage.html'

    context = {
        'featured':featured,
        'posts': posts,
        'embed':extvideo,
    }
    return render(request, template, context)
