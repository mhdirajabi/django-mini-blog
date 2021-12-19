from django.contrib import admin
from .models import Post, Comment, Category, Tag
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'slug')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
