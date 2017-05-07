import datetime
from haystack import indexes
from .models import Article


class ArticleSearch(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='author')
    title = indexes.CharField(model_attr='title')
    body = indexes.CharField(model_attr='body')
    id = indexes.CharField(model_attr='id')
    create_time = indexes.DateTimeField(model_attr='create_time')
    modified_time = indexes.DateTimeField(model_attr='modified_time')

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(create_time__lte=datetime.datetime.now())
