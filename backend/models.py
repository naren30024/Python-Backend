from django.db import models

class Registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    

    def __str__(self):
        return self.email
# class Upload(models.Model):
#     name = models.CharField(max_length=100)
#     resume = models.FileField(upload_to='uploads/')

#     def __str__(self):
#         return  self.name
    