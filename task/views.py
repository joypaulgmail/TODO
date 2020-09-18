from django.shortcuts import render
from task.models import task,working,shoping,meeting
from django.http import HttpResponse

def home(request):

    ob = task.objects.all()
    return render(request,"task/home.html",{"task":ob})

def personaltask(request):




    return render(request,"task/task.html")

def addtask(request):
    if request.method=="POST":
        title=request.POST.get('title')
        time=request.POST.get('time')
        date=request.POST.get('date')
        s=task(title=title,time=time,date=date,category="personal")
        s.save()
        newob = task.objects.all()
        return render(request, "task/home.html", {"task": newob})


def edittask(request):
    if request.method=="POST":
        id=request.POST.get('id')
        ob=task.objects.get(id=id)
        title=ob.title
        date=ob.date
        time=ob.time
        ob.delete()
        return render(request,"task/task.html",{"title":title,"date":date,"time":time,})
    else:
        return render(request, "task/home.html")


def deletetask(request):
    if request.method=="POST":
        id=request.POST.get('id')
        ob=task.objects.get(id=id)
        ob.delete()
        newob=task.objects.all()
        return render(request,"task/home.html",{"task":newob})
    else:
        return render(request, "task/home.html", {"task": newob})

def work(request):
    ob=meeting.objects.all()

    return render(request, "work/work.html",{"task":ob})

def worktask(request):




    return render(request,"work/worktask.html")


