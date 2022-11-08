from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import Student


# Create your views here.

def Hello(request):
    return HttpResponse('Hello World')


def login(request):
    return render()


def index(request):
    return render(request, 'index.html')


@csrf_protect
# 登录界面
def login(request):
    if request.method == "POST":
        id = request.POST.get('id')
        pwd = request.POST.get('pwd')
        if not all([id, pwd]):
            context = {
                'status': '错误！用户名和密码不能为空！',
                'length': 0
            }
            return render(request, 'login.html', context)
        else:
            student = Student.objects.filter(id=id, pwd=pwd)
            if len(student):

                return render(request, 'index.html')

            else:
                context = {
                    'status': '用户名密码错误！请重新输入！如未注册，请先注册！'
                }
                return render(request, 'login.html', context)
    else:
        context = {
            'status': '请输入用户名和密码',
            'length': 0
        }
        return render(request, 'login.html', context)
