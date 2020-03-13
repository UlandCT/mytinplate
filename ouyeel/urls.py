from django.conf.urls import url
from .views import *
# 导入url函数

# 创建视图函数，用于处理路由分发请求
urlpatterns = [
    url(r'^index$', index_views),
    url(r'^querySingleProduct/$', query_single_product),
    url(r'^bGradeProduct$', reportB_grade),
    url(r'^queryResultList$', queryResultList,),
    url(r'^getDataToOyDb$', getDataToOyDb),




]
urlpatterns += [
    url(r'^test', test_views),
    url(r'^islogged/$', islogged),
    url(r'^logout/$', logout),
]
