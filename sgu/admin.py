from django.contrib import admin
from .models import Sgu


class SguAdmin(admin.ModelAdmin):
    search_fields = ['name', 'code']
    list_display = ['code', 'name']


admin.site.register(Sgu, SguAdmin)

