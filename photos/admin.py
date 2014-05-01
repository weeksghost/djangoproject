from django.contrib import admin

from djangoproject.admin_forms import OrderedFormSet
from photos.models import Photo, Gallery, PhotoOrder


class PhotoAdmin(admin.ModelAdmin):
    search_fields = ('name', 'caption')
    list_display = ('name', 'caption')


class PhotoOrderInline(admin.TabularInline):
    model = PhotoOrder
    formset = OrderedFormSet
    raw_id_fields = ('photo',)


class GalleryAdmin(admin.ModelAdmin):
    inlines = (PhotoOrderInline,)
    search_fields = ('name',)

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Gallery, GalleryAdmin)
