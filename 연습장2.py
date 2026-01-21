# 함수 정의
def make_sum(x, y):
    """
    이것은 두 수를 파라미터로 받아 두 수의 합을 반환하는 함수
    >>> make_sum(1,2)
    3
    """
    result = x+y
    return result
# 함수 호출 및 반환 값 할당

print(make_sum(100,300))

# [번외] print() 함수는 반환값이 없다.

resu = print(100)
print(resu)


# 1. Positional Arguments
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')


greet('Alice', 25)  # 안녕하세요, Alice님! 25살이시군요.
greet(25, 'Alice')  # 안녕하세요, 25님! Alice살이시군요.
# greet('Alice')  # TypeError: greet() missing 1 required positional argument: 'age'


######################################################################## 


# 2. Default Argument Values
def greet(name, age=20):
    print(f'안녕하세요, {name}님! {age}살이시군요.')


greet('Bob')  # 안녕하세요, Bob님! 30살이시군요.
greet('Charlie', 40)  # 안녕하세요, Charlie님! 40살이시군요.


######################################################################## 


# 3. Keyword Arguments
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')


greet(name='Dave', age=35)  # 안녕하세요, Dave님! 35살이시군요.
greet(age=35, name='Dave')  # 안녕하세요, Dave님! 35살이시군요.
# greet(age=35, 'Dave')  # Positional argument cannot appear after keyword arguments


######################################################################## 


# 4. Arbitrary Argument Lists
def calculate_sum(*args):
    print(args)  # (1, 100, 5000, 30)
    print(type(args))  # <class 'tuple'>


calculate_sum(1, 100, 5000, 30)


######################################################################## 


# 5. Arbitrary Keyword Argument Lists
def print_info(**kwargs):
    print(kwargs)


print_info(name='Eve', age=30)  # {'name': 'Eve', 'age': 30}


######################################################################## 


# 인자의 모든 종류를 적용한 예시
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)
    print('pos2:', pos2)
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwargs)


func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')
"""
pos1: 1
pos2: 2
default_arg: 3
args: (4, 5, 6)
kwargs: {'key1': 'value1', 'key2': 'value2'}
"""








def factorial(n):
    # 종료 조건: n이 0이면 1을 반환
    if n == 0:
        return 1
    else:
        # 재귀 호출: n과 n-1의 팩토리얼을 곱한 결과를 반환
        return n * factorial(n - 1)


# 팩토리얼 계산 예시
print(factorial(5))  # 120







numbers = [1, 2, 3, 4, 5]

print(numbers)  # [1, 2, 3, 4, 5]
print(len(numbers))  # 5
print(max(numbers))  # 5
print(min(numbers))  # 1
print(sum(numbers))  # 15
print(sorted(numbers, reverse=True))  # [5, 4, 3, 2, 1]







# Scope 예시
def func():
    num = 20
    print('local', num)  # local 20


func()

# >print('global', num)  # NameError: name 'num' is not defined


# 내장 함수 sum의 이름을 사용해버려서 오류가 발생하는 예시
print(sum)  # <built-in function sum>
print(sum(range(3)))  # 3
sum = 5
print(sum)  # 5
# >print(sum(range(3)))  # TypeError: 'int' object is not callable


# LEGB Rule 퀴즈
x = 'G'
y = 'G'


def outer_func():
    x = 'E'
    y = 'E'

    def inner_func(y):
        z = 'L'
        print(x, y, z)  # ??

    inner_func('P')
    print(x, y)  # ??


outer_func()
print(x, y)  # ??








num = 0  # 전역 변수


def increment():
    global num  # num를 전역 변수로 선언
    num += 1


print(num)  # 0

increment()

print(num)  # 1


# ‘global’ 키워드 주의사항 1 - global 키워드 선언 전에는 참조불가
num = 0


# def increment():
#     # SyntaxError: name 'num' is used prior to global declaration
#     print(num)
#     global num
#     num += 1


# ‘global’ 키워드 주의사항 2 - 매개변수에는 global 키워드 사용불가
num = 0


# def increment(num):
#     # SyntaxError: name 'num' is parameter and global
#     global num
#     num += 1







# Good
def calculate_total_price(price, tax):
    return price + (price * tax)


