from django.db import models

class jobseeker_registration(models.Model):
    
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Phone = models.BigIntegerField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.Name
