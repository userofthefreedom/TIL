# import copy
# print(type('1'))  # <class 'str'>
# print(type([1, 2]))  # <class 'list'>
# # print(help(str))
# # print(help(list))


# # 함수
# def append():
#     pass


# # 함수 호출
# append()


# # # 메서드 호출
# # 리스트.append()
# # 객체.메서드()


# # 문자열 메서드 예시
# print('hello'.capitalize())  # Hello

# # 리스트 메서드 예시
# numbers = [1, 2, 3]
# numbers.append(4)
# print(numbers)  # [1, 2, 3, 4]


# # index
# text = 'banana'
# print(text.index('a'))  # 1

# my_list = [1, 2, 3]
# print(my_list.index(2))  # 1


# # count
# text = 'banana'
# print(text.count('a'))  # 3

# my_list = [1, 2, 2, 3, 3, 3]
# print(my_list.count(3))  # 3


# ################ 문자열 탐색 및 검증 ################

# # find
# text = 'banana'
# print(text.find('a'))  # 1
# print(text.find('z'))  # -1

# # isupper
# string1 = 'HELLO'
# string2 = 'Hello'
# print(string1.isupper())  # True
# print(string2.isupper())  # False

# # islower
# print(string1.islower())  # False
# print(string2.islower())  # False

# # isalpha
# string1 = 'Hello'
# string2 = '123heis98576ssh'
# print(string1.isalpha())  # True
# print(string2.isalpha())  # False


# ################ 문자열 조작 ################

# # replace
# text = 'Hello, world! world world'
# new_text1 = text.replace('world', 'Python')
# new_text2 = text.replace('world', 'Python', 1)
# print(new_text1)  # Hello, Python! Python Python
# print(new_text2)  # Hello, Python! world world

# # strip
# # 사용자 입력 등에서 불필요한 공백이 포함된 경우
# text = '   Hello    World   '

# # 1. 아무것도 지정하지 않으면 '공백(띄어쓰기, 탭, 엔터)'을 제거
# clean_text = text.strip()

# print(clean_text)
# # 결과: 'Hello    World'
# # (주의: 문자열 중간의 공백은 제거되지 않음)


# # 2. 제거할 문자를 지정하는 경우
# text = '!!!Hello World!!!'
# print(text.strip('!'))
# # 결과: 'Hello World'


# # [심화] 문자열 집합으로 제거 (순서 상관 없음)
# # 'w', '.', 'c', 'o', 'm' 중 하나라도 양쪽 끝에 있으면 계속 제거
# url = 'www.example.com'
# print(url.strip('w.com'))
# # 결과: 'example'
# # (왼쪽의 'www.'과 오른쪽의 '.com'이 모두 제거됨)


# # split
# # 1. 공백을 기준으로 분리 (기본 동작)
# # - 여러 개의 공백도 하나로 처리하며, 앞뒤 공백은 무시함
# text = '  Hello    Python  '
# print(text.split())
# # 결과: ['Hello', 'Python’]


# # 2. 특정 문자를 기준으로 분리
# # - 지정한 문자를 기준으로 '엄격하게' 분리함 (빈 문자열 발생 가능)
# data = '10,20,,30'
# print(data.split(','))
# # 결과: ['10', '20', '', '30']


# # 3. 분할 횟수 제한 (maxsplit)
# # - 앞에서부터 1번만 자르고 나머지는 그대로 둠
# path = 'User/admin/documents'
# print(path.split('/', maxsplit=1))
# # 결과: ['User', 'admin/documents']


# # join
# words = ['Python', 'is', 'awesome']

# sentence1 = ' '.join(words)
# sentence2 = "-".join(words)

# print(sentence1)  # Python is awesome
# print(sentence2)  # Python-is-awesome


# # capitalize
# text = 'heLLo, woRld!'
# new_text1 = text.capitalize()
# print(new_text1)  # Hello, world!

# # title
# new_text2 = text.title()
# print(new_text2)  # Hello, World!

# # upper
# new_text3 = text.upper()
# print(new_text3)  # HELLO, WORLD!

