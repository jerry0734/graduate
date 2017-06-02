from .models import Article, Category, Tag, Comments, Friends, Aboutme
from myuser.models import allUser
from django import forms
from draceditor.fields import DraceditorFormField, DraceditorWidget


class ReplyForm(forms.ModelForm):
    """回复表单"""
    content = forms.CharField()

    class Meta:
        model = Comments
        fields = ['content']


class CommentForm(forms.ModelForm):
    """评论表单"""
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'color-form-control', 'id': 'commentcontent', 'rows': 3}))

    class Meta:
        model = Comments
        fields = ['content']


class ArticleForm(forms.ModelForm):
    """文章表单"""
    title = forms.CharField(max_length=70)
    author = forms.ModelChoiceField(queryset=allUser.objects.filter(is_superuser=True),
                                    widget=forms.Select(attrs={'data-am-selected': None}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      widget=forms.Select(attrs={'data-am-selected': None}))
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
                                         widget=forms.SelectMultiple(
                                             attrs={'multiple': None, 'data-am-selected': "{btnWidth: '50%'}"}))
    abstract = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Article
        fields = ['title', 'author', 'category', 'tag', 'abstract', 'body', 'status']


class TitlePhotoForm(forms.ModelForm):
    titlephoto = forms.ImageField()

    class Meta:
        model = Article
        fields = ['titlephoto']

class CategoryForm(forms.ModelForm):
    """分类表单"""
    name = forms.CharField(max_length=20,
                           widget=forms.TextInput(attrs={'class': 'am-form-field am-round', 'style': 'width:50%'}))

    class Meta:
        model = Category
        fields = ['name']
        labels = {'name': ''}


class TagForm(forms.ModelForm):
    """标签表单"""
    name = forms.CharField(max_length=20,
                           widget=forms.TextInput(attrs={'class': 'am-form-field am-round', 'style': 'width:50%'}))

    class Meta:
        model = Tag
        fields = '__all__'
        labels = {'name': ''}


class LinkForm(forms.ModelForm):
    name = forms.CharField(max_length=20,
                           label='名称',
                           widget=forms.TextInput(attrs={'class': 'am-form-field am-round', 'style': 'width:50%'}))
    links = forms.URLField(label='链接',
                           widget=forms.URLInput(attrs={'class': 'am-form-field am-round', 'style': 'width:50%'}))

    class Meta:
        model = Friends
        fields = ['name', 'links']
        labels = {'name': '名称', 'links': '链接'}


class AboutForm(forms.ModelForm):
    blog_name = forms.CharField(label='博客名称')
    admin_email = forms.EmailField(label='你的邮箱')
    other = forms.CharField(
        label='其他信息',
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 80}))

    class Meta:
        model = Aboutme
        fields = ['blog_name', 'admin_email', 'other']
