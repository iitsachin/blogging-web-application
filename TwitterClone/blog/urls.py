from django.urls import path, include
from blog import views
from .views import (postListView, postDetailView, postCreateView, postUpdateView, postDeleteView,userPostListView)

app_name = 'blog'
urlpatterns = [
    # path('', views.homepage, name='home'),
    path('', postListView.as_view(), name='home'),
    path('post/<str:username>', userPostListView.as_view(), name='user-post'),
    path('post/<int:pk>/', postDetailView.as_view(), name='post-detail'),
    path('post/create/new/', postCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', postUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', postDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='about'),

]
