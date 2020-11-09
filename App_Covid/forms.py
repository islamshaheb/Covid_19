from django import forms
from App_Covid.models import Blog, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
