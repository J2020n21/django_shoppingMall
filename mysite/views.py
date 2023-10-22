# from django.http import HttpResponse
from django.shortcuts import render
from .models import MainContent

def index(request):
    # return HttpResponse("Hello World")
    content_list = MainContent.objects.order_by('pub_date')
    context = {'content_list':content_list}
    return render(request,'mysite/content_list.html',context)

def detail(req):
    # 선택된 요소의 id를 가져와 보여줌
    content_list = MainContent.objects.order_by('pub_date')
    context = {'content_list':content_list}
    return render(req, 'mysite/content_detail.html',context)