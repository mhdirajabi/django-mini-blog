from django.contrib import admin
from .models import Post, Comment, Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'slug')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category, CategoryAdmin)
