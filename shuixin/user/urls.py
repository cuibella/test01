from django.urls import path
from . import views

urlpatterns = [
    #访问注册页面
    path('first_page/',views.first_page,name='first_page'),

]