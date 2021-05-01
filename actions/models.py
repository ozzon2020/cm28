from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Action(models.Model):
    
    name = models.CharField(max_length=150,verbose_name="Пользователь")
    #user = models.ForeignKey('auth.User',
                             #related_name='actions',
                             #db_index=True,
                             #on_delete=models.CASCADE,verbose_name="Пользователь")
    verb = models.CharField(max_length=255,verbose_name="Действие")
    verbico = models.CharField(max_length=150,verbose_name="Иконка")
    target_ct = models.ForeignKey(ContentType,
                                  blank=True,
                                  null=True,
                                  related_name='target_obj',
                                  on_delete=models.CASCADE,verbose_name="Название")
    target_id = models.PositiveIntegerField(null=True,
                                            blank=True,
                                            db_index=True,verbose_name="Название")
    target = GenericForeignKey('target_ct', 'target_id')
    created = models.DateTimeField(auto_now_add=True,
                                   db_index=True,verbose_name="Дата")

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = "Активность"
