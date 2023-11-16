from django.shortcuts import render
from rest_framework import generics, response
from .models import Registration
from .serializers import RegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
# Create your views here.
@api_view(['POST'])
def register(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=401)
@api_view(['GET'])
def registration_data(request):
    registration = Registration.objects.all()
    serializer = RegistrationSerializer(registration, many=True)
    return Response(serializer.data)
@api_view(['POST'])
def loginpage(request):
    email = request.data.get('email')
    password = request.data.get('password')
    logindata1 = Registration.objects.filter(email=email,password=password)
    if logindata1:
        logindata = Registration.objects.get(email=email,password=password)
        serializer = {"first_name":logindata.first_name,"last_name":logindata.last_name,"email":logindata.email,"password":logindata.password}
        return Response({"data":[serializer]}, status=200)
    return Response({"error":"user not exist"}, status=400)
# @api_view(['GET'])
# def upload(request, file_id):
#     try:
#         file = Upload.objects.get(id=file_id)
#     except Upload.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     file_path = file.file.path
#     with open(file_path, 'rb') as file_content:
#         response = HttpResponse(file_content.read(), content_type='application/octet-stream')
#         response['Content-Disposition'] = f'attachment; filename="{file.name}"'
#         return response


