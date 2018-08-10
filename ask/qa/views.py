from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth import login as dologin
from django.contrib.auth import logout as dologout
from django.db.models import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from .models import *
from .forms import *


def home(request):
    print(request.user.get_username())
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
    print()
    questions = get_object_or_404(Question, id=id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        form.question = questions.id
        form.author = request.user.id
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
    request.encoding = 'utf-8'
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form.author = request.user
            ask = form.save()
            return HttpResponseRedirect(ask.get_url())
    else:
        form = AskForm()
        return render(request, 'qa/ask.html', {'form': form
                                               })


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            dologin(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'qa/signup.html', {'form': form})

    else:
        form = SignUpForm()
        return render(request, 'qa/signup.html', {'form': form})


@require_GET
def logout(request):
    dologout(request)
    return HttpResponseRedirect('/')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        next_ref = request.POST.get('next_ref', '/')
        print(request.POST.get('login'), request.POST.get('password'))
        user = authenticate(username=request.POST.get('login'), password=request.POST.get('password'))
        if form.is_valid():
            if user:
                dologin(request, user=user)
                return HttpResponseRedirect(next_ref)
            else:
                form.bad_login()
                return render(request, 'qa/login.html', {'form': form})
        else:
            return render(request, 'qa/login.html', {'form': form})
    else:
        next_ref = request.GET.get('next_ref', '/')
        form = LoginForm()
        return render(request, 'qa/login.html', {'form': form,
                                                 'next_ref': next_ref})

