from django.contrib import admin
from .models import Municipality


class MunicipalityAdmin(admin.ModelAdmin):
    search_fields = ['name', 'code']
    list_display = ['code', 'name']


admin.site.register(Municipality, MunicipalityAdmin)
