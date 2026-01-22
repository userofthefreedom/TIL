# import 문 사용
import math

print(math.pi)  # 3.141592653589793
print(math.sqrt(4))  # 2.0


# from 절 사용
from math import pi, sqrt

print(pi)  # 변수명
print(sqrt(4))  # 함수명






# from 절 단점
from math import sqrt

math_result = sqrt(16)  # 실수형 4.0


def sqrt(x):  # 사용자가 정의한 sqrt 함수
    return str(x**0.5)


my_result = sqrt(16)  # 문자열 4.0

print(type(math_result), type(my_result))  # <class 'float'> <class 'str'>


# from 절 사용 주의 사항
## 같은 이름인 경우 덮어쓰기 주의
# from math import sqrt  # math.sqrt가 먼저 import됨
# from my_math import sqrt  # my_math.sqrt가 math.sqrt를 덮어씀

result = sqrt(9)  # math.sqrt가 아닌 my_math.sqrt가 사용됨


# from 절 사용 주의 사항
## 모든 요소를 한 번에 import 하는 * 은 권장하지 않음
from math import *
# from my_math import sqrt, tangent  # 어느 함수가 math 모듈과 중복되는지 모름

# 아래는 사용자가 임의로 정의한 변수들
a = 100
c = 200
e = 300  # math 모듈의 자연상수 e를 사용할 수 없게 됨




## as 키워드 사용 1
from math import sqrt
from my_math import sqrt as my_sqrt

print(sqrt(4))  # 2.0
print(my_sqrt(4))  # 2.0


# ## as 키워드 사용 2
# ## (참고) pandas와 matplotlib 패키지 설치해야 정상 동작
# import pandas as pd # type: ignore
# import matplotlib.pyplot as plt # type: ignore

# # # 별칭을 부여하지 않으면 길고 불편함
# # df = pandas.DataFrame()
# # matplotlib.pyplot.plot(x, y)

# # 별칭을 사용하면 짧고 편리
# df = pd.DataFrame()
# plt.plot(x, y) # type: ignore




# # requests 패키지 사용 예제
# # requests 패키지 설치해야 정상 동작

# import requests

# # 공휴일 정보 API
# url = "https://date.nager.at/api/v3/publicholidays/2026/KR"
# response = requests.get(url).json()
# print(response)











# if문 기본


# 복수 조건문
## 순서 1. 결과: 매우 나쁨
dust = 155

if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')


## 순서 2. # 결과: 보통
dust = 155

if dust > 30:
    print('보통')
elif dust > 80:
    print('나쁨')
elif dust > 150:
    print('매우 나쁨')
else:
    print('좋음')


# 중첩 조건문 동작 예시
# 출력: 매우 나쁨
#      위험해요! 나가지 마세요!
dust = 480

if dust > 150:
    print('매우 나쁨')
    if dust > 300:
        print('위험해요! 나가지 마세요!')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')








# for문 기본
student_list = ['Alice', 'Bob', 'Charlie']


# for문 작동 원리
item_list = ['apple', 'banana', 'coconut']

for item in item_list:  # item: 반복 변수
    print(item)


# 문자열 순회
country = 'Korea'

for char in country:
    print(char)


# range 순회
for i in range(5):
    print(i)


# for문 dictionary 순회
my_dict = {
    'x': 10,
    'y': 20,
    'z': 30,
}

for key in my_dict:
    print(key)
    print(my_dict[key])


# 인덱스 순회
numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)


# 중첩 반복문
outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:
    for inner in inners:
        print(outer, inner)


# 중첩 리스트 순회
elements = [['A', 'B'], ['c', 'd']]

# 1
for elem in elements:
    print(elem)

# 2
for elem in elements:
    for item in elem:
        print(item)









# while문 기본 1


# while문 기본 2
input_value = ''
while input_value != 'exit':  # exit 를 입력하면 반복 종료
    input_value = input("Enter a value: ")
    print(input_value)


# while문 사용자 입력에 따른 반복
number = int(input('양의 정수를 입력해주세요.: '))

while number <= 0:
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')

    number = int(input('양의 정수를 입력해주세요.: '))

print('잘했습니다!')










# break 키워드 기본
for i in range(10):
    if i == 5:
        break
    print(i)  # 0 1 2 3 4


# break 키워드 예시 (for문)
# 리스트에서 첫번째 짝수만 찾은 후 반복 종료하기
numbers = [1, 3, 5, 6, 7, 9, 10, 11]
found_even = False

for num in numbers:
    if num % 2 == 0:
        print('첫 번째 짝수를 찾았습니다:', num)
        found_even = True
        break

if not found_even:
    print('짝수를 찾지 못했습니다')


