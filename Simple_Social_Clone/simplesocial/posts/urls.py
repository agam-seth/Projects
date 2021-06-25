from django.urls import path
from posts import views

# POSTS URL.PY

app_name = 'posts'

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('new/', views.CreatePost.as_view(), name='new_post'),
    path('by/<username>/', views.UserPosts.as_view(), name='post_user'),
    path('by/<username>/<pk>/', views.PostDeatil.as_view(), name='single'),
    path('delete/<pk>/', views.DeletePost.as_view(), name='delete_post'),
]
