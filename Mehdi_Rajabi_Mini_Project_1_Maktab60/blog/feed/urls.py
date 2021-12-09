from django.urls import path, re_path
from .views import (
    CategoryListView, FeedView,
    IndexView, PostDetailView,
    CreatePostView, UpdatePostView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('feed/', FeedView.as_view(), name='feed'),
    re_path(
        'feed/post/(?P<slug>[-\w]+)/',
        PostDetailView.as_view(),
        name='post_detail'
    ),
    path(
        'feed/create-new-post/',
        CreatePostView.as_view(), name='create_post'
    ),
    re_path(
        'feed/edit/post/(?P<slug>[-\w]+)/',
        UpdatePostView.as_view(), name='update_post'
    ),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    # path('posts/<slug:slug>', views.post_detail_view, name='post_detail'),
    # path(
    #     'categories/<slug:slug>',
    #     views.CategoryDetailView.as_view(),
    #     name='category_detail'
    # )
]
