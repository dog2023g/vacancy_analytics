from django.shortcuts import render
from django.http import HttpResponse

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
    context = {
        'links': links,
        'current_link': 'link_stat'
    }
    return render(request, 'main_vacancy_analytics/stat.html', context=context)


def salaries(request):
    context = {
        'links': links,
        'current_link': 'link_salaries'
    }
    return render(request, 'main_vacancy_analytics/salaries.html', context=context)


def geography(request):
    context = {
        'links': links,
        'current_link': 'link_geo'
    }
    return render(request, 'main_vacancy_analytics/geo.html', context=context)

def skills(request):
    context = {
        'links': links,
        'current_link': 'link_skills'
    }
    return render(request, 'main_vacancy_analytics/skills.html', context=context)

def last_vacancies(request):
    context = {
        'links': links,
        'current_link': 'link_last_vac'
    }
    return render(request, 'main_vacancy_analytics/last_vac.html', context=context)

