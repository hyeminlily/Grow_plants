#1번문제
국어=80
영어=75
수학=55
print("1번",(국어+영어+수학)/3)

#2번문제
num=13
if num%2==1:
    print("2번","홀수")
else :
    print("2번","짝수")

#3번문제
a = "881120-1068234"
date = a[:6]
num = a[7:]
print("3번",date,num)

#4번문제
pin="881120-1068234"
a=pin[7]
if a=="1":
    print("4번","남자")
else:
    print("4번","여자")

#5번문제
a="a:b:c:d"
b = a.replace(":","#")
print("5번",b)

#6번문제
a=[1,3,5,4,2]
a.sort()
print("6번",a)

#7번문제
a=["life","is","too","short"]
print("7번"," ".join(a))

#8번문제
a=(1,2,3)
b=(4,)
print("8번",a+b)

#9번문제
a=dict()
print("9번","답은 3번")

#a["name"] = "python" #문자열
#a[("a",)] = "python" #튜플자료형
#a[[1]] = "python" #"[1]"이라는 문자로 지정해야함
#a[250] = "python"
#print("9번",a)

#10번문제ㅠㅠ
#a={'A':90,'B':80,'C':70}
#list(a.keys())
#del a[0]
#del a[2]
#print(a)

#11번문제
a=[1,1,1,2,2,3,3,3,4,4,5]
b=set(a)
print("11번",b)

#12번문제
a=b=[1,2,3]
a[1] =4
print("12번",b)
#a,b모두 동일한 리스트의 주소를 가리키고 있기 때문
#b변수를 생성할 때 a와 다른 주소를 가르키게 하려면 [:]를 사용, copy를 사용
