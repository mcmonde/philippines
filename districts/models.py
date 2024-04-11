from django.db import models


class District(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, null=True)
    old_names = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
