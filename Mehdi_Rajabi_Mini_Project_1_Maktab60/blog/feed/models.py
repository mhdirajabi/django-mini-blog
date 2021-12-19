from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.urls import reverse
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User

# Create your models here.


def unique_slugify(instance, slug):
    model = instance.__class__
    unique_slug = slug
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = slug + '-' + get_random_string(length=4)
    return unique_slug


class General(models.Model):
    content = models.TextField(verbose_name="متن")
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(General):
    title = models.CharField("عنوان", max_length=100)
    creator = models.ForeignKey(
        User,
        on_delete=CASCADE,
        related_name="posts",
        verbose_name="نویسنده"
    )
    image = models.ImageField(
        "عکس",
        null=True,
        blank=True,
        upload_to='images/post_images'
    )
    slug = models.SlugField(null=True, blank=True, allow_unicode=True)
    categories = models.ManyToManyField(
        'Category',
        db_table='Post_Categories',
        related_name='posts',
        verbose_name="دسته‌بندی‌ها"
    )
    tags = models.ManyToManyField(
        'Tag',
        db_table='Post_Tags',
        related_name='posts',
        verbose_name="تگ‌ها",
        blank=True,
    )
    likes = models.ManyToManyField(
        User,
        db_table="Post_likes",
        related_name="liked_posts",
        verbose_name="لایک‌ها"
    )

    class Meta:
        ordering = ["-date_created"]

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(
                self, slugify(self.title, allow_unicode=True)
            )
        return super().save(*args, **kwargs)


class Comment(General):
    author = models.ForeignKey(
        User,
        on_delete=SET_NULL,
        null=True,
        related_name="comments",
        verbose_name="نویسنده"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name="پست"
    )

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return '%s | %s' % (self.content, self.post.title)


class Category(models.Model):
    name = models.CharField("نام", max_length=200, unique=True)
    owner = models.ForeignKey(
        User,
        on_delete=CASCADE,
        related_name='categories',
        verbose_name="سازنده"
    )
    slug = models.SlugField(null=True, blank=True, allow_unicode=True)

    class Meta:
        verbose_name_plural = "categories"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(
                self, slugify(self.name, allow_unicode=True)
            )
        return super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField("نام", max_length=100, unique=True)
    owner = models.ForeignKey(
        User,
        on_delete=CASCADE,
        related_name='tags',
        verbose_name="سازنده"
    )
    slug = models.SlugField(null=True, blank=True, allow_unicode=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(
                self, slugify(self.name, allow_unicode=True)
            )
        return super().save(*args, **kwargs)
