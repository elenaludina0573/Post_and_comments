from rest_framework import serializers
from posts.models import Post, Comment
from posts.validators import TitleValidator, AuthorValidator


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'created_at', 'author', 'updated_at']
        validators = [TitleValidator(field='title'), AuthorValidator(field='author')]


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'created_at', 'updated_at', 'author', 'post']
