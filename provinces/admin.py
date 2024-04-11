from django.contrib import admin
from .models import Province


class ProvinceAdmin(admin.ModelAdmin):
    search_fields = ['name', 'code']
    list_display = ['code', 'name']


admin.site.register(Province, ProvinceAdmin)
