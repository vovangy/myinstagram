from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from app.serializers import MomentSerializer, CommentSerializer, LikeOnCommentSerializer, LikeOnMomentSerializer, SubscriptionSerializer, TagSerializer
from app.models import Moment, Comment, LikeOnComment, LikeOnMoment, Subscrition, Tag

@api_view(['Get'])
def get_moments_list(request, format=None):
    print(request.user.is_authenticated)
    """
    Возвращает список моментов
    """
    print('get')
    moments = Moment.objects.all()
    serializer = MomentSerializer(moments, many=True)
    return Response(serializer.data)

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

@api_view(['Get'])
def get_moments_list_by_owner_id(request, pk, format=None):
    print(request.user.is_authenticated)

    """
    Возвращает список моментов
    """
    print('get')
    moments = Moment.objects.filter(user_id=pk)
    serializer = MomentSerializer(moments, many=True)
    return Response(serializer.data)

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
    likeOnComment = get_object_or_404(LikeOnComment, id=pk)
    likeOnComment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

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
    likeOnMoment = get_object_or_404(LikeOnMoment, id=pk)
    likeOnMoment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['Get'])
def get_subscription_list(request, format=None):
    """
    Возвращает список подписок
    """
    print('get')
    subscriptions = Subscrition.objects.all()
    serializer = SubscriptionSerializer(subscriptions, many=True)
    return Response(serializer.data)

@api_view(['Post'])
def post_subscription(request, format=None):
    """
    Добавляет новую подписку
    """
    print('post')
    print(request.data)
    serializer = SubscriptionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['Get'])
def get_detail_by_id_subscription(request, pk, format=None):
    subscription = get_object_or_404(Subscrition, id=pk)
    if request.method == 'GET':
        """
        Возвращает информацию о подписке
        """
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data)

@api_view(['Delete'])
def delete_subscription_by_id(request, pk, format=None):
    """
    Удаляет подписку
    """
    subscription = get_object_or_404(Subscrition, id=pk)
    subscription.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

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
def delete_tag_by_id(request, pk, format=None):
    """
    Удаляет тег
    """
    tag = get_object_or_404(Tag, id=pk)
    tag.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)