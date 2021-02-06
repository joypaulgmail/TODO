from rest_framework import serializers
from task.models import task
from django.contrib.auth.models import User
class TaskSerializer(serializers.ModelSerializer):

    #url=serializers.HyperlinkedIdentityField(view_name='view_post',read_only=True)

    class Meta:
        model=task
        fields=['id','title','date','time']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

'''class TaskSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=150)
    date = serializers.CharField(max_length=100)
    time = serializers.CharField(max_length=100)
    category = serializers.CharField(max_length=100, default="anything")
    def create(self,validate_data):
        return task.objects.create(validate_data)

    def update(self,instance,validate_data):
        instance.title = validated_data.get('title', instance.title)
        instance.date = validated_data.get('date', instance.date)
        instance.time = validated_data.get('time', instance.time)
        instance.category= validated_data.get('category', instance.category)
        instance.save()
        return instance
        '''


'''from django.contrib.auth import authenticate,login,logout

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self,data):
        username=data.get("userame","")
        password=data.get("password","")
        if username and password:'''



