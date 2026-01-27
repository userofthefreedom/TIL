
from collections import defaultdict
### 딕셔너리 method ###
# get
person = {'name': 'Alice', 'age': 25}
print(person.get('name'))
print(person.get('count'))
print(person.get('count', 'nothing'))
# print(person['country'])  # KeyError: 'country'

# keys
person = {'name': 'Alice', 'age': 25}
print(person.keys())  # dict_keys(['name', 'age'])
for item in person.keys():
    print(item)

# values
person = {'name': 'Alice', 'age': 25}
print(person.values())  # dict_values(['Alice', 25])
for item in person.values():
    print(item)

# items
person = {'name': 'Alice', 'age': 25}
print(person.items())  # dict_items([('name', 'Alice'), ('age', 25)])
for key, value in person.items():
    print(key, value)

# pop -> 반환값이 존재한다
person = {'name': 'Alice', 'age': 25}
print(person.pop('age'))  # 25
print(person)  # {'name': 'Alice'}
print(person.pop('country', None))  # None -> 디폴트값을 통해 버그를 막는다
# print(person.pop('country'))  # KeyError: 'country'

# clear
person = {'name': 'Alice', 'age': 25}
person.clear()
print(person)

# setdefault : get의 기본 조회 기능에 추가 기능을 더함 (단 원본 데이터를 보존 한다)
person = {'name': 'Alice', 'age': 25}
print(person.setdefault('country', 'KOREA'))  # KOREA
print(person)  # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}

# update
person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'country': 'KOREA'}
person.update(other_person)
print(person)  # {'name': 'Jane', 'age': 25, 'country': 'KOREA'}
person.update(age=100, address='SEOUL')
# {'name': 'Jane', 'age': 100, 'country': 'KOREA', 'address': 'SEOUL'}
print(person)

# del (없는 키 사용시 에러)
person = {'name': 'Alice', 'age': 25}
del person['age']
print(person)  # {'name': 'Alice'}


### set method ###
# add
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.add(4)
print(my_set)
my_set.add(4)
print(my_set)


# update
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.update([1, 4, 5])
print(my_set)  # {'c', 2, 3, 1, 'b', 4, 5, 'a'}

# clear
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.clear()
print(my_set)  # set()

# remove
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.remove(2)
print(my_set)
# my_set.remove(10)  # KeyError: 10

# pop
my_set = {'a', 'b', 'c', 1, 2, 3}
element = my_set.pop()
print(element)
print(my_set)

# discard
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.discard(2)
print(my_set)
my_set.discard(10)

# 집합 연산 메서드
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set1.difference(set2))  # {0, 2, 4} -
print(set1.intersection(set2))  # {1, 3} &
print(set1.issubset(set2))  # False <=
print(set3.issubset(set1))  # True <=
print(set1.issuperset(set2))  # False >=
print(set1.union(set2))  # {0, 1, 2, 3, 4, 5, 7, 9} |

### 딕셔너리 심화 ###
# defaultdic
# 기존: 기본 딕셔너리
text = 'banana'
counts = {}
for char in text:
    if char not in counts:  # 키가 있는지 매번 확인해야 함
        counts[char] = 0
    counts[char] += 1
print(counts)  # {'b': 3, 'a': 3, 'n': 2}

# 개선: defaultdict 활용
text = 'banana'
counts = defaultdict(int)  # 기본값을 정수(0)로 설정
for char in text:
    # 키 확인 불필요! 없으면 0으로 자동 생성 후 +1
    counts[char] += 1
print(counts)  # defaultdict(<class 'int'>, {'b': 1, 'a': 3, 'n': 2})

# # 활용 예제
# 색상별 과일 분류
fruits = [('red', 'apple'), ('yellow', 'banana'), ('red', 'cherry')]
fruit_by_color = defaultdict(list)

for color, fruit in fruits:
    # color 키가 없으면 빈 리스트 생성 -> append 바로 가능
    fruit_by_color[color].append(fruit)

print(
    fruit_by_color
)  # defaultdict(<class 'list'>, {'red': ['apple', 'cherry'], 'yellow': ['banana']})
print(
    dict(fruit_by_color)
)  # {'red': ['apple', 'cherry'], 'yellow': ['banana']}


### 해시 테이블 ###

# 해시 : 임의의 크기를 가진 데이터를 고정된 크기의 고유한 값으로 변환하는 것
# 해시 함수가 고정 길이(정수) 함수로 변환 해준다 -> 이 정수가 해시 값
# 정수
my_set = {3, 2, 1, 9, 100, 4, 87, 39, 10, 52}
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set)

# 문자열
my_str_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
print(my_str_set.pop())
print(my_str_set.pop())
print(my_str_set.pop())
print(my_str_set.pop())
print(my_str_set.pop())

print(hash(1))
print(hash(1))
print(hash('a'))
print(hash('a'))

print(hash(1))
print(hash(1.0))
print(hash('1'))
print(hash((1, 2, 3)))

# TypeError: unhashable type: 'list'
# print(hash((1, 2, [3, 4])))

# TypeError: unhashable type: 'list'
# print(hash([1, 2, 3]))
# TypeError: unhashable type: 'list'
# my_set = {[1, 2, 3], 1, 2, 3, 4, 5}
# TypeError: unhashable type: 'set'
# my_dict = {{3, 2}: 'a'}
