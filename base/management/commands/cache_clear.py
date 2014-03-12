from django.core.cache import cache
from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    help="Clear memcached"

    def handle_noargs(self, **options):
        try:
            cache.clear()
        except:
            print 'Unable to clear memcache'
