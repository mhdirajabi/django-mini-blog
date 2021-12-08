from django.contrib import admin
from .models import Post, Comment, Category, Tag
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'slug')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Tag)