# # lower
# new_text4 = text.lower()
# print(new_text4)  # hello, world!

# # swapcase
# new_text5 = text.swapcase()
# print(new_text5)  # HEllO, WOrLD!


# ################ 리스트 값 추가 및 삭제 ################

# # append
# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)  # [1, 2, 3, 4]
# # append는 None을 반환합니다.
# print(my_list.append(4))  # None

# # extend
# my_list = [1, 2, 3]
# my_list.extend([4, 5, 6])
# print(my_list)  # [1, 2, 3, 4, 5, 6]

# # extend와 append의 비교
# my_list.append([5, 6, 7])
# print(my_list)  # [1, 2, 3, 4, 5, 6, [5, 6, 7]]

# # my_list.extend(100)  # TypeError: 'int' object is not iterable

# # insert
# my_list = [1, 2, 3]
# my_list.insert(1, 5)
# print(my_list)  # [1, 5, 2, 3]

# # remove
# my_list = [1, 2, 3, 2, 2, 2]
# my_list.remove(2)
# print(my_list)  # [1, 3, 2, 2, 2]

# # pop
# my_list = [1, 2, 3, 4, 5]
# item1 = my_list.pop()
# item2 = my_list.pop(0)

# print(item1)  # 5
# print(item2)  # 1
# print(my_list)  # [2, 3, 4]

# # clear
# my_list = [1, 2, 3]
# my_list.clear()
# print(my_list)  # []


# ################ 리스트 정렬 및 순서 변경 ################

# # reverse
# my_list = [1, 3, 2, 8, 1, 9]
# my_list.reverse()
# # reverse는 None을 반환합니다.
# # print(my_list.reverse())  # None
# # reverse는 원본 리스트를 변경합니다.
# print(my_list)  # [9, 1, 8, 2, 3, 1]

# # sort
# my_list = [3, 2, 100, 1]
# my_list.sort()
# # sort는 None을 반환합니다.
# # print(my_list.sort())  # None
# # sort는 원본 리스트를 변경합니다.
# print(my_list)  # [1, 2, 3, 100]

# # sort(내림차순 정렬)
# my_list.sort(reverse=True)
# print(my_list)  # [100, 3, 2, 1]


# # 가변(mutable) 객체 예시
# print('가변(mutable) 객체 예시')
# a = [1, 2, 3, 4]
# b = a
# b[0] = 100

# print(f'a의 값: {a}')  # [100, 2, 3, 4]
# print(f'b의 값: {b}')  # [100, 2, 3, 4]
# print(f'a와 b가 같은 객체를 참조하는가? {a is b}')  # True

# # 불변(immutable) 객체 예시
# print('\n불변(immutable) 객체 예시')
# a = 20
# b = a
# b = 10

# print(f'a의 값: {a}')  # 20
# print(f'b의 값: {b}')  # 10
# print(a is b)  # False

# # id() 함수를 사용한 메모리 주소 확인
# print('\n메모리 주소 확인')
# x = [1, 2, 3]
# y = x
# z = [1, 2, 3]

# print(f'x의 id: {id(x)}')
# print(f'y의 id: {id(y)}')
# print(f'z의 id: {id(z)}')
# print(f'x와 y는 같은 객체인가? {x is y}')
# print(f'x와 z는 같은 객체인가? {x is z}')


# # 얕은 복사
# print('\n얕은 복사 예시')

# # 1차원 리스트에서의 얕은 복사 (리스트 슬라이싱)
# a = [1, 2, 3]
# b = a[:]

# print(a)  # [1, 2, 3]
# print(b)  # [1, 2, 3]

# # 1차원 리스트에서의 얕은 복사 (copy 메서드)
# a = [1, 2, 3]
# b = a.copy()

# print(a)  # [1, 2, 3]
# print(b)  # [1, 2, 3]


# # 1차원 리스트에서의 얕은 복사 (list() 함수)
# a = [1, 2, 3]
# d = list(a)
# a[0] = 100
# print(a)  # [100, 2, 3]
# print(d)  # [1, 2, 3]


# # 얕은 복사의 한계
# print('\n다차원 리스트 얕은 복사의 한계')
# a = [1, 2, [3, 4, 5]]
# b = a[:]

