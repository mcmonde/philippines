from django.contrib import admin
from .models import District


class DistrictAdmin(admin.ModelAdmin):
    search_fields = ['name', 'code']
    list_display = ['code', 'name']


admin.site.register(District, DistrictAdmin)
