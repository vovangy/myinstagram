"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from app.views import get_subscription_moments_list, get_subscribers_on_by_user_id , get_subscribers_by_user_id ,get_user_id_by_username, get_moments_list, get_moments_list_by_owner_id, post_moment, get_comments_list, post_comment, get_detail_by_id_comment, get_subscription_list, post_subscription, get_detail_by_id_subscription, get_like_on_comment_list, post_like_on_comment, get_detail_by_id_like_on_comment, get_like_on_moment_list, get_detail_by_id_like_on_moment, get_tags_list, get_detail_by_id_tag, get_detail_by_id_moment, post_tag, delete_tag_by_id, put_detail_tag_by_id, post_like_on_moment, get_comments_by_moment_id
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'api/moments/', get_moments_list, name='moments-list'),
    path(r'api/subscription/moments/<int:pk>', get_subscription_moments_list, name='moments-list'),
    path(r'api/moments/<int:pk>', get_moments_list_by_owner_id, name='moments-list-by-owner-id'),

path(r'api/moments/post/', post_moment, name='moments-post'),

    path(r'api/comments/', get_comments_list, name='comments-list'),
    path(r'api/commentsbymoment/<int:pk>/', get_comments_by_moment_id, name='comments-by-moment-list'),
    path(r'api/comments/post/', post_comment, name='comments-post'),
    path(r'api/comments/<int:pk>/', get_detail_by_id_comment, name='comment-detail'),

    path(r'api/users/<str:username>/', get_user_id_by_username, name='user-detail-by-username'),

    path(r'api/subscriptions/', get_subscription_list, name='subscriptions-list'),
    path(r'api/subscriptions/user/<int:pk>', get_subscribers_on_by_user_id, name='subscriptions-list-user'),
    path(r'api/subscriptions/post/', post_subscription, name='subscriptions-post'),
    path(r'api/subscriptions/<int:pk>/', get_detail_by_id_subscription, name='subscription-detail'),
    path(r'api/subscribers/<int:user_id>/', get_subscribers_by_user_id, name='subscription-detail'),

    path(r'api/likeoncomments/', get_like_on_comment_list, name='likeOnComment-list'),
    path(r'api/likeoncomments/post/', post_like_on_comment, name='likeOnComment-post'),
    path(r'api/likeoncomments/<int:pk>/', get_detail_by_id_like_on_comment, name='likeOnComment-detail'),

    path(r'api/likeonmoments/', get_like_on_moment_list, name='likeOnMoment-list'),
    path(r'api/likeonmoments/post/', post_like_on_moment, name='likeOnMoment-post'),
    path(r'api/likeonmoments/<int:pk>/', get_detail_by_id_like_on_moment,
         name='likeOnMoment-detail'),

    path(r'api/tags/', get_tags_list, name='tag-list'),
    path(r'api/tags/post/', post_tag, name='tag-post'),
    path(r'api/tags/<int:pk>/', get_detail_by_id_tag, name='tag-detail'),

    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),

    #
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