# b[0] = 999
# print(a)  # [1, 2, [3, 4, 5]]
# print(b)  # [999, 2, [3, 4, 5]]

# b[2][1] = 100
# print(a)  # [1, 2, [3, 100, 5]]
# print(b)  # [999, 2, [3, 100, 5]]

# print(f'a[2]와 b[2]가 같은 객체인가? {a[2] is b[2]}')  # True


# # 깊은 복사

# print('깊은 복사 예시')
# a = [1, 2, [3, 4, 5]]
# b = copy.deepcopy(a)

# b[2][1] = 100

# print(a)  # [1, 2, [3, 4, 5]]
# print(b)  # [1, 2, [3, 100, 5]]
# print(f'a[2]와 b[2]가 같은 객체인가? {a[2] is b[2]}')  # False

# # 복잡한 중첩 객체 예시
# print('복잡한 중첩 객체 깊은 복사')
# original = {
#     'a': [1, 2, 3],
#     'b': {'c': 4, 'd': [5, 6]},
# }
# copied = copy.deepcopy(original)

# copied['a'][1] = 100
# copied['b']['d'][0] = 500

# print(f'원본: {original}')  # {'a': [1, 2, 3], 'b': {'c': 4, 'd': [5, 6]}}
# print(f'복사본: {copied}')  # {'a': [1, 100, 3], 'b': {'c': 4, 'd': [500, 6]}}
# print(
#     f"original['b']와 copied['b']가 같은 객체인가? {original['b'] is copied['b']}"
# )  # False


# # 사용 전
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = []

# for num in numbers:
#     squared_numbers.append(num**2)

# print(squared_numbers)


# # 사용 후
# squared_numbers2 = [num**2 for num in numbers]
# # squared_numbers2 = list(num**2 for num in numbers)
# print(squared_numbers2)


# # List Comprehension 활용 예시
# # "2차원 배열 생성 시 (인접행렬 생성 시)"
# data1 = [[0] * 5 for _ in range(5)]
# print(data1)
# # 또는
# data2 = [[0 for _ in range(5)] for _ in range(5)]
# print(data2)


# # 리스트를 생성하는 방법 비교

# # 1. loop
# result1 = []
# for i in range(10):
#     result1.append(i)

# # 2. list comprehension
# result2 = [i for i in range(10)]
# # result2 = list(i for i in range(10))

# # 3. map
# result3 = list(map(lambda i: i, range(10)))

# print(result1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(result2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(result3)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# # 문자열 메서드 체이닝
# text = 'heLLo, woRld!'
# new_text = text.swapcase().replace('l', 'z')
# print(new_text)  # HEzzO, WOrLD!


# # 1. 단계별로 실행하기
# text = 'heLLo, woRld!'
# step1 = text.swapcase()
# print('1단계 결과:', step1)  # HEllO, WOrLD!

# step2 = step1.replace('l', 'z')
# print('2단계 결과:', step2)  # HEzzO, WOrLD!

# # 2. 한 줄로 실행하기 (위와 동일한 결과)
# new_text = text.swapcase().replace('l', 'z')
# print('최종 결과:', new_text)  # HEzzO, WOrLD!


# # 리스트 메서드 체이닝

# # 1. 리스트 메서드 체이닝의 흔한 실수
# numbers = [3, 1, 4, 1, 5, 9, 2]

# # [실수 1] sort()는 None을 반환하므로, 변수에 아무것도 저장되지 않음
# result = numbers.copy().sort()
# print(result)  # None (정렬된 리스트를 기대했으나 None 출력)

# # # [실수 2] append()가 반환한 None 뒤에 메서드를 이을 수 없음
# # numbers.append(7).extend(
# #     [8, 9]
# # )  # AttributeError: 'NoneType' object has no attribute 'extend'


# # 2. 올바른 해결책 (Good Cases)
# numbers = [3, 1, 4, 1, 5, 9, 2]

