from django.shortcuts import render

def home(request):
    return render(request, 'home_index.html')


def catalog(request):
    return render(request, 'catalog_index.html')

def contacts(request):
    return render(request, 'contacts_index.html')
