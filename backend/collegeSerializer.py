from rest_framework import serializers
from .collegemodel import  TeacherData, Student, Login

class SDserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
class TDserializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherData
        fields = '__all__'
class LGserializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'

