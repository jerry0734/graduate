from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Aritcle, Category

class IndexView(ListView):

    template_name = "blog_articles/index.html"

    context_object_name = "article_list"

