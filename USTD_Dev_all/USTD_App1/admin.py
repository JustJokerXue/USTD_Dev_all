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

# Register your models here.
admin.site.register(Student)
admin.site.register(Score)
admin.site.register(Knowledge)
admin.site.register(Innovation)
admin.site.register(majorTechnology)
admin.site.register(manage)
admin.site.register(ComprehensiveDevelopment)
admin.site.register(responsible)
admin.site.register(administrator)
admin.site.register(shenhe)

admin.site.site_header = '大学生发展规划与评估系统管理后台'  # 设置header
admin.site.site_title = '大学生发展规划与评估系统管理后台'  # 设置title
admin.site.index_title = '大学生发展规划与评估系统管理后台'
