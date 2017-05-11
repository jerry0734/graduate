from django.db import models
from django.conf import settings
# 导入自带的User，为文章作者显示正确的用户名
from django.contrib.auth.models import User
from draceditor.models import DraceditorField


# Create your models here.

# 创建博客主题模型
class Article(models.Model):
    """博客主体，内包含文章，编者，发布状态与时间等等"""

    # Field.choices
    # 选择器，可以选择
    DRAFT = 'd'
    PUBLISHED = 'p'
    PUBLISH_STATUS_CHOICES = (
        (DRAFT, '草稿'),
        (PUBLISHED, '发布'),
    )

    # 文章标题，max_length为标题最大长度
    # '标题'是一个位置参数，admin后台管理提示符
    title = models.CharField('文章标题', max_length=70, help_text='标题')

    # 文章主体
    # '正文'的作用同上，都只是用于admin管理界面
    # help_text是在admin界面文本框中显示的提示文字
    # 换用DraceEditor来实现Markdown编辑器
    body = DraceditorField('正文', help_text='请编写你的文章')

    # 创建时间
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    # 修改时间
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    # 文章发布状态，默认值为草稿
    status = models.CharField('发布状态', max_length=1,
                              choices=PUBLISH_STATUS_CHOICES,
                              default=DRAFT)

    # 文章摘要,长度100个字符
    # null 是针对数据库的，当null=True, 表示数据库的该字段可以为空。
    # blank 是针对表单的，当blank=True，表示你的表单填写该字段的时候可以不填
    abstract = models.CharField('文章摘要', max_length=100, blank=True, null=True,
                                help_text='摘要，可填选项')
    # 文章被浏览次数
    # PositiveIntegerField，指定这个数必须为0以上的正整数，范围from 0 to 2147483647
    reading = models.PositiveIntegerField('阅读量', default=0)

    # 文章点赞次数
    likes = models.PositiveIntegerField('赞', default=0)

    # 文章被置顶状态（废弃）
    # BooleanField : A true/false field.不设定值的话默认是null，故设置默认值
    # top = models.BooleanField('置顶', default=False)

    # 文章分类
    # verbose_name:A human-readable name for the field. 人类可读的名字
    # on_delete有四种选项，这里选择SET_NULL。当删除分类后使相关文章的外键变为空
    category = models.ForeignKey('Category', verbose_name='分类', null=True,
                                 on_delete=models.SET_NULL)

    # 20170408添加
    # 文章标签（从Tag类获取）
    # blank=True 即表示没有标签也可以
    tag = models.ManyToManyField('Tag', blank=True)

    # 文章作者
    # User是django内置的用户模型，
    # 通过 ForeignKey 把文章和User关联起来
    # limit_choice_to 控制只有超级管理员才能是作者，从而把评论者和撰文者分开
    author = models.ForeignKey(settings.AUTH_USER_MODEL, limit_choices_to={'is_superuser': 1})

    def __str__(self):
        # 显示文章的标题
        return self.title

    class Meta:
        # 告诉Django模型对象返回的记录结果集是依照哪个字段排序的
        # 下面的意思是按照修改日期降序排列
        # modified_time前面没有-号的话，就是按照升序排列
        ordering = ['-modified_time']
        # 在admin主页中显示的名字从Articles变为文章
        verbose_name_plural = '文章'


class Category(models.Model):
    """文章分类"""
    # 分类名称,独一无二
    name = models.CharField('分类名', max_length=20, unique=True)
    # 分类创建时间
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    # 分类修改时间
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '分类'


class Tag(models.Model):
    """文章标签"""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '标签'


# 关于博客页面
class Aboutme(models.Model):
    blog_name = models.CharField('博客名称', max_length=50)
    admin_email = models.EmailField()
    other = models.TextField()

    class Meta:
        verbose_name_plural = '关于博客'

    def __str__(self):
        return self.blog_name


class Comments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='用户')
    article = models.ForeignKey(Article, verbose_name='关联文章')
    content = models.TextField(verbose_name='内容')
    published_time = models.DateTimeField('创建时间', auto_now_add=True)

    # 预留接口
    related = models.ForeignKey('self', default=None, blank=True, null=True,
                                verbose_name='引用')

    def __str__(self):
        if (len(self.content) <= 20):
            return self.content
        else:
            return self.content[:20] + '...'

    class Meta:
        verbose_name_plural = '评论'
        ordering = ['-published_time']
