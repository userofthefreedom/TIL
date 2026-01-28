
### 절차지향과 객체지향 ###
# # OOP 객체지향 프로그래밍 (Object Orient Programming)
# 클래스란 틀이다
# 틀 안의 변수는 - 속성 (attribute)
# 틀 안의 함수 - 메소드 (method)
# 틀로 찍어낸 객체 - 인스턴스
# > 절차 지향보다 확장성, 재활용성이 높고 유지보수가 편하다 but 데이터 처리 속도가 느리다는 단점

# 예: 사람(객체) 안에 name, age와 이와 관련된 기능(메서드) 포함
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'안녕하세요, {self.name}입니다. 나이는 {self.age}살입니다.')


alice = Person('Alice', 25)
print(type(alice))
alice.introduce()  # 객체가 자신의 정보를 출력

# 절차 지향 프로그래밍  - c 언어를 통한 개발
# 예: 변수와 함수를 별개로 다룸
name = 'Alice'
age = 25


def introduce(name, age):
    print(f'안녕하세요, {name}입니다. 나이는 {age}살입니다.')


introduce(name, age)


### 객체와 클래스, 그리고 인스턴스 ###
# 클래스 : 관련한 데이터(속성, attribute)와 기능(method)을 하나의 묶음으로 정의하는 설계도

class Person:  # 파스칼 케이스 방식으로 클래스 이름을 작성
    def __init__(self, name, age):
        '''
        __init__method 는 생성자 method라 불리며 객체를 위해 필요한 초기값을 설정한다
        __ ?? __ method 는 매직 method로, python에서 호출 시점을 결정한다
        '''
        self.name = name  # 인스턴스 속성
        self.age = age  # 인스턴스 속성

    def introduce(self):
        print(f'안녕하세요. 저는 {self.name}, 나이는 {self.age}살입니다.')


# 인스턴스 : 클래스를 통해 생성된 객체, 서로 독립된 데이터를 가진다
p1 = Person('Alice', 25)
p1.introduce()  # "안녕하세요. 저는 Alice, 나이는 25살입니다."

p2 = Person('Bella', 30)
p2.introduce()  # "안녕하세요. 저는 Bella, 나이는 30살입니다."


class Singer:
    pass


iu = Singer()
bts = Singer()
print(type(iu))
print(type(bts))
# iu와 bts는 Singer 클래스의 인스턴스
name = 'alice'
print(type(name))
data = [1, 2, 3]
data.append(4)
print(type(data))
# 문자열 변수 name은 str 클래스의 인스턴스이다.
# 리스트형 데이터 data에 append()를 사용할 수 있는 이유는 클래스 list에 정의되어 있기 때문


### 클래스 구성 요소 ###
class Circle:
    pi = 3.14  # class 변수, 속성

    # 생성자 메서드, init 매직 method, 생성자 함수 (constructor)
    def __init__(self, radius):
        self.radius = radius  # 인스턴스 변수, 속성


# 인스턴스 생성
c1 = Circle(1)
c2 = Circle(2)

# 인스턴스 변수(속성) 접근
print(c1.radius)  # 1
print(c2.radius)  # 2

# 인스턴스 c1의 인스턴스 변수 pi를 생성
c1.pi = 100

# 인스턴스 c1의 인스턴스 변수 pi를 출력
print(c1.pi)  # 100

# 클래스 변수 접근
print(Circle.pi)  # 3.14

# 반면 인스턴스 c2는 인스턴스 변수 pi가 없으므로 클래스 변수 pi를 참조
print(c2.pi)  # 3.14

# 클래스 변수를 인스턴스로 접근하면 안된다


class Calculator():
    numberofCalCul = 0

    def __init__(self):
        self.result = 0

    def getsum(self, value):
        self.result += value
        return self.result


cal1 = Calculator()
cal2 = Calculator()

Calculator.numberofCalCul = 4
print(cal1.numberofCalCul)
print(cal2.numberofCalCul)


cal1.numberofCalCul = 10
print(cal1.numberofCalCul)
print(cal2.numberofCalCul)

# 인스턴스의 삭제는 del을 통해 진행한다


### 클래스와 method, 그 종류 ###
# # 인스턴스 method : 인스턴스의 상태를 조작하거나 동작을 수행
class Counter:
    def __init__(self):  # 모든 인스턴스 method 는 반드시 첫번째 인자로 인스턴스 자신(self)을 받는다
        self.count = 0
    # 인스턴스 메서드

    def increment(self):
        self.count += 1


c = Counter()
# 왜 첫 인자는 인스턴스 자신인가?
# 'hello'.upper() 는 파이썬 내부에서 실제로 str.upper('hello') 이다.

# 인스턴스 메서드 호출
c.increment()
print(c.count)  # 1


# # 생성자 method : 인스턴스 객체가 생성될때 자동으로 호출되어 인스턴스 변수들의 초기값을 설정
class Person:
    def __init__(self, name):
        # 왼쪽 name : 인스턴스 변수 name
        # 오른쪽 name : 생성자 메서드의 매개변수 이름
        self.name = name
        print("인스턴스가 생성되었습니다.")

    def greeting(self):
        print(f'안녕하세요 {self.name}입니다.')


person1 = Person('지민')  # 인스턴스가 생성되었습니다.
person1.greeting()  # 안녕하세요. 지민입니다.
# Person.greeting(person1) 와 위 코드는 동일하다


