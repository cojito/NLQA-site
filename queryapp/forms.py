from django import forms

class Question(forms.Form):
    question = forms.CharField(label='question', max_length=250)