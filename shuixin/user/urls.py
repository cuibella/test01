from django.urls import path
from . import views

urlpatterns = [
    #访问注册页面
    path('/v/register',views.register_view,name='register_page'),
    path('/api/register',views.register_post),
]