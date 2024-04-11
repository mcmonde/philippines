from django.db import models
from provinces.models import Province


class SubMunicipality(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    old_names = models.CharField(max_length=200, null=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
