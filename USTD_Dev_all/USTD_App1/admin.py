from django.contrib import admin
from USTD_App1.models import Student
from USTD_App1.models import Score
from USTD_App1.models import Knowledge
from USTD_App1.models import Innovation
from USTD_App1.models import majorTechnology
from USTD_App1.models import manage
from USTD_App1.models import ComprehensiveDevelopment
from USTD_App1.models import responsible
from USTD_App1.models import administrator
from USTD_App1.models import shenhe
from USTD_App1.models import Early_Warning

# Register your models here.

admin.site.register(Early_Warning)
admin.site.register(Student)
admin.site.register(Score)
admin.site.register(Knowledge)
admin.site.register(Innovation)
admin.site.register(majorTechnology)
admin.site.register(manage)
admin.site.register(ComprehensiveDevelopment)
admin.site.register(responsible)
admin.site.register(administrator)
@admin.register(shenhe)
# admin.site.register(要写的表)  与  @admin.register(要写的表)  功能是一样的
class shenheAdmin(admin.ModelAdmin):
    list_display = ('no', 'miaoshu', 'leibie','image','zhuangtai')
    list_per_page = 20
    actions = ['mak_pub', 'mak_pub1']
    # 判断通过的

    def mak_pub(self, request, queryset):
        no=request.POST.get('no')
        print(no)
        shenhe.objects.update(no=no).update(zhuangtai='T')
        # shenhe.objects.update(zhuangtai='T')


    # 判断未通过的
    def mak_pub1(self, request, queryset):
        shenhe.objects.update(zhuangtai='F')
       # 更改Action的内容为通过
    mak_pub.short_description = "通过"
    mak_pub1.short_description = "未通过"

admin.site.site_header = '大学生综合素质测评系统管理后台'  # 设置header
admin.site.site_title = '大学生综合素质测评系统管理后台'  # 设置title
admin.site.index_title = '大学生综合素质测评系统管理后台'
