from django.test import TestCase
import requests,urllib.parse,urllib.request,json
# Create your tests here.
def main():
    headers = {}
    url = "http://localhost:8000/queryResultList"
    param = {"parameters":{
        'sourceCode':'1',
        'productCode':'1',
    }}
    # param = {"param":[1,2,3,4]}
    # param = {"param":"this is param!"}
    # res = requests.get(url=url,params=param)
    param = urllib.parse.urlencode(param)
    url = url + "?" +param
    request = urllib.request.Request(url,headers=headers)
    res1 = urllib.request.urlopen(request)
    print(res1)

def jsonstr():
    a = {
        '1':'a',
        '2':'b',
        '3':'c',
    }
    b = json.dumps(a)
    c = "{'a':'1'}"
    adf = 123
    evalc = eval("adf")
    print(evalc)
    adf = eval(a)



if __name__ == "__main__":
    main()
    # jsonstr()