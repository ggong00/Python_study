import operator
import os
W_EMPTY = '단어를 추가해주세요'
W_MAX = '최대 5개단어만 저장할 수 있습니다.'
W_NOT_FOUND = '단어를 검색할 수 없습니다.'
I_ADD = '단어를 추가했습니다.'
I_UPDATE = '단어의 뜻을 수정하였습니다.'
I_DELETE = '단어를 삭제했습니다.'
FILE_PATH = r'D:\javaedu\dictionary.txt'

class DupliException(Exception):
    def __init__(self):
        super().__init__('이미 등록되었습니다.')

# 단어장
class Dictionary:

    # 기본설정
    def __init__(self):
        if os.path.exists(FILE_PATH):
            file = open(FILE_PATH,'r',encoding='UTF8')
            self.memoryDic = self.getLocalDic(file)
            file.close()
        else:
            self.memoryDic = {}                
        self.maxsize = 5

    # 로컬단어장 가져오기
    def getLocalDic(self,file):
        localDic = {}
        for ele in file.readlines():
            list = ele.split(":")
            localDic[list[0].strip()] = list[1].strip() 

        return localDic    

    # 단어추가
    def add(self,key,value):
        key = key.lower()

        if len(self.memoryDic) == self.maxsize: return W_MAX
        if key in self.memoryDic.keys(): raise DupliException()

        self.memoryDic[key] = value

        return I_ADD

    # 단어검색
    def search(self,key):
        key = key.lower()
        result = {}
        
        for i in self.memoryDic:
            if i.find(key) == 0:
                result[i] = self.memoryDic[i]

        return result

    # 단어수정
    def update(self,key,value):
        key = key.lower()

        if key not in self.memoryDic.keys(): return W_NOT_FOUND

        self.memoryDic[key] = value    
        return I_UPDATE    

    # 단어삭제    
    def delete(self,key):
        key = key.lower()

        if key not in self.memoryDic.keys(): return W_NOT_FOUND

        del self.memoryDic[key]
        return I_DELETE
        
    # 단어장 리스트 출력    
    def list(self,mode):
        dic = self.memoryDic.items()

        if mode == '1':
            return sorted(dic,key=operator.itemgetter(0))

        elif mode == '2':    
            return sorted(dic,key=operator.itemgetter(0),reverse=True)

    #통계
    def state(self):        
        if not self.memoryDic:
            return W_EMPTY

        result = ''
        sortedBylen = sorted(self.memoryDic.keys(), key=lambda x : len(x), reverse=True)
        result += '저장된 단어 갯수 >> {}\n'.format(len(self.memoryDic))
        result += '문자수가 가장 많은 단어 >> {}\n'.format(sortedBylen[0])
        result += '단어 글자수 내림차순 출력\n'

        for i in sortedBylen:
            result += '{}\n'.format(i) 

        return result

    # 단어장 로컬파일에 저장
    def saveLocalFile(self):
        file = open(FILE_PATH,'w',encoding='UTF8')
        for i in self.memoryDic.items():
            file.write('{}:{}\n'.format(i[0],i[1]))
        file.close()

# 프로그램 실행부
myDic = Dictionary()
stop = False
while not stop:
    menu = input('1.저장 2.검색 3.수정 4.삭제 5.목록 6.통계 7.종료\n')

    #저장
    if menu == '1':        
        try:
            print(myDic.add(input('단어 >> '),input('뜻 >> ')))
        except DupliException as e:    
            print(e)
            
    #검색
    elif menu == '2':
        result = myDic.search(input('단어 >> '))
        if result:
            for i in result.items():
                print('{} : {}'.format(i[0],i[1]))
        else:
            print(W_NOT_FOUND)        

    #수정
    elif menu == '3':
        print(myDic.update(input('단어 >> '),input('뜻 >> ')))
        
    #삭제    
    elif menu == '4':
        print(myDic.delete(input('단어 >> ')))

    #목록
    elif menu == '5':
        result = myDic.list(input('1.오름차순 2.내림차순\n')) 
        if result:
            for i in result:
                print('{} : {}'.format(i[0],i[1]))
        else:
            print(W_EMPTY)   

    #통계        
    elif menu == '6':
        print(myDic.state())

    #종료
    elif menu == '7':
        print('프로그램을 종료합니다.')
        myDic.saveLocalFile()
        stop = True

    #기타입력
    else:
        print('메뉴가 올바르지 않습니다.')
