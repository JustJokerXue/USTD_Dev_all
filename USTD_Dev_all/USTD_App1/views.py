from django.shortcuts import HttpResponseRedirect, Http404, HttpResponse, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

from . import models
from .models import Student
from .models import Score
from .models import shenhe
import numpy as np
import matplotlib.pyplot as plt
import sqlite3


# Create your views here.

def Hello(request):
    return HttpResponse('Hello World')


def login(request):
    return render()


def index(request):
    return render(request, 'index.html')


def shenhe(request):
    if request.method == "POST":
        file = request.FILES['image']
        if file:
            models.shenhe.objects.create(id=request.POST['id'], miaoshu=request.POST['miaoshu'],
                                         leibie=request.POST['leibie'], image=file)
    shenhe_list_obj = models.shenhe.objects.all()
    return render(request, 'tables-editable.html', {'shenhe_list': shenhe_list_obj})


# def shenhe(request):
#     # 创建连接
#     conn = sqlite3.connect('db.sqlite3')
#     # 创建游标
#     cursor = conn.cursor()
#
#     # 执行SQL，并返回收影响行数
#
#     shenhe_list =cursor.execute("select id,miaoshu,leibie,image from shenhe").fetchall()
#     print(shenhe_list)
#
#     # 关闭游标
#     cursor.close()
#     # 关闭连接
#     conn.close()
#     # 将查询得到的数据放在shenhe_list列表
#     #eturn render(request, 'test.html',{'shenhe_list':shenhe_list})
#     return render(request, 'tables-editable.html',{'shenhe_list': shenhe_list})


@csrf_protect
# 登录界面
def login(request):
    if request.method == "POST":
        id = request.POST.get('id')
        pwd = request.POST.get('pwd')
        # request.session['ID'] = id
        if not all([id, pwd]):

            return render(request, 'error.html')
        else:
            student = Student.objects.filter(id=id, pwd=pwd)
            if len(student):
                select(id)
                return render(request, 'index.html')  # {"ID":ID}

            else:

                return render(request, 'error.html')
    else:
        return render(request, 'login.html')

def Academic_Early_Warning(request):
    return render(request, 'Academic_Early_Warning.html')

def select(i):
    conn = sqlite3.connect('db.sqlite3')
    cursor0 = conn.cursor()
    cursor1 = conn.cursor()
    cursor2 = conn.cursor()
    cursor3 = conn.cursor()
    cursor4 = conn.cursor()
    S = Score.objects.get(id=i)
    avg_zy = cursor0.execute("SELECT AVG(zy) FROM Score")
    avg_cx = cursor1.execute("SELECT AVG(cx) FROM Score")
    avg_zs = cursor2.execute("SELECT AVG(zs) FROM Score")
    avg_gl = cursor3.execute("SELECT AVG(gl) FROM Score")
    avg_zh = cursor4.execute("SELECT AVG(zh) FROM Score")
    avg_zy = avg_zy.fetchone()[0]
    avg_cx = avg_cx.fetchone()[0]
    avg_zs = avg_zs.fetchone()[0]
    avg_gl = avg_gl.fetchone()[0]
    avg_zh = avg_zh.fetchone()[0]
    # print("\n")
    # print("\n")
    # print(avg_zy,avg_cx,avg_zs,avg_gl,avg_zh)
    # #print(avg_zy,avg_cx)
    # print("\n")
    # print("\n")
    results = [{"专业技术": S.zy, "创新创业": S.cx, "知识学习": S.zs, "管理实践": S.gl, "综合发展": S.zh},
               {"专业技术": avg_zy, "创新创业": avg_cx, "知识学习": avg_zs, "管理实践": avg_gl, "综合发展": avg_zh}]
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
