from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Post, Category


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('pk', 'author', 'title', 'text', 'created', 'category')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')

