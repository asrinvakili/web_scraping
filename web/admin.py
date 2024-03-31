from django.contrib import admin
from web.models import house

# Register your models here.
admin.site.register(house)


class FilterTable(admin.ModelAdmin):
    fields = ('id', 'location', 'price', 'rooms', 'parking', 'metr')
    list_display = ('id', 'location', 'price', 'rooms', 'parking', 'metr')
    list_filter = ('id', 'price', 'rooms', 'parking', 'metr', 'location')
    search_fields = ('id', 'location', 'price', 'rooms', 'parking', 'metr')
    empty_value_display = '-empty-'
    date_hierarchy = ('id', 'location', 'price', 'rooms', 'parking', 'metr')
