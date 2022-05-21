from django.shortcuts import render
from django.http import HttpResponse
from .test_api.register_api import Register

# Create your views here.

def register_view(request):
    result = ''
    if request.method == 'POST':
        sources = request.POST.get('sources')
        patter = request.POST.get('patter')
        phone = request.POST.get('phone')
        res = Register().test01(phone)
        result = f'注册成功:{res}'
    return render(request,'register.html',locals())

def register_post(request):
    sources = request.POST.get('sources')
    patter = request.POST.get('patter')
    phone = request.POST.get('phone')
    print('1')
    return HttpResponse(f'注册成功')

def first_page(request):
    dict = {}
    if request.method == 'GET':
        return render(request,'first_page.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        dict['name'] = name
        return render(request, 'first_page.html',dict)



