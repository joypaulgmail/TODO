from django.contrib import admin
from task.models import task,shoping,meeting,working,task2

class Meetingadmin(admin.ModelAdmin):
    list_display = ['title','date','time']

admin.site.register(meeting,Meetingadmin)


class task2admin(admin.ModelAdmin):
    list_display = ['name','details']
admin.site.register(task2,task2admin)



class Taskadmin(admin.ModelAdmin):
    list_display = ['id','title','date','time','category']

admin.site.register(task,Taskadmin)




class Shopingadmin(admin.ModelAdmin):
    list_display = ['title','date','time']

admin.site.register(shoping,Shopingadmin)



class workadmin(admin.ModelAdmin):
    list_display = ['title','date','time']

admin.site.register(working,workadmin)
