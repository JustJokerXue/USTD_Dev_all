
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
    results = [{"专业技术": S.zy, "创新创业": S.cx, "知识学习": S.zs, "管理实践": S.gl, "综合发展": S.zh},
               {"专业技术": 50, "创新创业": 70, "知识学习": 53, "管理实践": 75, "综合发展": 85}]
    data_length = len(results[0])
    angles = np.linspace(0, 2 * np.pi, data_length, endpoint=False)
    labels = [key for key in results[0].keys()]
    score = [[v for v in result.values()] for result in results]
    score_a = np.concatenate((score[0], [score[0][0]]))
    score_b = np.concatenate((score[1], [score[1][0]]))
    angles = np.concatenate((angles, [angles[0]]))
    labels = np.concatenate((labels, [labels[0]]))
    fig = plt.figure(figsize=(15, 6), dpi=100)
    fig.suptitle("XXXX专业")
    ax1 = plt.subplot(121, polar=True)
    ax2 = plt.subplot(122, polar=True)
    ax, data, name = [ax1, ax2], [score_a, score_b], ["个人", "平均"]
    for i in range(2):
        for j in np.arange(0, 100 + 20, 20):
            ax[i].plot(angles, 6 * [j], '-.', lw=0.5, color='black')
        for j in range(5):
            ax[i].plot([angles[j], angles[j]], [0, 100], '-.', lw=0.5, color='black')
        ax[i].plot(angles, data[i], color='b')
        # 隐藏最外圈的圆
        ax[i].spines['polar'].set_visible(False)
        # 隐藏圆形网格线
        ax[i].grid(False)
        for a, b in zip(angles, data[i]):
            ax[i].text(a, b + 5, '%.00f' % b, ha='center', va='center', fontsize=12, color='b')
        ax[i].set_thetagrids(angles * 180 / np.pi, labels)
        ax[i].set_theta_zero_location('N')
        ax[i].set_rlim(0, 100)
        ax[i].set_rlabel_position(0)
        ax[i].set_title(name[i])
    # 汉字字体，优先使用楷体，找不到则使用黑体
    plt.rcParams['font.sans-serif'] = ['Kaitt', 'SimHei']
    # 正常显示负号
    plt.rcParams['axes.unicode_minus'] = False
    # plt.show()
    plt.savefig("static\\image\\1.png", format='png')