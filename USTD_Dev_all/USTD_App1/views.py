import sqlite3

import matplotlib.pyplot as plt
import numpy as np
from django.db.models import Max
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from . import models
from .models import Score
from .models import Student, Early_Warning


# Create your views here.

def Hello(request):
    return HttpResponse('Hello World')


def login_view(request):
    return render(request, 'login.html')


def index(request):
    name = request.session.get('name')
    print(name)
    num_all = Score.objects.all().count()
    num_pass = Score.objects.filter(zy__gte=60, cx__gte=60, zs__gte=60, gl__gte=60, zh__gte=60).count()
    number = int((num_pass / num_all) * 100)
    zh = Score.objects.filter(zy__gte=60).count()
    ch = Score.objects.filter(cx__gte=60).count()
    know = Score.objects.filter(zs__gte=60).count()
    gl = Score.objects.filter(gl__gte=60).count()
    e = Student.objects.get(name=name)
    std_id = e.id
    print(std_id)
    select(std_id)
    max_Score_list = max_Score()
    m1 = max_Score_list[0]
    m2 = max_Score_list[1]
    m3 = max_Score_list[2]
    m4 = max_Score_list[3]
    m5 = max_Score_list[4]
    std = Early_Warning.objects.get(id=std_id)
    if std.minimum > 24 and std.compulsory > 20 and std.elective > 4 and std.physical > 60 and std.cet4 > 425 and std.mandarin > 80:
        ans = '满足毕业最低要求'
    else:
        ans = '不满足毕业最低要求'
    return render(request, 'index.html', locals())


def infor(request):
    name = request.session.get('name')
    print(name)
    e = Student.objects.get(name=name)
    std_id = e.id
    print(std_id)
    std = Student.objects.get(id=std_id)
    id = std.id
    age = std.age
    sp = std.sp
    pwd = std.pwd
    return render(request, "infor.html", locals())


# def shenhe(request):
#     ID0 = request.session.get('ID')
#     print(ID0)
#     print("ww")
#     shenhe1 = shenhe.objects.get(id=ID0)
#
#     return render(request, 'tables-editable.html')

def shenhe_upload(request):
    ID0 = request.session.get('ID')
    name = request.session.get('name')
    num_all = Score.objects.all().count()
    num_pass = Score.objects.filter(zy__gte=60, cx__gte=60, zs__gte=60, gl__gte=60, zh__gte=60).count()
    number = int((num_pass / num_all) * 100)
    print(ID0)
    if request.method == "POST":
        file = request.FILES['image']
        name = str(file)
        print(name)
        if file and (
                name.lower().endswith(
                    ('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff'))):
            models.shenhe.objects.create(no=ID0, miaoshu=request.POST['miaoshu'], leibie=request.POST['leibie'],
                                         image=file)
        else:
            return render(request, 'error2.html')
    shenhe_list_obj = models.shenhe.objects.filter(no=ID0)
    request.session['ID0'] = ID0
    return render(request, 'tables-editable.html', {'shenhe_list': shenhe_list_obj, 'ID0': ID0, 'name': name,'num_pass':num_pass,'num_all':num_all,'number':number})


def shenhe_delete(request):
    id = request.GET.get('id')
    models.shenhe.objects.filter(id=id).delete()
    # return render(request, 'tables-editable.html')
    return redirect("http://127.0.0.1:8000/login/tables-editable.html")


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
#     #eturn render(request, 'error2.html',{'shenhe_list':shenhe_list})
#     return render(request, 'tables-editable.html',{'shenhe_list': shenhe_list})


