f = open('D:\javaedu\local_project_git\Python-study\\test.txt','w')
print(f.writable())
f.write('hello world~ \n')
f.close()

f = open('D:\javaedu\local_project_git\Python-study\\test.txt','r')
print(f.readlines())