import json
from .apiFuc import *
from django.db.models import Q
from .setting import *
# from django.core import serializers
# from django.shortcuts import render, redirect
from django.http import HttpResponse
from ouyeel.models import *
import datetime as dt


# 后端根目录视图函数
def index_views(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR']
        print("HTTP_X_FORWARDED_FOR:", ip)
    if "HTTP_VIA" in request.META:
        ip = request.META['HTTP_VIA']
        print("HTTP_VIA:", ip)
    if "REMOTE_ADDR" in request.META:
        ip = request.META['REMOTE_ADDR']
        print("REMOTE_ADDR:", ip)
    timeStamp = (dt.datetime.now() - dt.timedelta(days=1)).strftime("%y-%m-%d")
    res = Ouyeel.objects.filter(businessTimes=timeStamp, productCode=duxi, onBusiness="1", ).order_by('basicPrice')[0:25]
    resLst = []
    for i in res:
        dic = i.to_small_dic()
        # dic = json.dumps(dic)
        resLst.append(dic)

    print("长度==", len(resLst), "类型：", type(res))
    print(resLst)
    return HttpResponse("welcome to mytinplate view!")


def query_single_product(request):
    print("正在查询单一数据...")
    if request.method == 'GET':
        try:
            param = request.GET.get("parameters")
            param = json.loads(json.dumps(eval(param)))  # bad code
            if "packCode" not in param.keys():
                return HttpResponse(json.dumps(errCode))
        except Exception as e:
            print("Get err :", e)
            return HttpResponse(json.dumps(errCode))

        try:
            res = query_single_record(param)
            if not res:
                return HttpResponse(json.dumps(nullCode))
            res = res.to_small_dic()
            # 生成详情页的静态页面
            from django.conf import settings
            path = settings.NGX_DIR + "detail/{}.html".format(res["packCode"])
            print("生成静态页面", path)
            generate_detail(res, "detail.html", path)
            newSuccessCode = successCode.copy()
            newSuccessCode["result"] = res
            return HttpResponse(json.dumps(newSuccessCode))
        except Exception as e:
            print("static Html Error:", e)
            return HttpResponse(json.dumps(errCode))


def queryResultList(request):
    print("正在查询...")
    if request.method == 'GET':
        try:
            param = request.GET.get("parameters")
            param = json.loads(json.dumps(eval(param)))
            if "sourceCode" not in param.keys() or "productCode" not in param.keys():
                return HttpResponse(json.dumps(errCode))
        except Exception as e:
            print("Get err :", e)
            return HttpResponse(json.dumps(errCode))

        try:
            res, amount = queryResult(param)
            if not res:
                return HttpResponse(json.dumps(nullCode))
            resLst = []

            for i in res:
                dic = i.to_small_dic()
                # dic = json.dumps(dic)
                resLst.append(dic)
            # querydic = serializers.serialize('json', res)
            # print("记录条数：", len(resLst))
            newSuccessCode = successCode.copy()
            newSuccessCode["resultList"] = resLst
            newSuccessCode["amount"] = amount
            # print(newSuccessCode)
            return HttpResponse(json.dumps(newSuccessCode))
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps(errCode))


def reportB_grade(request):
    print("begin grab!!!")
    try:
        timeStamp = dt.datetime.now().strftime("%y-%m-%d")
        modiTime = dt.datetime.now().hour
        res = Ouyeel.objects.filter(Q(qualityGrade__startswith="B"), \
                                    businessTimes=timeStamp, onBusiness='1', modiDate=modiTime)
        if res:
            resLst = []
            for i in res:
                dic = i.to_little_dic()
                # dic = json.dumps(dic)
                resLst.append(dic)
            # querydic = serializers.serialize('json', res)
            print("记录条数：", len(resLst))
            successCode["resultList"] = resLst
            return HttpResponse(json.dumps(successCode))
    except Exception as e:
        print("filterData error!", e)
    print("空记录！")
    return HttpResponse(json.dumps(nullCode))


def getDataToOyDb(request):
    # TODO monitor requests
    print("receiving data!")
    try:
        data = request.body.decode('utf8')
        data = json.loads(data)
        updateNum = 0
        insertNum = 0
        for i in data:
            try:
                if "packCode" in i:
                    try:
                        # this record in db, then switch to next record
                        obj = Ouyeel.objects.get(packCode=i["packCode"])
                        if obj:
                            # print(" record exists！")
                            updateNum = updateProduct(obj, i, updateNum)

                            continue
                    except Ouyeel.DoesNotExist as e:
                        # print("%s does not exists!"%i['packCode'])
                        pass
                    except Exception as e:
                        print("updating data Error", e)
                        continue
                    timeStamp = dt.datetime.now().strftime("%y-%m-%d")
                    modiTime = dt.datetime.now().hour
                    i["businessTimes"] = timeStamp
                    i["modiDate"] = modiTime
                    if "B" in i["qualityGrade"]:
                        modiTime = dt.datetime.now().hour
                        i["modiDate"] = modiTime
                    obj = Ouyeel(**i)
                    obj.save()
                    insertNum += 1

            except Exception as e:
                print("insertErr:", e, "\n", "packCode:", i["packCode"])

        timeStamp2 = dt.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        try:
            with open('./ouyeel/config/insertOuyeel.txt', 'at', encoding='utf8') as f:
                if insertNum != 0:
                    f.write("%s --insert records amounts %d \n" % (timeStamp2, insertNum))
            with open('./ouyeel/config/updateOuyeel.txt', 'at', encoding='utf8') as f:
                if updateNum != 0:
                    f.write("%s --update records amounts %d \n" % (timeStamp2, updateNum))
        except Exception as e:
            pass
        print("Data saved!")
        return HttpResponse("data has been saved!")
    except Exception as e:
        print("InsertError", e, )
    return HttpResponse("you got 404!")





