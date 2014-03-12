from django.contrib import admin
from blog.models import Post

from markitup.widgets import AdminMarkItUpWidget


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['published', 'created']
    search_fields = ['title', 'description', 'content']
    date_hierarchy = 'created'
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
                kwargs['widget'] = AdminMarkItUpWidget()
        return super(PostAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Post, PostAdmin)
