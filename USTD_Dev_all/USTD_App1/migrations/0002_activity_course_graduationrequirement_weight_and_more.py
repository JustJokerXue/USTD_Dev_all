# Generated by Django 4.1.4 on 2023-04-18 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('USTD_App1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid', models.IntegerField(default=0, null=True, verbose_name='活动编号')),
                ('aname', models.CharField(max_length=200, null=True, verbose_name='活动名称')),
                ('content', models.CharField(max_length=200, null=True, verbose_name='活动内容')),
                ('organizer', models.CharField(max_length=200, null=True, verbose_name='活动举办方')),
                ('baoming', models.CharField(max_length=200, null=True, verbose_name='报名方式')),
            ],
            options={
                'verbose_name': '活动',
                'verbose_name_plural': '活动',
                'db_table': 'Activity',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='姓名')),
                ('stu_id', models.IntegerField(default=0, verbose_name='学号')),
                ('course', models.CharField(default='', max_length=200, null=True, verbose_name='课程')),
                ('grade', models.IntegerField(default=0, null=True, verbose_name='成绩')),
                ('gpa', models.FloatField(default=0, null=True, verbose_name='绩点')),
            ],
            options={
                'verbose_name': '知识学习',
                'verbose_name_plural': '知识学习',
                'db_table': 'Course',
            },
        ),
        migrations.CreateModel(
            name='GraduationRequirement',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='学业要求id')),
                ('credit', models.FloatField(default=0, null=True, verbose_name='要求学分')),
                ('compulsory', models.FloatField(default=0, null=True, verbose_name='必修课成绩')),
                ('elective', models.FloatField(default=0, null=True, verbose_name='选修课成绩')),
                ('physical', models.FloatField(default=0, null=True, verbose_name='体测成绩')),
                ('cet4', models.FloatField(default=0, null=True, verbose_name='四级成绩')),
                ('mandarin', models.FloatField(default=0, null=True, verbose_name='普通话成绩')),
            ],
            options={
                'verbose_name': '学业要求',
                'verbose_name_plural': '学业要求',
                'db_table': 'GraduationRequirement',
            },
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zyweight', models.FloatField(default=0, null=True, verbose_name='专业技术权重')),
                ('cxweight', models.FloatField(default=0, null=True, verbose_name='创新创业权重')),
                ('zsweight', models.FloatField(default=0, null=True, verbose_name='知识学习权重')),
                ('glweight', models.FloatField(default=0, null=True, verbose_name='管理实践权重')),
                ('zhweight', models.FloatField(default=0, null=True, verbose_name='综合发展权重')),
            ],
            options={
                'verbose_name': '综测权重系数',
                'verbose_name_plural': '综测权重系数',
                'db_table': 'Weight',
            },
        ),
        migrations.DeleteModel(
            name='Knowledge',
        ),
        migrations.AddField(
            model_name='score',
            name='overallgrade',
            field=models.IntegerField(default=0, null=True, verbose_name='总评成绩'),
        ),
        migrations.AddField(
            model_name='shenhe',
            name='extra_points',
            field=models.IntegerField(default=0, null=True, verbose_name='加分'),
        ),
        migrations.AlterField(
            model_name='early_warning',
            name='cet4',
            field=models.FloatField(default=0, null=True, verbose_name='四级成绩'),
        ),
        migrations.AlterField(
            model_name='early_warning',
            name='compulsory',
            field=models.FloatField(default=0, null=True, verbose_name='必修课成绩'),
        ),
        migrations.AlterField(
            model_name='early_warning',
            name='elective',
            field=models.FloatField(default=0, null=True, verbose_name='选修课成绩'),
        ),
        migrations.AlterField(
            model_name='early_warning',
            name='mandarin',
            field=models.FloatField(default=0, null=True, verbose_name='普通话成绩'),
        ),
        migrations.AlterField(
            model_name='early_warning',
            name='minimum',
            field=models.FloatField(default=0, null=True, verbose_name='实修学分'),
        ),
        migrations.AlterField(
            model_name='early_warning',
            name='physical',
            field=models.FloatField(default=0, null=True, verbose_name='体测成绩'),
        ),
        migrations.AlterField(
            model_name='shenhe',
            name='leibie',
            field=models.CharField(
                choices=[('专业技术', '专业技术'), ('创新创业', '创新创业'), ('管理实践', '管理实践'),
                         ('综合发展', '综合发展')], default='专业技术', max_length=200, verbose_name='材料类别'),
        ),
        migrations.AddConstraint(
            model_name='score',
            constraint=models.CheckConstraint(check=models.Q(('overallgrade__gte', 0), ('overallgrade__lte', 100)),
                                              name='overallgrade'),
        ),
        migrations.AddConstraint(
            model_name='shenhe',
            constraint=models.CheckConstraint(check=models.Q(('extra_points__gte', 0), ('extra_points__lte', 100)),
                                              name='extra_points'),
        ),
        migrations.AddConstraint(
            model_name='weight',
            constraint=models.CheckConstraint(check=models.Q(('zyweight__gte', 0), ('zyweight__lte', 1)),
                                              name='zyweight'),
        ),
        migrations.AddConstraint(
            model_name='weight',
            constraint=models.CheckConstraint(check=models.Q(('cxweight__gte', 0), ('cxweight__lte', 1)),
                                              name='cxweight'),
        ),
        migrations.AddConstraint(
            model_name='weight',
            constraint=models.CheckConstraint(check=models.Q(('zsweight__gte', 0), ('zsweight__lte', 1)),
                                              name='zsweight'),
        ),
        migrations.AddConstraint(
            model_name='weight',
            constraint=models.CheckConstraint(check=models.Q(('glweight__gte', 0), ('glweight__lte', 1)),
                                              name='glweight'),
        ),
        migrations.AddConstraint(
            model_name='weight',
            constraint=models.CheckConstraint(check=models.Q(('zhweight__gte', 0), ('zhweight__lte', 1)),
                                              name='zhweight'),
        ),
        migrations.AddConstraint(
            model_name='graduationrequirement',
            constraint=models.CheckConstraint(check=models.Q(('credit__gte', 0), ('credit__lte', 170)),
                                              name='grad_req_credit'),
        ),
        migrations.AddConstraint(
            model_name='graduationrequirement',
            constraint=models.CheckConstraint(check=models.Q(('compulsory__gte', 0), ('compulsory__lte', 100)),
                                              name='grad_req_compulsory'),
        ),
        migrations.AddConstraint(
            model_name='graduationrequirement',
            constraint=models.CheckConstraint(check=models.Q(('elective__gte', 0), ('elective__lte', 100)),
                                              name='grad_req_elective'),
        ),
        migrations.AddConstraint(
            model_name='graduationrequirement',
            constraint=models.CheckConstraint(check=models.Q(('physical__gte', 0), ('physical__lte', 100)),
                                              name='grad_req_physical'),
        ),
        migrations.AddConstraint(
            model_name='graduationrequirement',
            constraint=models.CheckConstraint(check=models.Q(('cet4__gte', 0), ('cet4__lte', 750)),
                                              name='grad_req_cet4'),
        ),
        migrations.AddConstraint(
            model_name='graduationrequirement',
            constraint=models.CheckConstraint(check=models.Q(('mandarin__gte', 0), ('mandarin__lte', 100)),
                                              name='grad_req_mandarin'),
        ),
        migrations.AddConstraint(
            model_name='course',
            constraint=models.CheckConstraint(check=models.Q(('grade__gte', 0), ('grade__lte', 100)), name='grade'),
        ),
        migrations.AddConstraint(
            model_name='course',
            constraint=models.CheckConstraint(check=models.Q(('gpa__gte', 0), ('gpa__lte', 5)), name='gpa'),
        ),
        migrations.AddField(
            model_name='early_warning',
            name='grad_req_id',
            field=models.ForeignKey(blank=True, db_column='stu_gradReq_id', null=True,
                                    on_delete=django.db.models.deletion.DO_NOTHING,
                                    to='USTD_App1.graduationrequirement', verbose_name='学业要求id'),
        ),
    ]