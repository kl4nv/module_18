from django.shortcuts import render
from django.http import HttpResponse

def sign_up_by_django(request):
    users = ['Valera', 'Michael', 'Nikita']
    context = {'info': {}}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if username not in users:
            if password == repeat_password:
                if int(age) >= 18:
                    users.append(username)
                    return HttpResponse(f'Приветствуем, {username}!')
                else:
                    context['info'] = {'error': 'Вы должны быть старше 18'}
            else:
                context['info'] = {'error': 'Пароли не совпадают'}
        else:
            context['info'] = {'error': 'Пользователь уже существует'}

        return render(request, 'registration_page.html', context)

    return render(request, 'registration_page.html', context)

def sign_up_by_html(request):
    return sign_up_by_django(request)
