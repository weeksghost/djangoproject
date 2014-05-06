from django.contrib import admin
from contact_us.models import Contact


class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contact, ContactAdmin)