# Bad
def calc_price(p, t):
    return p + (p * t)


# # 잘못된 설계 예시 (여러 책임이 섞인 함수)
# def process_user_data(user_data):
#     # 책임 1: 데이터 유효성 검사
#     if len(user_data['password']) < 8:
#         raise ValueError('비밀번호는 8자 이상이어야 합니다')

#     # 책임 2: 비밀번호 암호화 및 저장
#     user_data['password'] = hash_password(user_data['password'])
#     db.users.insert(user_data)

#     # 책임 3: 이메일 발송
#     send_email(user_data['email'], '가입을 환영합니다!')


# # 올바른 설계 예시 (책임을 분리한 함수들)
# def validate_password(password):
#     """비밀번호 유효성 검사"""
#     if len(password) < 8:
#         raise ValueError('비밀번호는 8자 이상이어야 합니다')


# def save_user(user_data):
#     """비밀번호 암호화 및 저장"""
#     user_data['password'] = hash_password(user_data['password'])
#     db.users.insert(user_data)


# def send_welcome_email(email):
#     """환영 이메일 발송"""
#     send_email(email, '가입을 환영합니다!')


# # 메인 함수에서 순차적으로 실행
# def process_user_data(user_data):
#     validate_password(user_data['password'])
#     save_user(user_data)
#     send_welcome_email(user_data['email'])










packed_values = 1, 2, 3, 4, 5
print(packed_values)  # (1, 2, 3, 4, 5)


# ‘*’ 을 활용한 패킹 (함수 매개변수 작성 시)
def my_func(*args):
    print(args)  # (1, 2, 3, 4, 5)
    print(type(args))  # <class 'tuple'>


my_func(1, 2, 3, 4, 5)


# ‘**’ 을 활용한 패킹 (함수 매개변수 작성 시)
def my_func2(**kwargs):
    print(kwargs)  # {'a': 1, 'b': 2, 'c': 3}
    print(type(kwargs))  # <class 'dict’>


my_func2(a=1, b=2, c=3)




packed_values = 1, 2, 3, 4, 5

# 언패킹
a, b, c, d, e = packed_values
print(a, b, c, d, e)  # 1 2 3 4 5


# ‘*’ 을 활용한 언패킹 (함수 인자 전달)
def my_function(x, y, z):
    print(x, y, z)


names = ['alice', 'jane', 'peter']
my_function(*names)  # alice jane peter


# ‘**’을 활용한 언패킹 (딕셔너리 -> 함수 키워드 인자)
def my_function(x, y, z):
    print(x, y, z)


my_dict = {'x': 1, 'y': 2, 'z': 3}
my_function(**my_dict)  # 1 2 3













# 람다 표현식 적용 전
def addition(x, y):
    return x + y


# 람다 표현식 적용 후


"""
람다 표현식 활용 (with sorted 함수)
sorted() 함수는 리스트를 정렬해주며, key라는 매개변수에 함수를 전달하여 
"무엇을 기준으로 정렬할지"를 지정할 수 있습니다. 
이때 간단한 기준을 제시하기 위해 lambda를 사용하는 것이 매우 효과적입니다.

예시: 학생들의 점수를 나이순으로 정렬하기
학생 데이터가 (이름, 나이) 형태의 튜플로 묶여있는 리스트가 있다고 가정해 봅시다

# 목표: 학생들을 '나이'가 어린 순서대로 정렬하고 싶다!
"""
# 학생 데이터가 (이름, 나이) 형태의 튜플로 묶여있는 리스트
students = [('지민', 25), ('서준', 20), ('민우', 30)]


# 1. lambda 미사용
# 정렬 기준 함수를 굳이 정의해야 함
def get_age(student):
    return student[1]


# sorted 함수의 key 매개변수에 우리가 만든 get_age 함수를 전달
result = sorted(students, key=get_age)
print(result)  # [('서준', 20), ('지민', 25), ('민우', 30)]


# 2. lambda 사용
"""
get_age처럼 간단하고 한 번만 쓸 함수를 굳이 따로 정의할 필요 없이, lambda로 즉석에서 만들어 전달할 수 있습니다.
key=lambda student: student[1]
-> "정렬할 때 각 데이터를 student라고 부를게."
-> "그리고 그 데이터의 1번 인덱스 값(나이)을 기준으로 삼아줘."
"""
result = sorted(students, key=lambda student: student[1])
print(result)  # [('서준', 20), ('지민', 25), ('민우', 30)]















