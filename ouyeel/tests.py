from django.test import TestCase
from time import ctime, sleep
import requests,urllib.parse,urllib.request,json,threading
# Create your tests here.
def main():
    headers = {}
    url = "http://localhost:8000/queryResultList"
    param = {"parameters":{
        'sourceCode':'2',
        'productCode':'3',
    }}
    # param = {"param":[1,2,3,4]}
    # param = {"param":"this is param!"}
    # res = requests.get(url=url,params=param)
    param = urllib.parse.urlencode(param)
    url = url + "?" +param
    request = urllib.request.Request(url,headers=headers)
    res1 = urllib.request.urlopen(request)
    print(res1.read())

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
    jsonstr()