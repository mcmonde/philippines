from django.test import TestCase
from regions.models import Region
from provinces.models import Province
from .models import Municipality


class MunicipalityTestCase(TestCase):

    def setUp(self):
        region = Region.objects.create(name='New Region', code='0100000000')
        province = Province.objects.create(name='New Province', code='0100100000', region_id=region.id)
        Municipality.objects.create(name='New Municipality', code='0100101000', type='Mun', province_id=province.id)
        Municipality.objects.create(name='New City', code='0100102000', type='City', province_id=province.id)
        Municipality.objects.create(name='Sub Municipality', code='0100103000', type='SubMun', province_id=province.id)
        Municipality.objects.create(name='SGU', code='0100104000', type='SGU', province_id=province.id)

    def test_regions_creation(self):
        obj = Region.objects.get(name='New Region')
        self.assertEqual(obj.name, 'New Region')
        self.assertEqual(obj.code, '0100000000')

    def test_provinces_creation(self):
        obj = Province.objects.get(name='New Province')
        self.assertEqual(obj.name, 'New Province')
        self.assertEqual(obj.code, '0100100000')

    def test_municipalities_create_municipality(self):
        obj = Municipality.objects.get(name='New Municipality')
        self.assertEqual(obj.name, 'New Municipality')
        self.assertEqual(obj.code, '0100101000')
        self.assertEqual(obj.type, 'Mun')

    def test_municipalities_create_city(self):
        obj = Municipality.objects.get(name='New City')
        self.assertEqual(obj.name, 'New City')
        self.assertEqual(obj.code, '0100102000')
        self.assertEqual(obj.type, 'City')

    def test_municipalities_create_submun(self):
        obj = Municipality.objects.get(name='Sub Municipality')
        self.assertEqual(obj.name, 'Sub Municipality')
        self.assertEqual(obj.code, '0100103000')
        self.assertEqual(obj.type, 'SubMun')

    def test_municipalities_create_sgu(self):
        obj = Municipality.objects.get(name='SGU')
        self.assertEqual(obj.name, 'SGU')
        self.assertEqual(obj.code, '0100104000')
        self.assertEqual(obj.type, 'SGU')
