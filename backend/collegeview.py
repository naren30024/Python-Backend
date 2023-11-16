from rest_framework.decorators import api_view
from rest_framework.response import Response
from  .collegemodel import TeacherData, Student
from .collegeSerializer import TDserializer,SDserializer,Login

@api_view(['POST'])
def student(request):
    serializer = SDserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=401)

@api_view(['POST'])
def teacher(request):
    serializer = TDserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=401)

@api_view(['GET'])
def getstudentdata(request):
    stud = Student.objects.all()
    serializer = SDserializer(stud, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def geteacherdata(request):
    teach = TeacherData.objects.all()
    serializer = TDserializer(teach, many=True)
    return Response(serializer.data) 
@api_view(['POST'])
def checklogin(request):
    UserID = request.data.get("UserID")
    password = request.data.get("password")
    result = Login.objects.filter(UserID = UserID , password=password)
    if(result):
        return Response({"status":200},status=200)
    else:
        return Response({"status":400})
