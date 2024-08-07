from django.shortcuts import render

from goods.models import Category


def index(request):
    categories = Category.objects.all().order_by('name')
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        'categories': categories,
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том какой классный этот интернет магазин.',
    }

    return render(request, 'main/about.html', context)
