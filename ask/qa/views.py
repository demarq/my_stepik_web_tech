from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import *

def home(request):
    questions = Question.objects.new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/blog/all_posts/?page='
    page = paginator.page(page)  # Page
    return render(request, 'qa/home.html', {
        'posts': page.object_list,
        'paginator': paginator, 'page': page,
    })


def test(request, *args, **kwargs):
    return HttpResponse('OK')

