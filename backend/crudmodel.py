from django.db import models

class details_crud(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.PositiveBigIntegerField()
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.name