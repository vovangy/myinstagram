from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status, viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from app.serializers import UserSerializerPhoto, UserSerializerList, SubscriptionSerializerMinimal, UserSerializer, MomentSerializer, CommentSerializer, LikeOnCommentSerializer, LikeOnMomentSerializer, SubscriptionSerializer, TagSerializer
from app.models import Moment, Comment, LikeOnComment, LikeOnMoment, Subscrition, Tag, User
import json

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializerList
    def get_queryset(self):
        username = self.request.query_params.get('username', '')
        return User.objects.filter(username__icontains=username)

class MomentsViewSet(viewsets.ModelViewSet):
    serializer_class = MomentSerializer
    def get_queryset(self):
        offset = self.request.query_params.get('offset', 0)
        count = self.request.query_params.get('count', 5)
        pk = str(self.kwargs.get('pk'))
        sub_users = User.objects.filter(id__in=list(map(lambda x: x["subscriber_id"],list(Subscrition.objects.filter(user_id=pk, is_deleted=False).values("subscriber_id"))))).values_list("id")
        moments = Moment.objects.get_subscriptions(list(sub_users))
        queryset = moments
        queryset = queryset[int(offset):(int(count)+int(offset))]
        return queryset

@api_view(['Get'])
def get_user_id_by_username(request, username, format=None):
    user = get_object_or_404(User, username=username)
    #print(json.loads(request.body))
    if request.method == 'GET':
        """
        Возвращает информацию о моменте
        """
        return Response(user.id)


@api_view(['Get'])
def get_is_subscribed(request, user_id, main_user_id, format=None):
    subscription = Subscrition.objects.filter(user_id=main_user_id, subscriber_id=user_id)
    if (subscription):
        if list(subscription)[0].is_deleted == False:
            return Response(True)
        else:
            return Response(False)
    else:
        return Response(False)

@api_view(['Get'])
def get_is_liked(request, user_id, moment_id, format=None):
    like = LikeOnMoment.objects.filter(user_id=user_id, moment_id=moment_id)
    if (like):
        print(like)
        if list(like)[0].is_deleted == False:
            return Response(True)
        else:
            return Response(False)
    else:
        return Response(False)

@api_view(['Get'])
def get_count_likes(request, moment_id, format=None):
    like = LikeOnMoment.objects.filter(moment_id=moment_id, is_deleted=False)
    if (like):
        return Response(like.count())
    else:
        return Response(0)
@api_view(['Get'])
def get_username_by_user_id(request, user_id, format=None):
    print("TUT")
    user = get_object_or_404(User, id=user_id)
    if request.method == 'GET':
        """
        Возвращает информацию о моменте
        """
        return Response(user.username)

@api_view(['Get'])
def get_subscribers_by_user_id(request, user_id, format=None):
    #print(json.loads(request.body))
    if request.method == 'GET':
        """
        Возвращает информацию о моменте
        """
        print('get')
        #print(list(map(lambda x: x["subscriber_id"],list(Subscrition.objects.filter(user_id=1).values("subscriber_id")))))
        users = User.objects.filter(id__in=list(map(lambda x: x["subscriber_id"],list(Subscrition.objects.filter(user_id=user_id, is_deleted=False).values("subscriber_id")))))
        serializer = UserSerializerList(users, many=True)
        return Response(serializer.data)

@api_view(['Get'])
def get_photo_by_user_id(request, user_id, format=None):
    #print(json.loads(request.body))
    if request.method == 'GET':
        """
        Возвращает информацию о моменте
        """
        print('get')
        user = User.objects.filter(id=user_id)
        return Response(user.values("image_url", "username"))

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

@api_view(['Get'])
def get_subscription_moments_list(request, pk, format=None):
    print(request.user.is_authenticated)
    """
    Возвращает список моментов
    """
    print('get')
    moments = Moment.objects.filter(user_id__in=list(
        map(lambda x: x["user_id"], list(Subscrition.objects.filter(subscriber_id=pk).values("user_id"))))).order_by("pub_date").reverse()
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
    moments = Moment.objects.filter(user_id=pk).order_by("-pub_date")
    serializer = MomentSerializer(moments, many=True)
    return Response(serializer.data)

@api_view(['Get'])
def get_comments_list(request, format=None):
    """
    Возвращает список комментариев
    """
    print('get')
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['Get'])
def get_comments_by_moment_id(request, pk, format=None):
    """
    Возвращает список комментариев по моменту
    """
    print('get')
    comments = Comment.objects.filter(moment_id=pk)
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
    print('post')
    print(request.data)
    serializer = LikeOnMomentSerializer(data=request.data)
    like = LikeOnMoment.objects.filter(user_id=request.data["user_id"],
                                              moment_id=request.data["moment_id"])
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif (like):
        sub = LikeOnMoment.objects.get(id=list(like)[0].id)
        if sub.is_deleted == False:
            print("Tut")
            sub.is_deleted = True
        else:
            sub.is_deleted = False
        sub.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

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

@api_view(['Get'])
def get_subscribers_on_by_user_id(request, pk, format=None):
    """
    Возвращает список подписок
    """
    print('get')
    users = User.objects.filter(id__in=list(
        map(lambda x: x["user_id"], list(Subscrition.objects.filter(subscriber_id=pk).values("user_id")))))
    serializer = UserSerializerList(users, many=True)
    return Response(serializer.data)

@api_view(['Post'])
def post_subscription(request, format=None):
    """
    Добавляет новую подписку
    """
    print('post')
    print(request.data)
    serializer = SubscriptionSerializer(data=request.data)
    subscription = Subscrition.objects.filter(user_id=request.data["user_id"], subscriber_id=request.data["subscriber_id"])
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif (subscription):
        sub = Subscrition.objects.get(id=list(subscription)[0].id)
        if sub.is_deleted == False:
            print("Tut")
            sub.is_deleted = True
        else:
            sub.is_deleted = False
        sub.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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