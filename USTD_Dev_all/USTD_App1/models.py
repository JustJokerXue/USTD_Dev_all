from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.shortcuts import redirect

# Create your models here.
from django.utils.html import format_html


# class Messages(models.Model):
#     title = models.CharField(max_length=50)
#     # type = models.ForeignKey(Type, on_delete=models.CASCADE)
#     # content = RichTextUploadingField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     # read_details = GenericRelation(ReadDetail)
#     created_time = models.DateTimeField(auto_now_add=True)
#     last_updated_time = models.DateTimeField(auto_now=True)
#
#     def get_url(self):
#         return reverse('blog_detail', kwargs={'blog_pk': self.pk})
#
#     def get_user(self):
#         return self.author
#
#     # def get_email(self):
#     #     return self.author.email
#
#     def __str__(self):
#         return "<Blog:%s>" % self.title
#
#     class Meta:
#         ordering = ['-created_time']


# class Early_Warning(models.Model):  # 学业预警成绩表
#     id = models.IntegerField(default=0, verbose_name='学号', primary_key=True)
#     minimum = models.IntegerField(default=0, verbose_name='最低学分要求', null=True)
#     compulsory = models.IntegerField(default=0, verbose_name='必修课成绩', null=True)
#     elective = models.IntegerField(default=0, verbose_name='选修课成绩', null=True)
#     physical = models.IntegerField(default=0, verbose_name='体测成绩', null=True)
#     cet4 = models.IntegerField(default=0, verbose_name='四级成绩', null=True)
#     mandarin = models.IntegerField(default=0, verbose_name='普通话成绩', null=True)
#
#     class Meta:
#         db_table = 'Early_Warning'
#         verbose_name = "学业预警"
#         verbose_name_plural = "学业预警"
#         constraints = [
#             models.CheckConstraint(check=models.Q(minimum__gte=0, minimum__lte=170), name='minimum'),
#             models.CheckConstraint(check=models.Q(compulsory__gte=0, compulsory__lte=100), name='compulsory'),
#             models.CheckConstraint(check=models.Q(elective__gte=0, elective__lte=100), name='elective'),
#             models.CheckConstraint(check=models.Q(physical__gte=0, physical__lte=100), name='physical'),
#             models.CheckConstraint(check=models.Q(cet4__gte=0, cet4__lte=750), name='cet4'),
#             models.CheckConstraint(check=models.Q(mandarin__gte=0, mandarin__lte=100), name='mandarin'),
#         ]

class GraduationRequirement(models.Model):  # 学生毕业要求表
    id = models.IntegerField(default=0, verbose_name='学业要求id', primary_key=True)
    credit = models.FloatField(default=0, verbose_name='要求学分', null=True)
    compulsory = models.FloatField(default=0, verbose_name='必修课成绩', null=True)
    elective = models.FloatField(default=0, verbose_name='选修课成绩', null=True)
    physical = models.FloatField(default=0, verbose_name='体测成绩', null=True)
    cet4 = models.FloatField(default=0, verbose_name='四级成绩', null=True)
    mandarin = models.FloatField(default=0, verbose_name='普通话成绩', null=True)

    class Meta:
        db_table = 'GraduationRequirement'
        verbose_name = "学业要求"
        verbose_name_plural = "学业要求"
        constraints = [
            models.CheckConstraint(check=models.Q(credit__gte=0, credit__lte=170), name='grad_req_credit'),
            models.CheckConstraint(check=models.Q(compulsory__gte=0, compulsory__lte=100), name='grad_req_compulsory'),
            models.CheckConstraint(check=models.Q(elective__gte=0, elective__lte=100), name='grad_req_elective'),
            models.CheckConstraint(check=models.Q(physical__gte=0, physical__lte=100), name='grad_req_physical'),
            models.CheckConstraint(check=models.Q(cet4__gte=0, cet4__lte=750), name='grad_req_cet4'),
            models.CheckConstraint(check=models.Q(mandarin__gte=0, mandarin__lte=100), name='grad_req_mandarin'),
        ]


