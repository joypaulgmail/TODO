from django.urls import path
from task.views import home,personaltask,addtask,edittask,deletetask,work,workadd,addsubmit,editwork,deletework

urlpatterns = [
    path('',home,name="home"),
    path('personaltask/',personaltask),
    path('addtask/',addtask),
    path('delete/',deletetask),
    path('edit/',edittask),
    path('work/',work),
    path('workadd/',workadd),
    path('addsubmit/',addsubmit),
    path('editwork/',editwork),
    path('deletework/',deletework)

]