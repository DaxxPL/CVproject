from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/<str:category>', views.post_list_filtered_by_category, name='post_list_filtered_by_category'),
]
