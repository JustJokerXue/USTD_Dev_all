"""USTD_Dev_all URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from USTD_App1 import views
from django.conf.urls.static import static

urlpatterns = [
                  path('login/', views.login),
                  path('', views.login_view),
                  path('index/', views.index),
                  path('admin/', admin.site.urls),
                  path(r'login/tables-editable.html', views.shenhe_upload),
                  path(r'shenhe_delete.html', views.shenhe_delete),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