# 함수

def kfc():
    abc()
    print("!")

def abc():
    print("치킨")

kfc() # 정의된 후에 호출했기에, abc() 정의 전에 kfc() 선언해도 된다
print("#") # 함수가 끝난 후에는 호출한 곳으로 돌아간다




def getsum(a,b,k=8):  #parameter 매개변수
    return a+b, k  # 2개 이상 return일 경우 튜플로 묶어 리턴
    print("22") #return은 함수를 종료시킨다

ret = getsum(3, 7) #arguments 인자값
print(ret)



#PACKING
num = [1,2,3,4,5]
num_2 = (1,2,3,4,5)

#unpacking (*이용 가능)
a,b,c,d,e = num
f,g,*h = num_2
print(a,b,c,d,e)
print(f,g,h)
a,*b,c,d = num
print(a,b,c,d)



def getsum(*a): #가변인자
    print(type(a))
    return a[0]+a[1]+a[2]

ret = getsum(1,2,3)
print(ret)


def print_info(**test): #키워드가변인자
    print(test)

print_info(kevin=1,bob=2,kate=3)





#함수에서 사용하는 변수 > 지역변수, 전역변수
aa = 1
def abc():
    aa=3
    bb=5
    print(aa,bb)
abc()
print(aa) # 함수가 종료되면 지역 변수는 사라진다, 때문에 위에서 선언하지 않으면 버그



aa = 7
bb = 6
def abc():
    global aa, bb #여부에따라 지역변수가 되느냐 전역변수가 되느냐 차이
    print(aa,bb)
    aa = 3
    bb = 5
    print(aa,bb)

abc()
print(aa,bb)





def kef():
    print(aa,bb)
    # aa += 1
    # bb += 1
    # print(aa,bb) #앞에 글로벌이 있다면 가능하다
def test():
    global aa,bb
    aa = 3
    bb = 5
    print(aa,bb)

test()
kef() #다른 함수에서 글로벌 함수를 출력만 한다면 그것은 가능






# 내장함수
## map
num = ["1","2","3"]
lst = []
for i in num:
    lst.append(int(i))
print(lst)
list2=map(int,num)
print(list2)
print(list(list2))

## zip
a = '12345'
b = 'qwert'
c = 'ㄱㄴㄷㄹㅁ'
ret = zip (a,b)
print(ret)
print(list(ret))
for i in zip(a,b,c):
    print(list(i)) # 리스트로 출력
for x,y,z in zip(a,b,c):
    print(x,y,z) #값만 출력


arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
for i in zip(arr[0],arr[1],arr[2]):
    print(list(i))
for i in zip(*arr):
    print(list(i))

ret=list(map(list,zip(*arr)))
print(ret)


## filter

num  = list(range(1,8))
def get_even(value):
    if value%2==0:
        return True
    else:
        return False
    # return True if value%2==0 else False <컴프리핸션

ret = filter(get_even, num) # 겟 이븐 안에 num을 넣어 참인 값만 걸러주는 것
print(list(ret))


## lambda 익명함수

def sum(a,b):
    return a+b
ret = sum(4,6)
print(ret)

ret = (lambda a,b:a+b)(3,9)
print(ret)

ret = (lambda a,b:a+b)
print(ret(10,11))

lst1 = list(range(1,5))
lst2 = list(range(3,7))

ret = (lambda r,t:r+t)
lst3 = list(map(ret,lst1,lst2))
print(lst3)

lst3 = list(map(lambda c,d:c+d,lst1,lst2))
print(lst3)




## 재귀

for i in range(1, 11):
    print(i, end=" ")
for i in range(10,0,-1):
    print(i, end=" ")

print("")

def abc(level):
    if level==11:
        return
    print(level,end=" ")
    abc(level+1)
    print(level,end=" ")

abc(0)
print("")



n = int(input())
path = [0]*n

def abc(level):
    if level == n:
        print(*path)
        return
    for i in range(6):
        path[level] = i+1
        abc(level+1)
        path[level] = 0

abc(0)