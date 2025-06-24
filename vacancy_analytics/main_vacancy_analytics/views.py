from django.shortcuts import render
from django.http import HttpResponse
from .models import *

links = [{"link_slug": "link_main", "link_name": "Главная", "path_name": "main"},
    {"link_slug": "link_stat", "link_name": "Общая статистика", "path_name": "stat"},
    {"link_slug": "link_salaries", "link_name": "Востребованность", "path_name": "demand"},
    {"link_slug": "link_geo", "link_name": "География", "path_name": "geography"},
    {"link_slug": "link_skills", "link_name": "Навыки", "path_name": "skills"},
    {"link_slug": "link_last_vac", "link_name": "Последние вакансии", "path_name": "last_vacancies"},
]

# Create your views here.
def index(request):
    context = {
        'links': links,
        'current_link': 'link_main'
    }
    return render(request, 'main_vacancy_analytics/main.html', context=context)


def statistic(request):
    salary_years_images = ImageModel.objects.filter(text='g_salary_years')
    salary_years = GeneralSalariesYear.objects.all()
    count_years_images = ImageModel.objects.filter(text='g_count_years')
    count_years = GeneralCountVacanciesYear.objects.all()
    salary_cities_images = ImageModel.objects.filter(text='g_salary_cities')
    salary_cities = GeneralCitySalary.objects.all()
    count_cities_images = ImageModel.objects.filter(text='g_count_cities')
    count_cities = GeneralCityShare.objects.all()
    skills_years_images = ImageModel.objects.filter(text='g_skills_years')
    skills_years = GeneralSkillFrequency.objects.all()
    context = {
        'links': links,
        'current_link': 'link_stat',
        'salary_years_images': salary_years_images,
        'salary_years': salary_years,
        'count_years_images': count_years_images,
        'count_years': count_years,
        'salary_cities_images': salary_cities_images,
        'salary_cities': salary_cities,
        'count_cities_images': count_cities_images,
        'count_cities': count_cities,
        'skills_years_images': skills_years_images,
        'skills_years': skills_years
    }
    return render(request, 'main_vacancy_analytics/stat.html', context=context)


def salaries(request):
    salary_years_images = ImageModel.objects.filter(text='salary_years')
    salary_years = SalariesYear.objects.all()
    count_years_images = ImageModel.objects.filter(text='count_years')
    count_years = CountVacanciesYear.objects.all()
    context = {
        'links': links,
        'current_link': 'link_salaries',
        'salary_years_images': salary_years_images,
        'salary_years': salary_years,
        'count_years_images': count_years_images,
        'count_years': count_years
    }
    return render(request, 'main_vacancy_analytics/salaries.html', context=context)


def geography(request):
    salary_cities_images = ImageModel.objects.filter(text='salary_cities')
    salary_cities = CitySalary.objects.all()
    count_cities_images = ImageModel.objects.filter(text='count_cities')
    count_cities = CityShare.objects.all()
    context = {
        'links': links,
        'current_link': 'link_geo',
        'salary_cities_images': salary_cities_images,
        'salary_cities': salary_cities,
        'count_cities_images': count_cities_images,
        'count_cities': count_cities,
    }
    return render(request, 'main_vacancy_analytics/geo.html', context=context)


def skills(request):
    skills_years_images = ImageModel.objects.filter(text='skills_years')
    skills_years = SkillFrequency.objects.all()
    context = {
        'links': links,
        'current_link': 'link_skills',
        'skills_years_images': skills_years_images,
        'skills_years': skills_years,
    }
    return render(request, 'main_vacancy_analytics/skills.html', context=context)


def last_vacancies(request):
    context = {
        'links': links,
        'current_link': 'link_last_vac'
    }
    return render(request, 'main_vacancy_analytics/last_vac.html', context=context)

