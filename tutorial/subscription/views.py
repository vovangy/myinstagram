from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from subscription.serializers import SubscriptionSerializer
from subscription.models import Subscrition
from rest_framework.decorators import api_view

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
def delete_comment_by_id(request, pk, format=None):
    """
    Удаляет подписку
    """
    subscription = get_object_or_404(Subscrition, id=pk)
    subscription.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)