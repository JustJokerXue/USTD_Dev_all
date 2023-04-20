import sqlite3

import matplotlib.pyplot as plt
import numpy as np
from cachecontrol.serialize import Serializer
from django.contrib import messages
from django.core import serializers
from django.db.models import Max
from django.http import JsonResponse, request
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from requests import session
from sqlalchemy import Integer

from . import models
from .models import Score, Weight, Activity,Application
from .models import Student, Early_Warning, Course
# from django.utils.html import strip_tags
# from notifications.signals import notify
from notifications.models import Notification


def my_notifications(request):
    context = {}
    return render(request, 'my_notifications.html', context)


def my_notification(request, my_notification_pk):
    my_notification = get_object_or_404(Notification, pk=my_notification_pk)
    my_notification.unread = False
    my_notification.save()
    return redirect('http://127.0.0.1:8000/login/index.html')


# def notification(request):
#     send_notifications(request.user, "转正申请", request.user,
#                        description="sp", level="danger")
#     return render(request, 'my_notifications.html')


def Application_message(request):  # 学生个人活动报名信息
    stu_id = request.session.get('ID')
    stu_application = Application.objects.filter(no=stu_id)
    stu_application_json = serializers.serialize("json", stu_application)
    return stu_application_json


def Application_new(request):  # 活动报名
    act_id = request.GET.get('id')
    act = Activity.objects.get(id = act_id)
    act_aname = act.aname
    print(act_id,act_aname,act,type(act_id))
    stu_id = request.session.get('ID')
    stu = Student.objects.get(id=stu_id)
    application = Application.objects.filter(aid=act_id,no = stu.id)
    if application.exists():
        # 需要弹出的消息框
        messages.success(request, '请勿重复报名')
        #  注意你需要在index.html添加我们上面的js代码
    else:
        application = Application(aid=act_id,aname = act_aname,no=stu.id, name=stu.name, banji=stu.banji)
        application.save()
        messages.success(request, '报名成功')
    return redirect("http://127.0.0.1:8000/login/activity.html")


def queryCourse(request):  # 获取学生成绩信息
    stu_id = request.session.get('ID')
    student = Student.objects.get(id=stu_id)
    course_list_obj = models.Course.objects.filter(stu_id=stu_id)
    stu_cour = Course.objects.filter(stu_id=stu_id)
    name = student.name
    stu_cour_json = serializers.serialize("json", stu_cour)
    print(stu_cour_json)
    return render(request, 'student_score.html', {'course_list': course_list_obj, 'name': name, })


# Create your views here.
# 进入主页前进行判断，若学生在评分表，课程表等无数据，则创建数据对象
def Model_creat(id):
    student = Student.objects.get(id=id)
    name = student.name
    score = Score.objects.filter(id=id)
    course = Course.objects.filter(stu_id=id)
    if score.exists() and course.exists():
        print("score and course is exists")
        print("course and course is exists")
    else:
        score = Score(id=id)
        score.save()
        course = Course(stu_id=id, name=name)
        course.save()
        print(score)
        print(course)
    return score


def Calculate_grades(id):  # 计算总评分调用,在登录功能中登录成功就调用
    # 获取权重系数
    weigth = Weight.objects.get(id=1)
    # 获取学生各方面评分
    score = Score.objects.get(id=id)
    # 计算总成绩
    overallgrade = weigth.zyweight * score.zy + weigth.cxweight * score.cx + weigth.zsweight * score.zs + weigth.glweight * score.gl + weigth.zhweight * score.zh
    score.overallgrade = overallgrade
    score.save()
    print(weigth.zyweight, score.zy)
    print(overallgrade)


def Activity_new(request):  # 活动汇总调用
    stu_id = request.session.get('ID')
    student = Student.objects.get(id=stu_id)
    name = student.name
    act_list = list()
    act_list = Activity.objects.all()
    act_json = serializers.serialize("json", act_list)
    print(act_list)
    print(act_json)
    return render(request, 'activity.html', locals())


def login_view(request):  # 登录页面调用
    return render(request, 'login.html')


def index(request):  # 主页面功能实现及调用
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


def infor(request):  # 用户信息页面功能实现及调用
    num_all = Score.objects.all().count()
    num_pass = Score.objects.filter(zy__gte=60, cx__gte=60, zs__gte=60, gl__gte=60, zh__gte=60).count()
    number = int((num_pass / num_all) * 100)
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


