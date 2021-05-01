import datetime
from django.utils import timezone
from django.utils.timezone import now
from haystack import indexes
from .models import Qs

class QsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    theme = indexes.CharField(model_attr='theme')
    main = indexes.CharField(model_attr='main')
    #reply = indexes.CharField(model_attr='reply')
    #doctor = indexes.CharField(model_attr='doctor')
    pub_date = indexes.DateTimeField(model_attr='created')

    def get_model(self):
        return Qs

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(active__exact=True).exclude(reply__isnull=True).filter(created__lte=timezone.now()).all()
        #return self.get_model().objects.filter(active__exact=True).filter(created__lte=timezone.now()).all()