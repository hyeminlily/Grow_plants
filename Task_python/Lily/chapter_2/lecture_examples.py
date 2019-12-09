# 숫자형
a = 3
b = 4
print(a ** b)   # a의 b제곱

c = 7
d = 3
print(c % d)    # 나머지
print(d % c)

e = 7
f = 4
print(e / f)
print(e // f)   # 몫


# 문자열 자료형
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."
print(food)
print(say)

multiline='''
Life is too short
You need python
'''
print(multiline)

print(len(multiline))
print(multiline[7])
print(multiline[-5])
print(multiline[0:5])

a = "20191209Rainy"
year = a[0:4]
day = a[4:8]
weather = a[8:]
print(year, day, weather)

a = "Pithon"
print(a[:1] + "y" + a[2:])