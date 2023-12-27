from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from app.models import Moment, Comment, LikeOnMoment, LikeOnComment, Subscrition, Tag
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'username', 'password']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserSerializerList(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "image_url"]

class UserSerializerPhoto(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "image_url"]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class LikeOnCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeOnComment
        fields = "__all__"

class LikeOnMomentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeOnMoment
        fields = "__all__"

class MomentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moment
        fields = "__all__"

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscrition
        fields = "__all__"

class SubscriptionSerializerMinimal(serializers.ModelSerializer):
    class Meta:
        model = Subscrition
        fields = ["user_id", "subscriber_id"]

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
