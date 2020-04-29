from .setting import *
import datetime as dt
from django.db.models import Q
from django.template import loader
from ouyeel.models import Ouyeel
from mt.models import Mt



def generate_detail(res, temp, path):
    try:
        html = loader.get_template(temp)
        html = html.render({"goodsInfo": res})
        with open(path, 'wt', encoding="utf8") as f:
            f.write(html)
    except Exception as e:
        print("write Html Error:", e)





def getCode(param):
    if "sourceCode" in param:
        if isinstance(param["sourceCode"], int):
            param["sourceCode"] = str(param["sourceCode"])
        if param["sourceCode"] == '2':
            modelName = oy
        elif param["sourceCode"] == '1':
            modelName = mt
        elif param["sourceCode"] == '3':
            modelName = ot
        else:
            modelName = None
    else:
        modelName = None
    if "productCode" in param:
        if isinstance(param["productCode"], int):
            param["productCode"] = str(param["productCode"])
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
    else:
        productCode = None
    if "page" in param:
        page = int(param["page"])
    else:
        page = 1
    return modelName, productCode, page


def query_single_record(param):
    modelName, productCode, page = getCode(param)
    if modelName != None and "packCode" in param:
        try:
            res = eval(modelName).objects.get(packCode=param["packCode"])
            res = res.to_small_dic()
            return res
        except Exception as e:
            print("no packCode : ",param["packCode"])


def queryResult(param):
    modelName, productCode, page = getCode(param)
    timeStamp = dt.datetime.now().strftime("%y-%m-%d")
    res = eval(modelName).objects
    if modelName == oy and productCode != None:
        if productCode != "ALL":
            res = eval(modelName).objects.filter(~Q(qualityGrade__startswith="B"), businessTimes=timeStamp, productCode=productCode, onBusiness="1", )
            if not res:
                timeStamp = (dt.datetime.now() - dt.timedelta(days=1)).strftime("%y-%m-%d")
                res = eval(modelName).objects.filter(~Q(qualityGrade__startswith="B"), businessTimes=timeStamp, productCode=productCode, onBusiness="1", )
        else:
            res = eval(modelName).objects.filter(~Q(qualityGrade__startswith="B"), businessTimes=timeStamp, onBusiness="1", )
            if not res:
                timeStamp = (dt.datetime.now() - dt.timedelta(days=1)).strftime("%y-%m-%d")
                res = eval(modelName).objects.filter(~Q(qualityGrade__startswith="B"), businessTimes=timeStamp, onBusiness="1", )
    elif modelName == mt:
        res = eval(modelName).objects.filter()

    if not res:
        return "", 0
    begin = 0 + (page - 1) * MOUNTS
    end = page * MOUNTS
    if len(res) <= begin:
        if len(res) >= 20:
            end = len(res)
            begin = end - 20
        else:
            end = len(res)
            begin = 0
    elif begin < len(res) <= end:
        end = len(res)
    return res.order_by("publishPrice")[begin:end], len(res)


def updateProduct(obj, i, updateNum):
    num , time_update= 0, 0
    if obj.publishDate != i["publishDate"]:
        obj.publishDate = i["publishDate"]
        time_update += 1
    if int(obj.publishPrice) != i["publishPrice"]:
        obj.publishPrice = i["publishPrice"]
        num += 1
    if int(obj.basicPrice) != i["basicPrice"]:
        obj.basicPrice = i["basicPrice"]
        num += 1
    if int(obj.publishPrice) != i["publishPrice"]:
        obj.publishPrice = i["publishPrice"]
        num += 1
    if obj.hasShop != i["hasShop"]:  # 是否竞拍
        obj.hasShop = i["hasShop"]
        time_update += 1
    if int(obj.onBusiness) != i["onBusiness"]:  # 是否正在营业
        obj.onBusiness = i["onBusiness"]
        num += 1
    if obj.bidBeginDate != i["bidBeginDate"]:
        obj.bidBeginDate = i["bidBeginDate"]
        time_update += 1
    if obj.bidEndDate != i["bidEndDate"]:
        obj.bidEndDate = i["bidEndDate"]
        time_update += 1
    if obj.warehouseName != i["warehouseName"]:
        obj.warehouseName = i["warehouseName"]
        num += 1
    if obj.storeCityName != i["storeCityName"]:
        obj.storeCityName = i["storeCityName"]
        num += 1
    timeStamp = dt.datetime.now().strftime("%y-%m-%d")
    if obj.businessTimes != timeStamp:
        obj.businessTimes = timeStamp
        time_update = 1
    modiTime = dt.datetime.now().hour
    if time_update >= 1:
        obj.save()  # 刷新 bussiness time，bidTime,hasshop——拍卖
    if num > 0:
        obj.modiDate = modiTime  # 刷新 modiTime 展示当前小时数的记录
        obj.save()
        updateNum += 1
    return updateNum


def has_dic_attr(o, key):
    return key in o


def generate_home():
    paramList = [
        {"sourceCode": "2", "productCode": "0"},
        {"sourceCode": "1", "productCode": "0"},
    ]
    try:
        static_res = {
            # "sourceCode1": [],
            # "sourceCode2": [],
        }
        for param in paramList:
            try:
                res, amount = queryResult(param)
                resLst = []
                for i in res:
                    dic = i.to_small_dic()
                    # dic = json.dumps(dic)
                    resLst.append(dic)
                if not res:
                    static_res["sourceCode"+param["sourceCode"]] = nullCode
                else:
                    newSuccessCode = successCode.copy()
                    newSuccessCode["resultList"] = resLst
                    newSuccessCode["amount"] = amount
                    static_res["sourceCode"+param["sourceCode"]] = newSuccessCode
            except Exception as e:
                print("queryResult Error:", e)

        from django.conf import settings
        path = settings.NGX_DIR + "index.html"
        try:
            html = loader.get_template("index.html")
            html = html.render(static_res)
            with open(path, 'wt', encoding="utf8") as f:
                f.write(html)
            return successCode
        except Exception as e:
            print("write Html Error:", e)
            return errCode
    except Exception as e:
        print("static Html Error:", e)
        return errCode
