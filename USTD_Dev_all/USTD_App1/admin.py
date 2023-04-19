from USTD_App1.models import Early_Warning
# Register your models here.
<<<<<<< HEAD
from .models import Innovation, majorTechnology, manage, ComprehensiveDevelopment, responsible, \
    administrator, GraduationRequirement, Application, Activity
=======
from USTD_App1.models import Innovation, majorTechnology, manage, ComprehensiveDevelopment, responsible, \
    administrator, GraduationRequirement, Application, OverallScore
>>>>>>> 7a9a20fdf8864799bfc1c23a4593d87c97d29d53
# from USTD_App1.models import Knowledge
from USTD_App1.models import Course
from USTD_App1.models import Score
from USTD_App1.models import Student
from USTD_App1.models import Activity
from USTD_App1.models import Weight
from USTD_App1.models import shenhe
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.text import capfirst

admin.site.site_header = '大学生发展综合素质测评系统管理后台'  # 设置header
admin.site.site_title = '大学生发展综合素质测评系统管理后台'  # 设置title
admin.site.index_title = '大学生发展综合素质测评系统管理后台'


# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):  # 学生用户信息表后台布局设计
#     list_display = ('id', 'name', 'age', 'sp', 'pwd')
#     list_display_links = ("id",)
#     search_fields = ('id', 'name')  # 查找
#     list_per_page = 20
#     list_editable = ('name', 'age', 'sp', 'pwd')
#     list_filter = ("id", "sp")
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):  # 学生用户信息表后台布局设计
    list_display = ('id', 'name', 'age', 'major', 'pwd', 'banji', 'department')
    list_display_links = ("id",)
    search_fields = ('id', 'name')  # 查找
    list_per_page = 20
    list_editable = ('name', 'age', 'major', 'pwd')
    list_filter = ("id", "major", 'banji', 'department')

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            stu = form.save()
            print(stu.id)
            stu_cx = Innovation(sno=stu.id, name=stu.name)
            stu_cx.save()

        super().save_model(request, obj, form, change)


@admin.register(OverallScore)
class OverallScoreAdmin(admin.ModelAdmin):  # 总评成绩表后台布局设计
    list_display = ('id', 'name', 'banji', 'major', 'department', 'total_score')
    list_display_links = ("id",)
    search_fields = ('id', 'name',)  # 查找
    list_per_page = 20
    list_editable = ('total_score',)
    list_filter = ('banji', 'major', 'department')


@admin.register(Weight)
class Weight(admin.ModelAdmin):  # 学业预警成绩表后台布局设计
    list_display = ('id', 'zyweight', 'cxweight', 'zsweight', 'glweight', 'zhweight')
    list_display_links = ("id",)
    search_fields = ('zyweight',)  # 查找
    list_per_page = 20
    list_editable = ('zyweight', 'cxweight', 'zsweight', 'glweight', 'zhweight')
    # list_filter = ("id", "sp")


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):  # 学生五大方面评分表后台布局设计
    list_display = ('id', 'zy', 'cx', 'zs', 'gl', 'zh', 'overallgrade')
    list_display_links = ("id",)
    search_fields = ('id',)  # 查找
    list_per_page = 20
    list_editable = ('zy', 'cx', 'zs', 'gl', 'zh', 'overallgrade')


@admin.register(Course)
class Course(admin.ModelAdmin):  # 知识学习表后台布局设计
    list_display = ('stu_id', 'name', 'course', 'grade', 'gpa')
    list_display_links = ("stu_id",)
    search_fields = ('stu_id', 'course')  # 查找
    list_per_page = 20
    list_editable = ('course', 'grade', 'gpa')
    # list_filter = ("id", "sp")


