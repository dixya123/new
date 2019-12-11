from django import forms
from .models import QuestionModel, AnswerModel

class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionForm
        fields = '__all__'