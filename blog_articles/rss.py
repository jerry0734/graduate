from django.contrib.syndication.views import Feed
from .models import Article
from django.urls import reverse


class LatestArticle(Feed):
    title = "Jerry's Blog"
    link = '/feeds/'
    description = "updates on Jerry's Blog"

    def items(self):
        return Article.objects.order_by('-create_time')[:5]

    def item_title(self, item):
        return item.title

    def item_link(self, item):
        return reverse('blog:detail', args=[item.pk])
