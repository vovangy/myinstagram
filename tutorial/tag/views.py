from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from tag.serializers import TagSerializer
from tag.models import Tag
from rest_framework.decorators import api_view

@api_view(['Get'])
def get_tags_list(request, format=None):
    """
    Возвращает список тегов
    """
    print('get')
    tags = Tag.objects.all()
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)

@api_view(['Post'])
def post_tag(request, format=None):
    """
    Добавляет новый тег
    """
    print('post')
    print(request.data)
    serializer = TagSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['Get'])
def get_detail_by_id_tag(request, pk, format=None):
    comment = get_object_or_404(Tag, id=pk)
    if request.method == 'GET':
        """
        Возвращает информацию о комментарии
        """
        serializer = TagSerializer(comment)
        return Response(serializer.data)

@api_view(['Put'])
def put_detail_tag_by_id(request, pk, format=None):
    """
    Обновляет информацию о теге
    """
    tag = get_object_or_404(Tag, id=pk)
    serializer = TagSerializer(tag, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['Delete'])
def delete_comment_by_id(request, pk, format=None):
    """
    Удаляет тег
    """
    tag = get_object_or_404(Tag, id=pk)
    tag.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)