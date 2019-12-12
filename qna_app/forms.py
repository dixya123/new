from django import forms
from .models import QuestionModel, AnswerModel,CategoryModel


class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionModel
        fields = '__all__'

