#!/usr/bin/env python
# coding: utf-8

# ### 함수2

# In[4]:


# 매개변수 기본값 설정
i = 5
def func2(arg = i):
    print(arg)
    
i = 6
func2()

# 가변인수
def add10(*args):
    sum = 0
    for ele in args:
        sum += ele
     
    return sum
print(add10(10,20))
print(add10(10,20,30))
print(add10(10,20,30,40))


# In[9]:


import time
print(time.ctime())


# In[16]:


import math
print(dir(math))


# In[34]:


class Person:
    # 인스턴스가 공유하는 객체    
    nation = '한국'
    
    # 생성자
    def __init__(self,name,age):
        
        #인스턴스 객체
        self.name = name
        self.age = age
    
    def study(self):
        print('공부하다',self.name,self.age,self.nation)
     
    def eat(self):
        print('먹다')
        
    # 객체 소멸메소드    
    def __del__(self):
        print('Person 객체를 소멸')

p1,p2 = Person('홍길동',30),Person('홍길순',20)

p1.study()
p2.study()
del p1


# In[ ]:




