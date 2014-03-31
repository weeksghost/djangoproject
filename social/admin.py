from django.contrib import admin

from social.models import Social

class SocialAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields' : ('title', 'github_url', 'linkedin_url', 'twitter_url', 'facebook_url',)}),
    )
    list_display = ('title',)


admin.site.register(Social, SocialAdmin)
