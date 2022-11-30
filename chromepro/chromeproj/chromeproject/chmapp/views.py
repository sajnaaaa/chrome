from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile


# Create your views here.

def chrome(request):
    obj = Profile.objects.all()
    return render(request,"index.html",{'result':obj})


# def operation(request):
   # num1 = int(request.GET['num1'])
   # num2 = int(request.GET['num2'])
   # res1 = num1 - num2
    #res2 = num1 * num2
   # res3 = num1 / num2
    #return render(request, "result.html", {'result1': res1, 'result2': res2, 'result3': res3})
