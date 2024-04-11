from django.test import TestCase
from .models import Region

class BarangayTestCase(TestCase):

    def setUp(self):
        Region.objects.create(name='New Region', code='0100000000')

    def test_regions_creation(self):
        obj = Region.objects.get(name='New Region')
        self.assertEqual(obj.name, 'New Region')
        self.assertEqual(obj.code, '0100000000')
