from django import forms
from .models import Notice


class NoticePost(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'body']
