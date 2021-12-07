from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('posts/', views.post_list_view, name='post_list'),
    # path('posts/<slug:slug>', views.post_detail_view, name='post_detail'),
    # path(
    #     'categories/<slug:slug>',
    #     views.CategoryDetailView.as_view(),
    #     name='category_detail'
    # )
]
