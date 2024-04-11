from django.db import models

from municipalities.models import Municipality


class Barangay(models.Model):
    TYPES = (
        ('U', 'Urban'),
        ('R', 'Rural'),
    )
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    old_names = models.CharField(max_length=200, null=True)
    # type = models.CharField(max_length=2, choices=TYPES)

    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
