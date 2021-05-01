import datetime
from django.utils import timezone
from django.utils.timezone import now
from haystack import indexes
from content.models import Section,Chast,Razdel

class SectionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    name = indexes.CharField(model_attr='name')
    main = indexes.CharField(model_attr='main')
    var = indexes.CharField(model_attr='ch')
    pub_date = indexes.DateTimeField(model_attr='created')

    def get_model(self):
        return Section

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(active__exact=True).filter(created__lte=timezone.now()).all()
    


    
    
    
#def index_queryset(self, using=None):
    #qs = Note.objects.all()
    #archive_limit = datetime.datetime.now() - datetime.timedelta(days=90)

    #if using == "archive":
        #return qs.filter(pub_date__lte=archive_limit)
    #else:
        #return qs.filter(pub_date__gte=archive_limit)
