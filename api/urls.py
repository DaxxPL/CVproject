from django.urls import path
from . import views
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth.models import User
from api.serializers import UserSerializer


urlpatterns = [
    path('posts/', views.PostList.as_view(), name='api_posts_list'),
    path('posts/<int:pk>', views.PostDetail.as_view(), name='api_post_detail'),
    path('users/', ListCreateAPIView.as_view(queryset=User.objects.all(),
                                             serializer_class=UserSerializer), name='user-list'),
    path('categories/', views.CategoryList.as_view(), name='api_category_list'),
]
