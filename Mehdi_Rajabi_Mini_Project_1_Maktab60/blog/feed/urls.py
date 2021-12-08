from django.urls import path
from .views import CategoryListView, FeedView, IndexView, PostDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('feed/', FeedView.as_view(), name='feed'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    # path('posts/<slug:slug>', views.post_detail_view, name='post_detail'),
    # path(
    #     'categories/<slug:slug>',
    #     views.CategoryDetailView.as_view(),
    #     name='category_detail'
    # )
]
