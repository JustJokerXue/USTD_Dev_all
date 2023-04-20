from import_export import resources

from .models import majorTechnology


class majorTechnologyResource(resources.ModelResource):
    class Meta:
        model = majorTechnology


from .models import Student


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student


from .models import GraduationRequirement


class GraduationRequirementResource(resources.ModelResource):
    class Meta:
        model = GraduationRequirement


from .models import Early_Warning


class Early_WarningResource(resources.ModelResource):
    class Meta:
        model = Early_Warning


from .models import Score


class ScoreResource(resources.ModelResource):
    class Meta:
        model = Score


from .models import Innovation


class InnovationResource(resources.ModelResource):
    class Meta:
        model = Innovation


from .models import Activity


class ActivityResource(resources.ModelResource):
    class Meta:
        model = Activity


from .models import Course


class CourseResource(resources.ModelResource):
    class Meta:
        model = Course


from .models import administrator


class administratorResource(resources.ModelResource):
    class Meta:
        model = administrator


from .models import manage


class manageResource(resources.ModelResource):
    class Meta:
        model = manage


from .models import ComprehensiveDevelopment


class ComprehensiveDevelopmentResource(resources.ModelResource):
    class Meta:
        model = ComprehensiveDevelopment


from .models import responsible


class responsibleResource(resources.ModelResource):
    class Meta:
        model = responsible


from .models import OverallScore


class OverallScoreResource(resources.ModelResource):
    class Meta:
        model = OverallScore


from .models import Weight


class WeightResource(resources.ModelResource):
    class Meta:
        model = Weight


from .models import Application


class ApplicationResource(resources.ModelResource):
    class Meta:
        model = Application


from .models import shenhe


class shenheResource(resources.ModelResource):
    class Meta:
        model = shenhe


from .models import learning


class learningResource(resources.ModelResource):
    class Meta:
        model = learning
