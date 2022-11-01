from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, like_post, CategoryView, AddCommentView

urlpatterns = [
    path('', views.home, name='main-home'),
    path('about/', views.about, name='site-about'),
    path('posts/', PostListView.as_view(), name='site-posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('category/', CategoryView.as_view(), name='add-category'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='add-comment'),
    path('like/', like_post, name='like-post'),

]
