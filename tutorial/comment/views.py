from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from comment.serializers import CommentSerializer
from comment.models import Comment
from rest_framework.decorators import api_view

@api_view(['Get'])
def get_comments_list(request, format=None):
    """
    Возвращает список комментариев
    """
    print('get')
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['Post'])
def post_comment(request, format=None):
    """
    Добавляет новый комментарий
    """
    print('post')
    print(request.data)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['Get'])
def get_detail_by_id_comment(request, pk, format=None):
    comment = get_object_or_404(Comment, id=pk)
    if request.method == 'GET':
        """
        Возвращает информацию о комментарии
        """
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

@api_view(['Put'])
def put_detail_comment_by_id(request, pk, format=None):
    """
    Обновляет информацию о коментарии
    """
    comment = get_object_or_404(Comment, id=pk)
    serializer = CommentSerializer(comment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['Delete'])
def delete_comment_by_id(request, pk, format=None):
    """
    Удаляет комментарий
    """
    comment = get_object_or_404(Comment, id=pk)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)