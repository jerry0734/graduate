from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Aritcle, Category
import markdown_deux
import markdown2


class IndexView(ListView):
    template_name = "blog_articles/index.html"

    context_object_name = "article_list"

    def get_queryset(self):
        article_list = Aritcle.objects.filter(status='p')

        for article in article_list:
            article.body = markdown_deux.markdown(article.body, )
            # article.body = markdown2.markdown(article.body,)
            return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(IndexView, self).get_context_data(**kwargs)
