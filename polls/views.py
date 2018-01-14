from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from rest_framework.pagination import (LimitOffsetPagination,PageNumberPagination,)
from django.shortcuts import render
from .pagination import PostLimitOffsetPagination,PostPageNumberPagination
from . models import employees,uploadem,uploadphone,receiverequest,Posts,Likes,Shares
from . serializers import employeesSerializer,emailSerializer,phoneSerializer,requestSerializer,likesSerializer,postSerializer,shareSerializer,countlikeSerializer,countshareSerializer
class employeeList(APIView):

    def get(self,request):
        employees1=employees.objects.all() #get all employees
        serializer=employeesSerializer(employees1,many=True) #after serializing dats
        return Response(serializer.data)
    def post(self,request):
        employees1 = employees.objects.all()  # get all employees
        se = employeesSerializer(employees1, many=True)
        serializer=employeesSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            return  Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class emailList(APIView):
    def get(self,request):
        email1=uploadem.objects.all()
        serializer=emailSerializer(email1,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = emailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#class emailLi(generics.ListAPIView):
    #serializer_class = emailSerializer
    #permission_classes = [IsAuthenticated]
 #   def get_queryset(self):
  #     employee1 = self.kwargs['employ']
   #    email2=uploadem.objects.filter(employee=employee1)
    #  return Response(serializer.data)
    #def post(self):
    #    pass

class emailLi(APIView):
    #serializer_class = emailSerializer
    #permission_classes = [IsAuthenticated]
    def get(self,*args,**kwargs):
       employee1 = self.kwargs['employ']
       email2=uploadem.objects.filter(employee=employee1)
       serializer = emailSerializer(email2, many=True)
       return Response(serializer.data)
    def post(self):
        pass

class phoneList(APIView):
    def get(self,request):
        phone1=uploadphone.objects.all()
        serializer=phoneSerializer(phone1,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = phoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class phoneLi(APIView):
    def get(self,*args,**kwargs):
       employee1 = self.kwargs['contactno']
       phone2=uploadphone.objects.filter(employee=employee1)
       serializer = phoneSerializer(phone2, many=True)
       return Response(serializer.data)
    def post(self):
        pass

class receiveList(APIView):
    def get(self, request):
        request1 = receiverequest.objects.all()
        serializer = requestSerializer(request1, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = requestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class receiveLi(APIView):
    def get(self,*args,**kwargs):
       employee1 = self.kwargs['req']
       requ2=receiverequest.objects.filter(receive_id=employee1)
       serializer = requestSerializer(requ2, many=True)
       return Response(serializer.data)
    def post(self):
        pass

class likesList(APIView):
    def get(self, request):
        like1 = Likes.objects.all()
        serializer = likesSerializer(like1, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = likesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class numoflikes(APIView):
    pagination_class = PostLimitOffsetPagination
    def get(self,*args,**kwargs):
         like1=self.kwargs['idofpost']
         id1=Likes.objects.filter(id=like1)
         count=id1.count()
         serializer=countlikeSerializer(id1,many=True)
         return Response({"no_of_likes":count,"list_by_whom_postisliked":serializer.data})


class shareList(APIView):
    def get(self, request):
        share1 = Shares.objects.all()
        serializer = shareSerializer(share1, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer =shareSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class numofshares(APIView):
    pagination_class = PostLimitOffsetPagination
    def get(self,*args,**kwargs):
         like1=self.kwargs['idofpost']
         id1=Shares.objects.filter(id=like1)
         count=id1.count()
         serializer=countshareSerializer(id1,many=True)
         return Response({"no_of_shares":count,"list_by_whom_postisshared":serializer.data})

