from django.apps import AppConfig


class QsConfig(AppConfig):
    name = 'qs'
    verbose_name = "Онлайн ответы врача"
    icon_name = 'thumbs_up_down'
    
    #def ready(self):
        ## import signal handlers
        #import questions.signals    
