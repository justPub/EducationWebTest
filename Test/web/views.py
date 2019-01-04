from django.shortcuts import render
from django.http.response import HttpResponse
from django.core.mail import send_mail
from web.models import Dreamreal
import json
import datetime

def Login(request):
    if request.method == "GET":
        result = {} # 先指定一个字典
        username = request.GET.get('username')
        mobile = request.GET.get('mobile')
        date = request.GET.get('date')
        result['user'] = username
        result['mobileNum'] = mobile
        result['date'] = date
        result = json.dumps(result)
        # 指定返回数据类型为json且编码为utf-8
        return HttpResponse(result, content_type='application/json;charset=utf-8')


def hello(request):
    today = datetime.datetime.now()

    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return render(request, "hello.html", {"today": today, "days_of_week": daysOfWeek})


def viewArticle(request, articleId):
   """ A view that display an article based on his ID"""
   text = "Displaying article Number : %s" %articleId
   return HttpResponse(text)


def viewArticles(request, year, month):
   text = "Displaying articles of : %s/%s"%(year, month)
   return HttpResponse(text)

def sendSimpleEmail(request,emailto):
   res = send_mail("hello paul", "comment tu vas?", "paul@polo.com", [emailto])
   return HttpResponse('%s'%res)