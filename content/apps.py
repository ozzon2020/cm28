from django.apps import AppConfig


class ContentConfig(AppConfig):
    name = 'content'
    verbose_name = "Контент"
    icon_name = 'note'    

        
    #def ready(self):
        ## import signal handlers
        #import content.signals