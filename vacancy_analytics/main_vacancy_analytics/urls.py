from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main'),
    path('stats', statistic, name='stat'),
    path('salaries', salaries, name='demand'),
    path('geo', geography, name='geography'),
    path('skills', skills, name='skills'),
    path('last_vacancies', last_vacancies, name='last_vacancies'),
]