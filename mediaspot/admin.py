from django.contrib import admin
from mediaspot.models import MediaFile

class MediaFileAdmin(admin.ModelAdmin):
    list_display = ['name',]

admin.site.register(MediaFile, MediaFileAdmin)
