from django.contrib import admin
from .models import City


class CityAdmin(admin.ModelAdmin):
    search_fields = ['name', 'code']
    list_display = ['code', 'name']


admin.site.register(City, CityAdmin)
