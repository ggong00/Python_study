# 딕셔너리 생성
dictionary = {}
print(type(dictionary))

# 요소추가
dictionary['student'] = '학생'
dictionary['teacher'] = '선생님'
dictionary['classroom'] = '교실'
print(dictionary)

# 요소삭제
del dictionary['classroom']
print(dictionary)

deleteditem = dictionary.pop('teacher')
print(deleteditem)
print(dictionary)

# 요소수정
dictionary['student'] = '학생2'
print(dictionary)

# 요소추가
dictionary['student'] = '학생'
dictionary['teacher'] = '선생님'
dictionary['classroom'] = '교실'

# 요소조회 1) 요소(키,값)들을 튜플로 변환 
items = dictionary.items()
print(items)

# 요소조회 2) 키를 요소로 갖는 리스트 반환
keys = dictionary.keys()
print(keys)

# 요소조회3 
values = dictionary.values()
print(values)

# 요소조회4 없으면 2번째 매개값을 반환
findedItem = dictionary.get('student','none')
print(findedItem)

# 요소전체 출력하기
for i in dictionary:
    print('{} : {}'.format(i,dictionary.get(i)))

# 객체 복사
dictionary2 = dictionary.copy()    
print(dictionary2)

# 키가 동일하면 업데이트 다르면 추가
dictionary2['test'] = '테스트'
dictionary.update(dictionary2)

# key 존재여부 판단
print('student' in dictionary)
print('student22' not in dictionary)

# 키가 있으면 반환 없으면 추가
print('setdefault --')
print(dictionary.setdefault('student','학생3'))
print(dictionary.setdefault('student2','학생3'))
print(dictionary)

# 요소의 갯수
print(len(dictionary))

# 요소 정렬
import operator
print('==정렬시작')
sortedDic = sorted(dictionary.items(),key=operator.itemgetter(0))
reverseDic2 = sorted(dictionary.items(),key=operator.itemgetter(0),reverse=True)
reverseDic = reversed(sortedDic)

print('==오름차순')
for i in sortedDic:
    print('{} : {}'.format(i[0],i[1]))

print('==내림차순')
for i in reverseDic:
    print('{} : {}'.format(i[0],i[1]))    

print('==파일 작성,읽기 시작')
# 쓰기모드
f = open('D:\javaedu\local_project_git\Python-study\\dictionary.txt','w',encoding='UTF8')
    for line in sortedDic :
        f.write('{} : {}\n'.format(line[0].strip(),line[1].strip()))
    f.close()

# 읽기모드
f = open('D:\javaedu\local_project_git\Python-study\\dictionary.txt','r',encoding='UTF8')
dic = {}
for line in f.readlines():
    list = line.split(':')
    dic[list[0].strip()] = list[1].strip() 
f.close()

print(dic)    

# 사전객체 제거 : 메모리에서 제거되어 접근불가
del dictionary
