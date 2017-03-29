from django.db import models


# Create your models here.

# 创建博客主题模型
class Aritcle(models.Model):
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
    body = models.TextField('正文', help_text='请编写你的文章')

    # 创建时间
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    # 修改时间
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    # 文章发布状态，默认值为草稿
    status = models.CharField('发布状态', max_length=1,
                              choices=PUBLISH_STATUS_CHOICES,
                              default=DRAFT)

    # 文章摘要,长度50个字符
    # null 是针对数据库的，当null=True, 表示数据库的该字段可以为空。
    # blank 是针对表单的，当blank=True，表示你的表单填写该字段的时候可以不填
    abstract = models.CharField('文章摘要', max_length=50, blank=True, null=True,
                                help_text='摘要，可填选项')
    # 文章被浏览次数
    # PositiveIntegerField，指定这个数必须为0以上的正整数，范围from 0 to 2147483647
    reading = models.PositiveIntegerField('阅读量', default=0)

    # 文章点赞次数
    likes = models.PositiveIntegerField('赞', default=0)

    # 文章被置顶状态
    # BooleanField : A true/false field.不设定值的话默认是null，故设置默认值
    top = models.BooleanField('置顶', default=False)

    # 文章分类
    # verbose_name:A human-readable name for the field. 人类可读的名字
    # on_delete有四种选项，这里选择SET_NULL。当删除分类后使相关文章的外键变为空
    category = models.ForeignKey('Category', verbose_name='分类', null=True,
                                 on_delete=models.SET_NULL)

    def __str__(self):
        # 显示文章的标题
        return self.title

    class Meta:
        # 告诉Django模型对象返回的记录结果集是依照哪个字段排序的
        # 下面的意思是按照修改日期降序排列，没有-号的话，就是按照升序排列
        ordering = ['-modified_time']

class Category(models.Model):
    """文章分类"""
    pass
