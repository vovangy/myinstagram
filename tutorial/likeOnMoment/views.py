from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from likeOnMoment.serializers import LikeOnMomentSerializer
from likeOnMoment.models import LikeOnMoment
from rest_framework.decorators import api_view

@api_view(['Get'])
def get_like_on_moment_list(request, format=None):
    """
    Возвращает список лайков на моменты
    """
    print('get')
    likeOnMoment = LikeOnMoment.objects.all()
    serializer = LikeOnMomentSerializer(likeOnMoment, many=True)
    return Response(serializer.data)

@api_view(['Post'])
def post_like_on_moment(request, format=None):
    """
    Добавляет новый лайк на момент
    """
    print('post')
    print(request.data)
    serializer = LikeOnMomentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['Get'])
def get_detail_by_id_like_on_moment(request, pk, format=None):
    likeOnMoment = get_object_or_404(LikeOnMoment, id=pk)
    if request.method == 'GET':
        """
        Возвращает информацию о лайке на момент
        """
        serializer = LikeOnMomentSerializer(likeOnMoment)
        return Response(serializer.data)

@api_view(['Delete'])
def delete_like_on_moment_by_id(request, pk, format=None):
    """
    Удаляет лайк на комментарий
    """
    subscription = get_object_or_404(LikeOnMoment, id=pk)
    subscription.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)