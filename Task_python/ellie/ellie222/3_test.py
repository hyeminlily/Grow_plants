##3장 연습문제

##1번
a="life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a : print("python")
elif "shirt" not in a : print("shirt")
else : print("none")

print("shirt")
print("=" * 50)

##2번
num = 0
sum = 0
while num <= 1000 :
    num = num + 1
    if(num % 3) !=0 : continue
    sum = sum + num
print(sum)
print("=" * 50)

##3번
num = 0
while num < 6:
    num = num +1
    print("*" * num)
    if num == 5:
        break
print("=" * 50)


##4번
num = 0
for a in range(1,101) :
    num = a
    print(num, end=" ")
print("")
print("=" * 50)

##5번
a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

total = 0
for i in a :
    total = total + i 
avg = total/len(a)
print(avg)
print("=" * 50)

##6번
""" number = [1,2,3,4,5]

result = []
for n in numbers :
    if n % 2 == 1:
        result.append(n*2) """

number = [1,2,3,4,5]
result=[n*2 for n in number if n % 2 == 1]
print(result)
print("=" * 50)


