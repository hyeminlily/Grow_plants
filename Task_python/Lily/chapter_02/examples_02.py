# Q1
kor = 80
eng = 75
math = 55
avg = (kor + eng + math) / 3

print("홍길동 씨의 평균 점수 =", avg)
print("-" * 30)

# Q2
n = 13

if n % 2 == 0:
    print("자연수 13은 짝수입니다.")
else:
    print("자연수 13은 홀수입니다.")
print("-" * 30)

# Q3
hongsNumber = "881120-1068234"
print("연월일 =", hongsNumber[:6])
print("뒷부분 =", hongsNumber[7:])
print("-" * 30)

split_hongsNumber = hongsNumber.split("-")
print(split_hongsNumber)
print("연월일 =", split_hongsNumber[0])
print("뒷부분 =", split_hongsNumber[1])
print("-" * 30)

# Q4
pin = "881020-1068234"

split_pin = pin.split("-")
if split_pin[1][0] == "1":
    print("성별은 남자입니다.")
else:
    print("성별은 여자입니다.")
print("-" * 30)

# Q5
a = "a:b:c:d"
b = a.replace(":", "#")
print("replace =", b)
print("-" * 30)

# Q6
list = [1, 3, 5, 4, 2]
list.sort()
list.reverse()
print("거꾸로 하면은 =", list)
print("-" * 30)

# Q7
str_list = ['Life', 'is', 'too', 'short']
str = (" ").join(str_list)

print(str)
print("-" * 30)

# Q8
tuples = (1, 2, 3)
tuples = tuples + (4, )
print(tuples)
print("-" * 30)

# Q9
a = dict()

a['name'] = 'python'
print(a)
a[('a',)] = 'python'
print(a)
# a[[1]] = 'python'
# print(a)
a[250] = 'python'
print(a)
print("-" * 30)

# Q10
a = {'A':90, 'B':80, 'C':70}
# print("B =",a.pop('B'))
print("B =", a['B'])
print("-" * 30)

# Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
b = set(a)
print("집합 자료형은 =", b)
print("-" * 30)

# Q12
a = b = [1, 2, 3]
a[1] = 4
print("b =", b)