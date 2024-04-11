from django.test import TestCase
from .models import Barangay


class BarangayTestCase(TestCase):
    def setUp(self):
        Barangay.objects.create(name='New Barangay', code='0101010101',)