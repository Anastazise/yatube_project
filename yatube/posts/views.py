from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):    
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Главная страница',
    }
    return render(request, template, context)

def group_posts(request, slug):
    template = 'posts/group_list.html' 
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Группаы проекта Yatube',
    }
    return render(request, template, context)