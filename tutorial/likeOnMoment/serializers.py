from likeOnMoment.models import LikeOnMoment
from rest_framework import serializers

class LikeOnMomentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeOnMoment
        fields = ['id', 'user_id', 'moment_id', 'pub_date']