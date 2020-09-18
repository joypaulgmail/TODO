from django.shortcuts import render
from task.models import task,working,shoping,meeting
from django.http import HttpResponse
from playsound import playsound
import datetime

def home(request):
    hour=datetime.datetime.now().hour
    if hour>12:
        hour=hour-12
    else:
        hour=hour
    if hour<10:
        hour="0"+str(hour)
    else:
        hour=str(hour)
    print(hour,"hour")






    minute=str(datetime.datetime.now().minute)

    current_time=hour+":"+minute

    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    year = str(datetime.datetime.now().year)

    if month<10:
        month=str(0)+str(month)
    else:
        month=str(month)

    if day < 10:
        day = str(0) + str(day)
    else:
        day = str(day)



    current_date =month+"/"+day+"/"+year
    print("current date",current_date)
    print(current_time)





    ob = task.objects.all()
    for i in ob:
        if i.date==current_date and i.time==current_time:
            playsound('M:\songs\mornig.mp3')
            break





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
    ob=working.objects.all()

    return render(request, "work/work.html",{"task":ob})


def workadd(request):

        return render(request, "work/worktask.html")

def addsubmit(request):
    if request.method == "POST":
        title = request.POST.get('title')
        time = request.POST.get('time')
        date = request.POST.get('date')
        s = working(title=title, time=time, date=date)
        s.save()
        newob = working.objects.all()
        return render(request, "work/work.html", {"task": newob})

def editwork(request):
    if request.method=="POST":
        id=request.POST.get('id')
        ob=working.objects.get(id=id)
        title=ob.title
        date=ob.date
        time=ob.time
        ob.delete()
        return render(request,"work/worktask.html",{"title":title,"date":date,"time":time,})
    else:
        return render(request, "work/work.html")


def deletework(request):
    if request.method=="POST":
        id=request.POST.get('id')
        ob=working.objects.get(id=id)
        ob.delete()
        newob=working.objects.all()
        return render(request,"work/work.html",{"task":newob})
    else:
        return render(request, "task/home.html", {"task": newob})








