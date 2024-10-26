from django.contrib import admin

from posts.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'text', 'author', 'created_at', 'updated_at']
    list_filter = ['created_at',]
    search_fields = ['title', 'author']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'text',  'post', 'created_at', ]
