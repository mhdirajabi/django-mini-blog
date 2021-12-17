from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string
from django.urls import reverse

# Create your models here.


def unique_slugify(instance, slug):
    model = instance.__class__
    unique_slug = slug
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = slug + '-' + get_random_string(length=4)
    return unique_slug


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=CASCADE,
        related_name="profile",
        verbose_name="کاربر",
    )
    profile_pic = models.ImageField(
        "عکس پروفایل",
        null=True,
        blank=True,
        upload_to='images/profile_pictures'
    )
    bio = models.TextField("درباره من", null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return f'پروفایل کاربری | {self.user.username}'

    def get_absolute_url(self):
        return reverse('profile', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.user.username))
        return super().save(*args, **kwargs)
