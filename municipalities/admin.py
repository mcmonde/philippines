from django.contrib import admin
from .models import Municipality


class MunicipalityAdmin(admin.ModelAdmin):
    search_fields = ['name', 'code']
    list_display = ['code', 'name', 'type']
    list_filter = ['type']


admin.site.register(Municipality, MunicipalityAdmin)