@csrf_protect
# 登录界面
def login(request):
    if request.method == 'POST':
        print("进入页面")
        id = str(request.POST.get('id'))
        pwd = str(request.POST.get('pwd'))
        # id = str(id)
        # pwd = str(pwd)
        if id.isdigit():
            try:
                student = Student.objects.get(id=id)
            except Exception as err:
                return render(request, 'error.html')
            sid = str(student.id)
            spwd = str(student.pwd)
            print(id, pwd)
            print(sid, spwd)
            if id == sid and pwd == spwd:
                print('登录成功')
                num_all = Score.objects.all().count()
                num_pass = Score.objects.filter(zy__gte=60, cx__gte=60, zs__gte=60, gl__gte=60, zh__gte=60).count()
                number = int((num_pass / num_all) * 100)
                zh = Score.objects.filter(zy__gte=60).count()
                ch = Score.objects.filter(cx__gte=60).count()
                know = Score.objects.filter(zs__gte=60).count()
                gl = Score.objects.filter(gl__gte=60).count()
                select(id)
                max_Score_list = max_Score()
                request.session['ID'] = student.id
                request.session['name'] = student.name
                std_id = student.id
                print(std_id)
                std = Early_Warning.objects.get(id=std_id)
                if std.minimum > 24 and std.compulsory > 20 and std.elective > 4 and std.physical > 60 and std.cet4 > 425 and std.mandarin > 80:
                    ans = '满足毕业最低要求'
                else:
                    ans = '不满足毕业最低要求'
                return render(request, 'index.html',
                              {'ID': student.id, 'name': student.name, 'ans': ans, 'm1': max_Score_list[0],
                               'm2': max_Score_list[1], 'm3': max_Score_list[2]
                                  , 'm4': max_Score_list[3], 'm5': max_Score_list[4],'num_all':num_all,'num_pass':num_pass,'number':number,'zh':zh,'ch':ch,'know':know,'gl':gl},)
            else:
                return render(request, 'error.html')
        else:
            return render(request, 'error.html')
    else:
        return render(request, 'error.html')
    # if request.method == "POST":
    #     id = request.POST.get('id')
    #     pwd = request.POST.get('pwd')
    #     print(id)
    #     # request.session['ID'] = id
    #     if not all([id, pwd]):
    #
    #         return render(request, 'error.html')
    #     else:
    #         student = Student.objects.filter(id=id, pwd=pwd)
    #         if student:
    #             select(id)
    #             return render(request, 'index.html',{"ID":id})
    #
    #         else:
    #             return render(request, 'error.html')
    # else:
    #     return render(request, 'error2.html')


def academic_Early_Warning(request):
    # num_all=
    # num_pass=
    name = request.session.get('name')
    print(name)
    num_all = Early_Warning.objects.all().count()
    num_pass = Early_Warning.objects.filter(minimum__gte=24, compulsory__gte=20, elective__gte=4, physical__gte=60,
                                            cet4__gte=425, mandarin__gte=80).count()
    number = int((num_pass / num_all) * 100)
    e = Student.objects.get(name=name)
    std_id = e.id
    print(std_id)
    std = Early_Warning.objects.get(id=std_id)
    minimum = std.minimum
    compulsory = std.compulsory
    elective = std.elective
    physical = std.physical
    cet4 = std.cet4
    mandarin = std.mandarin
    # ame = std.name
    # if std.minimum > 24 and std.compulsory > 20 and std.elective > 4 and std.physical > 60 and std.cet4 > 425 and std.mandarin > 80:
    #     ans = '满足毕业最低要求'
    # else:
    #     ans = '不满足毕业最低要求'
    # request.session['stdID0'] = ID0
    return render(request, 'Academic_Early_Warning.html', locals())


def max_Score():
    max_Score_list = list()
    m1 = Score.objects.aggregate(max1=Max("zy"))
    m2 = Score.objects.aggregate(max2=Max("cx"))
    m3 = Score.objects.aggregate(max3=Max("zs"))
    m4 = Score.objects.aggregate(max4=Max("gl"))
    m5 = Score.objects.aggregate(max5=Max("zh"))
    value1 = list(m1.values())[0]
    value2 = list(m2.values())[0]
    value3 = list(m3.values())[0]
    value4 = list(m4.values())[0]
    value5 = list(m5.values())[0]
    max_Score_list.append(value1)
    max_Score_list.append(value2)
    max_Score_list.append(value3)
    max_Score_list.append(value4)
    max_Score_list.append(value5)
    print(max_Score_list)
    return max_Score_list


def test_view(request):
    python_data = "python里的数据"
    return render(request, "test_view.html", {"html_data_name": python_data})


def form_editor(request):
    name = request.session.get('name')
    print(name)
    return render(request, "form-editors.html", locals())


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
