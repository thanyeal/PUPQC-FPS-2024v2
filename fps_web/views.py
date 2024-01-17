from django.http import JsonResponse
from executive.models import TableTwo
from .serializers import TableTwoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def table_list(request, format=None):
    if request.method == 'GET':
        table2 = TableTwo.objects.all()
        serializer = TableTwoSerializer(table2, many=True)
        return Response(serializer.data)
        # return JsonResponse(serializer.data, safe=False) # Also, it can set a list into dictionary by using this format {'var': var2.data, safe=False}
    
    if request.method == 'POST':
        serializer = TableTwoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def table2_detail(request, id, format=None):
    try:
        tablez = TableTwo.objects.get(pk=id)
    except TableTwo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TableTwoSerializer(tablez)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TableTwoSerializer(tablez, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tablez.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)