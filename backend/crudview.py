from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import  status
from .crudmodel import details_crud
from .crudserializer import dcserializer

@api_view(['GET', 'POST'])
def item_list(request):
    if request.method == 'GET':
        items = details_crud.objects.all()
        serializer = dcserializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = dcserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def item_detail(request, pk):
    try:
        item = details_crud.objects.get(pk=pk)
    except details_crud.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = dcserializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = dcserializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

