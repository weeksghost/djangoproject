from homepage.models import FeaturedText, FeaturedVideo 
from django.contrib import admin

from django.utils.translation import ugettext_lazy as _
from markitup.widgets import AdminMarkItUpWidget


class FeaturedTextAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields' : ('active', 'featured_title', 'featured_subtitle', 'content', 'call_to_action', )}),
    )
    list_display = ('featured_title', 'active',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
                kwargs['widget'] = AdminMarkItUpWidget()
        return super(FeaturedTextAdmin, self).formfield_for_dbfield(db_field, **kwargs)


class FeaturedVideoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields' : ('active', 'title', 'embed_url',)}),
    )
    list_display = ('title', 'active',)

admin.site.register(FeaturedText, FeaturedTextAdmin)
admin.site.register(FeaturedVideo, FeaturedVideoAdmin)
