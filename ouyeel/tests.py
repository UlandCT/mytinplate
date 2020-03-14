from django.test import TestCase
from time import ctime, sleep
import requests,urllib.parse,urllib.request,json,threading
# Create your tests here.
from mytinplate.settings import *
def main():
    origin_list = ["http://101.133.162.19:18181", "http://localhost:18181"]
    access_list = ["/api/querySingleProduct", "/api/queryResultList"]
    origin = origin_list[0]
    access = access_list[0]
    headers = {}
    url = origin + access
    param = {"parameters":{
        'sourceCode': '2',
        'productCode': "1",
        'packCode': '9ZG2165',
        # 'packCode': '01D0426',
    }}
    # param = {"param":[1,2,3,4]}
    # param = {"param":"this is param!"}
    param = urllib.parse.urlencode(param)
    url = url + "?" +param
    # request = urllib.request.Request(url,headers=headers)
    # res = urllib.request.urlopen(request)
    res = requests.get(url=url,headers=headers, timeout=10)
    print(res.text)
    res = json.loads(res.text)
    # resList = []
    # for i in res["resultList"]:
    #     if i["productTypeCode"]== "TL60":
    #         resList.append(i)
    print(1111)

def jsonstr():
    def act1():
        for i in range(2):
            print("act1 is running at %s" % ctime())
            sleep(2)

    def act2():
        for i in range(2):
            print("act2 is running at %s" % ctime())
            sleep(6)

    threads = []
    t1 = threading.Thread(target=act1)
    threads.append(t1)
    t2 = threading.Thread(target=act2)
    threads.append(t2)
    for t in threads:
        t.setDaemon(True)
        t.start()
        print("befor join at %s" % ctime())
        # t.join()
        print("after join")

    print("finished at %s" % ctime())


if __name__ == "__main__":
    # main()
    d = "20-03-11"
    d = "20" + d


    print(d)
