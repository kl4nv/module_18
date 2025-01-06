from django.shortcuts import render
from django.views.generic import TemplateView


class cls_index(TemplateView):
    template_name = 'class_templates.html'


def fnc_index(request):
    return render(request, 'func_templates.html')