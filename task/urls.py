from django.urls import path
from task.views import home,personaltask,addtask,edittask,deletetask,work,workadd,addsubmit,editwork,deletework,Totaldata,snippet_list,listdata,TaskList,gt,pst
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
    path('deletework/',deletework),
    path('data/',Totaldata.as_view()),
    path('list/<int:pk>',snippet_list),
    path('listdata/<int:pk>',listdata),
    path('tasklist/<int:pk>',TaskList.as_view()),
    path('get/<int:pk>',gt),
    path('pst/', pst),

]