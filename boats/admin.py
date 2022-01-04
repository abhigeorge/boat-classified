from django.contrib import admin
from .models import Boat
from django.utils.html import format_html

# Register your models here.
class BoatAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.boat_photo.url))

    thumbnail.short_description = 'Boat Image'
    list_display = ('id','thumbnail','boat_title','year','price','tax_status','condition','boat_location','is_featured')
    list_display_links = ('id','thumbnail','boat_title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'boat_title', 'city', 'make', 'model','fuel_type')
    list_filter = ('city', 'make', 'model', 'fuel_type')
admin.site.register(Boat, BoatAdmin)