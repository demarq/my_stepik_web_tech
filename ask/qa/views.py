from django.shortcuts import render, get_object_or_404, reverse
from django.db.models import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from .models import *
from .forms import *


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
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        form.question = questions.id
        if form.is_valid():
            a = form.save()
            return HttpResponseRedirect(questions.get_url())
    else:
        form = AnswerForm()
        questions = get_object_or_404(Question, id=id)
        try:
            answers = Answer.objects.filter(question_id=id)
        except ObjectDoesNotExist:
            answers = []
        return render(request, 'qa/question.html', {'question': questions,
                                                    'answers': answers,
                                                    'form': form
                                                })


def ask(request):
    author = 1
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            ask = form.save()
            return HttpResponseRedirect(ask.get_url())
        else:
            print(form.errors)
            return render(request, 'qa/ask.html', {'form': form,
                                                   'author_id': author,
                                                   })

    else:
        form = AskForm()
        return render(request, 'qa/ask.html', {'form': form,
                                               'author_id': author,
                                               })


def test(request, *args, **kwargs):
    return HttpResponse('OK')