# @admin.register(Knowledge)
# class KnowledgeAdmin(admin.ModelAdmin):  # 学生知识学习评分表后台布局设计
#     list_display = ('name', 'sno', 'java', 'dataStructure', 'Gaverage')
#     list_display_links = ("sno",)
#     search_fields = ('name',)  # 查找
#     list_per_page = 20
#     list_editable = ('name', 'java', 'dataStructure', 'Gaverage')


@admin.register(Innovation)
class InnovationAdmin(admin.ModelAdmin):  # 学生创新创业评分表后台布局设计
    list_display = ('name', 'sno', 'banji', 'major', 'department', 'total_score')
    list_display_links = ("sno",)
    search_fields = ('name',)  # 查找
    list_filter = ('banji', 'major', 'department')
    list_per_page = 20
    list_editable = ('total_score',)


@admin.register(majorTechnology)
class majorTechnologyAdmin(admin.ModelAdmin):  # 学生专业技术评分白后台布局设计
    list_display = ('name', 'sno', 'banji', 'major', 'department', 'total_score')
    list_display_links = ("sno",)
    search_fields = ('name',)  # 查找
    list_filter = ('banji', 'major', 'department')
    list_per_page = 20
    list_editable = ('total_score',)


@admin.register(manage)
class manageAdmin(admin.ModelAdmin):  # 学生管理实践评分表后台布局设计
    list_display = ('name', 'sno', 'banji', 'major', 'department', 'total_score')
    list_display_links = ("sno",)
    search_fields = ('name',)  # 查找
    list_filter = ('banji', 'major', 'department')
    list_per_page = 20
    list_editable = ('total_score',)


@admin.register(ComprehensiveDevelopment)
class ComprehensiveDevelopmentAdmin(admin.ModelAdmin):  # 学生综合发展评分表后台布局设计
    list_display = ('name', 'sno', 'banji', 'major', 'department', 'total_score')
    list_display_links = ("sno",)
    search_fields = ('name',)  # 查找
    list_filter = ('banji', 'major', 'department')
    list_per_page = 20
    list_editable = ('total_score',)


@admin.register(Activity)
class Activity(admin.ModelAdmin):  # 活动汇总表后台布局设计
    list_display = ('id', 'aname', 'content', 'category', 'time')
    list_display_links = ("id",)
    search_fields = ('id', 'aname')  # 查找
    list_per_page = 10
    list_editable = ('aname', 'content', 'category', 'time')
    ordering = ('id',)
    # list_filter = ("id", "sp")


@admin.register(Application)
class Application(admin.ModelAdmin):  # 活动报名表后台布局设计
    list_display = ('aid', 'aname', 'no', 'name', 'banji')
    list_display_links = ("aid",)
    search_fields = ('aid', 'no')  # 查找
    list_per_page = 10
    # list_editable = ('aname', 'content', 'category', 'time')
    ordering = ('aid',)


# @admin.register(Early_Warning)
# class Early_WarningAdmin(admin.ModelAdmin):  # 学业预警成绩表后台布局设计
#     list_display = ('id', 'minimum', 'compulsory', 'elective', 'physical', 'cet4', 'mandarin')
#     list_display_links = ("id",)
#     search_fields = ('id',)  # 查找
#     list_per_page = 20
#     list_editable = ('minimum', 'compulsory', 'elective', 'physical', 'cet4', 'mandarin')
#     # list_filter = ("id", "sp")
@admin.register(Early_Warning)
class Early_WarningAdmin(admin.ModelAdmin):  # 学业预警成绩表后台布局设计
    list_display = ('id', 'minimum', 'compulsory', 'elective', 'physical', 'cet4', 'mandarin', 'grad_req_id')
    list_display_links = ("id",)
    search_fields = ('id',)  # 查找
    list_per_page = 20
    list_editable = ('minimum', 'compulsory', 'elective', 'physical', 'cet4', 'mandarin')
    fk_fields = ['grad_req_id']
    # list_filter = ("id", "sp")


