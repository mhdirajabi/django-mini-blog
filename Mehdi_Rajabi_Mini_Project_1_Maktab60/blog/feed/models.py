from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.urls import reverse
from uuslug import slugify
from django.contrib.auth.models import User

# Create your models here.


class General(models.Model):
    content = models.TextField("Content")
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(General):
    title = models.CharField("Post Title", max_length=100)
    creator = models.ForeignKey(
        User,
        on_delete=CASCADE,
        related_name="posts"
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='images/post_images'
    )
    slug = models.SlugField(null=True, blank=True)
    categories = models.ManyToManyField(
        'Category',
        db_table='Post_Categories',
        related_name='posts'
    )
    tags = models.ManyToManyField(
        'Tag',
        db_table='Post_Tags',
        related_name='posts'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)


class Comment(General):
    author = models.ForeignKey(
        User,
        on_delete=SET_NULL,
        null=True,
        related_name="comments"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    def __str__(self):
        return 'Comment (%s) for %s' % (self.pk, self.post.title)


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Tag, self).save(*args, **kwargs)
