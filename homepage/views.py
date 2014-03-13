from django.shortcuts import render

from homepage.models import FeaturedText, HomeWidget, FeaturedVideo
from blog.models import Post

def homepage(request):
    # For main text on homepage
    featured_text = FeaturedText.objects.all()
    featured = featured_text.order_by('featured_title', 'featured_subtitle', 'content', 'call_to_action').filter(active=True)[:1]

    try:
        featured
    except:
        pass

    # For blog entries in home widgets
    posts = Post.objects.all().filter(published=True)
    # Had to do this becuase of original grid layout
    third_post = Post.objects.order_by('created').filter(published=True)

    # For video on homepage
    video = FeaturedVideo.objects.all()
    extvideo = video.order_by('title', 'embed_url').filter(active=True)[:1]

    template = 'homepage.html'

    context = {
        'featured':featured,
        'posts': posts,
        'third': third_post,
        'embed':extvideo,
    }
    return render(request, template, context)
