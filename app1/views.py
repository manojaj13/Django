from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import teacher
from.models import answer
from.models import studentl
from.models import trainerl
# Create your views here.
def create(request):
    if request.method=='POST':
        x=request.POST['cname']
        c1=teacher.objects.create(cname=x,)
        c1.save()
        return render(request,'dashboard.html')
    else:
        return HttpResponse('accepts the post')
    
def course(request):
    content={}
    content['data']=teacher.objects.all()
    return render(request,'student.html',content)


def student(request):
    if request.method=='POST':
        x=request.POST['name']
        c1=answer.objects.create(name=x,)
        c1.save()
        return render(request,'dashboard.html')
    else:
        return HttpResponse('accepts the post')
    
def trainer(request):
    content={}
    content['data']=answer.objects.all()
    return render(request,'trainer.html',content)

def dashboard(request):
    return render(request,'dashboard.html')

def studentlog(request):
    if request.method=='POST':
        x=request.POST['slog']
        c1=studentl.objects.create(slog=x,)
        c1.save()
        content={}
        content['data']=teacher.objects.all()
        return render(request,'student.html',content)
    else:
        return HttpResponse('accepts the post')
    
def trainerlog(request):
    if request.method=='POST':
        x=request.POST['tlog']
        c1=trainerl.objects.create(tlog=x,)
        c1.save()
        content={}
        content['data']=answer.objects.all()
        return render(request,'trainer.html',content)
    else:
        return HttpResponse('accepts the post')
def studentlo(request):
    return render(request,'studentlog.html')
def trainerlo(request):
    return render(request,'trainerlog.html')