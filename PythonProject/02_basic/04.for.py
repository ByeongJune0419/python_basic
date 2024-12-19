# 반복문
# from operator import index

# from mkl_random.mklrand import lenth

# 콘솔창에 Hello 를 10번 출력


# 반복문을 이용해서 hello를 10번 출력
for i in range(0, 10):
    print("Hello")

# range(0,10) 는 배열 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(range(0, 10))
print(list(range(0, 10)))

for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print("Hello")

# 콘솔창에 1부터 10까지 출력
# 반복문을 이용하는 가장 큰 이유 -> 중복코드 합치기
for i in range(1, 11):
    print(i)

numArray = [2, 5, 3, 4]
for i in numArray:
    print(i)

stuArray = ["김호빵", "이찐빵", "박꿀빵"]
for i in stuArray:
    print(i)

# numArray의 모든 값에 3을 곱하기
numArray * 3
print(numArray * 3)  # [2, 5, 3, 4, 2, 5, 3, 4, 2, 5, 3, 4]

# 배열 내 값 수정
print(numArray)  # [2, 5, 3, 4]
print(numArray[0])  # 2
numArray[0] * 3
print(numArray[0] * 3)  # 6

numArray[0] = numArray[0] * 3
print(numArray[0])  # 6

numArray[1] = numArray[1] * 3
print(numArray)

numArray[2] *= 3
print(numArray)

numArray[3] *= 3
print(numArray)

numArray = [2, 5, 3, 4]
# for문으로 바꿔보기
numArray[0] *= 3
numArray[1] *= 3
numArray[2] *= 3
numArray[3] *= 3
print(numArray)

numArray = [2, 5, 3, 4, 8, 9]
print(numArray)

# i를 0, 1, 2, 3, 이 되도록 하는 for문
for i in range(0, len(numArray)):
    numArray[i] *= 3

print(numArray)

# 다른 사람이 만든 배열 라이브러리 numpy 라이브러리 사용
# numpy 라이브러리 불러오기

import numpy as np  # as 는 alias(별칭) 의 약자

numArray = [2, 5, 3, 4]
npArray = np.array([2, 5, 3, 4])

print(numArray)
print(npArray)

print(type(numArray))  # <claas 'list'>
print(type(npArray))  # <class ' numpy.ndarray'>

print(npArray * 3)
print(npArray)

npArray = npArray * 3
print(npArray)

npArray *= 3
print(npArray)

# 20부터 40까지 다 더하면?
# i가 1부터 100이 되도록 for문 만들기
sum = 0

for i in range(20, 41):  # n부터 n+1
    sum += i

print(sum)

# 5 팩토리얼의 값은? 5! = 5 * 4 * 3 * 2 * 1 = 120
# 10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 3628800

sum = 1
for i in range(1, 6):
    sum *= i
print(sum)

sum = 1
for i in range(1, 11):
    sum *= i
print(sum)

# range로 거꾸로 배열 생성
sum = 1
for i in range(10, 0, -1):  # 10(10)부터 1(0)까지, 그리고 거꾸로(-1)라는 뜻
    sum *= i
print(sum)

# 1부터 30까지 숫자 중에 홀수만 출력
# i가 1부터 30이 되도록 for 문 생성

for i in range(1, 31):
    # i 가 1부터 30이 되는데, i가 홀수인지 체크(= 조건 체크 -> 조건문 사용)
    if i % 2 == 1:
        print(i)
    else:
        print(i)

# 30부터 60까지 숫자 중에 짝수만 다 더하면?
# i가 30부터 60이 되도록 for 문 생성

sum = 0  # 변수를 설정해야 다 더하거나,곱하거나 등 할 수 있음

for i in range(30, 61):
    # i 가 짝수인지 확인
    if i % 2 == 0:
        sum += i

print(sum)

# range의 범위 조정

sum = 0
for i in range(30, 61, 2):  # [30, 32, 34, 36, ..., 60]
    sum += i

print(sum)

nameArray = ["김호빵", "이찐빵", "박꿀빵", "김식빵", "김붕어빵"]

# 김씨 성을 가진 사람이 몇명인지 세어보기
sum = 0
for i in nameArray:
    print(i)
    # i의 첫번째 글자만 꺼내기 -> index 활용 ([0])
    fst = (i[0])
    print(fst)
    # 꺼낸 첫번째 글자가 "김" 인지 조건체크 -> 조건문 활용
    if fst == "김":
        # 조건이 True면 sum에 1을 더하기
        sum += 1

print(sum)

# 콘솔 창에
# *
# **
# ***
# ****
# *****
# 와 같이 출력 될 수 있도록 반복문을 작성하기

# 빈 무자열(empty)
star = ""
# 5번 반복되는 for문 선언 [*을 반복하는 반복문 작성하기(내가쓴것)]
print(list(range(0,5)))

for i in range (5):
    # for문이 반복될때마다 star에 "*"를 추가한 후 출력[그 반복문에 *을 추가하기(내가쓴것)]
    star = star + "*"
    print(star)


# 콘솔 창에
# *****
# ****
# ***
# **
# *
# 출력해보기

# 5번 반복하는 for문 생성
star = "******"
for i in range(5, 0, -1): # [5, 4, 3, 2, 1]
# for문이 반복될대마다 star의 길이를 한칸씩 줄이기
    print(star[0:i])

for i in range(5): # [0, 1, 2, 3, 4, 5]
    # i 는 0, 1, 2, 3, ,4
    # ? 는 5, 4, 3, 2, ,1
    # 5 - i = ?
    print(star[0:5-i])


# 트리 만들기
#    *
#   ***
#  *****
# *******
#*********

# print가 5번 실행되므로 5번 반복하는 for문 생성
for i in range(5): # [0, 1, 2, 3, 4,]
    star = ""
    for k in range(2*i+1):  # 바깥 for문의 내부변수 i와 다른 변수명 사용
        star += "*"
        # i 가 0, 1, 2, 3, 4
        # * 은 1, 3, 5, 7, 9 ... i와의 관계? -> 2*i+1
        #   은 4, 3, 2, 1, 0 ... i와의 관계? -> 4-i

    blank = ""
    for k in range(4-i):
        blank += " "

    print(blank + star)









