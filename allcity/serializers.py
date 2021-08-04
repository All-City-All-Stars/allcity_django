from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.HyperlinkedRelatedField(
        view_name='comment_detail', many=True, read_only=True
    )

    class Meta:
        model = Post
        fields = (
            'image_url',
            'author',
            'location',
            'caption_body',
            'post_time',
            'comments',
        )

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedRelatedField(
        view_name='post_detail', read_only=True
    )
    post_id = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(), source='post'
    )

    class Meta:
        model = Comment
        fields = (
            'post',
            'author',
            'comment_body',
            'post_time',
            'post_id',
        )