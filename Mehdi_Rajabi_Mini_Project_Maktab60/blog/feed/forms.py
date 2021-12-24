from django import forms
from .models import Comment, Post, Category, Tag


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'categories', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'عنوان پستت رو اینجا وارد کن...'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'متن پستت رو اینجا وارد کن...'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'categories': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
        }


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'categories', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'عنوان پستت رو اینجا وارد کن...'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'متن پستت رو اینجا وارد کن...'
            }),
            'categories': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
        }


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'owner')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام دسته‌بندی...'
            }),
            'owner': forms.TextInput(attrs={
                'id': 'owner',
                'value': '',
                'type': 'hidden'
            }),
        }


class UpdateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام جدید...'
            }),
        }


class CreateTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name', 'owner')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام تگ...'
            }),
            'owner': forms.TextInput(attrs={
                'id': 'owner',
                'value': '',
                'type': 'hidden'
            }),
        }


class UpdateTagForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام جدید...'
            }),
        }


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'متن کامنت رو اینجا وارد کن...',
                'rows': 4
            })
        }
