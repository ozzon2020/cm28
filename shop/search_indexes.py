import datetime
from django.utils import timezone
from django.utils.timezone import now
from haystack import indexes
from .models import Product,Review

class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    description = indexes.CharField(model_attr='description')
   
    #doctor = indexes.CharField(model_attr='doctor')
    pub_date = indexes.DateTimeField(model_attr='created')

    def get_model(self):
        return Product

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(active__exact=True).filter(created__lte=timezone.now()).all()
    
class ReviewIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    body = indexes.CharField(model_attr='body')
   
    #doctor = indexes.CharField(model_attr='doctor')
    pub_date = indexes.DateTimeField(model_attr='created')

    def get_model(self):
        return Review

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(active__exact=True).filter(created__lte=timezone.now()).all()
    
