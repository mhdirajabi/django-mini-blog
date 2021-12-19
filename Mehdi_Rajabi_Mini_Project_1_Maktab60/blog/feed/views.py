from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from .models import Post, Category, Tag
from django.views.generic import (
    ListView,
    TemplateView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import (
    CreatePostForm, UpdatePostForm,
    CreateCategoryForm, UpdateCategoryForm,
    CreateTagForm, UpdateTagForm,
    CreateCommentForm,
)
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

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
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        comment_form = CreateCommentForm()
        context["comments"] = post.comments.all()
        context["total_likes"] = post.total_likes()
        context["liked"] = liked
        context["comment_form"] = comment_form
        return context

    def post(self, request, *args, **kwargs):
        comment_form = CreateCommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment_form.instance.post = Post.objects.get(slug=self.kwargs['slug'])
            comment_form.save()
            return HttpResponseRedirect(reverse(
                'post_detail',
                kwargs={'slug': self.kwargs['slug']}
            ))
        else:
            return HttpResponse(comment_form.errors)


def post_like_view(request, slug):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post_detail', kwargs={'slug': slug}))


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'feed/create_post.html'
    login_url = '/members/login/'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        post = form.save(commit=False)
        post.save()
        form.save_m2m()
        user_profile = post.creator.profile
        return HttpResponseRedirect(reverse_lazy('profile', kwargs={
            'slug': user_profile.slug
        }))


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'feed/update_post.html'
    login_url = '/members/login/'


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'feed/delete_post.html'
    success_url = reverse_lazy('feed')
    login_url = '/members/login/'


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


class CreateCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = 'feed/create_category.html'
    success_url = reverse_lazy('category_list')
    login_url = '/members/login/'


class UpdateCategoryView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = UpdateCategoryForm
    template_name = 'feed/update_category.html'
    success_url = reverse_lazy('category_list')
    login_url = '/members/login/'


class DeleteCategoryView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'feed/delete_category.html'
    success_url = reverse_lazy('category_list')
    login_url = '/members/login/'


class TagListView(ListView):
    model = Tag
    template_name = 'feed/tags.html'


class TagDetailView(DetailView):
    model = Tag
    template_name = 'feed/tag_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(
            tags=context["tag"]
        )
        return context


class CreateTagView(LoginRequiredMixin, CreateView):
    model = Tag
    form_class = CreateTagForm
    template_name = 'feed/create_tag.html'
    success_url = reverse_lazy('tag_list')
    login_url = '/members/login/'


class UpdateTagView(LoginRequiredMixin, UpdateView):
    model = Tag
    form_class = UpdateTagForm
    template_name = 'feed/update_tag.html'
    success_url = reverse_lazy('tag_list')
    login_url = '/members/login/'


class DeleteTagView(LoginRequiredMixin, DeleteView):
    model = Tag
    template_name = 'feed/delete_tag.html'
    success_url = reverse_lazy('tag_list')
    login_url = '/members/login/'


def search_blog(request):
    if request.method == 'POST':
        search = request.POST['search']
        post_title = Post.objects.filter(title__contains=search)
        post_content = Post.objects.filter(content__contains=search)
        posts = set(list(post_title) + list(post_content))
        context = {
            'search': search,
            'posts': posts
        }
        return render(request, 'feed/search.html', context)
    else:
        return render(request, 'feed/search.html', {})
