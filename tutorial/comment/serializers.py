from comment.models import Comment
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"#['id', 'content', 'user_id', 'pub_date'] переделать ко всем