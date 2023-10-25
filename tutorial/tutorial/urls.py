from django.urls import include, path, re_path
from django.contrib import admin
from rest_framework import routers
import sys

import comment.views

sys.path.append('../users')
from moment import views as moment_views
from comment import views as comment_views
from subscription import views as subscription_views
from likeOnComment import views as likeOnComment_views
from likeOnMoment import  views as likeOnMoment_views
from tag import views as tag_views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    path(r'api/moments/', moment_views.get_moments_list, name='moments-list'),
    path(r'api/moments/post/', moment_views.post_moment, name='moments-post'),
    path(r'api/moments/<int:pk>/', moment_views.get_detail_by_id_moment, name='moment-detail'),

    path(r'api/comments/', comment_views.get_comments_list, name='comments-list'),
    path(r'api/comments/post/', comment_views.post_comment, name='comments-post'),
    path(r'api/comments/<int:pk>/', comment_views.get_detail_by_id_comment, name='comment-detail'),

    path(r'api/subscriptions/', subscription_views.get_subscription_list, name='subscriptions-list'),
    path(r'api/subscriptions/post/', subscription_views.post_subscription, name='subscriptions-post'),
    path(r'api/subscriptions/<int:pk>/', subscription_views.get_detail_by_id_subscription, name='subscription-detail'),

    path(r'api/likeoncomments/', likeOnComment_views.get_like_on_comment_list, name='likeOnComment-list'),
    path(r'api/likeoncomments/post/', likeOnComment_views.post_like_on_comment, name='likeOnComment-post'),
    path(r'api/likeoncomments/<int:pk>/', likeOnComment_views.get_detail_by_id_like_on_comment, name='likeOnComment-detail'),

    path(r'api/likeonmoments/', likeOnMoment_views.get_like_on_moment_list, name='likeOnMoment-list'),
    path(r'api/likeonmoments/post/', likeOnMoment_views.post_like_on_moment, name='likeOnMoment-post'),
    path(r'api/likeonmoments/<int:pk>/', likeOnMoment_views.get_detail_by_id_like_on_moment,
         name='likeOnMoment-detail'),

    path(r'api/tags/', tag_views.get_tags_list, name='tag-list'),
    path(r'api/tags/post/', tag_views.post_tag, name='tag-post'),
    path(r'api/tags/<int:pk>/', tag_views.get_detail_by_id_tag,
         name='tag-detail'),

    #path(r'api/users/<int:pk>/put/', views.put_detail, name='users-put'),
    #path(r'api/users/<int:pk>/delete/', views.delete_detail, name='users-delete'),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
