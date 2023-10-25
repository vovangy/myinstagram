from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from moment.serializers import MomentSerializer
from moment.models import Moment
from rest_framework.decorators import api_view

@api_view(['Get'])
def get_moments_list(request, format=None):
    """
    Возвращает список моментов
    """
    print('get')
    moments = Moment.objects.all()
    serializer = MomentSerializer(moments, many=True)
    return Response(serializer.data)

#viewset

@api_view(['Post'])
def post_moment(request, format=None):
    """
    Добавляет новый момент
    """
    print('post')
    print(request.data)
    serializer = MomentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['Get'])
def get_detail_by_id_moment(request, pk, format=None):
    moment = get_object_or_404(Moment, id=pk)
    if request.method == 'GET':
        """
        Возвращает информацию о моменте
        """
        serializer = MomentSerializer(moment)
        return Response(serializer.data)

@api_view(['Put'])
def put_detail_moment_by_id(request, pk, format=None):
    """
    Обновляет информацию о моменте
    """
    moment = get_object_or_404(Moment, id=pk)
    serializer = MomentSerializer(moment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['Delete'])
def delete_moment_by_id(request, pk, format=None):
    """
    Удаляет информацию о моменте
    """
    moment = get_object_or_404(Moment, id=pk)
    moment.delete() #в жизни не удаляют из базы
    return Response(status=status.HTTP_204_NO_CONTENT)