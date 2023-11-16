from rest_framework import serializers
from .crudmodel import details_crud

class dcserializer(serializers.ModelSerializer):
    class Meta:
        model = details_crud
        fields = '__all__'
        