# # 클래스 method : 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행
class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        # 클래스 메서드를 통해 인스턴스가 생성될 때마다 인구 수 증가
        Person.increase_population()

    @classmethod  # 클래스 method로 데코레이터를 통해 전환
    def increase_population(cls):  # 첫 인자로 cls를 쓰는 것이 관례
        cls.population += 1


# 인스턴스 생성
person1 = Person('Alice')
person2 = Person('Bob')

# 클래스 변수 접근
print(Person.population)  # 2


# # 스태택 (정적) method : 클래스, 인스턴스와 상관없이 독립적으로 동작하는 method
class MathUtils:
    @staticmethod  # 데코레이터를 통해 전환
    def add(a, b):  # 정적 method 이기에 self, cls가 필요 없다
        return a + b


# 정적 메서드 호출
print(MathUtils.add(3, 5))  # 8


# # 메서드 활용
# 입출금이 가능한 은행 계좌 클래스 만들기
# 은행 계좌를 모델링하는 클래스를 만들고, 입출금 기능(메서드)를 구현


class BankAccount:
    interest_rate = 0.02  # 이자율

    def __init__(self, owner, balance=0):
        self.owner = owner  # 계좌 소유자
        self.balance = balance  # 초기 잔액

    # 입금
    def deposit(self, amount):
        self.balance += amount

    # 출금
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('잔액 부족!')

    # 이자율 설정
    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate

    # 금액이 양수인지 검증
    @staticmethod
    def is_positive(amount):
        return amount > 0


# 계좌 개설 (인스턴스 생성)
alice_acc = BankAccount('Alice', 1000)

# 입금 및 출금 (인스턴스 메서드 호출)
alice_acc.deposit(500)
alice_acc.withdraw(200)

# 잔액 확인 (인스턴스 변수 참조)
print(alice_acc.balance)  # 1300

# 이자율 변경 (클래스 메서드 호출)
BankAccount.set_interest_rate(0.03)
print(BankAccount.interest_rate)  # 0.03

# 잔액이 양수인지 확인 (정적 메서드 호출)
print(BankAccount.is_positive(alice_acc.balance))  # True


### method 심화 ###
# 클래스는 클래스 method와 스태틱 method를
# 인스턴스는 인스턴스 method를 사용하는 것이 좋다
class MyClass:
    def instance_method(self):
        return 'instance method', self

    @classmethod
    def class_method(cls):
        return 'class method', cls

    @staticmethod
    def static_method():
        return 'static method'


instance = MyClass()
# 클래스가 할 수 있는 것
# 사실 클래스는 모든 메서드를 호출할 수 있음
print(MyClass.instance_method(instance))
print(MyClass.class_method())
print(MyClass.static_method())


# 인스턴스가 할 수 있는 것
# 사실 인스턴스는 모든 메서드를 호출할 수 있음
print(instance.instance_method())
print(instance.class_method())
print(instance.static_method())


# 기술적인 '가능 여부(Can)'와 논리적인 '사용 의도(Should)'를 구분해야 함
# 1. 클래스의 입장
# - 클래스 메서드와 정적 메서드를 호출하는 것이 주된 역할입니다.
print(MyClass.class_method())
print(MyClass.static_method())

# 2. 인스턴스의 입장
# - 인스턴스 메서드는 오직 인스턴스만 호출하는 것이 좋습니다.
print(instance.instance_method())


### 매직 method ###
class Circle:
    def __init__(self, radius):
        self.radius = radius

    # __str__ 메서드 정의
    # 인스턴스를 문자열로 표현할 때 호출됨
    # print(c1) 호출 시 사용됨
    # 이 메서드를 정의하면 인스턴스를 print()로 출력할 때 더 읽기 쉬운 형식으로 출력됨
    # __str__ 메서드는 문자열을 반환해야 함
    def __str__(self):
        return f'원의 반지름: {self.radius}'


c1 = Circle(10)
c2 = Circle(1)

print(c1)  # 원의 반지름: 10
print(c2)  # 원의 반지름: 1


class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        result = self.price + other.price
        return result


kia = Car('k8', 300)
bmw = Car('m5', 500)
print(kia + bmw)  # 800


### 클래스와 인스턴스 간 이름 공간 ###
# 독립적인 이름 공간을 가지는 이유 : 클래스와 인스턴스를 모듈화 하고 각각 객체가 독립적으로 동작하도록 보장
class Person:
    name = 'unknown'

    def talk(self):
        print(self.name)


# p1 인스턴스 생성
p1 = Person()
p1.talk()  # unknown

# p2 인스턴스 생성 (인스턴스 변수 설정 전)
p2 = Person()
p2.talk()  # unknown

# p2 인스턴스 변수 설정 후
p2.name = 'Kim'
p2.talk()  # Kim

# 클래스 변수 name 값이 변경된 것이 아님(클래스 변수 name은 여전히 'unknown')
print(Person.name)  # unknown
# p2의 name은 인스턴스 변수로 설정된 값
print(p2.name)  # Kim
# 인스턴스는 독립적이므로 p1의 name은 여전히 'unknown'
print(p1.name)  # unknown


### 데코레이터 ###
# 다른 함수 코드를 유지한 채로 수정하거나 확장하기 위해 사용되는 함수
