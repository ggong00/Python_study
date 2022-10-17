#!/usr/bin/env python
# coding: utf-8

# ### print()함수는 콘솔에 출력하는 명령입니다.

# In[2]:


print('반갑습니다.')


# ### input()함수는 콘솔로부터 입력을 받는 명령입니다.

# In[5]:


name = input('당신의 이름은?')
print('나의 이름은 :' + name)


# ### 원의 넓이를 구하는 프로그램을 작성하시오

# In[27]:


radius = int(input('반지름은 ? '))
areaOfCircle = radius * radius * 3.14
print('반지름은 %d 이고 원의 넓이는 %0.2f' % (radius,areaOfCircle))


# In[23]:


radius = int(input('반지름은 ? '))
areaOfCircle = radius * radius * 3.14
print(f'반지름은 {radius} 이고 원의 넓이는 {areaOfCircle}')


# ### type()함수는 변수의 타입을 알수있습니다.
# ### id()함수는 변수의 주소값을 알수있습니다.

# In[30]:


name = '홍길동'
print(type(name))
age = 30
print(type(age))
print(id(age))
name2 = '홍길동'
print(id(name))
print(id(name2))


# In[40]:


whos


# In[43]:


help(print)


# ### 연산자
#     ** 지수
#     /  나누기
#     // 몫
#     %  나머지

# In[44]:


print(2 ** 2)
print(6 // 4)


# ### 문자열

# In[49]:


str = '''
abcdabcdabc 'dabcd'
abcdabcdabcd
abcdabcd
abcd
'''
print(str)

str2 = 'abcdabcd \nabcd abcd \'abcd\' '
print(str2)


# In[57]:


str3 = 'hello world. hi~'
print(str3[0])
print(str3[1])
print(str3[-1])
print(str3[6:])
print(str3[:5])
print(str3.index('w'))
print(str3[::-2])

a = 1234
print('[{0:<10.2f}]'.format(a))


# ### 문자열 포맷

# In[57]:


a = 1234
print('[{0:<10.2f}]'.format(a))


# ### Boolean
#     True  False
#     1     0
#     [a]   []
#     (a)   ()
#     {a:a} {}
#           None
#     'a'   ''      
#     

# In[77]:


a = True
b = False
print(type(a))
print(type(b))

a = ('a','b')
if a :
    print('참')
else :
    print('거짓')
        


# ### 여러값을 가질수 있는 객체
#     - 튜플 () 여러값을 요소로 가질수 있는 불변객체
#     - 리스트 [] 여러값을 요소로 가질수 있는 가변객체
#     - 딕셔너리 {} 키,값을 쌍으로 갖는 요소를 가질수 있는 가변객체

# In[146]:


dic = {'student' : '학생', 'teacher' : '교사', 'classroom' : '교실'}

# 요소갯수
print(len(dic))

# entry 가져오기
print(dic.items())

# key 가져오기
print(dic.keys())

# value 가져오기
print(dic.values())


# ### 함수

# In[151]:


def add(num1,num2):
    print(num1 + num2)
add(10,20)    


# In[161]:


# doc문서 작성
def add2(num1,num2):
    """
        매개값을 2개 받아 합을 구하는 함수
    """
    
    return num1 + num2
print(add2(10,20))


# In[162]:


# doc문서 출력
print(add2.__doc__)


# In[155]:


# 익명함수
add3 = lambda x,y : x+y
print(add3(10,20))


# In[157]:


# doc문서 출력
print(print.__doc__)

