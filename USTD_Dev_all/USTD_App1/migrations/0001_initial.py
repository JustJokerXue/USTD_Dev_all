# Generated by Django 4.1.3 on 2022-11-08 09:42

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='学号')),
                ('zy', models.IntegerField(default=0, null=True, verbose_name='专业技术能力')),
                ('cx', models.IntegerField(default=0, null=True, verbose_name='创新创业能力')),
                ('zs', models.IntegerField(default=0, null=True, verbose_name='知识学习能力')),
                ('gl', models.IntegerField(default=0, null=True, verbose_name='管理实践能力')),
                ('zh', models.IntegerField(default=0, null=True, verbose_name='综合发展能力')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='学号')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='姓名')),
                ('age', models.IntegerField(default=0, null=True, verbose_name='年龄')),
                ('sp', models.CharField(max_length=200, null=True, verbose_name='专业')),
                ('pwd', models.IntegerField(default=0, null=True, verbose_name='密码')),
            ],
        ),
    ]