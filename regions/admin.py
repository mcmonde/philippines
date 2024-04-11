from django.contrib import admin

from barangays.models import Barangay
from cities.models import City
from municipalities.models import Municipality
from provinces.models import Province
from .models import Region


class RegionAdmin(admin.ModelAdmin):
    def count_provinces(self, obj):
        return Province.objects.filter(region=obj).count()

    def count_municipalities(self, obj):
        return Municipality.objects.filter(province__region=obj).count()

    def count_cities(self, obj):
        return City.objects.filter(province__region=obj).count()

    def count_barangays(self, obj):
        return Barangay.objects.filter(municipality__province__region=obj).count()

    count_barangays.short_description = 'Barangays'
    count_provinces.short_description = 'Provinces'
    count_municipalities.short_description = 'Municipalities'
    count_cities.short_description = "Cities"

    search_fields = ['name', 'code']
    list_display = ['code', 'name', 'count_provinces', 'count_cities', 'count_municipalities', 'count_barangays']


admin.site.register(Region, RegionAdmin)
