from django.shortcuts import render
import json
from ouyeel.apiFuc import *
from django.db.models import Q
from ouyeel.setting import *
# from django.core import serializers
# from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
import datetime as dt
from .api import work_on_mt
# Create your views here.


def insert_mt_db(request):
    try:
        from django.conf import settings
        file = request.FILES.get("file")
        filename = file.name
        file_content = file.chunks()
        log_dir = settings.BASE_DIR + "/mt/config/"
        file_name = log_dir + "xls/{}".format(filename)
        with open(file_name, "wb") as f:
            for i in file_content:
                f.write(i)
        try:
            insert_num, update_num = work_on_mt(file_name, log_dir)
            new = successCode.copy()
            new['msg'] = "succeed!insert %d records,update %d records" % (insert_num, update_num)
            generate_home()
            return HttpResponse(json.dumps(new))
        except Exception as e:
            print("insertdb error:", e)
            new_err = errCode.copy()
            new_err['msg'] = "%s" % e
            return HttpResponse(json.dumps(new_err))
    # except Ouyeel.DoesNotExist as e:
    except Exception as e:
        print(e)
        return HttpResponse("it's wrong method!")