class Early_Warning(models.Model):  # 学业预警成绩表
    id = models.IntegerField(default=0, verbose_name='学号', primary_key=True)
    minimum = models.FloatField(default=0, verbose_name='实修学分', null=True)
    compulsory = models.FloatField(default=0, verbose_name='必修课成绩', null=True)
    elective = models.FloatField(default=0, verbose_name='选修课成绩', null=True)
    physical = models.FloatField(default=0, verbose_name='体测成绩', null=True)
    cet4 = models.FloatField(default=0, verbose_name='四级成绩', null=True)
    mandarin = models.FloatField(default=0, verbose_name='普通话成绩', null=True)
    grad_req_id = models.ForeignKey(GraduationRequirement, blank=True, null=True,
                                    verbose_name="学业要求id", on_delete=models.DO_NOTHING,
                                    db_column='stu_gradReq_id')

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
    major = models.CharField(max_length=200, verbose_name='专业', null=True)
    pwd = models.IntegerField(verbose_name='密码', default=123456)
    banji = models.CharField(max_length=200, verbose_name='班级', null=True)
    department = models.CharField(max_length=200, verbose_name='院系', null=True)

    class Meta:
        db_table = 'Student'
        verbose_name = "学生"
        verbose_name_plural = "学生"

    def __str__(self):
        return self.name


class OverallScore(models.Model):  # 总评成绩表
    id = models.IntegerField(default=0, verbose_name='学号', primary_key=True)
    name = models.CharField(max_length=200, verbose_name='姓名', null=True)
    banji = models.CharField(max_length=200, verbose_name='班级', null=True)
    major = models.CharField(max_length=200, verbose_name='专业', null=True)
    department = models.CharField(max_length=200, verbose_name='院系', null=True)
    total_score = models.IntegerField(default=0, verbose_name='总评成绩')

    class Meta:
        db_table = 'OverallScore'
        verbose_name = "综测总评成绩"
        verbose_name_plural = "综测总评成绩"
        constraints = [
            models.CheckConstraint(check=models.Q(total_score__gte=0, total_score__lte=100),
                                   name='overall_score_total_score'),
        ]


class Score(models.Model):  # 学生五大方面评分表
    id = models.IntegerField(default=0, verbose_name='学号', primary_key=True)
    zy = models.IntegerField(default=0, verbose_name='专业技术能力', null=True)
    cx = models.IntegerField(default=0, verbose_name='创新创业能力', null=True)
    zs = models.IntegerField(default=0, verbose_name='知识学习能力', null=True)
    gl = models.IntegerField(default=0, verbose_name='管理实践能力', null=True)
    zh = models.IntegerField(default=0, verbose_name='综合发展能力', null=True)
    overallgrade = models.IntegerField(default=0, verbose_name='总评成绩', null=True)

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
            models.CheckConstraint(check=models.Q(overallgrade__gte=0, overallgrade__lte=100), name='overallgrade'),
        ]


class Course(models.Model):  # 学生学习成绩表
    name = models.CharField(max_length=200, verbose_name='姓名', null=True)
    stu_id = models.IntegerField(default=0, verbose_name='学号')
    course = models.CharField(max_length=200, default='', verbose_name='课程', null=True)
    grade = models.IntegerField(default=0, verbose_name='成绩', null=True)
    gpa = models.FloatField(default=0, verbose_name='绩点', null=True)

    class Meta:
        db_table = 'Course'
        verbose_name = "知识学习"
        verbose_name_plural = "知识学习"
        constraints = [
            models.CheckConstraint(check=models.Q(grade__gte=0, grade__lte=100), name='grade'),
            models.CheckConstraint(check=models.Q(gpa__gte=0, gpa__lte=5), name='gpa'),
        ]

    def __str__(self):
        return self.name


