from django.contrib import admin
from .models import Post
from django import forms


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostForm,self).__init__(*args, **kwargs)

        self.fields['title'].help_text = 'New Help Text'

    class Meta:
        model = Post
        exclude = ('',)

