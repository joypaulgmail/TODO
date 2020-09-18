from django.db import models
class task(models.Model):
    title=models.CharField(max_length=150)
    date=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    category=models.CharField(max_length=100,default="anything")
    class Meta:
        db_table="task"

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







