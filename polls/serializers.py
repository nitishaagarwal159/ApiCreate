from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField
from . models import employees,uploadem,uploadphone,receiverequest,Posts,Likes,Shares

class employeesSerializer(serializers.ModelSerializer):
   # emp_id = serializers.Field()
    class Meta:
        model=employees
       # fields=('firstname','lastname')
        fields='__all__'

class emailSerializer(serializers.ModelSerializer):
    class Meta:
        model =uploadem
       # fields=('id','email')
        fields='__all__'

class phoneSerializer(serializers.ModelSerializer):
    class Meta:
        model =uploadphone
       # fields=('id','email')
        fields='__all__'

class requestSerializer(serializers.ModelSerializer):
    class Meta:
        model=receiverequest
        fields='__all__'

class postSerializer(serializers.ModelSerializer):
    class Meta:
        model =Posts
       # fields=('id','email')
        fields='__all__'

class likesSerializer(serializers.ModelSerializer):
    class Meta:
        model =Likes
       # fields=('id','email')
        fields='__all__'

class countlikeSerializer(serializers.ModelSerializer):
     #like_count = serializers.SerializerMethodField()
     class Meta:
         model = Likes
         fields=('postliked','postlikedby')
    # def get_like_count(self,obj):
     #        return obj.postlikedby.all().count()


class shareSerializer(serializers.ModelSerializer):
    class Meta:
        model =Shares
       # fields=('id','email')
        fields='__all__'


class countshareSerializer(serializers.ModelSerializer):
    # like_count = serializers.SerializerMethodField()
    class Meta:
        model = Shares
        fields = ('postshared', 'postsharedby')