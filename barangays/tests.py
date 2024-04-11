from django.test import TestCase
from regions.models import Region
from provinces.models import Province
from municipalities.models import Municipality
from .models import Barangay


class BarangayTestCase(TestCase):
    def setUp(self):
        region = Region.objects.create(name='New Region', code='0100000000')
        province = Province.objects.create(name='New Province', code='0100100000', region_id=region.id)
        municipality = Municipality.objects.create(name='New Municipality', code='0100101000', type='Mun',
                                                   province_id=province.id)
        Barangay.objects.create(name='New Barangay', code='0100101001', municipality_id=municipality.id)

    def test_regions_creation(self):
        obj = Region.objects.get(name='New Region')
        self.assertEqual(obj.name, 'New Region')
        self.assertEqual(obj.code, '0100000000')

    def test_provinces_creation(self):
        obj = Province.objects.get(name='New Province')
        self.assertEqual(obj.name, 'New Province')
        self.assertEqual(obj.code, '0100100000')

    def test_municipalities_creation(self):
        obj = Municipality.objects.get(name='New Municipality')
        self.assertEqual(obj.name,'New Municipality')
        self.assertEqual(obj.code, '0100101000')
        self.assertEqual(obj.type, 'Mun')

    def test_barangays_creation(self):
        obj = Barangay.objects.get(name='New Barangay')
        self.assertEqual(obj.name,'New Barangay')
        self.assertEqual(obj.code, '0100101001')
