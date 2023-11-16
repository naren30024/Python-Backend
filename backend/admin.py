from django.contrib import admin
from .models import Registration
from .crudmodel import details_crud
from .collegemodel import TeacherData, Student,Login

# Register your models here.
admin.site.register(Registration)
admin.site.register(details_crud)
admin.site.register(Student)
admin.site.register(TeacherData)
admin.site.register(Login)