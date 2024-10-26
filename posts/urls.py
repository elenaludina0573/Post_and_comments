from django.urls import path
from rest_framework.routers import DefaultRouter

from posts.apps import PostConfig
from posts.views import PostCreateAPIView, PostRetrieveAPIView, PostUpdateAPIView, PostDestroyAPIView, PostListAPIView, \
    CommentListAPIView

app_name = PostConfig.name
router = DefaultRouter()

urlpatterns = [
    path('post/', PostListAPIView.as_view(), name='post_list'),
    path('post/create/', PostCreateAPIView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostRetrieveAPIView.as_view(), name='post_retrieve'),
    path('post/<int:pk>/update/', PostUpdateAPIView.as_view(), name='post_update'),
    path('post/<int:pk>/delete', PostDestroyAPIView.as_view(), name='post_delete'),
    path('comment/', CommentListAPIView.as_view(), name='comment_list'),
    path('comment/create/', PostCreateAPIView.as_view(), name='comment_create'),
    path('comment/<int:pk>/', PostRetrieveAPIView.as_view(), name='comment_retrieve'),
    path('comment/<int:pk>/update/', PostUpdateAPIView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete', PostDestroyAPIView.as_view(), name='comment_delete'),
] + router.urls
