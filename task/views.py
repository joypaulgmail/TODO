from django.shortcuts import render
from task.models import task,working,shoping,meeting
from django.http import HttpResponse,Http404
from playsound import playsound
import datetime
from django.views.generic import View
import json
month = datetime.datetime.now().month
day = datetime.datetime.now().day
dm = str(day) + "/" + str(month)
weekday=datetime.datetime.today().strftime('%A')

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








    minute=datetime.datetime.now().minute

    if minute<10:
        minute=str(0)+str(minute)

    else:
        minute = str(minute)

    print(hour, "hour")

    current_time=hour+":"+minute

    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    dm=str(day)+"/"+str(month)
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






    return render(request,"task/home.html",{"task":ob,"time":dm,'weekday':weekday})

def personaltask(request):




    return render(request,"task/task.html")

def addtask(request):
    date=datetime.datetime.now().day
    month=datetime.datetime.now().month

    if request.method=="POST":
        title=request.POST.get('title')
        time=request.POST.get('time')
        date=request.POST.get('date')
        s=task(title=title,time=time,date=date,category="personal")
        s.save()
        newob = task.objects.all()
        return render(request, "task/home.html", {"task": newob,"time":dm})


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
        return render(request,"task/home.html",{"task":newob,"time":dm})


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

class Totaldata(View):
    def get(self,request,*args,**kwargs):
        ob=task.objects.all()

        json_data=serialize('json',ob,fields=('title','date'))
        dic=json.loads(json_data)
        lis=[]
        for ob in dic:
            single=ob['fields']
            lis.append(single)
        json_data=json.dumps(lis)
        print(lis)

        return HttpResponse(json_data,content_type="application/json")
        


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from task.models import task
from task.serial import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@csrf_exempt
def snippet_list(request,pk):
    try:
        single = task.objects.get(id=pk)
    except task.DoesNotExist:
        return HttpResponse(status=401)

    if request.method == 'GET':
        totalobjects=task.objects.all()
        serializer = TaskSerializer(totalobjects,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            print("post")
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)





    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(single, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        single.delete()
        return HttpResponse(status=201)








@api_view(['GET','POST','PUT','DELETE'])
def listdata(request,pk):
    try:
        single = task.objects.get(id=pk)
    except task.DoesNotExist:
        return HttpResponse(status=401)
    if request.method=="GET":
        ob=task.objects.all()
        serializer=TaskSerializer(ob,many=True)
        return Response(serializer.data)

    elif request.method=="POST":
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=="PUT":
        serializer=TaskSerializer(single,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=="DELETE":
        single.delete()
        return HttpResponse(status=201)


from rest_framework.views import APIView
class TaskList(APIView):

    def get_object(self, pk):
        try:
            return task.objects.get(id=pk)
        except task.DoesNotExist:
            raise Http404





    def get(self,request,pk,format=None):
        qr=task.objects.all()
        serializer=TaskSerializer(qr,many=True)
        return Response(serializer.data)
    def post(self,request,pk):
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        ob=self.get_object(pk)
        serializer=TaskSerializer(ob,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        ob= self.get_object(pk)
        ob.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def gt(request,pk):
    try:
        qr=task.objects.get(id=pk)
    except task.DoesNotExist:
        return HttpResponse(status=401)
    serializer=TaskSerializer(qr)
    return Response(serializer.data)

@api_view(['POST'])
def pst(request):
    serializer=TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

























