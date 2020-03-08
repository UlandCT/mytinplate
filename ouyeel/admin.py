from django.contrib import admin
from .models import *
# from django.core.cache import cache


# class BaseModelAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         '''新增或者更新表中的数据时调用'''
#         super().save_model(request, obj, form, change)
#
#         # 发出任务，让celery worker重新生成首页静态页面
#         from celery_tasks.tasks import  generate_static_index_html
#         generate_static_index_html.delay()
#
#
#         # 清除首页的缓存存储 后面她会自动设置和更新
#         cache.delete('index_page_data')
#
#
#
#     def delete_model(self, request, obj):
#         '''删除表中的数据时调用'''
#         super().delete_model(request, obj)
#
#         # 发出任务，让celery worker重新生成首页静态页面
#         from celery_tasks.tasks import generate_static_index_html
#         generate_static_index_html.delay()


# Register your models here.
admin.site.register(Ouyeel)