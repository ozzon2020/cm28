from django.apps import AppConfig


class ShopConfig(AppConfig):
    name = 'shop'
    verbose_name = "Препараты"
    icon_name = 'view_list'
    
    def ready(self):
        # import signal handlers
        import shop.signals     
