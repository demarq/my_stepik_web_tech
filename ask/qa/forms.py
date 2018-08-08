from django import forms
from .models import *


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title']
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        return text

    def clean_author(self):
        try:
            print('author:', self.cleaned_data['author'])
            author_id = int(self.cleaned_data['author'])
            return author_id
        except ValueError:
            raise forms.ValidationError('Corrupted auth id')

    def save(self):
        q = Question.objects.create(**self.cleaned_data)
        return q


class AnswerForm(forms.Form):
    text = forms.CharField(max_length=100)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_text(self):
        text = self.cleaned_data['text']
        return text

    def clean_question(self):
        try:
            question_id = Question.objects.get(id=int(self.cleaned_data['question']))
            return question_id
        except models.ObjectDoesNotExist:
            raise forms.ValidationError('Corrupted question id')

    def save(self):
        a = Answer.objects.create(**self.cleaned_data)
        return a