# 退出登录函数
def logout(request):

    if 'uname' in request.session:
        print(request.session['uname'])
        del request.session['uname']
        print('已经删除uname')
    if 'uid' in request.session:
        del request.session['uid']
        print('已经删除uid')
    return HttpResponse('deleted')


# 判断是否登录的函数
def islogged(request):
    print("进入islogged")
    # 若seesion中有信息 ，则 回主页
    if 'uname' in request.session and 'uid' in request.session:
        print(request.session)
        uname = request.session.get('uname')
        uid = request.session.get('uid')
        print(uname)
        print(uid)

        return HttpResponse(uname)
    # else:
    #     # 若cookie中有信息# 也回主页
    #     if 'uname' in request.COOKIES and 'uid' in request.COOKIES:
    #         name = json.loads(request.COOKIES['uname'])
    #         print('cookie:', request.COOKIES['uname'])
    #         return redirect('/index/')
    print('并没有session在')
    return HttpResponse(False)


def islogged_views(request):
    print("进入islogged——views")
    # 若seesion中有信息 ，则 回主页
    if 'uname' in request.session and 'uid' in request.session:
        print(request.session)
        uname = request.session.get('uname')
        uid = request.session.get('uid')
        print(uname)
        print(uid)

        return True
    print('并没有session在')
    return False


def test_views(request):
    try:

        # re_request_body = getattr(request, '_body', request.body)
        # print("len(re_request_body):", len(re_request_body))
        dic = {
            "request.method": request.method,
            "request.GET": request.GET,
            "request.POST": request.POST,
            # "request.body.length": len(re_request_body),
        }
        from django.conf import settings
        file = request.FILES.get("file")
        filename = dt.datetime.now().strftime("%Y%m%d%H%M%S") + file.name
        file_content = file.chunks()
        path = settings.BASE_DIR + "/ouyeel/config/{}".format(filename)
        with open(path, "wb") as f:
            for i in file_content:
                f.write(i)

        res = json.dumps(dic)
        return HttpResponse(res)
    # except Ouyeel.DoesNotExist as e:
    except Exception as e:

        print(e)
        return HttpResponse("it's wrong method!")
# 演示cookie操作
# def cookie1_views(request):
#     # resp = HttpResponse('添加cookie成功')
#     # resp.set_cookie('uid', '1002', 60*60*24*366)
#     resp = redirect('/login/')
#     resp.set_cookie('uname', 'ct', 60*60*24*366)
#
#     return resp
# uname = request.GET.get('uname')
# uname = request.session.get('uname')
# if 'uname' in request.session:
#     print('unm:', request.sesson['uname'])
#     del request.session['uname']
# if 'uid' in request.session:
#     del request.session['uid']


# def log_views(request):
#     print('进入log——views')
#     # cookie = request.COOKIES
#     # for index in cookie:
#     #     print(index, ':', cookie[index])
#     # print(cookie['uname'])
#     # name = cookie['uname'].encode('latin-1').decode()
#     # name = json.loads(cookie['uname'])
#     # print(name)
#     if request.method == 'GET':
#         # 判断session中有没有登录信息
#         res = islogged_views(request)
#
#         if res:
#             return redirect('/video/index/')
#         else:
#             return render(request, 'login.html')
#
#     else:
#         return login_form(request)

# 判断提交的表单是否符合要求
# def login_form(request):
#     # 1、手动接受提交的数据
#     uname = request.POST['uname']
#     upwd = request.POST['upwd']
#     # print(uname)
#
#     # 2、自动接受提交的数据
#     form1 = Login(request.POST)
#     # print(form1)
#     # 2.1通过forms.Form的构造，接受request.POST
#     # 2.2is_valid()
#     if not form1.is_valid():
#         errmsg = '输入有误！'
#         # return errmsg
#         return render(request, 'login.html', locals())
#         # 2.3 form.cleaned_data
#     else:
#         cd = form1.cleaned_data
#         cur_name = User.objects.filter(uname=cd['uname'], upwd=cd['upwd'])
#         # print(cd)
#         if cur_name:
#             # 将登陆信息存入服务器的session中去
#             request.session['uid'] = cur_name[0].id
#             request.session['uname'] = uname
#             # 将要返回的内容放入一个变量中，并用该变量设置cookie
#             # resp = render(request, 'index.html', locals())
#             # uname = uname.encode('utf-8').decode('latin-1')
#             resp = redirect('/video/index/', locals())
#             # 用json存取值 先import json
#             uname = json.dumps(uname)
#             # 若要取值，则用json.loads(uname)
#             # uname = request.COOKIES['uname']
#             # uname = json.loads(uname)
#             if 'isSaved' in request.POST:
#                 uid = cur_name[0].id
#                 resp.set_cookie('uname', uname, 60 * 60 * 24 * 366)
#                 resp.set_cookie('uid', uid, 3600 * 24 * 366)
#             session = request.session
#             print(session)
#             return resp
#         else:
#             errmsg = '用户名或者密码错误，请重新输入!'
#             return render(request, 'login.html', locals())

# def get_views(request):
#     print(request.GET)
#     get = request.GET
#     # request.GET是个字典
#     # uname = request.GET['uname']
#     # upwd = request.GET['upwd']
#     # uhobby = request.GET['uhobby']
#     # print(request.GET.uhobby[0])
#     # print(uname, upwd, uhobby)
#     # return HttpResponse('用户名:'+uname+', 密码：'+upwd+', 爱好：'+uhobby)
#     return render(request, '02_form.html', locals())



