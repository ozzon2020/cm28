from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Product

#@receiver(m2m_changed, sender=Product.users_like.through)
#def users_like_changed(sender, instance, **kwargs):
    #instance.total_likes = instance.users_like.count()
    #instance.save()
    
#@receiver(m2m_changed, sender=Product.users_dislike.through)
#def users_dislike_changed(sender, instance, **kwargs):
    #instance.total_dislikes = instance.users_dislike.count()
    #instance.save()