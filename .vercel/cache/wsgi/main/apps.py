from django.apps import AppConfig

class MainConfig(AppConfig):  # Change from NewsConfig to MainConfig
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'