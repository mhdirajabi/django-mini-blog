from django import forms
from .models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'creator', 'image', 'categories', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'عنوان پستت رو اینجا وارد کن...'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'متن پستت رو اینجا وارد کن...'
            }),
            'creator': forms.Select(attrs={
                'class': 'form-control',
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
