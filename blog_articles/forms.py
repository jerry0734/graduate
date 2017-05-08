from .models import Article, Category, Tag, Comments
from myuser.models import allUser
from django import forms
from draceditor.fields import DraceditorFormField, DraceditorWidget


class CommentForm(forms.ModelForm):
    """评论表单"""
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'color-form-control', 'rows': 3}))

    class Meta:
        model = Comments
        fields = ['content']


class ArticleForm(forms.ModelForm):
    """文章表单"""
    title = forms.CharField(max_length=70)
    author = forms.ModelChoiceField(queryset=allUser.objects.filter(is_superuser=True))
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
    abstract = forms.CharField(widget=forms.TextInput, max_length=50, empty_value=None)
    body = forms.CharField(widget=forms.Textarea)

    # body = DraceditorFormField(widget=DraceditorWidget)

    class Meta:
        model = Article
        fields = ['title', 'author', 'category', 'tag', 'abstract', 'body', 'status']
