from django.shortcuts import render

def home(request):
    context = {
        'home': 'Главная',
        'catalog': 'Каталог услуг',
        'contacts': 'Контакты'
    }
    return render(request, 'home_index.html', context)


def catalog(request):
    return render(request, 'catalog_index.html')

def contacts(request):
    return render(request, 'contacts_index.html')
