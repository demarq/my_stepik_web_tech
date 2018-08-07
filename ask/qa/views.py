from django.shortcuts import render, get_object_or_404
from django.db.models import ObjectDoesNotExist
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import *


def home(request):
    print(request.path)
    if 'popular' in request.path:
        questions = Question.objects.popular()
    else:
        questions = Question.objects.new()
    limit = request.GET.get('limit', 5)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = request.path+'?page='
    page = paginator.page(page)  # Page
    print(page.object_list, '\n', paginator.num_pages, '\n', page)
    return render(request, 'qa/home.html', {
        'posts': page.object_list,
        'paginator': paginator, 'page': page,
        'object_list': page.object_list
    })


def question(request, id):
    questions = get_object_or_404(Question, id=id)
    try:
        answers = Answer.objects.filter(question_id=id)
    except ObjectDoesNotExist:
        answers = []
    return render(request, 'qa/question.html', {'question': questions,
                                                'answers': answers,
                                                })


def test(request, *args, **kwargs):
    return HttpResponse('OK')

