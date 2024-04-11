from django.test import TestCase
from regions.models import Region
from .models import Province


class RegionTestCase(TestCase):

    def setUp(self):
        region = Region.objects.create(name='New Region', code='0100000000')
        Province.objects.create(name='New Province', code='0100100000', region_id=region.id)

    def test_regions_creation(self):
        obj = Region.objects.get(name='New Region')
        self.assertEqual(obj.name, 'New Region')
        self.assertEqual(obj.code, '0100000000')

    def test_provinces_creation(self):
        obj = Province.objects.get(name='New Province')
        self.assertEqual(obj.name, 'New Province')
        self.assertEqual(obj.code, '0100100000')