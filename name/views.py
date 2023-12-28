from django.http import JsonResponse
from .models import name
from .serializers import nameserl
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
@api_view(['GET','POST'])
def name_list(request,format = None):
    if request.method == 'GET':
        n = name.objects.all()
        serializer = nameserl(n, many=True)
        return JsonResponse(serializer.data , safe=False)
    if request.method == 'POST':
        serializer = nameserl(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
@api_view(['GET','PUT','DELETE'])        
def name_detail(request , id , format = None):
    
    try:
        n = name.objects.get(pk=id)
    except name.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = nameserl(n)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = nameserl(n , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        n.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)