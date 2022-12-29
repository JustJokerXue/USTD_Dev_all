from django.apps import AppConfig


class UstdApp1Config(AppConfig):  # 主系统注册
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'USTD_App1'
    verbose_name = '信息管理'
