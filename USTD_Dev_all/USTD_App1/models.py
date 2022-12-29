from django.db import models

# Create your models here.
from django.utils.html import format_html


class Early_Warning(models.Model):  # 学业预警成绩表
    id = models.IntegerField(default=0, verbose_name='学号', primary_key=True)
    minimum = models.IntegerField(default=0, verbose_name='最低学分要求', null=True)
    compulsory = models.IntegerField(default=0, verbose_name='必修课成绩', null=True)
    elective = models.IntegerField(default=0, verbose_name='选修课成绩', null=True)
    physical = models.IntegerField(default=0, verbose_name='体测成绩', null=True)
    cet4 = models.IntegerField(default=0, verbose_name='四级成绩', null=True)
    mandarin = models.IntegerField(default=0, verbose_name='普通话成绩', null=True)

    class Meta:
        db_table = 'Early_Warning'
        verbose_name = "学业预警"
        verbose_name_plural = "学业预警"
        constraints = [
            models.CheckConstraint(check=models.Q(minimum__gte=0, minimum__lte=170), name='minimum'),
            models.CheckConstraint(check=models.Q(compulsory__gte=0, compulsory__lte=100), name='compulsory'),
            models.CheckConstraint(check=models.Q(elective__gte=0, elective__lte=100), name='elective'),
            models.CheckConstraint(check=models.Q(physical__gte=0, physical__lte=100), name='physical'),
            models.CheckConstraint(check=models.Q(cet4__gte=0, cet4__lte=750), name='cet4'),
            models.CheckConstraint(check=models.Q(mandarin__gte=0, mandarin__lte=100), name='mandarin'),
        ]


class Student(models.Model):  # 学生用户信息表
    id = models.IntegerField(default=0, verbose_name='学号', primary_key=True)
    name = models.CharField(max_length=200, verbose_name='姓名', null=True)
    age = models.IntegerField(default=0, verbose_name='年龄', null=True)
    sp = models.CharField(max_length=200, verbose_name='专业', null=True)
    pwd = models.IntegerField(verbose_name='密码', default=123456)

    class Meta:
        db_table = 'Student'
        verbose_name = "学生"
        verbose_name_plural = "学生"

    def __str__(self):
        return self.name


class Score(models.Model):  # 学生五大方面评分表
    id = models.IntegerField(default=0, verbose_name='学号', primary_key=True)
    zy = models.IntegerField(default=0, verbose_name='专业技术能力', null=True)
    cx = models.IntegerField(default=0, verbose_name='创新创业能力', null=True)
    zs = models.IntegerField(default=0, verbose_name='知识学习能力', null=True)
    gl = models.IntegerField(default=0, verbose_name='管理实践能力', null=True)
    zh = models.IntegerField(default=0, verbose_name='综合发展能力', null=True)

    class Meta:
        db_table = 'Score'
        verbose_name = "评分"
        verbose_name_plural = "评分"
        constraints = [
            models.CheckConstraint(check=models.Q(zy__gte=0, zy__lte=100), name='zy'),
            models.CheckConstraint(check=models.Q(cx__gte=0, cx__lte=100), name='cx'),
            models.CheckConstraint(check=models.Q(zs__gte=0, zs__lte=100), name='zs'),
            models.CheckConstraint(check=models.Q(gl__gte=0, gl__lte=100), name='gl'),
            models.CheckConstraint(check=models.Q(zh__gte=0, zh__lte=100), name='zh'),
        ]


class Knowledge(models.Model):  # 学生知识学习评分表
    name = models.CharField(max_length=200, verbose_name='姓名', null=True)
    sno = models.IntegerField(default=0, verbose_name='学号', primary_key=True)
    java = models.IntegerField(default=0, verbose_name='java课程', null=True)
    dataStructure = models.IntegerField(default=0, verbose_name='数据结构', null=True)
    Gaverage = models.FloatField(default=0, verbose_name='平均绩点', null=True)

    class Meta:
        db_table = 'Knowledge'
        verbose_name = "知识学习"
        verbose_name_plural = "知识学习"
        constraints = [
            models.CheckConstraint(check=models.Q(java__gte=0, java__lte=100), name='java'),
            models.CheckConstraint(check=models.Q(dataStructure__gte=0, dataStructure__lte=100), name='dataStructure'),
            models.CheckConstraint(check=models.Q(Gaverage__gte=0, Gaverage__lte=5), name='Gaverage'),
        ]

    def __str__(self):
        return self.name


class Innovation(models.Model):  # 学生创新创业评分表
    name = models.CharField(max_length=200, verbose_name='姓名', null=True)
    sno = models.IntegerField(default=0, verbose_name='学号', primary_key=True)
    ContestRating = models.IntegerField(default=0, verbose_name='竞赛评分', null=False)
    PatentRcoring = models.IntegerField(default=0, verbose_name='专利评分', null=False)
    EntrepreneurialAchievement = models.IntegerField(default=0, verbose_name='创业成果评分', null=False)

    class Meta:
        db_table = 'Innovation'
        verbose_name = "创新创业"
        verbose_name_plural = "创新创业"
        constraints = [
            models.CheckConstraint(check=models.Q(ContestRating__gte=0, ContestRating__lte=100), name='ContestRating'),
            models.CheckConstraint(check=models.Q(PatentRcoring__gte=0, PatentRcoring__lte=100), name='PatentRcoring'),
            models.CheckConstraint(
                check=models.Q(EntrepreneurialAchievement__gte=0, EntrepreneurialAchievement__lte=100),
                name='EntrepreneurialAchievement'),
        ]

    def __str__(self):
        return self.name


