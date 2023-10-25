# from django.contrib.auth.models import User, Group
from moment.models import Moment
from rest_framework import serializers

class MomentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moment
        fields = ['id', 'title', 'content', 'user_id', 'pub_date', 'photo_path']