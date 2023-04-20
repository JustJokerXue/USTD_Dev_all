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
from .models import Score, Weight, Activity, Application, OverallScore, learning, Innovation, majorTechnology, manage, \
    ComprehensiveDevelopment
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
    act = Activity.objects.get(id=act_id)
    act_aname = act.aname
    print(act_id, act_aname, act, type(act_id))
    stu_id = request.session.get('ID')
    stu = Student.objects.get(id=stu_id)
    application = Application.objects.filter(aid=act_id, no=stu.id)
    if application.exists():
        # 需要弹出的消息框
        messages.success(request, '请勿重复报名')
        #  注意你需要在index.html添加我们上面的js代码
    else:
        application = Application(aid=act_id, aname=act_aname, no=stu.id, name=stu.name, banji=stu.banji)
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
    overallsorce = OverallScore.objects.filter(id=id)
    course = Course.objects.filter(stu_id=id)
    learn = learning.objects.filter(sno=id)
    warning = Early_Warning.objects.filter(id=id)
    if learn.exists():
        print("learn is exists")
    else:
        learn = learning(sno=student.id, name=student.name, banji=student.banji, major=student.major,
                         department=student.department)
        learn.save()
        print(learn)

    if score.exists():
        print("score is exists")
    else:
        score = Score(id=id)
        score.save()
        print(score)

    if course.exists():
        print("course is exists")
    else:
        course = Course(stu_id=id, name=name)
        course.save()
        print(course)

    if overallsorce.exists():
        print("overallsorce is exists")
    else:
        overallsorce = OverallScore(id=id, name=student.name, banji=student.banji, major=student.major,
                                    department=student.department)
        overallsorce.save()
        print(overallsorce)

    if warning.exists():
        print("warning is exists")
    else:
        warning = Early_Warning(id=id, )
        warning.save()
        print(warning)

    return 1


def Calculate_grades(id):  # 计算总评分调用,在登录功能中登录成功就调用
    # 获取权重系数
    weigth = Weight.objects.get(id=1)
    # 获取学生各方面评分
    m1 = learning.objects.get(sno=id)
    m2 = Innovation.objects.get(sno=id)
    m3 = majorTechnology.objects.get(sno=id)
    m4 = manage.objects.get(sno=id)
    m5 = ComprehensiveDevelopment.objects.get(sno=id)

    # 计算总成绩
    overallgrade = weigth.zyweight * m3.total_score + weigth.cxweight * m1.total_score \
                   + weigth.zsweight * m1.total_score + weigth.glweight * m4.total_score \
                   + weigth.zhweight * m5.total_score
    overallscore = OverallScore.objects.get(id=id)
    overallscore.total_score = overallgrade
    overallscore.save()
    print(overallgrade)
    return overallgrade