class majorTechnology(models.Model):  # 学生专业技术评分白
    name = models.CharField(max_length=200, verbose_name='姓名', null=True)
    sno = models.IntegerField(default=0, verbose_name='学号', primary_key=True)
    ProjectPractice = models.IntegerField(default=0, verbose_name='项目实践', null=True)
    PaperGrading = models.IntegerField(default=0, verbose_name='论文评分', null=False)
    StudentTutor = models.IntegerField(default=0, verbose_name='学生导师评分', null=True)

    class Meta:
        db_table = 'majorTechnology'
        verbose_name = "专业技术"
        verbose_name_plural = "专业技术"
        constraints = [
            models.CheckConstraint(check=models.Q(ProjectPractice__gte=0, ProjectPractice__lte=100),
                                   name='ProjectPractice'),
            models.CheckConstraint(check=models.Q(PaperGrading__gte=0, PaperGrading__lte=100), name='PaperGrading'),
            models.CheckConstraint(check=models.Q(StudentTutor__gte=0, StudentTutor__lte=100), name='StudentTutor'),
        ]

    def __str__(self):
        return self.name


class manage(models.Model):  # 学生管理实践评分表
    name = models.CharField(max_length=200, verbose_name='姓名', null=True)
    sno = models.IntegerField(default=0, verbose_name='学号', primary_key=True)
    community = models.IntegerField(default=0, verbose_name='社团工作评分', null=False)
    StudentWork = models.IntegerField(default=0, verbose_name='学生工作评分', null=False)
    ProjectTeam = models.IntegerField(default=0, verbose_name='项目团队评分', null=True)

    class Meta:
        db_table = 'manage'
        verbose_name = "管理实践"
        verbose_name_plural = "管理实践"
        constraints = [
            models.CheckConstraint(check=models.Q(community__gte=0, community__lte=100),
                                   name='community'),
            models.CheckConstraint(check=models.Q(StudentWork__gte=0, StudentWork__lte=100), name='StudentWork'),
            models.CheckConstraint(check=models.Q(ProjectTeam__gte=0, ProjectTeam__lte=100), name='ProjectTeam'),
        ]

    def __str__(self):
        return self.name


class ComprehensiveDevelopment(models.Model):  # 学生综合发展评分表
    name = models.CharField(max_length=200, verbose_name='姓名', null=True)
    sno = models.IntegerField(default=0, verbose_name='学号', primary_key=True)
    physical = models.IntegerField(default=0, verbose_name='体育评分', null=True)
    Volunteer = models.IntegerField(default=0, verbose_name='志愿活动评分', null=False)
    Labor = models.IntegerField(default=0, verbose_name='劳务活动评分', null=False)
    morality = models.IntegerField(default=0, verbose_name='思想道德评分', null=True)

    class Meta:
        db_table = 'ComprehensiveDevelopment'
        verbose_name = "综合发展"
        verbose_name_plural = "综合发展"
        constraints = [
            models.CheckConstraint(check=models.Q(physical__gte=0, physical__lte=100),
                                   name='physical_1'),
            models.CheckConstraint(check=models.Q(Volunteer__gte=0, Volunteer__lte=100), name='Volunteer'),
            models.CheckConstraint(check=models.Q(Labor__gte=0, Labor__lte=100), name='Labor'),
            models.CheckConstraint(check=models.Q(morality__gte=0, morality__lte=100), name='morality'),
        ]

    def __str__(self):
        return self.name


class responsible(models.Model):  # 负责人用户信息表
    name = models.CharField(max_length=200, verbose_name='姓名', null=True)
    Employeeno = models.IntegerField(default=0, verbose_name='职工号', primary_key=True)
    password = models.IntegerField(default=0, verbose_name='密码', null=True)

    class Meta:
        db_table = 'responsible'
        verbose_name = "负责人"
        verbose_name_plural = "负责人"

    def __str__(self):
        return self.name


class administrator(models.Model):  # 管理员用户信息表
    name = models.CharField(max_length=200, verbose_name='姓名', null=True)
    Employeeno = models.IntegerField(default=0, verbose_name='职工号', primary_key=True)
    password = models.IntegerField(default=0, verbose_name='密码', null=True)

    class Meta:
        db_table = 'administrator'
        verbose_name = "管理员"
        verbose_name_plural = "管理员"

    def __str__(self):
        return self.name


class shenhe(models.Model):  # 上传审核材料汇总表
    no = models.IntegerField(default=0, verbose_name='学号', null=True)
    miaoshu = models.CharField(max_length=200, verbose_name='材料描述', null=True)
    leibie = models.CharField(max_length=200, verbose_name='材料类别', null=True)
    image = models.ImageField(default=0, verbose_name='材料图片', null=True)
    image_img = models.ImageField(default=0, verbose_name='材料图片', null=True)
    zhuangtai = models.CharField(max_length=200, verbose_name='状态',
                                 choices=(('T', '通过'), ('F', '不通过'), ('D', '待审核')), default='D')

    class Meta:
        db_table = 'shenhe'
        verbose_name = "审核"
        verbose_name_plural = "审核"

    def image_img(self):
        # 这里添加一个防空判断
        if not self.image:
            return '无'
        return format_html(
            """<img src='{}' style='width:100px;height:100px;' >""",
            self.image.url, self.image.url)

    image_img.short_description = '图片'
