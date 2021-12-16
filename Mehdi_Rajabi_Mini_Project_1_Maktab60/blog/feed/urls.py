from django.urls import path, re_path
from .views import (
    CategoryDetailView, CategoryListView, FeedView,
    IndexView, PostDetailView,
    CreatePostView, UpdatePostView,
    DeletePostView, CreateCategoryView,
    UpdateCategoryView, DeleteCategoryView,
    post_like_view, TagListView,
    TagDetailView, CreateTagView,
    UpdateTagView, DeleteTagView,
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
    ),
    path('feed/tags/', TagListView.as_view(), name='tag_list'),
    re_path(
        'feed/tags/(?P<slug>[-\w]+)/',
        TagDetailView.as_view(),
        name='tag_detail'
    ),
    path(
        'feed/create-new-tag/',
        CreateTagView.as_view(),
        name='create_tag'
    ),
    re_path(
        'feed/edit/tag/(?P<slug>[-\w]+)/',
        UpdateTagView.as_view(), name='update_tag'
    ),
    re_path(
        'feed/remove/tag/(?P<slug>[-\w]+)/',
        DeleteTagView.as_view(), name='delete_tag'
    ),
]