def Activity_new(request):  # 活动汇总调用
    stu_id = request.session.get('ID')
    student = Student.objects.get(id=stu_id)
    name = student.name
    act_list = list()
    act_list = Activity.objects.all()
    act_json = serializers.serialize("json", act_list)
    print(act_list)
    print(act_json)
    num_all = Score.objects.all().count()
    num_pass = Score.objects.filter(zy__gte=60, cx__gte=60, zs__gte=60, gl__gte=60, zh__gte=60).count()
    number = int((num_pass / num_all) * 100)
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
    overallgrade = Calculate_grades(std_id)
    ss1 = majorTechnology.objects.get(sno=std_id)
    ss2 = Innovation.objects.get(sno=std_id)
    ss3 = learning.objects.get(sno=std_id)
    ss4 = manage.objects.get(sno=std_id)
    ss5 = ComprehensiveDevelopment.objects.get(sno=std_id)
    s1 = ss1.total_score
    s2 = ss2.total_score
    s3 = ss3.total_score
    s4 = ss4.total_score
    s5 = ss5.total_score
    # zh = Score.objects.filter(zy__gte=60).count()
    # ch = Score.objects.filter(cx__gte=60).count()
    # know = Score.objects.filter(zs__gte=60).count()
    # gl = Score.objects.filter(gl__gte=60).count()
    # select(id)
    if std.minimum > 24 and std.compulsory > 20 and std.elective > 4 and std.physical > 60 and std.cet4 > 425 and std.mandarin > 80:
        ans = '满足毕业最低要求'
    else:
        ans = '不满足毕业最低要求'
    return render(request, 'index.html', locals(), )
    # {'ID': e.id, 'name': e.name, 'ans': ans, 'm1': max_Score_list[0],
    #  'm2': max_Score_list[1], 'm3': max_Score_list[2]
    #     , 'm4': max_Score_list[3], 'm5': max_Score_list[4], 'num_all': num_all,
    #  'num_pass': num_pass, 'number': number,
    #  's1': s1.total_score, 's2': s2.total_score, 's3': s3.total_score, 's4': s4.total_score,
    #  's5': s5.total_score,  }


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
    major = std.major
    pwd = std.pwd
    banji = std.banji
    department = std.department
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
    shenhe_list_obj_D = models.shenhe.objects.filter(no=ID0, zhuangtai='D')
    shenhe_list_obj_F = models.shenhe.objects.filter(no=ID0, zhuangtai='F')
    shenhe_list_obj_T = models.shenhe.objects.filter(no=ID0, zhuangtai='T')
    request.session['ID0'] = ID0
    return render(request, 'tables-editable.html',
                  {'shenhe_list_D': shenhe_list_obj_D, 'shenhe_list_F': shenhe_list_obj_F,
                   'shenhe_list_T': shenhe_list_obj_T, 'ID0': ID0, 'name': name, 'num_pass': num_pass,
                   'num_all': num_all,
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
                Model_creat(id)
                select(id)
                overallgrade = Calculate_grades(id)
                # Activity_new()
                # queryCourse(id)
                num_all = Score.objects.all().count()
                num_pass = Score.objects.filter(zy__gte=60, cx__gte=60, zs__gte=60, gl__gte=60, zh__gte=60).count()
                number = int((num_pass / num_all) * 100)
                s1 = majorTechnology.objects.get(sno=id)
                s2 = Innovation.objects.get(sno=id)
                s3 = learning.objects.get(sno=id)
                s4 = manage.objects.get(sno=id)
                s5 = ComprehensiveDevelopment.objects.get(sno=id)
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
                               's1': s1.total_score, 's2': s2.total_score, 's3': s3.total_score, 's4': s4.total_score,
                               's5': s5.total_score,
                               'overallgrade': overallgrade, }, )  # 'zh': zh, 'ch': ch, 'know': know, 'gl': gl
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
    m1 = majorTechnology.objects.aggregate(max1=Max("total_score"))
    m2 = Innovation.objects.aggregate(max2=Max("total_score"))
    m3 = learning.objects.aggregate(max3=Max("total_score"))
    m4 = manage.objects.aggregate(max4=Max("total_score"))
    m5 = ComprehensiveDevelopment.objects.aggregate(max5=Max("total_score"))
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
    s1 = majorTechnology.objects.get(sno=i)
    s2 = Innovation.objects.get(sno=i)
    s3 = learning.objects.get(sno=i)
    s4 = manage.objects.get(sno=i)
    s5 = ComprehensiveDevelopment.objects.get(sno=i)
    avg_zy = cursor0.execute("SELECT AVG(total_score) FROM majorTechnology")
    avg_cx = cursor1.execute("SELECT AVG(total_score) FROM Innovation")
    avg_zs = cursor2.execute("SELECT AVG(total_score) FROM learning")
    avg_gl = cursor3.execute("SELECT AVG(total_score) FROM manage")
    avg_zh = cursor4.execute("SELECT AVG(total_score) FROM ComprehensiveDevelopment")
    avg_zy = avg_zy.fetchone()[0]
    avg_cx = avg_cx.fetchone()[0]
    avg_zs = avg_zs.fetchone()[0]
    avg_gl = avg_gl.fetchone()[0]
    avg_zh = avg_zh.fetchone()[0]
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    # import matplotlib
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    # results = [{"专业技术": s1.total_score, "创新创业": S.cx, "知识学习": S.zs, "管理实践": S.gl, "综合发展": S.zh},
    #            {"专业技术": avg_zy, "创新创业": avg_cx, "知识学习": avg_zs, "管理实践": avg_gl, "综合发展": avg_zh}]
    dataset = pd.DataFrame(data=[[s1.total_score, avg_zy],
                                 [s2.total_score, avg_cx],
                                 [s3.total_score, avg_zs],
                                 [s4.total_score, avg_gl],
                                 [s5.total_score, avg_zh]],
                           index=['专业技术', '创新创业', '知识学习 ', '管理实践', '综合发展'],
                           columns=['个人水平', '平均水平'])
    radar_labels = dataset.index
    nAttr = 5
    data = dataset.values  # 数据值
    data_labels = dataset.columns
    # 设置角度
    angles = np.linspace(0, 2 * np.pi, nAttr,
                         endpoint=False)
    data = np.concatenate((data, [data[0]]))
    angles = np.concatenate((angles, [angles[0]]))
    # 设置画布
    fig = plt.figure(facecolor="white", figsize=(10, 6))
    plt.subplot(111, polar=True)
    # 绘图
    plt.plot(angles, data, 'o-',
             linewidth=1.5, alpha=0.2)
    # 填充颜色
    plt.fill(angles, data, alpha=0.25)
    plt.thetagrids(angles[:-1] * 180 / np.pi,
                   radar_labels, 1.2)
    plt.figtext(0.52, 0.95, '综合素质分析',
                ha='center', size=20)
    # 设置图例
    legend = plt.legend(data_labels,
                        loc=(1.1, 0.05),
                        labelspacing=0.1)
    plt.setp(legend.get_texts(),
             fontsize='large')
    plt.grid(True)
    # plt.savefig('tongshi.png')
    # plt.show()
    # results = [{"专业技术": S.zy, "创新创业": S.cx, "知识学习": S.zs, "管理实践": S.gl, "综合发展": S.zh},
    #            {"专业技术": avg_zy, "创新创业": avg_cx, "知识学习": avg_zs, "管理实践": avg_gl, "综合发展": avg_zh}]
    # data_length = len(results[0])
    # angles = np.linspace(0, 2 * np.pi, data_length, endpoint=False)
    # labels = [key for key in results[0].keys()]
    # score = [[v for v in result.values()] for result in results]
    # score_a = np.concatenate((score[0], [score[0][0]]))
    # score_b = np.concatenate((score[1], [score[1][0]]))
    # angles = np.concatenate((angles, [angles[0]]))
    # labels = np.concatenate((labels, [labels[0]]))
    # fig = plt.figure(figsize=(15, 6), dpi=100)
    # fig.suptitle("XXXX专业")
    # ax1 = plt.subplot(121, polar=True)
    # ax2 = plt.subplot(122, polar=True)
    # ax, data, name = [ax1, ax2], [score_a, score_b], ["个人", "平均"]
    # for i in range(2):
    #     for j in np.arange(0, 100 + 20, 20):
    #         ax[i].plot(angles, 6 * [j], '-.', lw=0.5, color='black')
    #     for j in range(5):
    #         ax[i].plot([angles[j], angles[j]], [0, 100], '-.', lw=0.5, color='black')
    #     ax[i].plot(angles, data[i], color='b')
    #     # 隐藏最外圈的圆
    #     ax[i].spines['polar'].set_visible(False)
    #     # 隐藏圆形网格线
    #     ax[i].grid(False)
    #     for a, b in zip(angles, data[i]):
    #         ax[i].text(a, b + 5, '%.00f' % b, ha='center', va='center', fontsize=12, color='b')
    #     ax[i].set_thetagrids(angles * 180 / np.pi, labels)
    #     ax[i].set_theta_zero_location('N')
    #     ax[i].set_rlim(0, 100)
    #     ax[i].set_rlabel_position(0)
    #     ax[i].set_title(name[i])
    # # 汉字字体，优先使用楷体，找不到则使用黑体
    # plt.rcParams['font.sans-serif'] = ['Kaitt', 'SimHei']
    # # 正常显示负号
    # plt.rcParams['axes.unicode_minus'] = False
    # # plt.show()
    plt.savefig("static\\image\\1.png", format='png')


def suggestion(request, p1):  # 该函数实现发展建议页面功能
    print(p1)
    ID = request.session.get('ID')
    name = request.session.get('name')
    s1 = majorTechnology.objects.get(sno=ID)
    s2 = Innovation.objects.get(sno=ID)
    s3 = learning.objects.get(sno=ID)
    s4 = manage.objects.get(sno=ID)
    s5 = ComprehensiveDevelopment.objects.get(sno=ID)
    print(ID)
    if p1 == 1:
        print(s1.total_score)
        g = grade(s1.total_score)
        print(g)
    elif p1 == 2:
        g = grade(s2.total_score)
        print(s2.total_score)
        print(g)
    elif p1 == 3:
        g = grade(s3.total_score)
        print(s3.total_score)
        print(g)
    elif p1 == 4:
        g = grade(s4.total_score)
        print(s4.total_score)
        print(g)
    else:
        g = grade(s5.total_score)
        print(s5.total_score)
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
