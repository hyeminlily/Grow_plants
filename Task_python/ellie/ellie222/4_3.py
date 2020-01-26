# <파일 생성하기>
# 파일객체 = open(파일이름, 파일 열기 모드)
# 파일열기모드의 종류
# 1) r : 읽기모드
# 2) W : 쓰기모드
# 3) a : 추가모드(파일의 마지막에 새로운 내용을 추가 시킬 때 사용)
# 파일을 쓰기 모드로 열었을 때 해당 파일이 이미 존재할 경우, 원래 있던 내용이 모두 사라진다.
# 4) `f.close()` 는 열려있는 파일 객체를 닫아 주는 역할

# <파일 생성하기_예제>
# f=open("새파일.txt",'w')
# f.close()


# #writedata.py
# f=open("C:/backup/Dev/git/새파일.txt", 'w')
# for i in range(1,11) :
#     data = "%d째 줄입니다. \n" % i
#     f.write(data)
# f.close()

#readline_test.py
#파일을 읽기 모드로 연 후 readline()을 사용해서 파일의 첫 번째 줄을 읽어 출력하는 경우
# f=open("C:/backup/Dev/git/새파일.txt", 'r')
# line = f.readline()
# print(line)
# f.close()

#★★★★★readlines_test.py★★★★★
#파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다.
# f=open("C:/backup/Dev/git/새파일.txt",'r')
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()
#★★★★★★★★★★★★★★★★★★★

#★★★★★read 함수 사용하기★★★★★
f = open("C:/Backup/Dev/git/새파일.txt", 'r')
data = f.read()
print(data)
f.close()
#★★★★★★★★★★★★★★★★★★★

# adddata.py
f =open("C:/Backup/Dev/git/새파일.txt", 'a')
for i in range(11,20):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()