"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task2.views import cls_index, fnc_index
from task3.views import home, catalog, contacts
from task4.views import home4, catalog4, contacts4
from task5.views import sign_up_by_django, sign_up_by_html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cls_index/', cls_index.as_view()),
    path('fnc_index/', fnc_index),

    path('', home, name='home'), # name указываем из-за конструкции {% url 'home' %} в шаблоне
    path('catalog/', catalog, name='catalog'),
    path('contacts/', contacts, name='contacts'),

    path('4', home4, name='home'),
    path('catalog4/', catalog4, name='catalog'),
    path('contacts4/', contacts4, name='contacts'),

    path('5', sign_up_by_html),
    path('django_sign_up/', sign_up_by_django)
]
