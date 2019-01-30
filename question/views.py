from django.shortcuts import render, redirect
from .models import Question

# Create your views here.
def index(request):
    questions = Question.objects.all()
    
    return render(request,"question/index.html",{"questions":questions})
    
def new(request):
    return render(request,"question/new.html")

def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    
    Question.objects.create(title=title,content=content)
    return redirect("/questions/")
    
def read(request, id):
    question = Question.objects.get(pk=id)
    return render(request, "question/read.html",{"question":question})
    
def comment_create(request):
    pass