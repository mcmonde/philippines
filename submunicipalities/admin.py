from django.contrib import admin
from .models import SubMunicipality


class SubMunicipalityAdmin(admin.ModelAdmin):
    search_fields = ['name', 'code']
    list_display = ['code', 'name']


admin.site.register(SubMunicipality, SubMunicipalityAdmin)
