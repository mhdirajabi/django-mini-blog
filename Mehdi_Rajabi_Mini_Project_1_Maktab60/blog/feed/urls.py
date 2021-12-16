from django.urls import path, re_path
from .views import (
    CategoryDetailView, CategoryListView, FeedView,
    IndexView, PostDetailView,
    CreatePostView, UpdatePostView,
    DeletePostView, CreateCategoryView,
    UpdateCategoryView, DeleteCategoryView,
    post_like_view
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
    re_path(
        'feed/remove/post/(?P<slug>[-\w]+)/',
        DeletePostView.as_view(), name='delete_post'
    ),
    path('feed/categories/', CategoryListView.as_view(), name='category_list'),
    re_path(
        'feed/categories/(?P<slug>[-\w]+)/',
        CategoryDetailView.as_view(),
        name='category_detail'
    ),
    path(
        'feed/create-new-category/',
        CreateCategoryView.as_view(),
        name='create_category'
    ),
    re_path(
        'feed/edit/category/(?P<slug>[-\w]+)/',
        UpdateCategoryView.as_view(), name='update_category'
    ),
    re_path(
        'feed/remove/category/(?P<slug>[-\w]+)/',
        DeleteCategoryView.as_view(), name='delete_category'
    ),
    re_path(
        'feed/like/post/(?P<slug>[-\w]+)/',
        post_like_view,
        name='post_like'
    )
]
