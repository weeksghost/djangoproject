from django.contrib import admin
from portfolio.models import Work


class WorkAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['created']
    search_fields = ['tite', 'description', 'content']
    date_hierarchy = 'created'
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Work, WorkAdmin)
