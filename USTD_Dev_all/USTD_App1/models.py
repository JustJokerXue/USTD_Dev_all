from django.db import models


# Create your models here.
class Student(models.Model):
    id = models.IntegerField(default=0, verbose_name='学号', primary_key=True)
    name = models.CharField(max_length=200, verbose_name='姓名', null=True)
    age = models.IntegerField(default=0, verbose_name='年龄', null=True)
    sp = models.CharField(max_length=200, verbose_name='专业', null=True)
    pwd = models.IntegerField(verbose_name='密码', default=123456)
    class Meta:
        db_table = 'Student'

class Score(models.Model):
    id = models.IntegerField(default=0, verbose_name='学号', primary_key=True)
    zy = models.IntegerField(default=0, verbose_name='专业技术能力', null=True)
    cx = models.IntegerField(default=0, verbose_name='创新创业能力', null=True)
    zs = models.IntegerField(default=0, verbose_name='知识学习能力', null=True)
    gl = models.IntegerField(default=0, verbose_name='管理实践能力', null=True)
    zh = models.IntegerField(default=0, verbose_name='综合发展能力', null=True)
    class Meta:
        db_table = 'Score'


class Knowledge(models.Model):
    name = models.CharField(max_length=200, verbose_name='姓名', null=True)
    sno = models.IntegerField(default=0, verbose_name='学号', primary_key=True)
    java = models.IntegerField(default=0, verbose_name='java课程', null=True)
    dataStructure = models.IntegerField(default=0, verbose_name='数据结构', null=True)
    Gaverage = models.IntegerField(default=0, verbose_name='平均绩点', null=True)
    class Meta:
        db_table = 'Knowledge'

class Innovation(models.Model):
    name = models.CharField(max_length=200, verbose_name='姓名', null=True)
    sno = models.IntegerField(default=0, verbose_name='学号', primary_key=True)
    ContestRating = models.IntegerField(default=0, verbose_name='竞赛评分', null=False)
    PatentRcoring = models.IntegerField(default=0, verbose_name='专利评分', null=False)
    EntrepreneurialAchievement = models.IntegerField(default=0, verbose_name='创业成果评分', null=False)
    class Meta:
        db_table = 'Innovation'

class majorTechnology(models.Model):
    name = models.CharField(max_length=200, verbose_name='姓名', null=True)
    sno = models.IntegerField(default=0, verbose_name='学号', primary_key=True)
    ProjectPractice = models.IntegerField(default=0, verbose_name='项目实践', null=True)
    PaperGrading = models.IntegerField(default=0, verbose_name='论文评分', null=False)
    StudentTutor = models.IntegerField(default=0, verbose_name='学生导师评分', null=True)
    class Meta:
        db_table = 'majorTechnology'
class manage(models.Model):
    name = models.CharField(max_length=200, verbose_name='姓名', null=True)
    sno = models.IntegerField(default=0, verbose_name='学号', primary_key=True)
    community = models.IntegerField(default=0, verbose_name='社团工作评分', null=False)
    StudentWork = models.IntegerField(default=0, verbose_name='学生工作评分', null=False)
    ProjectTeam = models.IntegerField(default=0, verbose_name='项目团队评分', null=True)
    class Meta:
        db_table = 'manage'
class ComprehensiveDevelopment(models.Model):
    name = models.CharField(max_length=200, verbose_name='姓名', null=True)
    sno = models.IntegerField(default=0, verbose_name='学号', primary_key=True)
    physical = models.IntegerField(default=0, verbose_name='体育评分', null=True)
    Volunteer = models.IntegerField(default=0, verbose_name='志愿活动评分', null=False)
    Labor = models.IntegerField(default=0, verbose_name='劳务活动评分', null=False)
    morality = models.IntegerField(default=0, verbose_name='思想道德评分', null=True)
    class Meta:
        db_table = 'ComprehensiveDevelopment'
class responsible(models.Model):
    name = models.CharField(max_length=200, verbose_name='姓名', null=True)
    Employeeno = models.IntegerField(default=0, verbose_name='职工号', primary_key=True)
    password = models.IntegerField(default=0, verbose_name='密码', null=True)
    class Meta:
        db_table = 'responsible'
class administrator(models.Model):
    name = models.CharField(max_length=200, verbose_name='姓名', null=True)
    Employeeno = models.IntegerField(default=0, verbose_name='职工号', primary_key=True)
    password = models.IntegerField(default=0, verbose_name='密码', null=True)
    class Meta:
        db_table = 'administrator'

class shenhe(models.Model):
    id = models.IntegerField(default=0, verbose_name='学号',  primary_key=True)
    miaoshu = models.CharField(max_length=200,verbose_name='材料描述', null=True )
    leibie = models.CharField(max_length=200,verbose_name='材料类别', null=True)
    image = models.ImageField(default=0,verbose_name='材料图片',  null=True)
    class Meta:
        db_table = 'shenhe'