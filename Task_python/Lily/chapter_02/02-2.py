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

# formatting
print("I eat %d apples." % 3)
print("I eat %s apples." % "five")

number = 3
day = "three"

print("I eat %d apples." % number)
print("I ate %d apples. so I was sick for %s days." % (number, day))

"""
%s = String
%c = character
%d = integer
%f = floating-point
%o = 8진수
%x = 16진수
%% = literal
"""

a = "1:2:3:4"
b = a.replace(":", "#")
print(b)