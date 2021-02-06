from django.db import models
class task(models.Model):
    title=models.CharField(max_length=150)
    date=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    category=models.CharField(max_length=100,default="anything")
    class Meta:
        db_table="task"

class task2(models.Model):
    name=models.CharField(max_length=255)
    details=models.ForeignKey(task,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        db_table="task2"



class shoping(models.Model):
    title=models.CharField(max_length=150)
    date=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    class Meta:
        db_table="shoping"
    
class meeting(models.Model):
    title=models.CharField(max_length=150)
    date=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    class Meta:
        db_table = "meeting"

class working(models.Model):
    title = models.CharField(max_length=150)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)

    class Meta:
        db_table ="working"


from django.db.models.signals import post_delete
from django.dispatch import receiver
'''@receiver(post_delete,sender=task2)
def taskdelete(sender,instance,**kwargs):
    print("delete")
    instance.details.delete()
 
    '''










