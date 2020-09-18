from django.urls import path
from task.views import home,personaltask,addtask,edittask,deletetask,work

urlpatterns = [
    path('',home,name="home"),
    path('personaltask/',personaltask),
    path('addtask/',addtask),
    path('delete/',deletetask),
    path('edit/',edittask),
    path('work/',work),
    path('worktask/',)
]