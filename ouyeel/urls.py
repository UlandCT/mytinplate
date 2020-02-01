from django.conf.urls import url
from .views import *
# 导入url函数

# 创建视图函数，用于处理路由分发请求
urlpatterns = [
    url(r'^$',index_views),
    # url(r'^index/$',index_views1),
    # url(r'^03_form/$',form_views),
    url(r'^queryList$',queryList,),
    url(r'^getDataToDb$',getDataToDb),



]
urlpatterns += [
    # url(r'^test/',test_views),
    url(r'^islogged/$',islogged),
    url(r'^logout/$',logout),
]