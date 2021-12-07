from django.shortcuts import render
from .models import Post, Category
from django.views.generic import ListView, DetailView, TemplateView

# Create your views here.


class IndexView(TemplateView):
    template_name = 'feed/index.html'

# def post_list_view(request):
#     context = {
#         'post_list': Post.objects.all(),
#         'categories_list': Category.objects.all()
#     }
#     return render(request, 'posts.html', context=context)


# class CategoriesListView(ListView):
#     model = Category
#     template_name = 'index.html'


# def post_detail_view(request, slug):
#     post = Post.objects.get(slug=slug)
#     comments = post.comments.all()
#     categories = Category.objects.all()
#     context = {
#         'post': post,
#         'comments': comments,
#         'categories_list': categories
#     }
#     return render(request, 'post_detail.html', context=context)


# class CategoryDetailView(DetailView):
#     model = Category
#     template_name = 'category_detail.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["posts"] = Post.objects.filter(
#             categories=context["categories"]
#         )
#         context["categories_list"] = Category.objects.all()
#         return context
