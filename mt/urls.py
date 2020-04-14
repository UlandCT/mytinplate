from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^insertMtDb', insert_mt_db),
]