from django.shortcuts import render
from .models import QuestionModel

# Create your views here.
def addquestion(request):
    question = QuestionModel.objects.all()
    return render( request,"newquestion.html", {"questions":question})
