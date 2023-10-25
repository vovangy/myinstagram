#import sys
#sys.path.append('../users')
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from users.serializers import UserSerializer
from users.models import User
from rest_framework.decorators import api_view

@api_view(['Get'])
def get_list(request, format=None):
    """
    Возвращает список пользователей
    """
    print('get')
    stocks = User.objects.all()
    serializer = UserSerializer(stocks, many=True)
    return Response(serializer.data)

@api_view(['Post'])
def post_list(request, format=None):
    """
    Добавляет нового пользователя
    """
    print('post')
    print(request.data)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['Get'])
def get_detail(request, pk, format=None):
    stock = get_object_or_404(User, id=pk)
    if request.method == 'GET':
        """
        Возвращает информацию о пользователе
        """
        serializer = UserSerializer(stock)
        return Response(serializer.data)

@api_view(['Put'])
def put_detail(request, pk, format=None):
    """
    Обновляет информацию о пользователе
    """
    user = get_object_or_404(User, id=pk)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['Delete'])
def delete_detail(request, pk, format=None):
    """
    Удаляет информацию о пользователе
    """
    user = get_object_or_404(User, id=pk)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
