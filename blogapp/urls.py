from django.urls import path
from .views import PostCreate, PostDetail, CommentCreate

urlpatterns = [
    path('posts/', PostCreate.as_view(), name='post_create'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('posts/<int:post_id>/comments/', CommentCreate.as_view(), name='comment_create'),
]