@admin.register(responsible)
class responsibleAdmin(admin.ModelAdmin):  # 负责人用户信息表后台布局设计
    list_display = ('name', 'Employeeno', 'password')
    list_display_links = ("Employeeno",)
    search_fields = ('name',)  # 查找
    list_per_page = 20
    list_editable = ('name', 'password')


@admin.register(administrator)
class administratorAdmin(admin.ModelAdmin):  # 管理员用户信息表后台布局设计
    list_display = ('name', 'Employeeno', 'password')
    list_display_links = ("Employeeno",)
    search_fields = ('name',)  # 查找
    list_per_page = 20
    list_editable = ('name', 'password')


@admin.register(shenhe)
# admin.site.register(要写的表)  与  @admin.register(要写的表)  功能是一样的
class shenheAdmin(admin.ModelAdmin):  # 上传审核材料汇总表后台布局设计
    list_display = ('no', 'miaoshu', 'leibie', 'extra_points', 'image', 'image_img', 'zhuangtai')
    list_display_links = ("no",)
    search_fields = ('no',)  # 查找
    list_per_page = 20
    list_filter = ("no", "leibie", "zhuangtai")
    actions = ['mak_pub', 'mak_pub1', 'operate']
    ordering = ('zhuangtai',)

    # 判断通过的
    def mak_pub(self, request, queryset):
        for item in queryset:
            if item.zhuangtai == 'T':
                return
            try:
                score_item = None
                if item.leibie == '专业技术':
                    score_item = majorTechnology.objects
                elif item.leibie == '创新创业':
                    score_item = Innovation.objects
                elif item.leibie == '管理实践':
                    score_item = manage.objects
                elif item.leibie == '综合发展':
                    score_item = ComprehensiveDevelopment.objects
                score_item = score_item.get(item.no)
                score_item.total_score += item.extra_points
                score_item.save()
            except Exception as err:
                print(err)
            print(item)
            item.zhuangtai = 'T'
            item.save()

    # 更改Action的内容为通过
    mak_pub.short_description = "通过"

    # 判断未通过的
    def mak_pub1(self, request, queryset):
        for item in queryset:
            if item.zhuangtai == 'F':
                return
            try:
                score_item = None
                if item.leibie == '专业技术':
                    score_item = majorTechnology.objects
                elif item.leibie == '创新创业':
                    score_item = Innovation.objects
                elif item.leibie == '管理实践':
                    score_item = manage.objects
                elif item.leibie == '综合发展':
                    score_item = ComprehensiveDevelopment.objects
                score_item = score_item.get(item.no)
                score_item.total_score -= item.extra_points
                score_item.save()
            except Exception as err:
                print(err)
            print(item)
            item.zhuangtai = 'F'
            item.save()

    # 更改Action的内容为通过
    mak_pub1.short_description = "未通过"


@admin.register(GraduationRequirement)
class GraduationRequirementAdmin(admin.ModelAdmin):  # 毕业要求后台设计
    list_display = ('id', 'credit', 'compulsory', 'elective', 'physical', 'cet4', 'mandarin')
    list_display_links = ("id",)
    search_fields = ('id',)  # 查找
    list_per_page = 20
    list_editable = ('credit', 'compulsory', 'elective', 'physical', 'cet4', 'mandarin')


def find_model_index(name):
    count = 0
    for model, model_admin in admin.site._registry.items():
        if capfirst(model._meta.verbose_name_plural) == name:
            return count
        else:
            count += 1
    return count


def index_decorator(func):
    def inner(*args, **kwargs):
        templateresponse = func(*args, **kwargs)
        for app in templateresponse.context_data['app_list']:
            app['models'].sort(key=lambda x: find_model_index(x['name']))
        return templateresponse

    return inner


#
# registry = SortedDict()
# registry.update(admin.site._registry)
# admin.site._registry = registry
admin.site.index = index_decorator(admin.site.index)
admin.site.app_index = index_decorator(admin.site.app_index)
