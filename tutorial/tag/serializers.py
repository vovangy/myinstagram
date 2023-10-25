from tag.models import Tag
from rest_framework import serializers

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title', 'moment_id']