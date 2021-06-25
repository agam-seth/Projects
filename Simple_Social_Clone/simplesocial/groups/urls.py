from django.urls import path
from groups import views

# GROUPS URL.PY

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroups.as_view(), name='list_group'),
    path('create/', views.CreateGroup.as_view(), name='create_group'),
    path('posts/in/<slug>/', views.SingleGroup.as_view(), name='single_group'),
    path('join/<slug>/', views.JoinGroup.as_view(), name='join'),
    path('leave/<slug>/', views.LeaveGroup.as_view(), name='leave'),
]
