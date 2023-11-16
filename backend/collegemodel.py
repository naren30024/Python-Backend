from django.db import models


class TeacherData(models.Model):
    Name = models.CharField(max_length=100)
    Subject= models.CharField(max_length=100)
    Gender = models.CharField(max_length=11)
    Mobile= models.PositiveBigIntegerField()
    Email = models.EmailField()
    def __str__(self):
        return self.Name
class Student(models.Model):
    Name = models.CharField(max_length=100)
    Branch = models.CharField(max_length=100)
    Year = models.CharField(max_length=50)
    RollNo = models.CharField(max_length=10)
    Mobile = models.PositiveBigIntegerField()
    Email = models.EmailField()
    Father = models.CharField(max_length=100)
    Mother = models.CharField(max_length=100)
    ParentMobile = models.PositiveBigIntegerField()
    def __str__(self):
        return self.Name
class Login(models.Model):
    UserID = models.CharField(max_length=40)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.UserID
    