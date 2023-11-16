from rest_framework import serializers
from .models import Registration


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'
# class UploadS(serializers.ModelSerializer):
#     class Meta:
#         model = Upload
#         fields = '__all__'