from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from likeOnComment.serializers import LikeOnCommentSerializer
from likeOnComment.models import LikeOnComment
from rest_framework.decorators import api_view

@api_view(['Get'])
def get_like_on_comment_list(request, format=None):
    """
    Возвращает список лайков на комментарии
    """
    print('get')
    likeOnComment = LikeOnComment.objects.all()
    serializer = LikeOnCommentSerializer(likeOnComment, many=True)
    return Response(serializer.data)

@api_view(['Post'])
def post_like_on_comment(request, format=None):
    """
    Добавляет новый лайк на комментарий
    """
    print('post')
    print(request.data)
    serializer = LikeOnCommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['Get'])
def get_detail_by_id_like_on_comment(request, pk, format=None):
    likeOnComment = get_object_or_404(LikeOnComment, id=pk)
    if request.method == 'GET':
        """
        Возвращает информацию о лайке на комментарий
        """
        serializer = LikeOnCommentSerializer(likeOnComment)
        return Response(serializer.data)

@api_view(['Delete'])
def delete_like_on_comment_by_id(request, pk, format=None):
    """
    Удаляет лайк на комментарий
    """
    subscription = get_object_or_404(LikeOnComment, id=pk)
    subscription.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)