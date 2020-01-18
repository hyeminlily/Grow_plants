# Q1
def is_odd(n):
    if n % 2 == 0:
        print("짝수에용")
    else:
        print("홀수에용")

is_odd(5)

# Q2
def avr_sum(*args):
    sum = 0
    for a in args:
        sum += a
    return sum / len(args)

print(avr_sum(3,4,5,6,7,8,9))

# Q3
input1 = input("첫번째 숫자를 입력하세요: ")
input2 = input("두번째 숫자를 입력하세요: ")

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다" % total)

# Q4
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))

# Q5
f1 = open("./test.txt", "w")
f1.write("Life is too short")
f1.close()

f2 = open("./test.txt", "r")
print(f2.read())
f2.close()

# Q6
content = input("내용을 입력하세욧: ")
file = open("./content.txt", "a")
file.write(content)
file.close()

# Q7
file1 = open("./text1.txt", "r")
content_new = file1.read()
file1.close()

content_new = content_new.replace('java', 'python')

file2 = open("./text1.txt", "w")
file2.write(content_new)
file2.close()