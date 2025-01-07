from django.shortcuts import render

def home4(request):
    context = {
        'home': 'Главная',
        'catalog': 'Каталог услуг',
        'contacts': 'Контакты'
    }
    return render(request, 'home_index.html', context)


def catalog4(request):
    context = {
        'home': 'Главная',
        'catalog': 'Каталог услуг',
        'contacts': 'Контакты',
        'services': ['Диагностика', 'Кузовные работы', 'Слесарные работы']
    }
    return render(request, 'catalog_index.html', context)


def contacts4(request):
    context = {
        'home': 'Главная',
        'catalog': 'Каталог услуг',
        'contacts': 'Контакты'
    }
    return render(request, 'contacts_index.html', context)
