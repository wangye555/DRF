"""loginDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# from views import login,index
from django.shortcuts import redirect,render,HttpResponse  # 跳转 请求  返回字符串


def demo(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'alex' and  pwd == 'alexbsb':
             return redirect('https://www.baidu.com')
        # print(request.POST,type(request.POST))
        # print(request.POST['user'],type(request.POST['user']))
        # print(request.POST['pwd'],type(request.POST['pwd']))
        # return HttpResponse("进来啊")
        # return redirect('https://www.baidu.com')
    return render(request,'demo.html')


def index(request):
    # return  render(request, 'index.html')
    return HttpResponse('这就是index页面')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^demo/',demo),
    url(r'^index/',index)
]
