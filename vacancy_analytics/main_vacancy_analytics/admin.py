from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(ImageModel)
admin.site.register(GeneralSalariesYear)
admin.site.register(GeneralCountVacanciesYear)
admin.site.register(GeneralCitySalary)
admin.site.register(GeneralCityShare)
admin.site.register(GeneralSkillFrequency)
admin.site.register(SalariesYear)
admin.site.register(CountVacanciesYear)
admin.site.register(CitySalary)
admin.site.register(CityShare)
admin.site.register(SkillFrequency)
