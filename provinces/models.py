from django.db import models
from regions.models import Region


class Province(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    old_names = models.CharField(max_length=200, null=True)
    # income_classification = models.CharField(max_length=4)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
