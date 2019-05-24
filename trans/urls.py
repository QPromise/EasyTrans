# -*- encoding: utf-8 -*-

'''
@Author  :  leoqin

@Contact :  qcs@stu.ouc.edu.cn

@Software:  Pycharm

@Time    :  May 24,2019

@Desc    :  绑定url与视图函数

'''
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^google_trans/$', views.google_trans, name='google_trans'),
    url(r'^youdao_trans/$', views.youdao_trans, name='youdao_trans'),
    url(r'^upload_func/$', views.upload_func, name='upload_func'),
    url(r'^upload_trans/$', views.upload_trans, name='upload_trans'),
    url(r'^download_pdf/$', views.download_pdf, name='download_pdf'),
    url(r'^download_docx/$', views.download_docx, name='download_docx'),

]