# class Knowledge(models.Model):  # 学生知识学习评分表
#     name = models.CharField(max_length=200, verbose_name='姓名', null=True)
#     sno = models.IntegerField(default=0, verbose_name='学号', primary_key=True)
#     java = models.IntegerField(default=0, verbose_name='java课程', null=True)
#     dataStructure = models.IntegerField(default=0, verbose_name='数据结构', null=True)
#     Gaverage = models.FloatField(default=0, verbose_name='平均绩点', null=True)
#
#     class Meta:
#         db_table = 'Knowledge'
#         verbose_name = "知识学习"
#         verbose_name_plural = "知识学习"
#         constraints = [
#             models.CheckConstraint(check=models.Q(java__gte=0, java__lte=100), name='java'),
#             models.CheckConstraint(check=models.Q(dataStructure__gte=0, dataStructure__lte=100), name='dataStructure'),
#             models.CheckConstraint(check=models.Q(Gaverage__gte=0, Gaverage__lte=5), name='Gaverage'),
#         ]
#
#     def __str__(self):
#         return self.name


class Innovation(models.Model):  # 学生创新创业评分表
    name = models.CharField(max_length=200, verbose_name='姓名', null=True)
    sno = models.IntegerField(default=0, verbose_name='学号', primary_key=True)
    banji = models.CharField(max_length=200, verbose_name='班级', null=True)
    major = models.CharField(max_length=200, verbose_name='专业', null=True)
    department = models.CharField(max_length=200, verbose_name='院系', null=True)
    total_score = models.IntegerField(default=0, verbose_name='成绩')

    class Meta:
        db_table = 'Innovation'
        verbose_name = "创新创业"
        verbose_name_plural = "创新创业"
        constraints = [
            models.CheckConstraint(check=models.Q(total_score__gte=0, total_score__lte=100),
                                   name='innovation_total_score'),
        ]

    def __str__(self):
        return self.name


class majorTechnology(models.Model):  # 学生专业技术评分白
    name = models.CharField(max_length=200, verbose_name='姓名', null=True)
    sno = models.IntegerField(default=0, verbose_name='学号', primary_key=True)
    banji = models.CharField(max_length=200, verbose_name='班级', null=True)
    major = models.CharField(max_length=200, verbose_name='专业', null=True)
    department = models.CharField(max_length=200, verbose_name='院系', null=True)
    total_score = models.IntegerField(default=0, verbose_name='成绩')

    class Meta:
        db_table = 'majorTechnology'
        verbose_name = "专业技术"
        verbose_name_plural = "专业技术"
        constraints = [
            models.CheckConstraint(check=models.Q(total_score__gte=0, total_score__lte=100),
                                   name='major_technology_total_score'),
        ]

    def __str__(self):
        return self.name


class manage(models.Model):  # 学生管理实践评分表
    name = models.CharField(max_length=200, verbose_name='姓名', null=True)
    sno = models.IntegerField(default=0, verbose_name='学号', primary_key=True)
    banji = models.CharField(max_length=200, verbose_name='班级', null=True)
    major = models.CharField(max_length=200, verbose_name='专业', null=True)
    department = models.CharField(max_length=200, verbose_name='院系', null=True)
    total_score = models.IntegerField(default=0, verbose_name='成绩')

    class Meta:
        db_table = 'manage'
        verbose_name = "管理实践"
        verbose_name_plural = "管理实践"
        constraints = [
            models.CheckConstraint(check=models.Q(total_score__gte=0, total_score__lte=100),
                                   name='manage_total_score'),
        ]

    def __str__(self):
        return self.name


