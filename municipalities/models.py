from django.db import models
from provinces.models import Province


class Municipality(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    old_names = models.CharField(max_length=200, null=True)
    # city_class = models.CharField(max_length=4)
    # income_classification = models.CharField(max_length=4)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
