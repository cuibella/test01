
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

def test01(request):

    return HttpResponse('这里是一个测试')

# 返回视图模板templates目录下的html文件

def test02(request):

    return render(request,'test01.html')


def index_view(request):
    return render(request, 'index.html')
