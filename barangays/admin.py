from django.contrib import admin
from .models import Barangay


class BarangayAdmin(admin.ModelAdmin):
    search_fields = ['name', 'code']
    list_display = ['code', 'name']


admin.site.register(Barangay, BarangayAdmin)
