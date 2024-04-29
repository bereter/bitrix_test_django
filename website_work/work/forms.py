from django import forms
from .models import Post, ReplyPost


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'name',
            'description',
            'price'
        ]

class ReplyForm(forms.ModelForm):

    class Meta:
        model = ReplyPost
        fields = [
            'description'
        ]