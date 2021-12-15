from django.urls import reverse_lazy
from .models import Post, Category
from django.views.generic import (
    ListView,
    TemplateView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import CreatePostForm, UpdatePostForm, CreateCategoryForm
from django.http import HttpResponseRedirect

# Create your views here.


class IndexView(TemplateView):
    template_name = 'feed/index.html'


class FeedView(ListView):
    model = Post
    template_name = 'feed/feed.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'feed/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context["post"]
        context["comments"] = post.comments.all()
        return context


class CreatePostView(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'feed/create_post.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        form.save_m2m()
        return HttpResponseRedirect(post.get_absolute_url())


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'feed/update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'feed/delete_post.html'
    success_url = reverse_lazy('feed')


class CategoryListView(ListView):
    model = Category
    template_name = 'feed/categories.html'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'feed/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(
            categories=context["category"]
        )
        return context


class CreateCategoryView(CreateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = 'feed/create_category.html'
    success_url = reverse_lazy('category_list')
