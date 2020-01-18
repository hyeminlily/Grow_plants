# Q1
a = "Life is too short, you need python"

if "wife" in a : print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a : print("shirt")
elif "need" in a : print("need")
else: print("none")

# Q2
n = 0
sum = 0

while(True):
    if n > 1000:
        break
    else:
        if n % 3 == 0:
            sum += n
        n += 1

print(sum)

# Q3
a = 1
while(True):
    if a > 5:
        break
    else:
        print("*" * a)
        a += 1

# Q4
b = range(1, 101)
for c in b:
    if c % 10 == 0:
        print(c, end="\n")
    else:
        print(c, end=" ")

# Q5
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum_score = 0

for score in A:
    sum_score += score

print("평균 점수는 " + str(sum_score/len(A)))

# Q6
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n % 2 == 1]
print(result)