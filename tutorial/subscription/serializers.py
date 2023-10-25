from subscription.models import Subscrition
from rest_framework import serializers

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscrition
        fields = ['id', 'user_id', 'subscriber_id', 'pub_date']