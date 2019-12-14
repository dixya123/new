from django.shortcuts import render, redirect
from .forms import QuestionForm
from .models import QuestionModel, CategoryModel,AnswerModel
from django.http import HttpResponse
from django.views.generic import CreateView, ListView



# Create your views here.
def addquestion(request):

    if request.method == "POST":
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
                return redirect('qna:read')
            except:
                return HttpResponse('failed')
        else:            
            return HttpResponse(form.errors)
    
    else:
        form = QuestionForm
        category = CategoryModel.objects.all()
        # return render( request,"question.html", {"question":question})
        return render( request,"questionmodel_create.html", {"category":category})


def update_question(request,id):
    question = QuestionModel.objects.get(id=id)
    if request.method == "POST":
       
        form = QuestionForm(request.POST, request.FILES, instance=question)
        if form.is_valid:
            try:

                form.save()
                return redirect('qna:update',id)
            except:
                return HttpResponse('failed')
        else:            
            return HttpResponse(form.errors)
    
    else:

        form = QuestionForm(instance=question)
        # return render( request,"question.html", {"question":question})
        return render( request,"questionmodel_update.html", {"form":form})


def delete_question(request,id):
    
    question = QuestionModel.objects.get(id=id)
    question.delete()
    return redirect('qna:read')

def question_detail(request,id):
    question =QuestionModel.objects.filter(id=id).first()
    if request.method=="POST":
        answer= AnswerModel(answer_desc = request.POST['answer'],question=question)
        answer.save(force_insert=True)
        print('parameter', request.POST['answer'])

    answers= AnswerModel.objects.filter(question=id)
    
    d={
        'question': question,
        'answers': answers
    }
    return render(request,'detail.html',d)

def up_vote(request,id):

    instance=QuestionModel.objects.get(id=id)
    instance.question_votes +=1
    instance.save()
    return redirect('qna:read')


def questionlist(request):
    if('id' in request.session):
        #id= request.session['id'] 
        lists= QuestionModel.objects.all()
        return render (request,'questionmodel_list.html',{'question_list':lists})
    else:

        return redirect ('user:login')

    

class QuestionModelCreateView(CreateView):
    model = QuestionModel
    fields = '__all__'

class QuestionModelListView(ListView):
    model = QuestionModel
    queryset = QuestionModel.objects.all()

def test(request):
    return render(request,'test.html')

def detail(request,id):
    question =QuestionModel.objects.get(id=id)
    answers= AnswerModel.objects.filter(question=id)
    d={
        'question': question,
        'answers': answers
    }
    return render(request,'detail.html',d)
def ques_list(request):
    question=QuestionModel.objects.all()
    return render(request,'ques_list.html',{'question':question})
    



