from django.urls import path,include
from task.views import home,personaltask,addtask,edittask,deletetask,work,workadd,addsubmit,editwork,\
    deletework,Totaldata,snippet_list,listdata,TaskList,gt,pst,put,delete,GenericAPIView,TaskAPI, DetailApi,\
    TaskCreate,TaskRetUpDes,usen,UserApi,UserGen,DemoApi,Another,TaskMixin,Cre,Upd,Ex,geter,Helptask,dis,profile
from django.views.generic.base import  RedirectView
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
    path('put/<int:pk>',put),
    path('delete/<int:pk>',delete),
    path('apiget/<int:pk>',GenericAPIView.as_view()),
    path('taskapi/', TaskAPI.as_view()),
    path('taskapi/<int:id>',TaskAPI.as_view()),
    path('detailapi/<int:pk>', DetailApi.as_view()),
    path('taskcreate/', TaskCreate.as_view()),
    path('user/',usen ),
    path('userapi/<int:pk>',UserApi.as_view()),
    path('usergen/<int:pk>',UserGen.as_view()),
    path('demoapi/', DemoApi.as_view()),
    path('ano/<int:pk>',Another.as_view()),
    path('taskmixin/<int:pk>',TaskMixin.as_view()),
    path('cre/',Cre.as_view(),name="cre"),
    path('upd/<int:pk>',Upd.as_view()),
    path('ex/<int:pk>',Ex.as_view()),
    path('dems',geter),
    path('help',Helptask.as_view()),
    path('dis',dis),
    path('accounts/profile/',profile)








]