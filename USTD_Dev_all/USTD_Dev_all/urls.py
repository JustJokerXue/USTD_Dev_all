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
from USTD_App1 import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [

                  path('', views.login_view),
                  path('login/', views.login),
                  path('test/', views.Activity_new),
                  path('test1/', views.queryCourse),
                  path('admin/', admin.site.urls),
                  path('login/index.html', views.index),
                  path(r'login/infor.html', views.infor),
                  path(r'shenhe_delete.html', views.shenhe_delete),
                  path(r'login/form-editors.html', views.form_editor),
                  path(r'login/tables-editable.html', views.shenhe_upload),
                  path(r'login/Academic_Early_Warning.html', views.academic_Early_Warning),
                  path('login/password_change_form.html', views.password_change_form, name='password_change_form'),
                  path(r'login/suggestion/<int:p1>/', views.suggestion),
                  path(r'login/student_score.html', views.queryCourse),
                  path(r'login/activity.html', views.Activity_new),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
