from django.contrib import admin
from .models import Listing

# Register your models here.
# List is a tuple, () can be not added on .
# error come from typo. 'is_pulished' not 'is_published'
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_pulished', 'list_date', 'doctor')
    list_display_links = ('id', 'title')
    list_filter = ('doctor', 'services')
    list_editable = ('is_pulished',)
    search_fields = ('title', 'description', 'doctor__name')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)