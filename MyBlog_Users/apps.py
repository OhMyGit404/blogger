from django.apps import AppConfig


class MyblogUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MyBlog_Users'

    def ready(self):
        import MyBlog_Users.signals