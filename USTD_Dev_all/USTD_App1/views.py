
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import Student
from .models import Score
import numpy as np
import matplotlib.pyplot as plt




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
        #request.session['ID'] = id
        if not all([id, pwd]):
            context = {
                'status': '错误！用户名和密码不能为空！',
                'length': 0
            }
            return render(request, 'login.html', context)
        else:
            student = Student.objects.filter(id=id, pwd=pwd)
            if len(student):
                select(id)
                return render(request, 'index.html')#{"ID":ID}

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

def select(i):
    S = Score.objects.get(id=i)
    results = [{"大学英语": S.zy, "高等数学": S.cx, "体育": S.zs, "计算机基础": S.gl, "程序设计": S.zh},
               {"大学英语": 80, "高等数学": 90, "体育": 91, "计算机基础": 85, "程序设计": 88}]
    data_length = len(results[0])
    # 将极坐标根据数据长度进行等分
    angles = np.linspace(0, 2 * np.pi, data_length, endpoint=False)
    labels = [key for key in results[0].keys()]
    score = [[v for v in result.values()] for result in results]
    # 使雷达图数据封闭
    score_a = np.concatenate((score[0], [score[0][0]]))
    score_b = np.concatenate((score[1], [score[1][0]]))
    angles = np.concatenate((angles, [angles[0]]))
    labels = np.concatenate((labels, [labels[0]]))
    # 设置图形的大小
    fig = plt.figure(figsize=(8, 6), dpi=100)
    # 新建一个子图
    ax = plt.subplot(111, polar=True)
    # 绘制雷达图
    ax.plot(angles, score_a, color='g')
    ax.plot(angles, score_b, color='b')
    # 设置雷达图中每一项的标签显示
    ax.set_thetagrids(angles * 180 / np.pi, labels)
    # 设置雷达图的0度起始位置
    ax.set_theta_zero_location('N')
    # 设置雷达图的坐标刻度范围
    ax.set_rlim(0, 100)
    # 设置雷达图的坐标值显示角度，相对于起始角度的偏移量
    ax.set_rlabel_position(270)
    ax.set_title("计算机专业大一（上）")
    plt.legend(["弓长张", "口天吴"], loc='best')
    # 汉字字体，优先使用楷体，找不到则使用黑体
    plt.rcParams['font.sans-serif'] = ['Kaitt', 'SimHei']
    # 正常显示负号
    plt.rcParams['axes.unicode_minus'] = False
    plt.savefig("1.png", format='png')