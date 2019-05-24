# -*- encoding: utf-8 -*-

'''
@Author  :  leoqin

@Contact :  qcs@stu.ouc.edu.cn

@Software:  Pycharm

@Time    :  May 24,2019

@Desc    :  测试正则匹配功能

'''
import re
def is_figure(target):
    return re.match(r'fig\..\.',target,re.I)
target = ' Fig. 1. Message queue group model'
print(is_figure(target.replace(' ','')))
goal = '[10] L. Chuang, Z. Gang, and G. Q. J. C. Engineering, "Research on Data Distribution Service for Ship Information System," vol. 39, no. 9, pp. 94-97, 2013. '
def is_reference(goal):
    res = re.search('',goal)
    match_3 = re.search(r'(.+?)\.(.+?)\.(.+?)\.(\d{4});(\d+)\((\d{1,2})\):(\d+-\d+)\.', goal, re.X|re.I|re.U)
    print(match_3)
is_reference(goal)