from django.db import models


# Create your models here.
class Student(models.Model):
    id = models.IntegerField(default=0, verbose_name='学号', primary_key=True)
    name = models.CharField(max_length=200, verbose_name='姓名', null=True)
    age = models.IntegerField(default=0, verbose_name='年龄', null=True)
    sp = models.CharField(max_length=200, verbose_name='专业', null=True)
    pwd = models.IntegerField(verbose_name='密码', default=123456)


class Score(models.Model):
    id = models.IntegerField(default=0, verbose_name='学号', primary_key=True)
    zy = models.IntegerField(default=0, verbose_name='专业技术能力', null=True)
    cx = models.IntegerField(default=0, verbose_name='创新创业能力', null=True)
    zs = models.IntegerField(default=0, verbose_name='知识学习能力', null=True)
    gl = models.IntegerField(default=0, verbose_name='管理实践能力', null=True)
    zh = models.IntegerField(default=0, verbose_name='综合发展能力', null=True)
