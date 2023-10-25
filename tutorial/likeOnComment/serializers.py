from likeOnComment.models import LikeOnComment
from rest_framework import serializers

class LikeOnCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeOnComment
        fields = ['id', 'user_id', 'comment_id', 'pub_date']