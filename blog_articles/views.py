from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Aritcle, Category, Aboutme, Tag
import markdown_deux
import markdown2


class IndexView(ListView):
    template_name = "blog_articles/index.html"

    context_object_name = "article_list"

    # 返回文章
    def get_queryset(self):
        article_list = Aritcle.objects.filter(status='p')
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(IndexView, self).get_context_data(**kwargs)


def aboutme(request):
    about = Aboutme.objects.get(id=1)
    context = {'about': about}
    return render(request, 'blog_articles/aboutme.html', context)
