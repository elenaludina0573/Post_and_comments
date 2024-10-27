from django.urls import path
from rest_framework.routers import DefaultRouter

from posts.apps import PostConfig
from posts.views import PostCreateAPIView, PostRetrieveAPIView, PostUpdateAPIView, PostDestroyAPIView, PostListAPIView, \
    CommentListAPIView

app_name = PostConfig.name
router = DefaultRouter()

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='post_list'),
    path('posts/create/', PostCreateAPIView.as_view(), name='post_create'),
    path('posts/<int:pk>/', PostRetrieveAPIView.as_view(), name='post_retrieve'),
    path('posts/<int:pk>/update/', PostUpdateAPIView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDestroyAPIView.as_view(), name='post_delete'),
    path('comments/', CommentListAPIView.as_view(), name='comment_list'),
    path('comments/create/', PostCreateAPIView.as_view(), name='comment_create'),
    path('comments/<int:pk>/', PostRetrieveAPIView.as_view(), name='comment_retrieve'),
    path('comments/<int:pk>/update/', PostUpdateAPIView.as_view(), name='comment_update'),
    path('comments/<int:pk>/delete/', PostDestroyAPIView.as_view(), name='comment_delete'),
] + router.urls
