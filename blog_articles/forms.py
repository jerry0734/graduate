from .models import Article, Category, Comments
from django import forms


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    class Meta:
        model = Comments
        fields = ['content']
