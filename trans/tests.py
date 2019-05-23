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
print( 0 if is_figure(target) else 1)