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


