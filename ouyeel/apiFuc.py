from .setting import *
import datetime as dt
from django.db.models import Q
from ouyeel.models import *

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
    if "page" in param:
        page = int(param["page"])
    else:
        page = 1
    return modelName, productCode, page


def queryResult(param):
    modelName, productCode, page = getCode(param)
    timeStamp = dt.datetime.now().strftime("%y-%m-%d")


    if modelName != None and productCode != None:
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
        if not res:
            return
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
        return res.order_by("basicPrice")[begin:end], len(res)


def updateProduct(obj, i, updateNum):
    num = 0
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
    obj.save()
    if num > 0:
        updateNum += 1
    return updateNum