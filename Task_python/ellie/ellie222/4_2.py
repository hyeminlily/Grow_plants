##input의 사용
#input은 입력되는 모든 것을 문자열로 취급한다.



##Print

#큰따옴표("")로 둘러싸인 문자열은 + 연산과 동일하다.

""" 
print("life", "is", "too short")  #1번
#결과 : life is too short

print("life" + "is" + "too short") #2번
#결과 : lifeistoo short
 """

#문자열 띄어쓰기는 콤마로 한다.

#한 줄에 결과값 출력하기
for i in range(10): #0부터 9까지
    print(i, end=' ') #한 줄에 결과값을 계속 이어서 출력하려면 매개변수 end를 사용해 끝 문자를 지정해야 한다.
