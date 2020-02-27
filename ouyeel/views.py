import json
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

    return HttpResponse("welcome to mytinplate view!")


def queryResultList(request):
    print("正在查询...")
    if request.method == 'GET':
        try:
            param = request.GET.get("parameters")
            param = json.loads(json.dumps(eval(param)))
            if "sourceCode" not in param.keys() or "productCode" not in param.keys():
                return HttpResponse("paramError")
        except Exception as e:
            print("Get err :", e)
            return HttpResponse(json.dumps(errCode))

        try:
            res = queryResult(param)
            if not res:
                return HttpResponse(json.dumps(nullCode))
            resLst = []

            for i in res:
                dic = i.to_small_dic()
                # dic = json.dumps(dic)
                resLst.append(dic)
            # querydic = serializers.serialize('json', res)
            print("记录条数：", len(resLst))
            successCode["resultList"] = resLst
            return HttpResponse(json.dumps(successCode))
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps(errCode))


def getCode(param):
    if param["sourceCode"] == '2':
        modelName = oy
    elif param["sourceCode"] == '1':
            modelName = mt
    elif param["sourceCode"] == '3':
        modelName = ot
    else:
        modelName = None

    if param["productCode"] == '0':
        productCode = "ALL"
    elif param["productCode"] == '1':
        productCode = duxi
    elif param["productCode"] == '2':
        productCode = duge
    elif param["productCode"] == '3':
        productCode = dugefumo
    else:
        productCode = None
    return modelName, productCode


def queryResult(param):
    modelName, productCode = getCode(param)
    timeStamp = dt.datetime.now().strftime("%y-%m-%d")

    if modelName != None and productCode != None:
        if productCode != "ALL":
            res = eval(modelName).objects.filter(businessTimes=timeStamp, productCode=productCode, onBusiness="1", )
            if not res:
                timeStamp = (dt.datetime.now() - dt.timedelta(days=1)).strftime("%y-%m-%d")
                res = eval(modelName).objects.filter(businessTimes=timeStamp, productCode=productCode, onBusiness="1", )
        else:
            res = eval(modelName).objects.filter(businessTimes=timeStamp, onBusiness="1", )
            if not res:
                timeStamp = (dt.datetime.now() - dt.timedelta(days=1)).strftime("%y-%m-%d")
                res = eval(modelName).objects.filter(businessTimes=timeStamp, onBusiness="1", )

        return res


def reportB_grade(request):
    print("begin grab!!!")
    try:
        timeStamp = dt.datetime.now().strftime("%y-%m-%d")
        modiTime = dt.datetime.now().hour
        res = Ouyeel.objects.filter(businessTimes=timeStamp, qualityGrade__contains="B", onBusiness='1', modiDate=modiTime)
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
                    obj = Ouyeel(**i)
                    obj.save()
                    insertNum += 1

            except Exception as e:
                print("insertErr:", e, "\n", "packCode:", i["packCode"])

        timeStamp2 = dt.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        try:
            with open('./ouyeel/config/insertOuyeel.txt', 'at', encoding='utf8') as f:
                if insertNum != 0:
                    f.write("%s --insert records amounts %d \n"%(timeStamp2, insertNum))
            with open('./ouyeel/config/updateOuyeel.txt', 'at', encoding='utf8') as f:
                if updateNum != 0:
                    f.write("%s --update records amounts %d \n"%(timeStamp2, updateNum))
        except Exception as e:
            pass
        print("Data saved!")
        return HttpResponse("data has been saved!")
    except Exception as e:
        print("InsertError", e, )
    return HttpResponse("you got 404!")


def updateProduct(obj, i, updateNum):
    num = 0
    modiTime = dt.datetime.now().hour
    obj.modiDate = modiTime
    if obj.publishDate != i["publishDate"]:
        obj.publishDate = i["publishDate"]
        num += 1
    if int(obj.publishPrice) != i["publishPrice"]:
        obj.publishPrice = i["publishPrice"]
        num += 1
    if int(obj.basicPrice) != i["basicPrice"]:
        obj.basicPrice = i["basicPrice"]
        num += 1
    if int(obj.basicPrice) != i["basicPrice"]:
        obj.basicPrice = i["basicPrice"]
        num += 1
    if obj.hasShop != i["hasShop"]:  # 是否竞拍
        obj.hasShop = i["hasShop"]
        num += 1
    if int(obj.onBusiness) != i["onBusiness"]:  # 是否正在营业
        obj.onBusiness = i["onBusiness"]
        num += 1
    if obj.bidBeginDate != i["bidBeginDate"]:
        obj.bidBeginDate = i["bidBeginDate"]
        num += 1
    if obj.bidEndDate != i["bidEndDate"]:
        obj.bidEndDate = i["bidEndDate"]
        num += 1
    if obj.warehouseName != i["warehouseName"]:
        obj.warehouseName = i["warehouseName"]
        num += 1
    if obj.storeCityName != i["storeCityName"]:
        obj.storeCityName = i["storeCityName"]
        num += 1
    timeStamp = dt.datetime.now().strftime("%y-%m-%d")
    if obj.businessTimes != timeStamp:
        obj.businessTimes = timeStamp
        num += 1
    if num > 0:
        obj.save()
        updateNum += 1
    return updateNum


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
        obj = Ouyeel.objects.get(packCode="121")
        print(obj)
    except Ouyeel.DoesNotExist as e:
        print(e)
    return HttpResponse("ok!")
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