class ComprehensiveDevelopment(models.Model):  # 学生综合发展评分表
    name = models.CharField(max_length=200, verbose_name='姓名', null=True)
    sno = models.IntegerField(default=0, verbose_name='学号', primary_key=True)
    banji = models.CharField(max_length=200, verbose_name='班级', null=True)
    major = models.CharField(max_length=200, verbose_name='专业', null=True)
    department = models.CharField(max_length=200, verbose_name='院系', null=True)
    total_score = models.IntegerField(default=0, verbose_name='成绩')

    class Meta:
        db_table = 'ComprehensiveDevelopment'
        verbose_name = "综合发展"
        verbose_name_plural = "综合发展"
        constraints = [
            models.CheckConstraint(check=models.Q(total_score__gte=0, total_score__lte=100),
                                   name='dev_total_score'),
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


# class shenhe(models.Model):  # 上传审核材料汇总表
#     no = models.IntegerField(default=0, verbose_name='学号', null=True)
#     miaoshu = models.CharField(max_length=200, verbose_name='材料描述', null=True)
#     leibie = models.CharField(max_length=200, verbose_name='材料类别', null=True)
#     image = models.ImageField(default=0, verbose_name='材料图片', null=True)
#     image_img = models.ImageField(default=0, verbose_name='材料图片', null=True)
#     zhuangtai = models.CharField(max_length=200, verbose_name='状态',
#                                  choices=(('T', '通过'), ('F', '不通过'), ('D', '待审核')), default='D')
#
#     class Meta:
#         db_table = 'shenhe'
#         verbose_name = "审核"
#         verbose_name_plural = "审核"
#
#     def image_img(self):
#         # 这里添加一个防空判断
#         if not self.image:
#             return '无'
#         return format_html(
#             """<img src='{}' style='width:100px;height:100px;' >""",
#             self.image.url, self.image.url)
#
#     image_img.short_description = '图片'

class shenhe(models.Model):  # 上传审核材料汇总表
    # id = models.IntegerField(default=0, verbose_name='审核材料id', primary_key=True)
    no = models.IntegerField(default=0, verbose_name='学号', null=True)
    miaoshu = models.CharField(max_length=200, verbose_name='材料描述', null=True)
    leibie = models.CharField(max_length=200, verbose_name='材料类别',
                              choices=(('专业技术', '专业技术'), ('创新创业', '创新创业'),
                                       ('管理实践', '管理实践'), ('综合发展', '综合发展')), default='专业技术')
    extra_points = models.IntegerField(default=0, verbose_name='加分', null=True)
    image = models.ImageField(default=0, verbose_name='材料图片', null=True)
    image_img = models.ImageField(default=0, verbose_name='材料图片', null=True)
    zhuangtai = models.CharField(max_length=200, verbose_name='状态',
                                 choices=(('T', '通过'), ('F', '不通过'), ('D', '待审核')), default='D')

    class Meta:
        db_table = 'shenhe'
        verbose_name = "审核"
        verbose_name_plural = "审核"
        constraints = [
            models.CheckConstraint(check=models.Q(extra_points__gte=0, extra_points__lte=100),
                                   name='extra_points'),
        ]

    def image_img(self):
        # 这里添加一个防空判断
        if not self.image:
            return '无'
        return format_html(
            """<img src='{}' style='width:100px;height:100px;' >""",
            self.image.url, self.image.url)

    image_img.short_description = '图片'


class Weight(models.Model):  # 综测权重系数表
    zyweight = models.FloatField(default=0, verbose_name='专业技术权重', null=True)
    cxweight = models.FloatField(default=0, verbose_name='创新创业权重', null=True)
    zsweight = models.FloatField(default=0, verbose_name='知识学习权重', null=True)
    glweight = models.FloatField(default=0, verbose_name='管理实践权重', null=True)
    zhweight = models.FloatField(default=0, verbose_name='综合发展权重', null=True)

    class Meta:
        db_table = 'Weight'
        verbose_name = "综测权重系数"
        verbose_name_plural = "综测权重系数"
        constraints = [
            models.CheckConstraint(check=models.Q(zyweight__gte=0, zyweight__lte=1), name='zyweight'),
            models.CheckConstraint(check=models.Q(cxweight__gte=0, cxweight__lte=1), name='cxweight'),
            models.CheckConstraint(check=models.Q(zsweight__gte=0, zsweight__lte=1), name='zsweight'),
            models.CheckConstraint(check=models.Q(glweight__gte=0, glweight__lte=1), name='glweight'),
            models.CheckConstraint(check=models.Q(zhweight__gte=0, zhweight__lte=1), name='zhweight'),

        ]


class Activity(models.Model):  # 活动表
    aid = models.IntegerField(default=0, verbose_name='活动编号', null=True)
    aname = models.CharField(max_length=200, verbose_name='活动名称', null=True)
    content = models.CharField(max_length=200, verbose_name='活动内容', null=True)
    organizer = models.CharField(max_length=200, verbose_name='活动举办方', null=True)
    baoming = models.CharField(max_length=200, verbose_name='报名方式', null=True)

    class Meta:
        db_table = 'Activity'
        verbose_name = "活动"
        verbose_name_plural = "活动"
