# 파일 존재여부 판단하기

import os

file = r'D:\javaedu\local_project_git\Python-study\test5.txt'
print(os.path.exists(file)) 

dic = None
if not os.path.exists(file):
    #파일이 존재하지 않으면 신규
    dic = open(file,'w',encoding='UTF8')
    print('신규파일열기')
else:
    #파일이 존재하면 추가    
    dic = open(file,'a',encoding='UTF8')
    print('파일존재')