# break 키워드 예시 (while문)
# 프로그램 종료 조건 만들기
number = int(input('양의 정수를 입력해주세요.: '))

while number <= 0:
    if number == -9999:
        print('프로그램을 종료합니다.')
        break

    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')

    number = int(input('양의 정수를 입력해주세요.: '))
print('잘했습니다!')










# continue 키워드 기본
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 1 3 5 7 9


# continue 키워드 예시
# 리스트에서 홀수만 출력하기
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        continue
    print(num)









# # pass 키워드 예시 (while 문)
# while True:
#     if condition1:
#         break
#     elif condition2:
#         pass  # 빈 코드를 의미
#     else:
#         print('출력')

# # pass 키워드 예시 (if 문)
# if condition:
#     pass  # 아무런 동작도 수행하지 않음
# else:
#     pass  # 구조를 잡을 뿐


# # pass 키워드 예시 (함수 정의)
# def my_function():
#     pass  # pass 없으면 오류 발생












# map 함수 사용 기본
numbers = [1, 2, 3]
result = map(str, numbers)

print(result)  # <map object at 0x00000239C915D760>
print(list(result))  # ['1', '2', '3']


# map 함수 활용 1 - input과 함께 사용
# 터미널 창에서 1 2 3 입력 (공백 주의)
numbers1 = input().split()
print(numbers1)  # ['1', '2', '3']

## 터미널 창에서 1 2 3 입력 (공백 주의)
numbers2 = list(map(int, input().split()))
print(numbers2)  # [1, 2, 3]


# map 함수 활용 2 - lambda와 함께 사용
numbers = [1, 2, 3, 4, 5]


def square(x):
    return x**2


# lambda 미사용
squared1 = list(map(square, numbers))
print(squared1)  # [1, 4, 9, 16, 25]

# lambda 사용
squared2 = list(map(lambda x: x**2, numbers))
print(squared2)  # [1, 4, 9, 16, 25]








# zip 함수 사용 기본
girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls, boys)

print(pair)  # <zip object at 0x000001C76DE58700>
print(list(pair))  # [('jane', 'peter'), ('ashley', 'jay')]


# zip 함수 활용
kr_scores = [10, 20, 30, 50]
math_scores = [20, 40, 50, 70]
en_scores = [40, 20, 30, 50]

for student_scores in zip(kr_scores, math_scores, en_scores):
    print(student_scores)

# zip 함수 활용 (전치 행렬)
scores = [
    [10, 20, 30],
    [40, 50, 39],
    [20, 40, 50],
]

for score in zip(*scores):
    print(score)












# enumerate 함수 기본
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)
"""
0 apple
1 banana
2 cherry
"""

# enumerate 함수 활용 1
# start 인자를 사용하여 인덱스 번호를 1부터 출력
movies = ['인터스텔라', '기생충', '인사이드 아웃', '라라랜드']

for idx, title in enumerate(movies, start=1):
    print(f"{idx}위: {title}")


# enumerate 함수 활용 2
# 인덱스 정보를 활용하여 특정 조건에 맞는 요소 찾기
respondents = ['은지', '정우', '소민', '태호']
answers = ['', '좋아요', '', '괜찮아요']

for i, response in enumerate(answers):
    if response == '':
        print(f"{respondents[i]} 미제출")














# for-else 구문 기본
for i in range(5):
    print(i)
    if i == 3:
        # break 문이 실행되면 else 블록은 실행되지 않음
        print('반복이 중단되었습니다.')
        break
else:
    print('이 메시지는 출력되지 않습니다.')


# for-else 구문 활용 1
# 중복 아이디 찾기 - 찾은 경우
registered_ids = ['admin', 'user01', 'guest', 'user02']
id_to_check = 'guest'  # 이미 리스트에 존재하는 아이디

for existing_id in registered_ids:
    if existing_id == id_to_check:
        print('이미 사용 중인 아이디입니다.')
        break  # 중복 아이디를 찾았으므로 확인 절차를 중단
else:
    # for 루프가 break로 중단되었기에 이 부분은 실행되지 않음
    print('사용 가능한 아이디입니다.')

print('아이디 확인 절차를 종료합니다.')


# for-else 구문 활용 2
# 중복 아이디 찾기 - 찾지 못한 경우
registered_ids = ['admin', 'user01', 'guest', 'user02']
id_to_check = 'new_user'  # 리스트에 없는 새로운 아이디

for existing_id in registered_ids:
    if existing_id == id_to_check:
        print('이미 사용 중인 아이디입니다.')
        break
else:
    # for 루프가 break 없이 마무리 되어 else 블록 실행
    print('사용 가능한 아이디입니다.')
