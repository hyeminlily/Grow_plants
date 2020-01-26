""" def add_and_mul(a,b):
    return a+b, a*b

#예시1
result = add_and_mul(3,4)
print(result)

#예시2
result1, result2 = add_and_mul(3,4)
print(result1, result2) """


""" def say_nick(nick) :
    if nick == "바보" :
        return
    print("나의 별명은 %s 입니다." % nick)

#예시1
say_nick("멍텅구리")

#예시2
say_nick("바보") """



""" def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나의 나이는 %d입니다." % old)
    if man :
        print("남자입니다.")
    else:
        print("여자입니다.")

#예시1
say_myself("이소영", 27, False)

#예시2
say_myself("이승환", 26, True)

##초기값을 설정해 놓은 매개변수 뒤에 초기값을 설정해 놓지 않은 매개변수는 사용할 수 없다.
##즉, 매개변수로 (name, old, man=True)는 가능
##    매개변수로 (name, man=True, old)는 불가능 """



""" 
#1번 : 일반적인 함수
def add(a,b):
    result = a+b
    return result

#예제
i = add(1,2)
print(i)
 """

""" 
#2번 : 입력값이 없는 함수
def say():
    return "hi"

#예제
a = say()
print(a)
 """


#★★★★★뭔소린지... 모르겠어...★★★★★
#결과값이 없는 함수
def add(a,b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

# #예제1
# i = add(5,9)
# print(i)
# ##결과값은 <none> ★★★

#예제2
# add(5,9) 
##결과값은 <5, 9의 합은 14입니다.> ★★★"""

""" 
#입력값도 결과값도 없는 함수
#입력 인수를 받는 매개변수도 없고 return문도 없으니 입력값도 결과값도 없는 함수
def say() :
    print("hi")

say()

 """  


##★★★★★
##함수 안에서 함수 밖의 변수를 변경하는 방법
# return 사용하기

a = 1
def vartest(a):
    a = a+1
    return a
    
a = vartest(2)
print(a)
##★★★★★



""" 
##lambda 함수 : def와 동일한 역할을 함

# 1. lambda를 이용
# 사용법
# lambda 매개변수1, 매개변수 2, ... : 매개변수를 이용한 표현식
add = lambda a, b : a+b
result = add(3,4)
print(result)

# 2. def를 이용
def add(a,b):
    return a+b

result = add(3,4)
print(result) """