def password_change_form(request):  # 用户信息页面功能实现及调用
    name = request.session.get('name')
    e = Student.objects.get(name=name)
    num_all = Score.objects.all().count()
    num_pass = Score.objects.filter(zy__gte=60, cx__gte=60, zs__gte=60, gl__gte=60, zh__gte=60).count()
    number = int((num_pass / num_all) * 100)
    if request.method == 'POST':
        opwd = request.POST.get('old_password')
        npwd1 = request.POST.get('new_password1')
        npwd2 = request.POST.get('new_password2')
        if opwd != "":
            opwd = int(opwd)
        if npwd1 != "":
            npwd1 = int(npwd1)
        if npwd2 != "":
            npwd2 = int(npwd2)
        print(opwd, npwd1, npwd2)
        print(type(opwd))
        std_id = e.id
        std = Student.objects.get(id=std_id)
        id = std.id
        pwd = std.pwd
        print(id, pwd)
        print(type(pwd))
        if opwd == pwd:
            if npwd1 == '' or npwd2 == '':
                pwd_error3 = "您的新密码与确认密码存在空值，请仔细检查重新输入"
                return render(request, "password_change_form.html", locals())
            else:
                if npwd1 == npwd2:
                    if opwd == npwd1:
                        pwd_error4 = "您的新密码与旧密码一致，请仔细检查重新输入"
                        return render(request, "password_change_form.html", locals())
                    else:
                        std.pwd = npwd1
                        std.save()
                        res = "密码修改成功，请您重新登录！"
                        return render(request, "password_change_form.html", locals())
                else:
                    pwd_error2 = "您的新密码与确认密码不一致，请仔细检查重新输入"
                    return render(request, "password_change_form.html", locals())
        else:
            pwd_error1 = "您的旧密码输入错误，请仔细检查重新输入"
            return render(request, "password_change_form.html", locals())
    return render(request, "password_change_form.html", locals())


def shenhe_upload(request):  # 上传审核材料页面功能实现及调用
    ID0 = request.session.get('ID')
    name = request.session.get('name')
    num_all = Score.objects.all().count()
    num_pass = Score.objects.filter(zy__gte=60, cx__gte=60, zs__gte=60, gl__gte=60, zh__gte=60).count()
    number = int((num_pass / num_all) * 100)
    print(ID0)
    if request.method == "POST":
        file = request.FILES['image']
        file_name = str(file)
        print(file_name)
        if file and (
                file_name.lower().endswith(
                    ('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff'))):
            models.shenhe.objects.create(no=ID0, miaoshu=request.POST['miaoshu'], leibie=request.POST['leibie'],
                                         extra_points=request.POST['extra_points'],
                                         image=file)
            print(request.POST['leibie'], request.POST['extra_points'])

        else:
            return render(request, 'error2.html')
    shenhe_list_obj = models.shenhe.objects.filter(no=ID0)
    request.session['ID0'] = ID0
    return render(request, 'tables-editable.html',
                  {'shenhe_list': shenhe_list_obj, 'ID0': ID0, 'name': name, 'num_pass': num_pass, 'num_all': num_all,
                   'number': number})


def shenhe_delete(request):  # 删除审核材料功能实现
    id = request.GET.get('id')
    models.shenhe.objects.filter(id=id).delete()
    # return render(request, 'tables-editable.html')
    return redirect("http://127.0.0.1:8000/login/tables-editable.html")


@csrf_protect
# 登录界面
def login(request):  # 登录页面功能实现
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
                select(id)
                Model_creat(id)
                Calculate_grades(id)
                # Activity_new()
                # queryCourse(id)
                num_all = Score.objects.all().count()
                num_pass = Score.objects.filter(zy__gte=60, cx__gte=60, zs__gte=60, gl__gte=60, zh__gte=60).count()
                number = int((num_pass / num_all) * 100)
                score = Score.objects.get(id=id);
                # zh = Score.objects.filter(zy__gte=60).count()
                # ch = Score.objects.filter(cx__gte=60).count()
                # know = Score.objects.filter(zs__gte=60).count()
                # gl = Score.objects.filter(gl__gte=60).count()
                # select(id)
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
                                  , 'm4': max_Score_list[3], 'm5': max_Score_list[4], 'num_all': num_all,
                               'num_pass': num_pass, 'number': number,
                               'score': score}, )  # 'zh': zh, 'ch': ch, 'know': know, 'gl': gl
            else:
                return render(request, 'error.html')
        else:
            return render(request, 'error.html')
    else:
        return render(request, 'error.html')


def academic_Early_Warning(request):  # 学业预警页面功能实现及调用
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
    return render(request, 'Academic_Early_Warning.html', locals())


def max_Score():  # 主页面最高成绩展示功能实现
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


def form_editor(request):  # 评分准则页面调用
    name = request.session.get('name')
    print(name)
    return render(request, "form-editors.html", locals())


def select(i):  # 主页面雷达图成绩展示功能实现
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


def suggestion(request, p1):  # 该函数实现发展建议页面功能
    print(p1)
    ID = request.session.get('ID')
    name = request.session.get('name')
    e = Score.objects.get(id=ID)
    print(ID)
    if p1 == 1:
        print(e.zy)
        g = grade(e.zy)
        print(g)
    elif p1 == 2:
        g = grade(e.cx)
        print(e.cx)
        print(g)
    elif p1 == 3:
        g = grade(e.zs)
        print(e.zs)
        print(g)
    elif p1 == 4:
        g = grade(e.gl)
        print(e.gl)
        print(g)
    else:
        g = grade(e.zh)
        print(e.zh)
        print(g)

    return render(request, 'suggestion.html', {'grade': g, 'name': name})


def grade(i):  # 该函数实现发展建议功能中的分级排名功能
    if i >= 80:
        grade = 'A'
    elif 60 <= i < 80:
        grade = 'B'
    elif i < 60:
        grade = 'C'

    return grade
