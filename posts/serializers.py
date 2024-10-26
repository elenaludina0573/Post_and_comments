from rest_framework import serializers
from posts.models import Post, Comment
from posts.validators import TitleValidator, AuthorValidator


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'created_at', 'author', 'updated_at']
        validators = [TitleValidator(field='title'), AuthorValidator(field='autor')]


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'text', 'created_at', 'updated_at', 'author', 'post']
