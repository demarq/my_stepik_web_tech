from django import forms
from django.contrib.auth import authenticate
from .models import *
from .custom_utils import startsWithWrongSymbol, containWrongSymbols


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if not startsWithWrongSymbol(username):
            raise forms.ValidationError('Username must starts with latin symbol.', code='WrongFirstSymbol')
        else:
            return username

    def clean_password(self):
        password = self.cleaned_data['password']
        return password

    def bad_login(self):
        self.add_error('username', 'Invalid login or password.')
        self.add_error('password', 'Invalid login or password.')


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    author = forms.HiddenInput()

    def clean_title(self):
        title = self.cleaned_data['title']
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        return text

    def clean_author(self):
        author = self.cleaned_data['login']
        print(author)
        return author

    def save(self):
        q = Question.objects.create(**self.cleaned_data)
        return q


class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Secret')
    email = forms.EmailField(label='Mail')

    def clean_username(self):
        un = self.cleaned_data['username']
        try:
            ifexist = User.objects.get(username=un)
            raise forms.ValidationError('Username already exist.')
        except models.ObjectDoesNotExist:
            pass

        if containWrongSymbols(un):
            return forms.ValidationError('Can contain only latin symbols')
        else:
            return un

    def clean_password(self):
        password = self.cleaned_data['password']
        return password

    def clean_email(self):
        email = self.cleaned_data['email']
        return email

    def save(self):
        q = User.objects.create_user(**self.cleaned_data)
        return q


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Ask a Question?', )
    author = forms.IntegerField(widget=forms.HiddenInput)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_text(self):
        text = self.cleaned_data['text']
        return text

    def clean_question(self):
        try:
            question_id = self.cleaned_data['question']
            question = Question.objects.get(id=question_id)
            return question
        except models.ObjectDoesNotExist:
            raise forms.ValidationError('Corrupted question id. Try again later.')

    def clean_author(self):
        try:
            author_id = self.cleaned_data['author']
            author = User.objects.get(id=author_id)
            return author
        except models.ObjectDoesNotExist:
            raise forms.ValidationError('Corrupted author id. Try again later.')

    def save(self):
        a = Answer.objects.create(**self.cleaned_data)
        return a