# # [해결 1] 내장 함수 sorted() 사용 (추천)
# # sorted()는 정렬된 '새로운 리스트'를 반환하므로 변수에 할당 가능
# # (원본을 건드리지 않으므로 copy()를 굳이 쓸 필요 없음)
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 9]

# # [해결 2] 메서드를 단계별로 나누어 작성
# # 체이닝을 포기하고, 명확하게 한 줄씩 실행
# copied_list = numbers.copy()
# copied_list.sort()
# print(copied_list)  # [1, 1, 2, 3, 4, 5, 9]


# ################ 문자 유형 판별 메서드 ################


# # isdecimal() : 가장 엄격한 기준을 적용, 오직 일반적인 십진수 숫자(0-9)만 True로 인식
# print('isdecimal() 메서드 예시:')
# print('"12345".isdecimal():', '12345'.isdecimal())
# print('"123.45".isdecimal():', '123.45'.isdecimal())
# print('"-123".isdecimal():', '-123'.isdecimal())
# print('"Ⅳ".isdecimal():', 'Ⅳ'.isdecimal())
# print('"½".isdecimal():', '½'.isdecimal())
# print('"²".isdecimal():', '²'.isdecimal())
# print()

# # isdigit() : 일반 숫자뿐만 아니라 지수 표현(²)도 True로 인식
# print('isdigit() 메서드 예시:')
# print('"12345".isdigit():', '12345'.isdigit())
# print('"123.45".isdigit():', '123.45'.isdigit())
# print('"-123".isdigit():', '-123'.isdigit())
# print('"Ⅳ".isdigit():', 'Ⅳ'.isdigit())
# print('"½".isdigit():', '½'.isdigit())
# print('"²".isdigit():', '²'.isdigit())
# print()

# # isnumeric() : 일반 숫자, 로마 숫자, 분수, 지수 등 다양한 형태의 숫자 표현을 True로 인식
# print('isnumeric() 메서드 예시:')
# print('"12345".isnumeric():', '12345'.isnumeric())
# print('"123.45".isnumeric():', '123.45'.isnumeric())
# print('"-123".isnumeric():', '-123'.isnumeric())
# print('"Ⅳ".isnumeric():', 'Ⅳ'.isnumeric())
# print('"½".isnumeric():', '½'.isnumeric())
# print('"²".isnumeric():', '²'.isnumeric())


# st = 'apple, banana, mango'
# ind = st.find('z')
# print(ind)


# print(st.isupper())
# print(st.islower())
# print(st.isalpha())

# st = ['apple', 'banana', 'mango']
# st2 = ','.join(st)
# print(st2)


# st = 'apple, banana, mango'
# st3 = st.upper()
# print(st3)


# st = 'apple'
# st4 = ''.join(reversed(st))
# print(st4)


# st = ['apple', 'banana', 'mango']
# st.append('orange')
# print(st)

# st.insert(2, 'watermelon')
# print(st)


# a = st.index('banana')
# print(a)


# st_1 = [1, 2, 3]
# st_2 = [4, 5]
# st_1.extend(st_2)
# print(st_1)


# print(st_1.pop())
# print(st_1)

# g = st_1.pop(2)
# print(st_1)
# print(g)


# del st_1[1:]
# print(st_1)

# st.clear()
# print(st)


# st = [1, 2, 3, 4, 5]
# st.reverse()
# print(st)


# a1 = [6, 3, 9]
# print(a1)
# a1.sort()
# print(a1)


# a1 = [6, 3, 9]
# a2 = sorted(a1)
# print(a2)


# a1.sort(reverse=True)
# print(a1)


# a3 = [4, 7, 1, 3, 2]
# a4 = sorted(a3)
# a5 = sorted(a3, reverse=True)
# print(a4)
# print(a5)


# st1 = 'sfgq'
# st1_list = sorted(st1)
# print(st1_list)
# print(''.join(st1_list))


# lst = list(range(1, 11))
# print(sorted(lst, reverse=True))

# ret = sorted(lst, key=lambda x: -x)
# print(ret)


lst = [(3, 'banana'), (2, 'apple'), (1, 'carrot')]

ret = sorted(lst, key=lambda lst: lst[1], reverse=True)

print(ret)
