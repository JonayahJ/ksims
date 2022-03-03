# Contact models
from django.contrib import admin
from .models import Contact

# Contact Form
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'sent_date')
    list_display_link = ('id', 'name', 'subject')
    search_fields = ('name', 'email', 'sent_date')

admin.site.register(Contact, ContactAdmin)