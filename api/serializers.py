from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Post, Category


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    category = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Post
        fields = ('pk', 'author', 'title', 'text', 'created', 'category')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')


class CategorySerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api_post_detail'
    )

    class Meta:
        model = Category
        fields = ('name', 'posts')

