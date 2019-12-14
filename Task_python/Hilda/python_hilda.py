#1번
a=80
b=75
c=55
(a+b+c)/3
#print(a+b+c)


#2번
a=13
b=a % 2
#print(b) 2로 나눴을때 값이 0이 나오면 짝수, 1이 나오면 홀수
#1이 나왔으므로 홀수!!!!!!!!


#3번
a="881120-168234"
#print(a[:6])
#print(a[7:])


#4번
pin="881120-1068234"
#print(pin[7])


#5번
a="a:b:c:d"
b=a.replace(":","#")
#print(b)


#6번
a=[1,3,5,4,2]
a.sort()
a.reverse()
#print(a)  얘는 왜 어디에 담지 않아도 되는가 값이 변하는게 아니고 순서가 변해서?


#7번
a=['Life', 'is', 'too', 'short']
#print(" ".join(a))


#8번
t1=(1,2,3)
t2=(4,)
#print(t1 + t2)


#9번
a = dict('name':'python', 'a':'python', '[1]':'python', '250':'python')
print(a['name'])




#10번
a = {'A':90, 'B':80, 'C':70}
#print(a.pop('B'))


#11번
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
s1=set(a)
#print(s1)


#12번
a = b = [1, 2, 3]
a[1] = 4
#print(b)
#b값도 동일하게 [1,4,3]으로 불러옴 / a와 b 모두 동일한 리스트를 가리키고 있기 때문에 동시에 변함