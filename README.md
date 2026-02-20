## 목차
- [Python Study Notes](#python-study-notes)
  - [Basic](#basic)
  - [변수와 자료형](#변수와-자료형)
  - [함수(Function)](#함수function)
  - [모듈](#모듈)
  - [제어문](#제어문)
  - [method](#method)
  - [클래스](#클래스)
  - [상속 (Inheritance)](#상속-inheritance)
  - [에러(Error)와 예외(Exception) 처리](#에러error와-예외exception-처리)
  - [Python으로 “클라이언트 → 서버 요청” 정리 (requests 중심)](#python으로-클라이언트--서버-요청-정리-requests-중심)
- [CLI 기본 명령어](#cli-기본-명령어)
- [Git 활용법 정리 (기능 + 예시)](#git-활용법-정리-기능--예시)
- [Markdown / README 작성법 정리](#markdown--readme-작성법-정리)
- [알고리즘(Algorithm) 기초](#알고리즘algorithm-기초)
  - [개념](#개념)
  - [시간 복잡도](#시간-복잡도)
  - [부분집합 (Subsets)](#부분집합-subsets)
  - [배열(Array)](#배열array)
  - [정렬(Sorting)](#정렬sorting)
  - [검색](#검색)
  - [Stack (스택)](#stack-스택)
  - [재귀 호출 (Recursion)](#재귀-호출-recursion)
  - [알고리즘 설계 전략](#알고리즘-설계-전략)
- [라이브러리](#라이브러리)
  - [collections](#collections)
  - [itertools](#itertools)
  - [pathlib (Path)](#pathlib-path)
  - [datetime](#datetime)
  - [random](#random)
  - [logging](#logging)
  - [Numpy](#numpy)
  - [Pandas](#pandas)
  - [Matplotlib](#matplotlib)

# Python Study Notes

## 핵심
- **값/타입/변수(객체)** → 데이터를 만든다
- **연산자/표현식/문장** → 데이터를 계산한다
- **제어문(if/for/while)** → 흐름을 만든다
- **함수/모듈** → 코드를 재사용한다
- **클래스/상속** → 데이터+기능을 묶어 큰 프로그램 구조를 만든다
- **예외처리** → 예상치 못한 상황에서도 프로그램이 멈추지 않게 한다


## Basic
- 실행과정
  - 컴퓨터는 기계어로 소통하지만 인간이 직접 기계어를 사용하긴 어렵다
  - 때문에 인터프리터를 통해 명령어를 운영체제가 이해하는 언어로 번역
- 인터프리터
  - 소스코드를 한줄씩 읽고 즉시 실행하는 프로그램
  - 오류 시 즉시 중단
  - python, JS의 방식 (C, C++의 경우 전체 변환 후 실행하는 컴파일러 사용)
- 표현식 : 하나의 값으로 평가될 수 있는 모든 코드 
  ```python
  3+5
  x>10
  5*4
  ```
- 값 : 표현식이 평가된 결과, 더 이상 계산/평가될 수 없는 프로그램 가장 기본 데이터 조각
  ```python
  13.14
  "안녕하세요"
  True, False
  ```
  - 모든 값은 그 자체로 가장 단순한 표현식
- 변수 : 값을 나중에 활용하기 위해 값에 붙이는 고유한 이름
  - 변수 할당 : 표현식이 만들어 낸 값이 이름을 붙이는 것
  ```python
  num = 36.5
  ```
    - num : 변수 이름
    - = : 할당 연산자
    - 36.5 : 표현식
  - 변수명 규칙
    - 영문,언더스코어(_),숫자로 구성 / 숫자로 시작 불가 / 대소문자 구분 / 예약어 사용 불가
- 객체
  - 객체란 값 + 타입 + 주소 정보(고유id)를 묶은 것
    - 변수는 특정 객체를 가리키는 이름표
  - 재할당 : 변수가 가리키는 대상을 새로운 값으로 변경하는 행위
    ```python
    number = 10
    double = 2 * number
    print(double)  # 20

    number = 5
    print(double)  # 20
    ```
    - 즉, 객체란 실제 사람 / 메모리 주소는 사람이 사는 주소 / 변수는 사람의 주소록 상 이름표
  - 가변 객체와 불변 객체
    - 정의
      - **가변 객체(mutable)**: 객체의 값이 변경될 수 있는 객체
        - 예: list, dict, set
      - **불변 객체(immutable)**: 객체 생성 후 값이 변경되지 않는 객체
        - 예: int, float, str, tuple, range
    - 이론
      - 가변 객체는 같은 객체를 여러 변수가 참조하면, 한 쪽의 변경이 모두에게 영향을 준다.
      - 불변 객체는 값이 바뀌는 것처럼 보여도 **새로운 객체가 생성**된다.
    - 예시 코드
    ```python
    # 가변 객체
    a = [1, 2, 3]
    b = a
    b[0] = 100
    print(a)  # [100, 2, 3]
    print(a is b)  # True

    # 불변 객체
    a = 20
    b = a
    b = 10
    print(a)  # 20
    print(a is b)  # False
    ```
  - 얕은 복사 (Shallow Copy)
    - 정의 : 새로운 객체를 만들지만, **내부에 포함된 객체는 원본과 공유**한다.
    - 예시 코드
    ```python
    # 1차원 리스트 (문제 없음)
    a = [1, 2, 3]
    b = a[:] # b = a.copy() /// b = list(a)
    a[0] = 100
    print(a)  # [100, 2, 3]
    print(b)  # [1, 2, 3]

    # 다차원 리스트 (문제 발생)
    a = [1, 2, [3, 4]]
    b = a[:]
    b[2][0] = 999
    print(a)  # [1, 2, [999, 4]]
    print(b)  # [1, 2, [999, 4]]
    ```
  - 깊은 복사 (Deep Copy)
    - 정의 : 객체 내부의 모든 중첩 객체까지 **완전히 새로운 객체로 복사**한다.
    - 예시
    ```python
    import copy

    a = [1, 2, [3, 4]]
    b = copy.deepcopy(a)
    b[2][0] = 999

    print(a)  # [1, 2, [3, 4]]
    print(b)  # [1, 2, [999, 4]]
    print(a[2] is b[2])  # False
    ```
- 문장
  - 할당문 (x=100), 정의문 (def sum_num()), 제어문 (pass) 등 동작을 지시하는 실행 가능 코드의 최소 단위
  - 그 자체로 완결된 하나의 명령
  - 표현식과 다르게 값이 남지 않음 (ex. name = '홍길동'이라는 문장은 지시하지 값은 x)
- 타입 : 변수나 값이 가질 수 있는 데이터의 종류
  - 값(피연산자)과 연산자로 구분
    - 연산자
      - 산술 연산자 :  ** |\~| -(음수부호) |\~| *, /, //, % |\~| +, -
      - 복합 연산자 : +=, -=, *=, /=, //=, %=, **=
      - 비교 연산자 : <, <=, >, >=, ==, !=, is, is not
        - == 연산자는 값을 비교하고, is 연산자는 객체 그 자체(주소)를 비교한다
        - is 연산자는 주로 싱글턴 객체 (None, True, False 등 파이썬에 단 하나뿐인 객체) 비교에 사용 
      - 논리 연산자 : and, or, not
      ```python
      print(True and False) # False
      print(True or False) # True
      print(not 0) # True
      ```
        - 단축 평가
          - and 연산자 : 처음 만나는 거짓 값을 반환, 아니면 마지막 참 값을 반환
          - or 연산자 : 처음 만나는 참 값을 반환, 아니라면 마지막 거짓 값을 반환
      - 멤버십 연산자 : in, not in
      - 시퀀스 연산자 (문자열, 리스트, 튜플에 특별히 사용되는 연산자) : +, *
    - 연산자 우선순위 총합
        ```
        ()
        []
        **
        +, - (양/음수)
        *, /, //, %
        +, -
        <, <=, >=, >, ==, !=
        is, is not
        in, not in
        not
        and
        or
        ```


## 변수와 자료형

- Data type 분류(요약)
  - Data type : 값의 종류와 그 값으로 할 수 있는 동작(연산) 결정 속성
    - numeric type : int, float. complex
    - text sequence type : str
    - sequence type : list tuple, range
    - non-sequence type : set, dict
    - others : Boolean, None, Functions

- **설명**
  - 파이썬은 다양한 자료형을 사용하며, `type()`으로 자료형 확인 가능
  - 한 줄에 여러 변수 할당 가능 (`a, b = 1, 2`)
  - `bool()` 변환 시 `0`, `""`는 False, 그 외는 대부분 True
  ```python
  a = 1
  b = '1'
  c = True

  a, b, c = 1, '1', True
  print(type(a), type(b), type(c))

  print(bool(0))     # False
  print(bool(-10))   # True
  print(bool(""))    # False
  print(bool("k"))   # True
  ```
  - **실수하기 쉬운 포인트**
    - `True/False`는 반드시 첫 글자 대문자
    - `"0"`(문자열)은 빈 문자열이 아니므로 `bool("0") == True`

- Numeric types : 숫자형 데이터
  - int / 정수 자료형
    ```python
    student_count = 14
    temp = -19
    zero = 0
    ```
  - float / 실수 자료형
    ```python
    pi=3.14
    tax_rate = 1.242
    ```
    - 부동소수점 오차
      - 컴퓨터는 2진법을 사용하는데, 일부 소수는 2진수로 바꾸면 무한 소수가 된다
      - 때문에 컴퓨터는 근사값으로 잘라 저장하며 오류가 생길 수 있음
    - 지수 표현법
      ```python
      # 1,230,000,000 (1.23 * 10^9)
      big = 1.23e9
      # 0.00314 (3.14 *10^-3)
      small = 3.14e-3
      ```
  - 숫자형 행동 -> 산술연산
    - 산술 연산자 (우선 순위) : ** |\~| -(음수부호) |\~| *, /, //, % |\~| +, -
- Sequence type : 여러 개 값을 순서대로 나열하여 저장하는 자료형 (str, list, tuple, range)
  - 특징
    - 순서가 존재, 인덱싱/슬라이싱 가능, len()을 통한 길이 측정, 반복문 가능
  - str / 문자열
    - **내용, 설명**
      - 문자열은 **순서가 있는 자료형**이라 인덱싱/슬라이싱 가능
      - 하지만 문자열은 **불변(immutable)** → 인덱스로 직접 수정 불가
      - `ord()`는 문자 → ASCII 숫자, `chr()`는 숫자 → 문자
    - **예시**
      ```python
      s = "abcdeFG"
      print(s[:3])     # abc
      print(s[3:])     # deFG
      print(s[::-1])   # GFedcba

      ret = s.replace(s[1], "ㄱ")
      print(ret)

      capital = "A"
      print(ord(capital))         # 65
      print(chr(ord(capital)+32)) # a
      ```
    - 이스케이프 시퀀스
      - 역슬래쉬 + 문자를 통해 줄바꿈 , 탭 등 특수 기능 수행
    - f-string
      ```py
      name = '홍길동'
      age = 25
      print(f'안녕하세요, {age}살 {name}입니다.')
      # 안녕하세요, 25살 홍길동입니다.
      ```
    - **실수하기 쉬운 포인트**
      - `s[1] = "x"` 같은 직접 변경은 불가능 (TypeError)
      - `s + 1`처럼 문자열과 숫자는 바로 더할 수 없음 → `s + str(1)`
    - **아스키코드**
      - 숫자 (0\~9) : 48\~57
      - 소문자 (a\~z) : 97\~122
      - 대문자 (A\~Z) : 65\~90
  - list / 리스트 
    - 여러 값을 순서대로 저장하는 변경 가능 자료형 (숫자, 문자열, 리스트 등 모든 종류 데이터 가능)
      - 중첩 리스트 (ex. lst = [1, 3, ['hy', 'lol', 4], 'pyth'])
    - 수정 (슬라이싱으로도 수정 가능)
      ```python
      my_list = ['java', 'django', 'C++', 'HTML', 'python']
      my_list[0] = 'python'
      print(my_list) # ['python', 'django', 'C++', 'HTML', 'python']
      ```
    - List Comprehension
      - [표현식 for 변수 in iterable if 조건식]
      - 예시 코드
        ```python
        numbers = [1, 2, 3]
        squared = [n**2 for n in numbers]
        ```
      - 2차원 리스트 생성
        ```python
        matrix = [[0 for _ in range(5)] for _ in range(5)]
        ```
  - tuple / 튜플
    - 여러개 값을 순서대로 저장하는 변경 불가 자료형
    - 형식
      - 소괄호 안의 값들을 쉼표로 구분하여 만듦
      - 단일 요소 튜플은 반드시 후행 쉼표가 필요하다
        ```python
        tuple1 = ()
        tuple2 = (2,)
        tuple3 = 'java', 2, 'C++', 7, 'python'
        ```
    - 변경 불가하기에 내부 동작과 안전한 데이터 전달 등에 사용
      ```python
      x, y = 10, 20
      ```
  - range
    - 연속된 정수 시퀀스를 생성하는 변경 불가 자료형
    - 형식
      - range(start, stop, step)
        ```python
        print(list(range(3)))       # [0,1,2]
        print(list(range(3,8,2)))   # [3,5,7]
        print(list(range(10,1,-2))) # [10, 8, 6, 4, 2]
        ```
  - **실수하기 쉬운 포인트**
    - `range(3)`를 출력하면 range 객체가 보임 → `list(range(3))`로 확인
    - 튜플은 값 변경 불가: `tp[0] = 10` → 오류

- non-sequence type : set, dict
  - dict / 딕셔너리 
    - `key:value` 형태, key 중복 불가, 순서가 없는 변경 가능 자료형
      ```python
      di = {
        1: 3,
        2: {"ㄱ": "가자", "ㄴ": "나는"},
        3: "집",
        "교": [2, 3, 4]
      }
      print(di[2]["ㄱ"]) # 가자
      ```
    - 규칙
      - key - 중복될 수 없으면 변경 불가 자료형만 가능하다 (str, int, float, tuple)
      - value - 어떤 자료형이든 가능
    - 딕셔너리 컴프리헨션 (Dictionary Comprehension)
      - 문법
        ```python
        {key_expression: value_expression for item in iterable if condition}
        ```
      - 구성 요소
        - key_expression: 딕셔너리의 키를 정의
        - value_expression: 딕셔너리의 값을 정의
        - iterable: 반복 가능한 객체 (리스트, 튜플 등)
        - condition: 선택 조건 (만족하는 항목만 포함, 생략 가능)
      - 예시
        ```python
        numbers = [1, 2, 3, 4, 5]

        squared = {n: n**2 for n in numbers}
        print(squared)
        # 출력: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

        even_squared = {n: n**2 for n in numbers if n % 2 == 0}
        print(even_squared)
        # 출력: {2: 4, 4: 16}
        ```
      - 실수하기 쉬운 포인트  
        - list, set, dict는 키로 사용 불가  
        - tuple은 내부가 전부 immutable일 때만 가능
  - set / 세트 / 집합
    - 중복 제거에 매우 유용, 합집합/교집합/차집합 가능, 순서가 없기에 슬라이싱이나 인덱싱도 없다
    - 형식 : 중괄호 안의 쉼표로 값을 구분하여 만든다
      ```python
      my_set1 = set() # 빈 딕셔너리와 구분을 위해 빈 세트는 반드시 이렇게
      my_set2 = {1, 1, 2, 2, 2, 3}
      print(my_set1) # set() 
      print(my_set2) # {1, 2, 3}
      
      s1 = {1,2,3}
      s2 = {3,6,9}
      print(s1 | s2)  # 합집합 {1, 2, 3, 6, 9}
      print(s1 & s2)  # 교집합 {3}
      print(s1 - s2)  # 차집합 {1, 2}
      ```
  - 해시 테이블 (Hash Table)
    - 해시란?
      - 데이터를 **고정된 크기의 정수 값(해시값)** 으로 변환하는 것  
      - dict와 set은 내부적으로 **해시 테이블 구조** 사용  
      - 그래서 평균 검색 속도가 **O(1)**
      - hash() 값은 타입에 따라 다르며(특히 문자열은) 실행마다 달라질 수 있다
    - 해시 가능 조건
      - 변경 불가능(immutable) 해야 함  
      - 내부 요소도 모두 해시 가능해야 함
      ```py
      print(hash(1))
      print(hash('a'))
      print(hash((1,2,3)))
      # 출력: (정수값)
      ```
    - 해시 불가능 예
      ```py
      # print(hash([1,2,3]))  # TypeError
      # print(hash({1,2,3}))  # TypeError
      ```
    - set.pop()이 랜덤처럼 보이는 이유
      - set은 해시 테이블 기반이라 **저장 순서 개념이 없음**
      - 그래서 pop()이 호출될 때마다 임의의 요소 반환
      - 진짜 난수(random)는 아니고, 내부 해시/버킷 상태에 따라 결정되어 예측이 어렵게 보이는 것.
    - 해시 테이블 성능의 함정
      - 내용, 설명  
        - dict와 set는 평균적으로 O(1)의 빠른 속도를 가진다.
        - 하지만 해시 충돌(collision)이 많아지면 같은 버킷에 데이터가 몰리게 된다.
        - 이 경우 탐색이 느려져 **최악의 경우 O(n)** 까지 성능이 떨어질 수 있다.
  - **실수하기 쉬운 포인트**
    - dict 접근은 인덱스가 아니라 key 기반: `di[0]` 같은 접근 불가
    - set은 순서가 없음 → 인덱싱 불가 (`s[0]` 안됨)
- other
  - None : 값이 없음을 표현하는 타입
  - Boolean
    - True 또는 False만 가지는 타입
      ```python
      is_act = True
      is_logged = False
      print(is_act) # True
      print(is_logged) # False
      print( 10 > 5 ) # True
      print(10 == 5) # False
  - collection : 여러개를 묶는 자료형 [str, list, tuple, range, set, dict]
- 형변환
  - 암시적 형변환 : Boolean과 Numeric Type만 가능하다
    ```python
    print( 3 + 5.0 ) # 8.0 float로 자동 변환
    print(True + 3) # 4 True를 1로 자동 변환
    print(True + False) # 1 False를 0으로 변환
    ```
  - 명시적 형변환 : 함수를 통해 지적하여 변환
    - int(), float(), str(), list(), tuple(), set()

## 함수(Function)
- What?
  - 특정 작업을 수행하기 위한 재사용 가능 코드 묶음
  - 구조
    - def 키워드로 정의
    - parameter 받아  function body 통해 return value (docstring + return value = function body)
      - parameter : 함수 전달되는 값을 나타내는 변수
      - function body : ":"다음 들여쓰기 된 코드 블록
      - docstring : 함수 설명서 (x 필수)
    - return 문이 없다면 None을 반환한다, return 키워드 이후 반환 값을 명시
      - `print()`는 반환값이 없어서 `None` 반환
      - return 문은 함수를 종료, 그 이후 코드는 실행되지 않는다
      파이썬 함수는 언제나 단 하나의 값 (객체) 만 반환 하며, 여러 값 반환의 경우에도 튜플로 반환
  - **예시**
    ```python
    def make_sum(x, y):
        return x + y

    print(make_sum(100, 300))

    resu = print(100)
    print(resu)  # None
    ```
- 함수 인자(Arguments)
  - 함수 호출할때 실제 전달되는 값
  - 종류
    - Positional arguments : 위치 인자
      - 인자의 위치에 따라 전달되어 함수 호출 시 반드시 값을 전달해야 한다
    - Default arguments : 기본 인자 값
      - 정의에서 매개변수에 기본값을 할당, 인자를 전달받지 못하면 기본값을 반영한다
    - Keyword arguments : 키워드 인자
      - 호출 시 인자의 이름과 함께 값을 전달
      - 예시
        ```python
        def greet(name, age):
          print(f'안녕 {name}님, {age}살이네요.')
        greet('홍길동', age=30 )
        ```
      - 위치 인자는 반드시 키워드 인자보다 먼저 와야 한다
    - arbitrary arguments list : `*args` 가변 위치 인자
      - 여러개의 인자를 tuple로 처리한다
    - arbitrary keyword arguments list : `**kwargs` 가변 키워드 인자
      - 여러개의 인자를 dictionary로 처리
    - 기본 순서 : 위치 > 기본 > 가변 > 가변 키워드
  - **예시**
  ```python
  def func(pos1, pos2, default_arg='default', *args, **kwargs):
      print('pos1:', pos1)
      print('pos2:', pos2)
      print('default_arg:', default_arg)
      print('args:', args)
      print('kwargs:', kwargs)

  func(1, 2, 3, 4, 5, key1='value1')
    ```
    pos1: 1
    pos2: 2
    default_arg: 3
    args: (4, 5)
    kwargs: {'key1': 'value1'}
    ```
  ```
  - **실수하기 쉬운 포인트**
    - 기본값 인자는 반드시 뒤에 위치해야 함
    - keyword 인자 뒤에 positional 인자 배치 불가
- 재귀(Recursion)
  - **내용, 설명**
    - 함수가 자기 자신을 호출
    - 종료 조건(base case) 필수
  - **예시**
    ```python
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)

    print(factorial(5))  # 120
    ```
  - **실수하기 쉬운 포인트**
    - 종료 조건이 없으면 무한 재귀 → RecursionError
- 스코프(Scope) & 전역변수 global (LEGB Rule)
  - **내용, 설명**
    - Local → Enclosed → Global → Built-in
    - 내장함수 이름(sum 등)을 변수로 쓰면 덮어쓰기 문제가 발생
    - 전역변수 값을 변경하려면 `global` 필요
  - **예시**
    ```python
    print(sum(range(3)))  # 3
    sum = 5
    print(sum)            # 5
    # sum(range(3))  # TypeError

    num = 0
    def increment():
        global num
        num += 1
    increment()
    print(num)  # 1
    ```
  - 변수의 수명 주기
    - built-in scope : 파이썬 실행 이후 영원히
    - global scope : 모듈 호출 이후 or 인터프리터 끝날때 까지
    - local scope : 함수 호출 시 생성, 종료 될때 까지
  - LEGB Rule
    - 파이썬은 식별자를 특정 이름 공간에 저장하고, LECB Rule 순서에 따라 찾아 나간다
    - local > enclosed > global > Built-in
  - global zldnjem
    - 변수의 스코프를 전역으로 확대한다
  - **실수하기 쉬운 포인트**
    - `sum`, `list`, `dict`, `str` 같은 내장함수 이름을 변수명으로 쓰지 말기
    - global 선언 전 참조하면 SyntaxError 발생할 수 있음
- 패킹/언패킹 (Packing / Unpacking)
  - **내용, 설명**
    - 패킹: 여러 값을 하나로 묶기
      - `*rest`로 남는 값 받기 가능
      - ** 활용시 남는 키워드 인자를 하나의 딕셔너리로 만든다
      - print 는 인자 개수 상관 없이 튜플로 하나로 패킹하여 내부 처리한다
    - 언패킹: 여러 변수로 풀어내기, 리스트 등 객체 요소를 개별 변수에 할당
      - 역시나 * 또는 ** 가능
  - **예시**
    ```python
    packed_values = 1, 2, 3, 4, 5
    a, b, *rest = packed_values # *을 활용한 패킹 (튜플로 만듦)
    print(a, b, rest)  # 1 2 [3,4,5]

    def my_function (x, y, z):
      print(x, y ,z)
    names = ['a', 'b', 'c']
    my_function(*names) # a b c
    ```
  - **swap**
    ```python
    a, b = 1, 2
    a, b = b, a
    print(a, b)  # 2 1
    ```
  - **실수하기 쉬운 포인트**
    - 언패킹 변수 개수가 안 맞으면 ValueError
    - `*`는 남는 값들을 리스트로 받는다
- lambda (익명 함수)
  - **내용, 설명**
    - 한 줄로 간단한 함수 작성
    - `sorted(key=...)`, map/filter에 자주 사용
  - 구조
    ```py
    lambda 매개변수들: 반환값_표현식
    ```
  - **예시**
    ```python
    numbers = [1, 2, 3, 4, 5]
    squared2 = list(map(lambda x: x**2, numbers))
    print(squared2) # [1, 4, 9, 16, 25]


    students = [('지민', 25), ('서준', 20), ('민우', 30)]
    result = sorted(students, key=lambda student: student[1])
    print(result) # [('서준', 20), ('지민', 25), ('민우', 30)]
    ```
  - **실수하기 쉬운 포인트**
    - 복잡한 로직은 lambda보다 def 함수가 더 가독성이 좋음
- 내장함수: map / zip / filter / enumerate 등 파이썬에 기본적으로 내장되어 import 없이 사용 가능 함수
  - map
    - **내용, 설명**: 요소에 함수를 적용한 결과를 map 객체로 반환
      ```python
      numbers2 = list(map(int, input().split()))
      print(numbers2)
      # 입력 3 7 28 # 출력 [3, 7, 28]
      ```
    - **실수하기 쉬운 포인트**
      - `map`은 한 번 소비하면 끝 → 다시 쓰려면 list로 변환해두기

  - zip
    - **내용, 설명**: 여러 iterable을 튜플로 묶음 (길이가 짧은 쪽 기준)
      ```python
      arr = [[1,2,3],[4,5,6],[7,8,9]]
      print(list(map(list, zip(*arr))))
      # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
      ```
    - **실수하기 쉬운 포인트**
      - 길이가 다르면 긴 쪽은 잘려 나감

  - filter
    - **내용, 설명**: True인 값만 남김
      ```python
      num = list(range(1, 8))
      ret = filter(lambda x: x % 2 == 0, num)
      print(list(ret))
      # [2, 4, 6]
      ```
    - **실수하기 쉬운 포인트**
      - filter도 map처럼 iterator → 한 번만 사용 가능

  - enumerate
    - **내용, 설명**: iterable 객체 요소에 대해 (index, value) 제공
    ```python
    for idx, fruit in enumerate(['apple', 'banana'], start=1):
        print(idx, fruit)
        """
        1 apple
        2 banana
        """
    ```
  - 지연평가
    - map은 리스트를 받아서 **"어떻게 처리할지에 대한 계획"**만 만들고, 실제 계산은 나중으로
      ```python
      numbers = [10, 20, 30]
      recipe = map(lambda x: x * 2, numbers)

      print(recipe)
      # 출력: <map object at 0x...>
      ```
      - 아직 `[20, 40, 60]`이 만들어진 것이 아니라 "각 요소를 2배로 만드는 방법"만 저장된 상태
      - 즉 map은 "다음 값을 어떻게 만들지 아는 객체"를 돌려줄 뿐, 값을 미리 만들어 두지 않음
    - '이터레이터(Iterator)'
      - map이 반환하는 것은 리스트가 아니라 **이터레이터(iterator)** 
      - iterable (이터러블) : 반복 가능한 객체 (list, tuple, str 등)
      - iterator (이터레이터) : 값을 하나씩 꺼내는 흐름(stream) 객체  
        - next()로 다음 값을 생성하며, 한 번 소비하면 다시 사용할 수 없음
    - 결과를 보려면 '소비(consumption)'해야 한다
      - list()로 한 번에 소비
        ```python
        numbers = [10, 20, 30]
        recipe = map(lambda x: x * 2, numbers)

        result = list(recipe)
        print(result)
        # 출력: [20, 40, 60]
        ```
      - for문으로 하나씩 소비
        ```python
        numbers = [10, 20, 30]
        recipe = map(lambda x: x * 2, numbers)

        for item in recipe:
            print(item)

        # 출력:
        # 20
        # 40
        # 60
        ```
      - 주의: 이터레이터는 일회용이라 이미 list()로 소비했다면 다시 사용할 수 없다
    - why? **메모리 효율성**
    - 지연 평가를 사용하는 다른 함수들
      - range() : range(100)은 숫자 100개 리스트가 아니라 "요청하면 숫자를 만들어 줄 수 있는 객체"
        ```python
        r = range(5)
        print(r)
        # 출력: range(0, 5)

        print(list(r))
        # 출력: [0, 1, 2, 3, 4]
        ```
      - zip() : 여러 iterable을 묶는 "계획"만 만들고 요청될 때 튜플을 하나씩 생성
        ```python
        names = ['철수', '영희']
        scores = [90, 85]

        z = zip(names, scores)
        print(z)
        # 출력: <zip object at 0x...>

        print(list(z))
        # 출력: [('철수', 90), ('영희', 85)]
        ```

- 제너레이터 (Generator)
  - `yield`를 사용해서 값을 **한 번에 다 만들지 않고**, 필요할 때 하나씩 생성(지연 생성)
  - 큰 데이터/무한 시퀀스 처리에 유리
  - 예시
    ```py
    def count_up(n):
        i = 1
        while i <= n:
            yield i
            i += 1

    for x in count_up(3):
        print(x)
    # 1
    # 2
    # 3
    ```

- 타입 힌트 (Type Hint)
  - 실행 성능/동작을 바꾸는 게 아니라, **가독성과 협업**을 위해 타입을 표시
  - 예시
    ```py
    def add(x: int, y: int) -> int:
        return x + y
    ```
  
- 재바인딩(Rebinding) vs 뮤테이션(Mutation) + global/스코프 정리
  - 핵심 요약
    - **뮤테이션**: “같은 객체” 내부를 바꿈 (list/dict/set 등 mutable)
      - 예: `lst.append(1)`, `d["k"]=v`, `s.add(x)`
      - ✅ 함수 안에서 해도 바깥(호출자)에서 변화가 보일 수 있음 (같은 객체를 공유하면)
      - ❌ global 필요 없음 (이름 재할당이 아니라 객체 내부 변경이기 때문)
    - **재바인딩**: “이름(변수)”이 가리키는 대상을 바꿈 (새 객체로 연결)
      - 예: `x = x + 1`, `lst = lst + [1]`, `d = {"a":1}`
      - ⚠️ 함수 안에서 지역변수로 처리됨(기본) → 바깥 변수와 다른 이름이 됨
      - ✅ global/nonlocal이 필요한 대표 케이스

  - 왜 이런 차이가 생기나? (원리/이론)
    - 파이썬에서 “변수”는 값 그 자체가 아니라 **객체를 가리키는 이름표(reference)**에 가깝다
      - `x`라는 이름이 어떤 객체를 가리키고 있을 뿐
    - 함수 스코프에서 중요한 규칙
      - 함수 안에서 어떤 이름에 **대입(=)** 이 한 번이라도 등장하면,
        그 이름은 그 함수 안에서 **지역 변수(local)** 로 취급된다 (컴파일 단계에서 결정)
      - 그래서 “대입 전에 읽기”가 나오면 `UnboundLocalError`가 터질 수 있다
    - 반면, `lst.append(...)` 같은 건
      - `lst`라는 이름에 대입하는 게 아니라
      - `lst`가 가리키는 객체의 메서드를 호출해서 내부를 바꾸는 것(뮤테이션)이라
      - 스코프 규칙에 의해 `lst`가 local로 바뀌지 않는다

  - global 이 “필요한 상황 / 아닌 상황”
    - ✅ global이 필요한 상황(함수 안에서 “모듈 전역 변수 이름”을 재바인딩해야 할 때)
      - 전역 숫자 카운터 증가: `cnt += 1`
      - 전역 리스트를 “새 리스트로 교체”: `nums = nums + [x]` 또는 `nums = []`
      - 전역 dict를 “새 dict로 교체”: `d = {**d, "k": v}`
    - ❌ global이 필요 없는 상황(전역 객체를 “뮤테이션”만 할 때)
      - `nums.append(x)`, `nums.pop()`, `nums.sort()`
      - `d["k"]=v`, `d.update(...)`, `d.pop(...)`
      - `s.add(x)`, `s.remove(x)`
      - `visited[y][x] = 1` 처럼 “전역 리스트/2차원 리스트 내부 값 변경”
    - ⚠️ global은 필요 없지만, 실무적으로 조심해야 하는 상황
      - 함수가 전역 리스트를 직접 append 해버리면 “부작용(side effect)”이 커짐
      - 테스트/재사용성이 떨어질 수 있음 → 복사본으로 작업하거나 반환값으로 처리 권장

  - 가장 헷갈리는 포인트: `+=` 는 재바인딩? 뮤테이션?
    - 결론: 타입에 따라 다르다
      - `int/str/tuple` (immutable)에서 `+=`는 **재바인딩**
        - `x += 1`  → 새 int를 만들고 x가 그걸 가리킴 → 함수 안이면 global 필요
        - `s += "a"` → 새 str 생성 → global 필요
      - `list` (mutable)에서 `+=`는 보통 **in-place 확장(뮤테이션)** (`list.__iadd__`)
        - `lst += [1]`는 대개 리스트를 제자리에서 확장 → global 없이도 동작할 수 있음
      - 하지만 코드 가독성/혼란 때문에
        - 전역을 다룰 땐 `+=` 대신 `append/extend` 또는 명시적 재할당을 추천

  - 예시 1) UnboundLocalError: “읽기 + 대입” 조합이 만드는 함정
    ```py
    cnt = 0

    def inc():
        # cnt += 1 은 내부적으로 cnt = cnt + 1 과 같음 (대입 발생)
        # 따라서 cnt를 local로 판단함
        # 그런데 오른쪽에서 cnt를 읽으려 하니 (로컬 cnt는 아직 없음)
        # UnboundLocalError 발생
        cnt += 1

    inc()
    # UnboundLocalError: local variable 'cnt' referenced before assignment
    ```

  - 예시 2) global로 재바인딩 허용하기
    ```py
    cnt = 0

    def inc():
        global cnt
        cnt += 1

    inc()
    inc()
    print(cnt)  # 2
    ```

  - 예시 3) 전역 리스트 “뮤테이션”은 global 없이 된다
    ```py
    nums = [1, 2]

    def add_value():
        nums.append(3)  # 뮤테이션(객체 내부 변경) → global 불필요

    add_value()
    print(nums)  # [1, 2, 3]
    ```

  - 예시 4) 전역 리스트를 “교체(재바인딩)”하면 global 필요
    ```py
    nums = [1, 2]

    def replace_list():
        # nums = nums + [3] 는 새 리스트를 만들어 nums 이름을 새 객체로 바꿈(재바인딩)
        # 함수 안에서는 nums가 local로 간주되어 에러가 나거나(읽기 포함 시)
        # 혹은 전역이 안 바뀜
        # nums = nums + [3]  # (대개 UnboundLocalError)

        global nums
        nums = nums + [3]

    replace_list()
    print(nums)  # [1, 2, 3]
    ```

  - 예시 5) 전역 2차원 배열 visited는 왜 global 없이 되나? (너가 질문했던 케이스!)
    - 포인트: `visited` 이름을 바꾸는 게 아니라, **visited가 가리키는 리스트 내부 값을 바꾸는 것**
    ```py
    visited = [[0, 0], [0, 0]]

    def mark():
        visited[0][1] = 1  # 내부 원소 변경(뮤테이션) → global 불필요

    mark()
    print(visited)  # [[0, 1], [0, 0]]
    ```

  - 예시 6) dict도 동일한 규칙
    ```py
    d = {"a": 1}

    def mutate_dict():
        d["b"] = 2  # 뮤테이션 → global 불필요

    def rebind_dict():
        global d
        d = {"a": 1, "b": 2}  # 재바인딩 → global 필요

    mutate_dict()
    print(d)  # {'a': 1, 'b': 2}
    ```

  - 예시 7) “전역을 굳이 global로 쓰지 않는” 더 좋은 패턴(추천)
    - (1) 값을 반환해서 바깥에서 갱신
    ```py
    def inc(cnt):
        return cnt + 1

    cnt = 0
    cnt = inc(cnt)
    print(cnt)  # 1
    ```

    - (2) mutable을 수정하되, 명시적으로 “부작용 함수”임을 드러내기
    ```py
    def add_inplace(nums, x):
        nums.append(x)  # 이 함수는 nums를 직접 바꿈(부작용)
        # 반환을 안 해도 됨(혹은 return None)

    nums = [1, 2]
    add_inplace(nums, 3)
    print(nums)  # [1, 2, 3]
    ```

  - 결론 체크리스트 (global 판단 빠르게)
    - 함수 안에서 어떤 이름에 `=` / `+=` / `-=` / `*=` / `/=` 가 나오나?
      - 나오면 “재바인딩 가능성” ↑ → 전역을 바꿔야 하면 global 고려
    - `.append`, `.extend`, `d[k]=v`, `visited[y][x]=...` 처럼 “내부 수정”인가?
      - 그럼 뮤테이션 → global 필요 없음
    - 전역 변수를 직접 바꾸는 설계가 계속 필요해 보이나?
      - 가능하면 “반환값으로 갱신” 패턴이 더 안전하고 테스트하기 좋음



## 모듈 
- what ?
  - 한 파일로 묶인 변수와 함수의 모음
  ```python
  import math
  print(math.pi) #3.141592653589793
  print(math.sqrt(4)) #2.0
  ```
- import 사용법 (import / from / as)
  - 형식
    - `import math` : 모듈 전체 사용
      - '.' dot 연산자 : 점 왼쪽 객체에서 점 오른쪽 이름을 찾아라
    - `from math import sqrt` : 특정 함수만
      - 사용자 선언 변수와 겹치면 문제가 생김
      - 마지막 import 된 것이 이전 것을 덮어쓴다
    - `as`로 별칭 가능

  - **예시**
    ```python
    import math
    print(math.sqrt(4))

    from math import sqrt 
    print(sqrt(4))

    from math import sqrt as msqrt
    print(msqrt(16))
    ```
  - **실수하기 쉬운 포인트**
    - `from math import *`는 충돌/가독성 문제로 비추천
- 사용자 정의 모듈
  - 직접 정의 한 모듈을 사용 가능
  - 모듈을 파일로 저장 후, 같은 위치에서 다른 파일에서 모듈을 호출 할 수 있다
    - import 파일명 (.py 없이)
- 패키지
  - 연관된 모듈들을 하나의 디렉토리에 모은 것
    - 폴더 형태로 만들어 그 폴더 안에 파일을 넣어 활용할 수 있다
    ```py
    from 폴더명.파일명 import 함수명
    ```
  - PSL 내부 패키지
    - math, os, sys, random 등 설치 없이 바로 import 가능한 패키지
  - 외부 패키지
    - 직접 다운하여 사용
    - 설치할때 pip 사용
      ```bash
      pip install requests
      ```

      ```py
      import requests

      url = "사이트 주소"
      response = requests.get(url).json()
      print(response)
      ```
- 파일 입출력 (File I/O)
  - 파일을 읽고/쓰는 기능 (실무/코테 모두 자주 등장)
  - `with open(...) as f:` 형태를 가장 많이 사용 (자동 close)
  - 기본 모드
    - `"r"` 읽기 / `"w"` 덮어쓰기 / `"a"` 이어쓰기
  - 자주 쓰는 메서드
    - `read()` 전체 읽기
    - `readline()` 한 줄 읽기
    - `readlines()` 모든 줄 리스트
    - `write()` 쓰기
  - 예시
    ```py
    # 쓰기
    with open("example.txt", "w", encoding="utf-8") as f:
        f.write("Hello Python\n")

    # 읽기
    with open("example.txt", "r", encoding="utf-8") as f:
        print(f.read())
        # Hello Python
    ```

- help ( 모듈 명 ) 을 통해 모듈 안에 든 것을 확인할 수 있다


## 제어문
- what?
  - 코드 실행 흐름을 제어하는데 사용되는 구문
- 조건문 (if / elif / else)
  - what? 
    - 주어진 조건식을 평가하여 해당 조건이 참인 경우에만 코드 블록을 실행하거나 건너뜀
    - 조건은 위에서부터 평가되므로 `elif` 순서가 매우 중요
    - 중첩 조건문으로 세부 조건 처리 가능
  - 구조
    - if 문 : 조건문의 기본 형태
      - 작성된 조건을 만조갈 경우 내부 코드를 실행하며, 조건을 표현식으로 작성
    - elif 문 : 이전 조건을 만족하지 못하고 다른 조건이 필요할 경우
      - 여러개 사용 가능
    - else : 모든 조건을 만족하지 않을 경우 실행됨
  - **예시**
  ```python
  dust = 480

  if dust > 150:
      print('매우 나쁨')
      if dust > 300:
          print('위험해요! 나가지 마세요!')
  elif dust > 80:
      print('나쁨')
  else:
      print('좋음')
  ```
- 반복문 (for / while / break / continue / pass)
  - 주어진 코드 블록을 여러번 반복해서 실행하는 구문
  - for 문
    - 반복 가능 객체 요소를 반복하는데 주로 사용 (횟수가 정해진 반복)
    - 반복 가능 객체 iterable : 시퀀스 자료형 뿐만 아니라 비 시퀀스 형 (dict, set) 도 반복 가능
  - while 문
    - while 조건이 참인 동안 반복 (횟수가 정해지지 않은 경우 주로 사용)
    - 반드시 종료 조건이 있어야 한다
  반복 제어
    - `break`: 반복 즉시 종료
      ```py
      for i in range(10):
        if i == 5 :
          break
        print(i) # 0 1 2 3 4
      ```
    - `continue`: 현재 회차 스킵
      ```py
      for i in range(10):
        if i % 2 == 0 :
          continue
        print(i) # 1 3 5 7 9
      ```
    - `pass`: 문법적으로 자리를 채우는 용도 (아무 동작 없음)
- for-else
  - for 루프가 break를 만나 중단되지 않고 끝까지 간다면 else 블록 실행하는 제어문
    ```py
    for i in range(5):
      print(i)
      if i == 3:
        print('중단')
        break
    else :
      print("출력되지 않는다")
      
      # 0 1 2 3 중단

    for i in range(5):
      print(i)
      if i == 6:
        print('중단')
        break
    else :
      print("출력된다")

      # 0 1 2 3 4 출력된다
    ```

## method
- what?
  - 사전 지식
    - 데이터 구조 : 여러 데이터를 효과적으로 사용, 관리하기 위한 구조 (str, list, dict 등)
    - method 는 각 데이터 구조를 효율적으로 조작하거나 특정 기능 수행하기 위한 것
  - detail
    - **메서드(method)**는 특정 객체에 소속된 함수이다.
    - `객체.메서드()` 형태로 호출한다.
    - class 내부 정의되는 함수
  - 호출 방식
    - 함수
      ```py
      def func():
          pass

      func()
      # 출력: None (아무것도 반환하지 않음)
      ```
      - 메서드
    ```python
    numbers = [1, 2, 3]
    numbers.append(4)
    print(numbers)
    # 출력: [1, 2, 3, 4]
    ```
- 공통 시퀀스 메서드
  - `.index()`
    - 특정 값이 **처음 등장하는 위치(인덱스)** 를 반환한다.
    - 값이 없으면 `ValueError` 발생
    - 예시 코드
      ```py
      text = 'banana'
      print(text.index('a'))
      # 출력: 1

      nums = [1, 2, 3]
      print(nums.index(2))
      # 출력: 1
      ```
  - `.count()`
    - 특정 값이 **몇 번 등장하는지** 개수를 반환한다.
    - 예시 코드
      ```py
      text = 'banana'
      print(text.count('a'))
      # 출력: 3

      nums = [1, 2, 2, 3]
      print(nums.count(2))
      # 출력: 2
      ```
- 불변 시퀀스 method (문자열 전용)
  -  탐색과 검증
    - `.find()`
      - 값이 없으면 `-1` 반환 (에러 없음)
        ```py
        text = 'banana'
        print(text.find('a'))
        # 출력: 1

        print(text.find('z'))
        # 출력: -1
        ```
    - `.isupper()` / `.islower()`
      - 모든 케이스가 대문자인지 / 소문자인지 확인
      ```python
      print('HELLO'.isupper())
      # 출력: True

      print('Hello'.islower())
      # 출력: False
      ```
    -  `.isalpha()`
      - 모든 문자가 알파벳이고 하나 이상의 문자가 포함되어 있다면 True
       ```py
       print('Hello'.isalpha())
       # 출력: True

       print('123abc'.isalpha())
       # 출력: False
       ```
  - 문자열 조작 메서드
    - `.replace()`
      - str. replace(old, new[,count])
      ```py
      text = 'Hello world world'
      print(text.replace('world', 'Python', 1))
      # 출력: Hello Python world
      ```
    -  `.strip()`
      - str.strip([chars])
        
    ```py
    text = '   Hello World   '
    print(text.strip())
    # 출력: Hello World
    ```
    - `.split()`
      - str.split(sep=None, maxsplit= -1)
      ```py
      text = 'Hello   Python'
      print(text.split())
      # 출력: ['Hello', 'Python']
      ```
    - `.join()`
      - str.join(iterable)
      ```py
      words = ['Python', 'is', 'fun']
      print(' '.join(words))
      # 출력: Python is fun
      ```
    - 기타
    ```py
    text = "hELLO, worLd!"

    new_text1 = text.capitalize()
    new_text2 = text.title()
    new_text3 = text.upper()
    new_text4 = text.lower()
    new_text5 = text.swapcase()

    print(new_text1)  # Hello, world!
    print(new_text2)  # Hello, World!
    print(new_text3)  # HELLO, WORLD!
    print(new_text4)  # hello, world!
    print(new_text5)  # HellO, WORlD!
    ```
- 가변 시퀀스 method (리스트 전용)
  - 값 추가 및 삭제
    - `.append()`
      - **원본 리스트 변경**, 반환값은 `None`
      ```py
      nums = [1, 2]
      result = nums.append(3)

      print(nums)
      # 출력: [1, 2, 3]

      print(result)
      # 출력: None
      ```
        
    - `.extend()`
      - 리스트에 다른 반복 가능 객체 모든 항목 추가
        ```py
        nums = [1, 2]
        nums.extend([4, 5])
        print(nums)
        # 출력: [1, 2, 4, 5]
        ```
    - `.insert(i, x)`
      - x를 인덱스 i에 삽입
        ```py
        nums = [1, 2, 3]
        nums.insert(1, 100)
        print(nums)
        # 출력: [1, 100, 2, 3]
        ```
    - `.remove()` / `.pop()` / `.clear()`
      ```py
      nums = [1, 2, 3, 2]
      nums.remove(2)
      print(nums)
      # 출력: [1, 3, 2] 첫번째 일치 항목 삭제

      item = nums.pop()
      print(item)
      # 출력: 2

      print(nums)
      # 출력: [1, 3] 리스트에서 지정한 인덱스 항목을 제거하고 반환, 없으면 마지막 항목

      nums.clear()
      print(nums)
      # 출력: [] 모든 항목 제거
      ```
  - 리스트 정렬 및 순서 변경
    - `.reverse()`
      ```py
      nums = [1, 3, 2]
      nums.reverse()
      print(nums)
      # 출력: [2, 3, 1]
      ```
    - `.sort()`
      ```py
      nums = [3, 1, 2]
      nums.sort()
      print(nums)
      # 출력: [1, 2, 3]

      nums.sort(reverse=True)
      print(nums)
      # 출력: [3, 2, 1]
      ```
      - `sort()`는 None 반환 → 체이닝 불가
        ```py
        nums = [3, 1, 2]
        result = nums.sort()
        print(result)
        # 출력: None
        ```
        ```py
        nums = [3, 1, 2]
        sorted_nums = sorted(nums)
        print(sorted_nums)
        # 출력: [1, 2, 3]
        ```
- 메서드 체이닝
  - 여러 메서드를 **연속해서 호출**하는 방식
  - 예시 코드
    ```py
    text = 'heLLo'
    result = text.swapcase().replace('l', 'z')
    print(result)
    # 출력: HEzzO
    ```
  - list의 append, sort 같은 경우 None을 반환하기에 체이닝이 되지 않는다
- 숫자 판별 메서드 비교
  - isdecimal : 가장 엄격, 문자열이 모두 숫자(0~9)면 True
  - isdigit : 유니코드 숫자 인식 
  - isnumeric : 로마 숫자·분수까지 허용
  ```py
  print('Ⅳ'.isnumeric())  # True
  print('Ⅳ'.isdigit())   # False
  ```
- 딕셔너리 method
  - .get(key[, default])
    - 내용, 설명  
      - 키가 존재하면 값을 반환  
      - 키가 없으면 `None` 또는 지정한 기본값 반환  
      - **KeyError를 방지할 때 매우 중요**
    - 예시 코드
      ```py
      person = {'name': 'Alice', 'age': 25}
      print(person.get('name'))
      # 출력: Alice
      print(person.get('count'))
      # 출력: None
      print(person.get('count', 'nothing'))
      # 출력: nothing
      ```
  - .keys() / .values() / .items()
    - 내용, 설명  
      - `.keys()` → 키 목록  
      - `.values()` → 값 목록  
      - `.items()` → (key, value) 튜플 묶음  
      - 반복문에서 매우 자주 사용
    - 예시 코드
      ```py
      person = {'name': 'Alice', 'age': 25}

      print(person.keys())
      # 출력: dict_keys(['name', 'age'])

      print(person.values())
      # 출력: dict_values(['Alice', 25])

      print(person.items())
      # 출력: dict_items([('name', 'Alice'), ('age', 25)])

      for k, v in person.items():
          print(k, v)
      # 출력:
      # name Alice
      # age 25
      ```
    - 실수하기 쉬운 포인트  
      - 반환값은 리스트가 아니라 **뷰 객체**  
      - 필요하면 `list(person.keys())`
  - .pop(key[, default])
    - 내용, 설명  
      - 키를 제거하면서 값을 반환  
      - default 지정 시 KeyError 방지
    - 예시 코드
      ```py
      person = {'name': 'Alice', 'age': 25}
      print(person.pop('age'))
      # 출력: 25
      print(person)
      # 출력: {'name': 'Alice'}
      print(person.pop('country', None))
      # 출력: None
      ```
    - 실수하기 쉬운 포인트  
      - 기본값 없이 없는 키 삭제 시 KeyError
  - .setdefault(key, default)
    - 내용, 설명  
      - 키가 있으면 기존 값 반환  
      - 없으면 default 넣고 그 값을 반환  
      - **초기값 세팅에 매우 유용**
        - defaultdict(int) : 키가 없다면 0으로 초기화
        - defaultdict(list) : 키가 없다면 [] 으로 초기화
    - 예시 코드
      ```py
      person = {'name': 'Alice'}
      print(person.setdefault('country', 'KOREA'))
      # 출력: KOREA
      print(person)
      # 출력: {'name': 'Alice', 'country': 'KOREA'}
      ```
    - 실수하기 쉬운 포인트  
      - get과 달리 **딕셔너리를 수정함** 
  - .update()
    - 내용, 설명  
      - 다른 딕셔너리 또는 키워드 인자를 병합  
      - 기존 키는 덮어씀
    - 예시 코드
      ```py
      person = {'name': 'Alice', 'age': 25}
      other = {'name': 'Jane', 'country': 'KOREA'}
      person.update(other)
      print(person)
      # 출력: {'name': 'Jane', 'age': 25, 'country': 'KOREA'}
      person.update(age=100, address='SEOUL')
      print(person)
      # 출력: {'name': 'Jane', 'age': 100, 'country': 'KOREA', 'address': 'SEOUL'}
      ```
    - 실수하기 쉬운 포인트  
      - 원본 딕셔너리 변경됨
  - clear(), del
    - 내용, 설명  
      - `.clear()` → 전체 삭제  
      - `del dict[key]` → 특정 키 삭제
    - 예시 코드
      ```py
      person = {'name': 'Alice', 'age': 25}
      person.clear()
      print(person)
      # 출력: {}
      person = {'name': 'Alice', 'age': 25}
      del person['age']
      print(person)
      # 출력: {'name': 'Alice'}
      ```
    - 실수하기 쉬운 포인트  
      - 없는 키 `del` 하면 KeyError
  - 심화 : defaultdict
    - 내용, 설명  
      - 존재하지 않는 키 접근 시 기본값 자동 생성  
      - 키 존재 여부 검사 코드 제거 가능
    - 예시 코드
      ```py
      from collections import defaultdict
      text = 'banana'
      counts = defaultdict(int)
      for c in text:
          counts[c] += 1
      print(counts)
      # 출력: {'b': 1, 'a': 3, 'n': 2}
      ```
    - 실수하기 쉬운 포인트  
      - 기본값 함수(int, list 등) 괄호 없이 전달
- Set method
  - .add(x)
    - 내용, 설명  
      - 요소 하나 추가  
      - 이미 있으면 변화 없음
    - 예시 코드
      ```py
      s = {'a', 'b'}
      s.add('c')
      print(s)
      # 출력: {'a', 'b', 'c'}

      s.add('c')
      print(s)
      # 출력: {'a', 'b', 'c'}
      ```
  - .update(iterable)
    - 내용, 설명  
      - 여러 요소 한 번에 추가
    - 예시 코드
      ```py
      s = {1, 2}
      s.update([2, 3, 4])
      print(s)
      # 출력: {1, 2, 3, 4}
      ```
  - .remove(x) vs .discard(x)
    - 내용, 설명  
      - remove → 없으면 KeyError  
      - discard → 없어도 에러 없음
    - 예시 코드
      ```py
      s = {1, 2, 3}
      s.remove(2)
      print(s)
      # 출력: {1, 3}
      s.discard(10)
      print(s)
      # 출력: {1, 3}
      ````
  - .pop()
    - 내용, 설명  
      - 임의의 요소 하나 제거 후 반환  
      - set은 순서가 없기 때문에 예측 불가
    - 예시 코드
      ```py
      s = {1, 2, 3}
      print(s.pop())
      # 출력: (임의 값)
      ```
  - 집합 연산 메서드
    ```py
    set1 = {0,1,2,3,4}
    set2 = {1,3,5,7,9}
    set3 = {0, 1}
    print(set1.intersection(set2))
    # 출력: {1, 3} set1 & set2

    print(set1.union(set2))
    # 출력: {0,1,2,3,4,5,7,9} set1 | set2

    print(set1.difference(set2))
    # 출력: {0,2,4} set1 - set2

    print(set1.issubset(set2))
    # 출력: False // set1 <= set2

    print(set1.issuperset(set3))
    # 출력: True // set1 => set3

    ```

## 클래스
- 객체지향 프로그래밍(OOP) vs 절차지향 프로그래밍
  - 내용, 설명  
    - 절차지향 프로그래밍은 데이터와 함수가 서로 분리되어 있음  
      → 함수에 데이터를 계속 전달해야 함  
    - 객체지향 프로그래밍(OOP)은 데이터(속성)와 기능(메서드)을 하나로 묶음  
      → 현실 세계의 “객체” 개념을 코드로 표현  
      → 유지보수와 확장에 유리
  - 객체지향
    ```py
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def introduce(self):
            print(f'안녕하세요, {self.name}입니다. 나이는 {self.age}살입니다.')

    alice = Person('Alice', 25)
    alice.introduce()
    # 출력: 안녕하세요, Alice입니다. 나이는 25살입니다.
    ```
  - 절차지향
    ```py
    name = 'Alice'
    age = 25

    def introduce(name, age):
        print(f'안녕하세요, {name}입니다. 나이는 {age}살입니다.')

    introduce(name, age)
    # 출력: 안녕하세요, Alice입니다. 나이는 25살입니다.
    ```
- 클래스의 기본 개념
  - 내용, 설명  
    - 클래스는 **객체를 만들기 위한 설계도(틀)** 이다.
    - 현실 세계의 “개념”을 코드로 표현한 것이라고 생각하면 이해하기 쉽다.
      - 예: “사람”, “자동차”, “은행계좌” 같은 개념
    - 클래스는 **데이터(속성)** 와 **기능(메서드)** 을 하나로 묶는 역할을 한다.
  - 왜 클래스를 사용할까?
    - 내용, 설명  
      - 관련 있는 데이터와 기능을 한 덩어리로 관리할 수 있다.
      - 코드의 **재사용성**, **확장성**, **유지보수성**이 좋아진다.
      - 여러 개의 비슷한 객체를 만들 때 매우 유리하다.
    - 클래스 없이 작성하면
      ```py
      name1 = "Alice"
      age1 = 25

      name2 = "Bob"
      age2 = 30
      ```
    - 클래스를 사용하면
      ```py
      class Person:
          def __init__(self, name, age):
              self.name = name
              self.age = age

      p1 = Person("Alice", 25)
      p2 = Person("Bob", 30)

      print(p1.name, p2.age)
      # 출력: Alice 30
      ```
  - 클래스와 인스턴스의 관계
    - 내용, 설명  
      - 클래스 = 설계도  
      - 인스턴스 = 설계도로 만든 실제 물건(객체)
      - 하나의 클래스에서 여러 개의 인스턴스를 만들 수 있다.
    - 예시 코드
      ```py
      class Dog:
          def __init__(self, name):
              self.name = name

      d1 = Dog("초코")
      d2 = Dog("보리")

      print(d1.name)
      print(d2.name)
      # 출력:
      # 초코
      # 보리
      ```
  - 클래스 안에는 무엇이 들어갈까?
    - 속성(Attribute)
      - 객체가 가지는 데이터
      - 예: 이름, 나이, 잔액 등
    - 메서드(Method)
      - 객체가 할 수 있는 동작(함수)
      - 예: 인사하기, 입금하기, 이동하기 등
    - 예시 코드
      ```py
      class Person:
          def __init__(self, name):
              self.name = name  # 속성

          def introduce(self):  # 메서드
              print(f"안녕하세요, {self.name}입니다.")

      p = Person("세진")
      p.introduce()
      # 출력: 안녕하세요, 세진입니다.
      ```
  - 한 줄 핵심 정리
    - 클래스는 **데이터(속성) + 동작(메서드)을 묶는 사용자 정의 자료형**
    - 클래스를 사용하면 “관련 있는 것들”을 하나의 객체 단위로 다룰 수 있다.
    - 인스턴스는 클래스로부터 만들어진 실제 객체이다.
- 속성(Attribute) 종류
  - 클래스 속성
    - 내용, 설명  
      - 클래스 내부에 정의된 변수  
      - **모든 인스턴스가 공유하는 값**
      - “객체마다 다를 필요 없는 공통 데이터” 저장 시 사용
    - 예시 코드
      ```py
      class Person:
          species = "Human"  # 클래스 속성

      p1 = Person()
      p2 = Person()

      print(p1.species)
      print(p2.species)
      # 출력:
      # Human
      # Human
      ```
  - 인스턴스 속성
    - 내용, 설명  
      - 각 객체마다 **독립적으로 가지는 변수**
      - 보통 생성자 `__init__` 안에서 정의
    - 예시 코드
      ```py
      class Person:
          def __init__(self, name):
              self.name = name  # 인스턴스 속성

      p1 = Person("Alice")
      p2 = Person("Bob")

      print(p1.name)
      print(p2.name)
      # 출력:
      # Alice
      # Bob
      ```
- 캡슐화
  - 캡슐화란?
    - 객체의 내부 데이터(속성)를 외부에서 직접 접근하지 못하게 하고  
      메서드를 통해서만 다루도록 하는 객체지향 개념
    - 데이터 보호 + 코드 안정성을 높이기 위해 사용
  - 파이썬의 접근 수준 개념
    - Public (공개)
      - 누구나 접근 가능
      - 이름 앞에 아무것도 붙이지 않음
      ```py
      class Person:
          def __init__(self, name):
              self.name = name  # public

      p = Person("Alice")
      print(p.name)  # 접근 가능
      ```
    - Protected (보호)
      - "외부에서 쓰지 말자"는 **약속(관례)**
      - 이름 앞에 `_` 한 개 사용
      - 실제로는 접근 가능하지만 내부용으로 간주
      ```py
      class Person:
          def __init__(self):
              self._age = 20  # protected

      p = Person()
      print(p._age)  # 가능은 하지만 권장되지 않음
      ```
    - Private (비공개)
      - 클래스 내부에서만 사용하도록 이름을 변경(Name Mangling)
      - 이름 앞에 `__` 두 개 사용
      ```py
      class Person:
          def __init__(self):
              self.__salary = 5000  # private

      p = Person()
      # print(p.__salary)  # 에러 발생
      print(p._Person__salary)  # 내부적으로 이름이 변경되어 접근 가능
      ```
  - 왜 캡슐화가 필요할까?
    - 객체의 중요한 데이터를 실수로 바꾸는 것을 방지
    - 내부 구현을 숨기고, 인터페이스(메서드)만 공개
    - 코드 수정 시 외부 코드에 영향을 덜 줌
  - getter / setter 개념 (캡슐화와 함께 사용)
    - 내용, 설명  
      - 속성을 직접 접근하지 않고 메서드를 통해 읽고 수정
    - 예시 코드
      ```py
      class Person:
          def __init__(self):
              self.__age = 0

          def get_age(self):
              return self.__age

          def set_age(self, value):
              if value >= 0:
                  self.__age = value

      p = Person()
      p.set_age(25)
      print(p.get_age())  # 출력: 25
      ```
      ```py
      class Person:
          def __init__(self):
              self.__age = 0  # private 속성

          @property
          def age(self):  # getter 역할
              return self.__age

          @age.setter
          def age(self, value):  # setter 역할
              if value >= 0:
                  self.__age = value
              else:
                  print("나이는 음수가 될 수 없습니다.")

      p = Person()
      p.age = 25          # setter 호출
      print(p.age)        # getter 호출
      # 출력: 25
      ```

- 메서드(Method) 종류
  - 인스턴스 메서드
    - 내용, 설명  
      - 객체의 상태(인스턴스 속성)를 다룰 때 사용
      - 첫 번째 매개변수로 **self**를 받음
      - 반드시 **인스턴스를 통해 호출**
    - 예시 코드
      ```py
      class Counter:
          def __init__(self):
              self.count = 0

          def increment(self):
              self.count += 1

      c = Counter()
      c.increment()
      print(c.count)
      # 출력: 1
      ```
  - 정적 메서드 (Static Method)
    - 내용, 설명  
      - 인스턴스 속성도, 클래스 속성도 사용하지 않는 기능성 메서드
      - 첫 매개변수로 `self`나 `cls`를 받지 않음
      - 일반 함수와 비슷하지만, **관련 기능이라 클래스 안에 넣는 것**
      - `@staticmethod` 데코레이터 사용
    - 예시 코드
      ```py
      class MathUtils:
          @staticmethod
          def add(a, b):
              return a + b

      print(MathUtils.add(3, 5))
      # 출력: 8
      ```
  - 클래스 메서드 (Class Method)
    - 내용, 설명  
      - 클래스 속성을 다루거나, 클래스 단위 동작을 정의할 때 사용
      - 첫 매개변수로 **cls**를 받음
      - 클래스 자체에서 직접 호출 가능
      - `@classmethod` 데코레이터 사용
    - 예시 코드
      ```py
      class Person:
          population = 0

          def __init__(self, name):
              self.name = name
              Person.population += 1

          @classmethod
          def get_population(cls):
              return cls.population

      p1 = Person("A")
      p2 = Person("B")

      print(Person.get_population())
      # 출력: 2
      ```
  - method 예제
    ```py
    class BankAccount:
      interest_rate = 0.02

      def __init__(self, owner, balance=0):
          self.owner = owner
          self.balance = balance

      def deposit(self, amount):
          self.balance += amount

      def withdraw(self, amount):
          if self.balance >= amount:
              self.balance -= amount
          else:
              print('잔액 부족!')

      @classmethod
      def set_interest_rate(cls, rate):
          cls.interest_rate = rate

      @staticmethod
      def is_positive(amount):
          return amount > 0

    acc = BankAccount('Alice', 1000)
    acc.deposit(500)
    acc.withdraw(200)
    print(acc.balance)
    # 출력: 1300
    ```
  - 데코레이터
    - 내용, 설명  
      - 기존 함수 기능을 수정/확장  
      - @classmethod, @staticmethod도 데코레이터의 예
    ```py
    def deco(func):
        def wrapping(*args, **kwargs):
            print("shine" * 3)
            result = func(*args, **kwargs)
            print("화이팅" * 3)
            return result
        return wrapping
    
    
    @deco
    def call_name(name):
        print(name)
    
    
    @deco
    def call_age(age):
        print(age)
    
    
    call_name("세진")
    call_age(30)

    ```
  - 매직 메서드 (Magic Method)
    - 내용, 설명  
      - __로 시작하고 __로 끝나는 특수 메서드  
      - 객체의 동작을 정의
    - __str__
      ```py
      class Circle:
          def __init__(self, r):
              self.r = r

          def __str__(self):
              return f'반지름: {self.r}'

      c = Circle(10)
      print(c)
      # 출력: 반지름: 10
      ```
    - 연산자 오버로딩 (__add__)
      ```py
      class Car:
          def __init__(self, price):
              self.price = price

          def __add__(self, other):
              return self.price + other.price

      a = Car(300)
      b = Car(500)
      print(a + b)
      # 출력: 800
      ```

- dataclass
  - 데이터(속성) 중심 클래스를 만들 때 `__init__`, `__repr__`, 비교 메서드 등을 자동 생성해주는 도구
  - 언제 쓰나?
    - “필드(속성)만 있는 객체”를 자주 만들 때 (DTO, 설정 값, 결과 구조 등)
  - 핵심 포인트
    - `@dataclass` 데코레이터 사용
    - 기본값/기본 팩토리: `field(default=...)`, `field(default_factory=list)`
    - 불변 객체로 만들기: `@dataclass(frozen=True)`
  - 예시
    ```py
    from dataclasses import dataclass, field

    @dataclass
    class Person:
        name: str
        age: int
        tags: list[str] = field(default_factory=list)

    p = Person("Alice", 25)
    print(p)
    # Person(name='Alice', age=25, tags=[])
    ```
## 상속 (Inheritance)
- 상속이란?
  - 기존 클래스(부모, Superclass)의 속성과 메서드를  
    새로운 클래스(자식, Subclass)가 물려받는 것
  - 목적: **코드 재사용 + 중복 제거 + 계층 구조 표현**
  - 상속 = 기존 클래스 기능 재사용
  - 오버라이딩 = 부모 메서드 재정의
  - super() = 부모 기능을 이어서 실행
  - 다중 상속에서는 MRO 순서가 매우 중요
- 기본 상속 구조
  - 내용, 설명  
    - 자식 클래스는 부모 클래스의 기능을 그대로 사용 가능  
    - 새로운 기능을 추가할 수도 있음
  - 예시 코드
    ```py
    class Animal:
        def eat(self):
            print('먹는 중')

    class Dog(Animal):  # Animal을 상속
        def bark(self):
            print('멍멍')

    my_dog = Dog()
    my_dog.bark()  # 멍멍
    my_dog.eat()   # 부모 메서드 사용 가능
    ```
- 상속을 사용하는 이유 (중복 제거)
  - 상속 없을 때
    ```py
    class Professor:
        def __init__(self, name, age, department):
            self.name = name
            self.age = age
            self.department = department

        def talk(self):
            print(f'반갑습니다. {self.name}입니다.')

    class Student:
        def __init__(self, name, age, gpa):
            self.name = name
            self.age = age
            self.gpa = gpa

        def talk(self):  # 중복
            print(f'반갑습니다. {self.name}입니다.')
    ```
  - 상속 사용
    ```py
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def talk(self):
            print(f'반갑습니다. {self.name}입니다.')

    class Professor(Person):
        def __init__(self, name, age, department):
            super().__init__(name, age)
            self.department = department

    class Student(Person):
        def __init__(self, name, age, gpa):
            super().__init__(name, age)
            self.gpa = gpa

    p = Professor('박교수', 49, '컴공')
    s = Student('김학생', 20, 3.5)
    p.talk()  # 반갑습니다. 박교수입니다.
    s.talk()  # 반갑습니다. 김학생입니다.
    ```
- 다형성, 메서드 오버라이딩 (Overriding)
  - 내용, 설명  
    - 부모의 메서드를 자식이 **재정의**하는 것  
    - 같은 이름의 메서드가 있으면 자식 것이 우선됨
  ```py
  class Animal:
      def eat(self):
          print('Animal이 먹는 중')

  class Dog(Animal):
      def eat(self):  # 오버라이딩
          print('Dog가 먹는 중')

  my_dog = Dog()
  my_dog.eat()  # Dog가 먹는 중
  ```
- 다중 상속
  - 내용, 설명  
    - 여러 부모 클래스를 동시에 상속 가능  
    - 하지만 **메서드 탐색 순서(MRO)** 가 중요
  ```py
  class Mom:
      def swim(self):
          return '엄마 수영'

  class Dad:
      def walk(self):
          return '아빠 걷기'

  class Child(Mom, Dad):
      pass

  baby = Child()
  print(baby.swim())  # 엄마 수영
  print(baby.walk())  # 아빠 걷기
  ```
  - MRO (Method Resolution Order)
    - 내용, 설명  
      - 파이썬이 메서드를 찾는 순서  
      - 다중 상속에서 매우 중요
      ```py
      class A: pass
      class B(A): pass
      class C(A): pass
      class D(B, C): pass

      print(D.mro())
      # 출력: [D, B, C, A, object]
      ```
      → D에서 메서드를 찾을 때 B → C → A 순으로 탐색
  - super()
    - 내용, 설명  
      - 부모 클래스의 메서드를 호출할 때 사용  
      - 상속 구조에서 **중복 코드 제거 핵심 도구**
      ```py
      class Person:
          def __init__(self, name, age):
              self.name = name
              self.age = age

      class Student(Person):
          def __init__(self, name, age, student_id):
              super().__init__(name, age)  # 부모 생성자 호출
              self.student_id = student_id
      ```
    - super()는 “직계 부모”가 아니라  
      **MRO에서 다음 순서의 클래스**를 가리킴
      ```py
      class ParentA:
          def __init__(self):
              print('ParentA')
              super().__init__()

      class ParentB:
          def __init__(self):
              print('ParentB')

      class Child(ParentA, ParentB):
          def __init__(self):
              super().__init__()
              print('Child')

      c = Child()
      # 출력:
      # ParentA
      # ParentB
      # Child
      ```
  - 오버로딩(Overloading) vs 오버라이딩(Overriding)
    - 비교
      - 오버로딩
        - 같은 이름의 메서드를 **매개변수 개수/타입을 다르게** 여러 개 정의하는 것
        - **Java, C++** 같은 언어에서 지원
      - 오버라이딩
        - 부모 클래스의 메서드를 **자식 클래스에서 재정의**하는 것
        - 파이썬에서 상속 시 매우 자주 사용
    - ⚠ 파이썬의 메서드 오버로딩 특징
      - 내용, 설명  
        - 파이썬은 **전통적인 의미의 메서드 오버로딩을 지원하지 않는다**
        - 같은 이름의 메서드를 여러 번 정의하면 **마지막에 정의된 것만 남는다**
        - 매개변수 타입에 따라 자동으로 다른 메서드를 호출하는 기능은 없다
      - 잘못된 예시 (오버로딩이 안 되는 이유)
        ```py
        class Calculator:
            def add(self, a, b):
                return a + b

            def add(self, a, b, c):  # 위 메서드를 덮어씀
                return a + b + c

        calc = Calculator()
        print(calc.add(1, 2, 3))
        # 출력: 6
        # 하지만 add(1, 2)는 에러 발생 (첫 번째 add는 사라졌기 때문)
        ```
    - 파이썬에서 오버로딩을 "흉내내는" 방법
      - 기본값(default argument) 사용
        ```py
        class Calculator:
            def add(self, a, b, c=0):
                return a + b + c

        calc = Calculator()
        print(calc.add(1, 2))      # 출력: 3
        print(calc.add(1, 2, 3))   # 출력: 6
        ```
      - 가변 인자(*args) 사용
        ```py
        class Calculator:
            def add(self, *nums):
                return sum(nums)

        calc = Calculator()
        print(calc.add(1, 2))        # 출력: 3
        print(calc.add(1, 2, 3, 4))  # 출력: 10
        ```
      - 타입에 따라 동작 다르게 하기
        ```py
        class Printer:
            def print_data(self, data):
                if isinstance(data, int):
                    print("숫자:", data)
                elif isinstance(data, str):
                    print("문자열:", data)
                else:
                    print("기타 데이터")

        p = Printer()
        p.print_data(10)     # 출력: 숫자: 10
        p.print_data("hi")   # 출력: 문자열: hi
        ```
    - 파이썬에서 진짜로 많이 쓰이는 것: 메서드 오버라이딩
      - 내용, 설명  
        - 자식 클래스가 부모의 메서드를 **자기 방식대로 다시 정의**하는 것
        - 상속에서 핵심 개념
      - 예시 코드
        ```py
        class Animal:
            def speak(self):
                print("동물이 소리를 냅니다.")

        class Dog(Animal):
            def speak(self):  # 부모 메서드 재정의 (오버라이딩)
                print("멍멍!")

        a = Animal()
        d = Dog()

        a.speak()  # 출력: 동물이 소리를 냅니다.
        d.speak()  # 출력: 멍멍!
        ```

## 에러(Error)와 예외(Exception) 처리
- 에러 vs 예외
  - 내용, 설명  
    - 에러(Error): 프로그램이 실행 자체를 못 하는 심각한 문제 (문법 오류 등)
    - 예외(Exception): 실행 중 발생하는 문제 → 코드로 “처리 가능”
    - 파이썬에서는 예외를 처리하지 않으면 프로그램이 중단된다.
- try - except 기본 구조
  - 내용, 설명  
    - 예외가 발생할 수 있는 코드를 `try` 블록에 작성
    - 문제가 생기면 `except` 블록이 실행됨
  - 예시 코드
    ```py
    try:
        num = int(input('100을 나눌 값을 입력하시오 : '))
        print(100 / num)
    except:
        print('에러가 발생했습니다.')
    ```
  - 실수하기 쉬운 포인트  
    - except만 쓰면 어떤 에러인지 구분이 어려움 → 구체적 예외 작성 권장
- 복수 예외 처리
  - 내용, 설명  
    - 여러 종류의 예외를 하나의 except에서 묶어 처리 가능
  - 예시 코드
    ```py
    try:
        num = int(input('100을 나눌 값을 입력하시오 : '))
        print(100 / num)
    except (ValueError, ZeroDivisionError):
        print('제대로 입력해주세요.')
    ```
- 예외를 각각 따로 처리
  - 내용, 설명  
    - 예외마다 다른 메시지를 줄 수 있음
  - 예시 코드
    ```py
    try:
        x = int(input('숫자를 입력하세요: '))
        y = 10 / x
    except ZeroDivisionError:
        print('0으로 나눌 수 없습니다.')
    except ValueError:
        print('유효한 숫자가 아닙니다.')
    ```
- 예외 객체 사용 (as)
  - 내용, 설명  
    - 예외 내용을 변수로 받아 출력 가능
  - 예시 코드
    ```py
    my_list = []

    try:
        number = my_list[1]
    except IndexError as error:
        print(f'{error}가 발생했습니다.')
    ```
- EAFP vs LBYL
  - EAFP (Easier to Ask Forgiveness than Permission)
    - 일단 시도하고 실패하면 예외 처리
    ```py
    my_dict = {'key': 'value'}

    try:
        result = my_dict['key']
        print(result)
    except KeyError:
        print('Key가 존재하지 않습니다.')
    ```
  - LBYL (Look Before You Leap)
    - 미리 조건을 검사한 후 실행
    ```py
    if 'key' in my_dict:
        result = my_dict['key']
        print(result)
    else:
        print('Key가 존재하지 않습니다.')
    ```
  - dict 안전하게 값 가져오기 패턴
    - get() 사용
      - 키가 없어도 에러 없이 기본값 반환
      ```py
      d = {'a': 1}
      print(d.get('b', 0))  # 출력: 0
      ```
    - setdefault()
      - 키가 없으면 기본값을 넣고 반환
      ```py
      d = {}
      d.setdefault('count', 0)
      print(d)  # 출력: {'count': 0}
      ```
    - defaultdict (collections 모듈)
      - 기본값 자동 생성
      ```py
      from collections import defaultdict

      d = defaultdict(int)
      d['a'] += 1
      print(d)  # 출력: {'a': 1}
      ```
  - 이해 포인트  
    - 파이썬에서는 EAFP 스타일을 더 많이 사용
- 예외 처리 순서가 중요한 이유
  - 내용, 설명  
    - 예외는 **상속 구조**를 가짐
    - 부모 예외를 먼저 쓰면 자식 예외는 절대 도달하지 못함
  - 잘못된 예시
    ```py
    try:
        num = int(input('100으로 나눌 값을 입력하시오 : '))
        print(100 / num)
    except Exception:
        print('숫자를 넣어주세요.')
    except ZeroDivisionError:
        print('0으로 나눌 수 없습니다.')
    ```
  - 올바른 순서 (구체적인 예외 → 범용 예외)
    ```py
    try:
        num = int(input('100으로 나눌 값을 입력하시오 : '))
        print(100 / num)
    except ZeroDivisionError:
        print('0으로 나눌 수 없습니다.')
    except ValueError:
        print('숫자를 넣어주세요.')
    except Exception:
        print('에러가 발생하였습니다.')
    ```
- finally (항상 실행되는 블록)
  - 내용, 설명  
    - 예외 발생 여부와 관계없이 반드시 실행됨
    - 파일 닫기, 자원 정리에 자주 사용
  - 예시 코드
    ```py
    try:
        print('시도')
    except:
        print('에러 발생')
    finally:
        print('항상 실행')
    ```
- else (예외가 없을 때 실행)
  - 내용, 설명  
    - try 블록이 성공했을 때만 실행
  - 예시 코드
    ```py
    try:
        x = int(input())
    except ValueError:
        print('숫자 아님')
    else:
        print('정상 입력:', x)
    ```
- 핵심 정리
  - 예외는 프로그램을 멈추지 않게 하는 안전장치
  - 구체적인 예외부터 처리
  - Exception은 마지막에
  - EAFP 스타일이 파이썬스럽다
  - finally는 정리용, else는 성공 시 실행

## Python으로 “클라이언트 → 서버 요청” 정리 (requests 중심)
- 기초 
  - 내용, 설명
    - 클라이언트(내 파이썬 코드)가 서버(API)에 요청(request)을 보내면 서버는 응답(response)을 반환한다.
    - 이 통신은 보통 HTTP/HTTPS 프로토콜을 사용한다.
    - 요청에는 **메서드(GET/POST 등)**, **URL**, **헤더**, **쿼리/바디**, **인증 정보** 등이 포함된다.
    - `requests` 라이브러리는 이 과정을 파이썬 코드로 쉽게 처리하게 해준다.
  - 실수하기 쉬운 포인트
    - 요청 성공 여부는 반드시 **상태코드(status code)** 로 확인해야 한다.
    - 응답이 JSON이 아닐 수도 있으니 `.json()` 호출 전에 주의.
    - 네트워크는 언제든 실패할 수 있으므로 **timeout + 예외 처리 필수**.
  - 용어 한눈에 보기
    - 내용, 설명
      - Endpoint: 서버 API 경로 (예: `/v1/users`)
      - URL: 전체 주소 (프로토콜 + 도메인 + 경로 + 쿼리)
      - Query String: URL 뒤 `?key=value&...`
      - Headers: 인증/콘텐츠 타입 등 메타데이터
      - Body: 요청 본문(POST/PUT/PATCH 등에서 사용)
      - Status Code
        - 2xx 성공 (200, 201)
        - 4xx 클라이언트 오류 (400, 401, 403, 404)
        - 5xx 서버 오류 (500 등)
    - 실수하기 쉬운 포인트
      - 401 = 인증 문제, 403 = 권한 문제, 404 = URL 경로 오류 가능성
- requests 기본 흐름
  - 내용, 설명
    - 1) 요청 보내기 → 2) 응답 확인 → 3) JSON 파싱 → 4) 예외 처리
  - 예시 코드
    ```py
    import requests

    r = requests.get("https://httpbin.org/get", timeout=5)
    print(r.status_code)
    print(r.text[:80])
    ```
- GET 요청 (조회)
  - 내용, 설명
    - 서버에서 데이터를 조회할 때 사용
    - 쿼리 파라미터는 `params` 사용
  - 예시 코드
    ```py
    import requests

    url = "https://httpbin.org/get"
    params = {"q": "python", "page": 1}

    r = requests.get(url, params=params, timeout=5)
    print(r.url)
    print(r.status_code)
    print(r.json()["args"])
    ```
- POST 요청 (JSON 전송)
  - 내용, 설명
    - 서버에 데이터를 생성/전송할 때 사용
    - JSON 바디는 `json=` 사용
  - 예시 코드
    ```py
    import requests

    url = "https://httpbin.org/post"
    payload = {"name": "sejin", "role": "planner"}

    r = requests.post(url, json=payload, timeout=5)
    print(r.status_code)
    print(r.json()["json"])
    ```
- POST 요청 (form 데이터)
  - 내용, 설명
    - `application/x-www-form-urlencoded` 전송 시 사용
  - 예시 코드
    ```py
    import requests

    url = "https://httpbin.org/post"
    form = {"username": "user1", "password": "pw1234"}

    r = requests.post(url, data=form, timeout=5)
    print(r.status_code)
    print(r.json()["form"])
    ```
- 헤더(headers)
  - 내용, 설명
    - 인증 토큰, User-Agent 등 전달
  - 예시 코드
    ```py
    import requests

    headers = {
      "Authorization": "Bearer YOUR_TOKEN",
      "User-Agent": "MyPythonClient/1.0",
    }

    r = requests.get("https://httpbin.org/headers", headers=headers, timeout=5)
    print(r.status_code)
    print(r.json())
    ```
- 상태코드 & 에러 처리
  - 내용, 설명
    - `raise_for_status()` 사용 시 4xx/5xx를 예외로 처리 가능
  - 예시 코드
    ```py
    import requests

    try:
        r = requests.get("https://httpbin.org/status/404", timeout=5)
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("HTTPError:", e)
    ```
- 응답 다루기
  - 내용, 설명
    - `r.text` 문자열
    - `r.json()` JSON 파싱
    - `r.content` 바이트 데이터
    - `r.headers` 응답 헤더
  - 예시 코드
    ```py
    import requests

    r = requests.get("https://httpbin.org/get", timeout=5)
    print(r.headers.get("Content-Type"))
    print(r.text[:80])
    print(r.json().keys())
    ```
- timeout & 재시도
  - 내용, 설명
    - timeout은 필수
    - 재시도는 제한적으로
  - 예시 코드
    ```py
    import time, requests

    for i in range(3):
        try:
            r = requests.get("https://httpbin.org/delay/2", timeout=1)
            print("Success")
            break
        except requests.exceptions.Timeout:
            print("Timeout retry:", i+1)
            time.sleep(1)
    ```
- Session 사용
  - 내용, 설명
    - 연결 재사용, 쿠키 유지, 공통 헤더 관리
  - 예시 코드
    ```py
    import requests

    session = requests.Session()
    session.headers.update({"User-Agent": "MyClient/1.0"})

    r1 = session.get("https://httpbin.org/get", timeout=5)
    r2 = session.get("https://httpbin.org/get", timeout=5)
    print(r1.status_code, r2.status_code)
    ```
- 파일 다운로드/업로드
  - 다운로드 예시
    ```py
    import requests

    r = requests.get("https://httpbin.org/image/png", timeout=5)
    with open("image.png", "wb") as f:
        f.write(r.content)
    ```
  - 업로드 예시
    ```py
    import requests

    with open("image.png", "rb") as f:
        r = requests.post("https://httpbin.org/post", files={"file": f}, timeout=10)

    print(r.status_code)
    ```
- 실전 템플릿 함수
  - 내용, 설명
    - 자주 쓰는 패턴을 함수로 묶으면 안정적
  - 예시 코드
    ```py
    import requests

    def get_json(url, params=None, headers=None, timeout=5):
        try:
            r = requests.get(url, params=params, headers=headers, timeout=timeout)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.Timeout:
            return {"error": "timeout"}
        except requests.exceptions.HTTPError as e:
            return {"error": "http_error", "detail": str(e)}
        except ValueError:
            return {"error": "not_json"}
        except requests.exceptions.RequestException as e:
            return {"error": "request_exception", "detail": str(e)}

    print(get_json("https://httpbin.org/get", params={"q": "python"}))
    ```

# CLI 기본 명령어
- CLI(Command Line Interface)
  - 내용, 설명  
    - 터미널에서 명령어로 컴퓨터를 조작하는 방식  
    - 폴더 이동, 파일 생성/삭제/복사 등을 빠르게 수행 가능
- 📍 현재 위치 & 파일 목록 확인
  - pwd
    - 내용, 설명  
      - 현재 내가 위치한 폴더(경로)를 출력
    - 예시
      ```bash
      pwd
      ```
    - 실수하기 쉬운 포인트  
      - 위치 헷갈릴 때 제일 먼저 실행
  - ls
    - 내용, 설명  
      - 현재 폴더의 파일/폴더 목록 출력
    - 예시
      ```bash
      ls
      ls -a     # 숨김 파일 포함
      ls -l     # 자세히 보기
      ls -al    # 숨김 + 자세히
      ```
    - 실수하기 쉬운 포인트  
      - 숨김 파일은 기본 `ls`에 안 보임 → `ls -a` 사용
- 📂 폴더 이동
  - cd
    - 내용, 설명  
      - 디렉토리를 이동하는 명령어
    - 예시
      ```bash
      cd 폴더이름
      cd ..     # 상위 폴더
      cd .      # 현재 폴더
      cd ~      # 홈 디렉토리
      cd /      # 루트 디렉토리
      ```
    - 실수하기 쉬운 포인트  
      - `..` = 상위, `.` = 현재 (변화 없음)
- 🏗 파일/폴더 생성
  - mkdir
    - 내용, 설명  
      - 폴더(디렉토리) 생성
      - `-p` 옵션 사용 시 중간 경로까지 한 번에 생성
    - 예시
      ```bash
      mkdir my_folder
      mkdir -p a/b/c
      ```
    - 실수하기 쉬운 포인트  
      - 중간 경로 없으면 실패 → `mkdir -p`
  - touch
    - 내용, 설명  
      - 파일이 없으면 새 파일 생성, 있으면 수정 시간 갱신
    - 예시
      ```bash
      touch test.txt
      touch main.py
      ```
    - 실수하기 쉬운 포인트  
      - 폴더는 만들 수 없음 → 폴더는 `mkdir`
- 📄 파일 내용 확인 & 출력
  - cat
    - 내용, 설명  
      - 텍스트 파일 내용을 터미널에 출력
    - 예시
      ```bash
      cat README.md
      cat test.txt
      ```
    - 실수하기 쉬운 포인트  
      - 이미지/바이너리 파일에는 사용 금지
  - echo
    - 내용, 설명  
      - 문자열 출력  
      - 리다이렉션으로 파일 저장 가능
    - 예시
      ```bash
      echo "hello"
      echo "hello" > hello.txt     # 덮어쓰기
      echo "world" >> hello.txt    # 이어쓰기
      ```
    - 실수하기 쉬운 포인트  
      - `>` 덮어쓰기 / `>>` 이어쓰기
- 📦 파일/폴더 복사 & 이동
  - cp
    - 내용, 설명  
      - 파일/폴더 복사
    - 예시
      ```bash
      cp a.txt b.txt
      cp a.txt folder/
      cp -r my_folder backup/
      ```
    - 실수하기 쉬운 포인트  
      - 폴더 복사 시 `-r` 필수
  - mv
    - 내용, 설명  
      - 파일/폴더 이동 또는 이름 변경
    - 예시
      ```bash
      mv a.txt folder/       # 이동
      mv old.txt new.txt     # 이름 변경
      mv my_folder backup_folder
      ```
    - 실수하기 쉬운 포인트  
      - 덮어쓰기 위험 있음
- 🗑 삭제 관련
  - rm
    - 내용, 설명  
      - 파일/폴더 삭제 (휴지통 안 거침)
    - 예시
      ```bash
      rm a.txt
      rm -r folder/
      rm -rf folder/   # ⚠ 강제 전체 삭제
      ```
    - 실수하기 쉬운 포인트  
      - `rm -rf`는 매우 위험
- 🧹 터미널 관리
  - clear
    - 내용, 설명  
      - 터미널 화면 정리
    - 예시
      ```bash
      clear
      ```
    - 실수하기 쉬운 포인트  
      - 기록이 삭제되는 건 아님
  - history
    - 내용, 설명  
      - 이전 명령어 기록 확인
    - 예시
      ```bash
      history
      ```
    - 실수하기 쉬운 포인트  
      - 이전 명령 재사용할 때 매우 유용
- 🧭 경로 기호 정리
  - 내용, 설명  
    - CLI에서 자주 사용하는 경로 기호
  - 예시
    ```bash
    cd ../..       # 상위 폴더 두 번 이동
    cd ~/Desktop   # 홈 디렉토리 → Desktop
    ```
  - 실수하기 쉬운 포인트  
    - `.` 현재 / `..` 상위 / `~` 홈 디렉토리

# Git 활용법 정리 (기능 + 예시)
- Git이란
  - 내용, 설명  
    - 코드 변경 사항을 기록하는 버전 관리 도구  
    - 협업 시 변경 이력을 안전하게 관리 가능  
    - 작업 흐름: 수정 → add → commit → push
- 📦 저장소 시작 & 복제
  - git init
    - 내용, 설명  
      - 현재 폴더를 Git 저장소로 초기화
    - 예시
      ```bash
      git init
      ```
    - 실수하기 쉬운 포인트  
      - 이미 Git 폴더에서 다시 init 주의  
      - `.git` 폴더 삭제 금지
  - git clone
    - 내용, 설명  
      - 원격 저장소를 내 컴퓨터로 복제
    - 예시
      ```bash
      git clone https://github.com/유저명/레포명.git
      ```
    - 실수하기 쉬운 포인트  
      - clone하면 remote 자동 연결됨
- 🔍 현재 상태 확인 & 변경 내용 보기
  - git status
    - 내용, 설명  
      - 변경 파일, 스테이징 여부 확인
    - 예시
      ```bash
      git status
      ```
  - git diff
    - 내용, 설명  
      - 변경된 코드 비교
    - 예시
      ```bash
      git diff
      git diff --staged
      ```
  - git log
    - 내용, 설명  
      - 커밋 기록 확인
    - 예시
      ```bash
      git log --oneline --graph --decorate
      ```
- 📝 변경 사항 저장 과정
  - git add
    - 내용, 설명  
      - 커밋할 변경 사항을 스테이징
    - 예시
      ```bash
      git add 파일이름
      git add .
      git add -A
      ```
  - git commit
    - 내용, 설명  
      - 스테이징된 변경을 하나의 버전으로 저장
    - 예시
      ```bash
      git commit -m "메시지"
      ```
- 🌍 원격 저장소 연결 & 동기화
  - git remote
    - 내용, 설명  
      - 원격 저장소 확인/등록
    - 예시
      ```bash
      git remote add origin URL
      git remote -v
      ```
  - git push
    - 내용, 설명  
      - 내 커밋을 원격 저장소에 업로드
    - 예시
      ```bash
      git push origin main
      ```
  - git pull
    - 내용, 설명  
      - 원격 저장소 최신 내용 가져오


# Markdown / README 작성법 정리
- Markdown 기본 이해
  - 내용, 설명  
    - 마크다운은 “렌더링되는 환경(README 미리보기)”에서 서식이 적용된다.
    - 일반 메모장에서는 기호만 보이는 것이 정상이다.
- 📑 문서 구조 잡기 (목차 & 내부 링크)
  - 목차 만들기
    - 내용, 설명  
      - 문서 상단에 목차를 두면 긴 문서를 빠르게 탐색 가능
      - 내부 링크는 `(#헤더이름)` 형식 사용
      - 영어는 소문자, 띄어쓰기는 `-`로 변환됨
    - 예시
      ```md
      - [헤더](#헤더적기)
      - [코드 블럭](#코드블럭)
      - [링크 걸기](#링크걸기)
      ```
  - 내부 링크
    - 내용, 설명  
      - 문서 내 특정 위치로 이동하는 링크
      - 구조: `[보여질 글자](#이동할-헤더)`
    - 예시
      ```md
      [맨 위로 이동](#markdown--readme-작성법-정리)
      ```
    - 실수하기 쉬운 포인트  
      - 헤더 이름 바꾸면 내부 링크도 수정해야 함
- 🏷 제목(헤더) 작성
  - 내용, 설명  
    - `#` 개수로 제목 크기 결정
    - 보통: `# 문서 제목 → ## 섹션 → ### 하위 섹션`
  - 예시
    ```md
    # 제목1
    ## 제목2
    ### 제목3
    ```
  - 실수하기 쉬운 포인트  
    - `#` 뒤에 공백 필요 (`#제목` ❌ / `# 제목` ✅)
- 📋 리스트 작성
  - 순서 리스트
    - 내용, 설명  
      - 숫자 + `.` 사용
      - 들여쓰기로 하위 목록 가능
    - 예시
      ```md
      1. 첫 번째
      2. 두 번째
         1. 하위 항목
      ```
  - 일반 리스트
    - 내용, 설명  
      - `-`, `*`, `+` 중 하나 사용 (한 문서에서 통일 권장)
    - 예시
      ```md
      - 항목
        - 하위 항목
      ```
  - 체크 리스트
    - 내용, 설명  
      - `- [ ]` 미완료 / `- [x]` 완료
    - 예시
      ```md
      - [x] 완료
      - [ ] 미완료
      ```
    - 실수하기 쉬운 포인트  
      - `[ ]` 사이 공백 필요
- 💻 코드 작성
  - 코드 블럭
    - 내용, 설명  
      - 백틱 3개로 감싸기
      - 언어 지정 시 하이라이팅 가능
    - 예시
      ```md
      [```python]
      print("hello")
      [```]
      ```
    - 실수하기 쉬운 포인트  
      - 시작/끝 백틱 개수 맞아야 함
  - 인라인 코드
    - 내용, 설명  
      - 문장 중 코드 강조는 백틱 1개
    - 예시  
      \`git status\` 명령어 실행
- 🔗 링크 & 이미지
  - 링크 걸기
    - 내용, 설명  
      - `[텍스트](URL)` 형식
    - 예시
      ```md
      [네이버](https://www.naver.com)
      ```
  - 이미지 넣기
    - 내용, 설명  
      - 링크 앞에 `!` 추가
    - 예시
      ```md
      ![이미지설명](https://via.placeholder.com/150)
      ```
- ✨ 텍스트 꾸미기
  - 굵게  
    ```md
    **굵게** 또는 __굵게__
    ```
  - 기울임  
    ```md
    *기울임* 또는 _기울임_
    ```
  - 취소선  
    ```md
    ~~취소선~~
    ```
- ➖ 문서 구분 요소
  - 수평선
    ```md
    ---
    ***
    ___
    ```
  - 줄바꿈
    ```md
    첫 줄<br>
    둘째 줄
    ```
- 📚 참고 링크

  - Markdown 공식 가이드  
    https://www.markdownguide.org/


# 알고리즘(Algorithm) 기초

## 알고리즘 공부의 큰 흐름
- 보통 아래 3가지를 같이 봐야 실력이 빨리 늘어요.
  - **정확성**: 답이 맞는가? (반례가 없는가?)
  - **시간 복잡도**: 입력이 커질 때 얼마나 느려지는가? (Big-O)
  - **공간 복잡도**: 메모리를 얼마나 쓰는가?
- 팁: 코드를 짜기 전에 ‘입력 크기’를 보고 (예: N ≤ 10^5) 어떤 전략이 가능한지 먼저 고르는 습관이 중요해요.


## 개념
- 알고리즘이란?
  - 내용, 설명  
    - 문제를 해결하기 위한 **절차적 방법(순서 있는 해결 과정)**
    - 입력(Input)을 받아 원하는 출력(Output)을 만드는 일련의 단계
    - 컴퓨터가 이해할 수 있도록 논리적으로 구성된 해결 방법

  - 예시  
    - 라면 끓이기 레시피도 알고리즘의 한 예  
      → 물 끓이기 → 면 넣기 → 스프 넣기 → 완성

  - 핵심 특징
    - 명확성: 단계가 모호하지 않아야 함
    - 유한성: 반드시 끝나야 함
    - 입력과 출력이 존재해야 함
- 기본 단축키 (디버그)
  - Ctrl + F8 : Toggle breakpoint
  - shift + f9 : 디버깅 시작
  - F8 : Step over
  - F7 : Step into
  - Ctrl + F2 : 디버깅 종료
  
- 알고리즘 문제 해결의 순서
  - 문제읽기
  - 설계
  - 구현
  - 디버깅
  
## 시간 복잡도
- 시간 복잡도란?
  - 내용, 설명  
    - 입력 크기(N)가 커질수록 알고리즘 실행 시간이 얼마나 증가하는지를 나타내는 척도
    - 코드가 “얼마나 빠른지”를 비교하기 위한 기준
- 왜 시간 복잡도가 중요할까?
  - 같은 문제라도 알고리즘에 따라 실행 시간이 크게 달라짐
  ```py
  # 예시: 리스트에서 최댓값 찾기

  # 방법 1: 정렬 후 마지막 값
  arr.sort()
  max_val = arr[-1]   # O(N log N)

  # 방법 2: 한 번 순회
  max_val = arr[0]
  for x in arr:
      if x > max_val:
          max_val = x   # O(N)
  ```
  - 두 코드 모두 결과는 같지만 속도 차이가 큼
- Big-O 표기법
  - Big-O란?
    - 내용, 설명  
      - 시간 복잡도를 간단하게 표현하는 방법
      - 입력 크기 N이 매우 커질 때 **가장 큰 영향만 남기고 나머지는 무시**
  - 자주 등장하는 시간 복잡도

    | 복잡도 | 이름 | 의미 |
    |--------|------|------|
    | O(1) | 상수 시간 | 입력 크기와 상관없이 항상 일정 |
    | O(log N) | 로그 시간 | 입력이 커질수록 천천히 증가 |
    | O(N) | 선형 시간 | 입력 크기만큼 증가 |
    | O(N log N) | 선형 로그 | 정렬 알고리즘에서 자주 등장 |
    | O(N²) | 이차 시간 | 이중 반복문 |
    | O(2ⁿ) | 지수 시간 | 완전 탐색(비효율적) |
    
    ```md
       증가율 : O(1) < O(log N) < O(N) < O(N log N) < O(N²) < O(N³) < O(2ⁿ) < O(N!)
    ```    
    
    - O(1) — 상수 시간 (Constant Time)
    
      - 의미
        - 내용, 설명  
          - 입력 크기 `N`이 커져도 실행 횟수가 **항상 일정**
          - “딱 한 번(또는 고정된 몇 번)”만 수행되는 작업
      
      - 예시 코드 (배열 인덱스 접근)
        ```py
        arr = [10, 20, 30, 40, 50]
        print(arr[3])
        # 출력: 40
        ```
        - 왜 O(1)?
          - 배열은 인덱스로 위치를 바로 계산해서 접근 가능
          - `N`이 5든 500만이든 `arr[3]`은 **한 번 접근**
      
      - 대표 상황
        - 배열 인덱스 접근
        - 딕셔너리 조회(평균적으로) `d[key]`
        - 스택의 push/pop(끝에서 추가/삭제)
      
      - 주의점
        - “O(1)”은 “무조건 빠름”이 아니라 “입력 크기에 따라 증가하지 않는다”는 의미
    
    - O(log N) — 로그 시간 (Logarithmic Time)
    
      - 의미
        - 내용, 설명  
          - 매 단계에서 문제 크기가 **절반(또는 일정 비율)** 로 줄어드는 경우
          - `N`이 커져도 증가 속도가 매우 느림
      
      - 예시 코드 (이진 탐색: 정렬된 배열에서 찾기)
        ```py
        # arr는 반드시 정렬되어 있어야 함
        arr = [1, 3, 5, 7, 9, 11, 13]
        target = 9
      
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                print(mid)
                break
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # 출력: 4
        ```
        - 왜 O(log N)?
          - 한 번 비교할 때마다 탐색 범위가 절반으로 줄어듦
          - `N = 128`이면 최대 7번(2^7=128) 정도 비교로 끝남
      
      - 대표 상황
        - 이진 탐색
        - 균형 이진 트리 탐색(높이만큼)
        - “절반씩 줄이기” 형태의 분할
      
      - 주의점
        - 이진 탐색은 **정렬이 필수**
        - 정렬까지 포함하면 전체는 보통 O(N log N)이 될 수 있음
      
    - O(N) — 선형 시간 (Linear Time)
      
      - 의미
        - 내용, 설명  
          - 입력 크기 `N`에 비례해서 실행 횟수가 증가
          - “한 번 쭉 훑는” 형태
      
      - 예시 코드 (최댓값 찾기)
        ```py
        arr = [5, 1, 9, 3, 7]
      
        max_val = arr[0]
        for x in arr:
            if x > max_val:
                max_val = x
      
        print(max_val)
        # 출력: 9
        ```
        - 왜 O(N)?
          - 모든 원소를 최소 1번씩은 봐야 최댓값을 확정 가능
          - 원소가 5개면 5번, 100만 개면 100만 번
      
      - 대표 상황
        - 리스트 전체 순회
        - 문자열 한 번 스캔
        - 단일 반복문 기반 처리
      
      - 주의점
        - “최댓값/최솟값/합”은 대부분 O(N)
      
    - O(N log N) — 선형 로그 시간
      
      - 의미
        - 내용, 설명  
          - 보통 “log N 단계”가 있고,
          - 각 단계에서 전체를 “N만큼 처리”하는 경우
          - 대표적으로 **효율적인 정렬 알고리즘**
      
      - 예시 상황 1 (정렬)
        ```py
        arr = [5, 1, 9, 3, 7]
        arr.sort()
        print(arr)
        # 출력: [1, 3, 5, 7, 9]
        ```
        - 왜 O(N log N)?
          - 비교 기반 정렬은 평균적으로 N log N이 하한에 가까움
          - 파이썬 정렬(Timsort)도 평균적으로 O(N log N)
      
      - 예시 상황 2 (병합 정렬의 직관)
        - 배열을 절반씩 나눔 → log N 단계
        - 각 단계에서 합칠 때 전체 N개를 훑음 → N
        - 그래서 N log N
      
      - 대표 상황
        - 병합 정렬, 힙 정렬, 퀵 정렬(평균)
        - “분할(로그) + 각 단계 전체 처리(N)” 구조
      
      - 주의점
        - 정렬을 한 번 하면 이후 탐색/투포인터가 쉬워져서 전체가 더 빨라지는 문제가 많음
      
    - O(N^2) — 이차 시간 (Quadratic Time)
      
      - 의미
        - 내용, 설명  
          - `N`이 커질 때 실행 횟수가 `N*N`으로 증가
          - 보통 **이중 반복문**에서 발생
      
      - 예시 코드 (모든 쌍 비교)
        ```py
        arr = [1, 2, 3, 4]
        n = len(arr)
      
        for i in range(n):
            for j in range(n):
                print(arr[i], arr[j])
        ```
        - 왜 O(N^2)?
          - i가 n번 돌 때마다 j도 n번 돈다
          - 총 실행 횟수 = n * n
      
      - 대표 상황
        - 버블/선택 정렬
        - 모든 쌍(pair) 비교 문제
        - “두 개를 동시에 뽑아 비교”하는 문제
      
      - 주의점
        - N이 10,000만 되어도 1억 번이라 매우 위험
        - 코테에서는 N 크기 확인이 중요
    
    - O(N^3) — 삼차 시간 (Cubic Time)
      
      - 의미
        - 내용, 설명  
          - 삼중 반복문 → `N^3`
          - `N`이 조금만 커져도 폭발적으로 증가
      
      - 예시 코드 (삼중 루프)
        ```py
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    pass
        ```
      - 대표 상황
        - 플로이드-워셜 알고리즘 (모든 정점 쌍 최단 경로)
      
      - 주의점
        - N=500만 해도 1.25e8 수준이라 부담 큼
      
    - O(2^N) — 지수 시간 (Exponential Time)
      
      - 의미
        - 내용, 설명  
          - 선택지가 2개씩 늘어나며 경우의 수가 폭발하는 형태
          - 보통 “선택/비선택”의 조합 문제(부분집합)
      
      - 예시 상황 (부분집합 개수)
        - 원소 N개면 부분집합은 2^N개
        - N=20 → 약 100만 (가능)
        - N=30 → 약 10억 (거의 불가능)
      
      - 예시 코드 (부분집합 생성 개념)
        ```py
        # 각 원소를 "넣는다/안 넣는다" 2가지 선택
        def subset(idx, picked):
            if idx == n:
                return
            subset(idx + 1, picked + [arr[idx]])  # 선택
            subset(idx + 1, picked)               # 비선택
        ```
      
      - 주의점
        - N이 조금만 커져도 실행 불가
        - 이런 문제는 보통 가지치기(백트래킹)나 DP로 줄임
      
    - O(N!) — 팩토리얼 시간
      
      - 의미
        - 내용, 설명  
          - 순열(Permutation)처럼 모든 경우를 나열하는 방식
          - N이 커지면 “지수 시간보다도 더 빨리” 폭발
      
      - 예시 상황
        - N개의 원소를 나열하는 경우의 수 = N!
        - N=10 → 3,628,800 (가능할 수도)
        - N=12 → 479,001,600 (빡셈)
        - N=15 → 1조 단위 (불가능)
      
      - 대표 상황
        - 모든 순열을 시도하는 완전탐색
        - 외판원 문제(TSP) 브루트포스
  
    - 시간 복잡도 계산 시 주의점
      - 상수는 무시  
        - O(2N) → O(N)
      - 가장 큰 항만 남김  
        - O(N² + N) → O(N²)
      - 중첩 반복문은 곱  
        - 바깥 N × 안쪽 N → O(N²)
  
## 부분집합 (Subsets)
- 개념
  - 부분집합(subset): 어떤 집합(또는 배열)의 원소들 중 일부를 골라 만든 집합
  - 크기가 n인 집합의 부분집합 개수: 2^n (각 원소를 "선택/비선택" 2가지로 본다)
- 설명
  - 자주 나오는 문제 유형
    - (1) 모든 부분집합 나열
    - (2) 부분집합 중 조건 만족(합=K, 길이=M, 최소/최대 등)
    - (3) 최적화(가능/불가능 판정, 카운트, 최댓값/최솟값)
  - 핵심 아이디어(선택/비선택)
    - 원소 하나를 기준으로 “넣는다 / 안 넣는다”의 분기(2갈래)가 반복됨 → 전체 경우의 수 2^n
- 프로세스
  - 방법 A: 백트래킹(재귀)로 생성
    - idx번째 원소를 선택하고 다음으로
    - idx번째 원소를 선택하지 않고 다음으로
    - 종료 조건: idx == n
  - 방법 B: 비트마스크로 생성
    - 0 ~ (2^n - 1) 까지 정수 mask를 순회
    - i번째 비트가 1이면 arr[i] 포함
  
- 🧮 비트 연산 & 부분집합

  - 개념
    - 비트 연산은 숫자를 **2진수(비트)** 단위로 다루는 연산이다.
    - 컴퓨터는 모든 수를 2진수로 저장하기 때문에, 비트 연산은 매우 빠르고 효율적이다.
    - 부분집합 문제에서는  
      👉 "각 원소를 선택할지 말지"를 **비트(0 또는 1)** 로 표현할 수 있다.
  
  - 비트 기본 개념
  
    - 어떤 정수를 2진수로 보면 각 자리는 "켜짐(1) / 꺼짐(0)" 상태를 의미한다.
  
      예:  
      5 = 0b0101  
      → 0번째 비트 ON  
      → 2번째 비트 ON  
  
    - 부분집합과 연결하면  
      👉 i번째 비트가 1이면 arr[i]를 선택  
      👉 0이면 선택하지 않음
  
  - 주요 비트 연산자
  
  | 연산자 | 의미 | 예시 | 결과 |
  |------:|------|------|-----:|
  | `&`   | AND (둘 다 1이면 1) | `5 & 3` | `1` |
  | &#124; | OR (하나라도 1이면 1) | 5 &#124; 3 | `7` |
  | `^`   | XOR (서로 다르면 1) | `5 ^ 3` | `6` |
  | `~`   | NOT (비트 반전) | `~5` | `-6` |
  | `<<`  | 왼쪽 시프트 | `1 << 3` | `8` |
  | `>>`  | 오른쪽 시프트 | `8 >> 2` | `2` |
  
  - 자주 쓰는 비트 연산 패턴
  
    ```python
    n = 5  # 0b0101
  
    # i번째 비트가 켜져 있는지 확인
    i = 2
    print(n & (1 << i))  # 4 (0이 아니면 해당 비트는 1)
  
    # i번째 비트 켜기
    n = n | (1 << 1)
    print(n)  # 7 (0b0111)
  
    # i번째 비트 끄기
    n = n & ~(1 << 2)
    print(n)  # 3 (0b0011)
  
    # i번째 비트 토글(반전)
    n = n ^ (1 << 0)
    print(n)  # 2 (0b0010)
    ```
  
  - 🧩 비트 연산으로 부분집합 만들기
  
    - 아이디어
      - 원소가 n개라면 부분집합 개수는 2^n
      - 0부터 (2^n - 1)까지의 수를 2진수로 보면  
        각 숫자가 하나의 "부분집합 선택 상태"가 된다
  
    - 예시 배열
    
      ```python
      arr = ['A', 'B', 'C']
      n = len(arr)
      ```
    
    - 전체 부분집합 생성 코드
    
      ```python
      arr = ['A', 'B', 'C']
      n = len(arr)
    
      for mask in range(1 << n):  # 0 ~ 2^n - 1
          subset = []
    
          for i in range(n):
              if mask & (1 << i):  # i번째 비트가 1이면
                  subset.append(arr[i])
    
          print(subset)
      ```
    
      실행 결과:
      ```
      []
      ['A']
      ['B']
      ['A', 'B']
      ['C']
      ['A', 'C']
      ['B', 'C']
      ['A', 'B', 'C']
      ```
    
    - 동작 원리 예시 (mask = 5)
    
      ```
      mask = 5 → 0b101
    
      i=0 → (1<<0)=1 → 5&1 = 1 → arr[0] 포함
      i=1 → (1<<1)=2 → 5&2 = 0 → arr[1] 제외
      i=2 → (1<<2)=4 → 5&4 = 4 → arr[2] 포함
    
      결과: ['A', 'C']
      ```
  
  - 🎯 부분집합 + 조건 문제 예시
  
    - 부분집합 중 합이 K인 경우 찾기
    
      ```python
      arr = [1, 2, 3, 4]
      K = 5
      n = len(arr)
    
      for mask in range(1 << n):
          subset_sum = 0
          subset = []
    
          for i in range(n):
              if mask & (1 << i):
                  subset_sum += arr[i]
                  subset.append(arr[i])
    
          if subset_sum == K:
              print(subset)
      ```
    
      실행 결과:
      ```
      [1, 4]
      [2, 3]
      ```

- 시간 복잡도
  - 부분집합 전체 나열: O(n * 2^n)
    - 부분집합 개수 2^n, 각 부분집합 구성/출력에 최대 n이 걸릴 수 있음
  - 조건 검사도 보통 부분집합 단위로 들어가서 최악 O(n * 2^n)
- 특징
  - n이 20~25 넘어가면 2^n이 급격히 커져서 “전부 나열”은 위험
  - pruning(가지치기)로 탐색 공간을 줄이는 문제가 자주 나온다
  - 합/카운트처럼 누적 값이 중요하면 “현재까지의 합”을 인자로 들고 다니는 방식이 좋다
- 예시 코드
  - 예시 1) 백트래킹으로 모든 부분집합 출력
    ```python
    def subsets_backtracking(arr):
        n = len(arr)
        path = []

        def dfs(idx):
            if idx == n:
                print(path)
                return

            # 선택
            path.append(arr[idx])
            dfs(idx + 1)

            # 비선택
            path.pop()
            dfs(idx + 1)

        dfs(0)

    subsets_backtracking([1, 2, 3])
    # 출력 예시(순서는 구현에 따라 달라질 수 있음):
    # [1, 2, 3]
    # [1, 2]
    # [1, 3]
    # [1]
    # [2, 3]
    # [2]
    # [3]
    # []
    ```
  - 예시 2) 비트마스크로 모든 부분집합 만들기(리스트로 반환)
    ```python
    def subsets_bitmask(arr):
        n = len(arr)
        result = []

        for mask in range(1 << n):
            cur = []
            for i in range(n):
                if mask & (1 << i):
                    cur.append(arr[i])
            result.append(cur)

        return result

    print(subsets_bitmask([1, 2, 3]))
    # 출력:
    # [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    ```
  - 예시 3) 부분집합 합이 K가 되는 경우의 수 (백트래킹 + 가지치기)
    - 전제: arr가 모두 양수일 때, sum이 K를 넘으면 더 볼 필요 없음(pruning 가능)
    ```python
    def count_subset_sum_k(arr, K):
        n = len(arr)
        cnt = 0

        def dfs(idx, s):
            nonlocal cnt

            if s > K:  # pruning (양수일 때만 안전)
                return

            if idx == n:
                if s == K:
                    cnt += 1
                return

            # 선택
            dfs(idx + 1, s + arr[idx])
            # 비선택
            dfs(idx + 1, s)

        dfs(0, 0)
        return cnt

    print(count_subset_sum_k([1, 2, 3, 4], 5))
    # 출력: 2
    # (1+4), (2+3)
    ```
    
## 배열(Array)
- 배열이란?
  - 내용, 설명  
    - 같은 타입의 데이터를 **연속된 메모리 공간**에 저장하는 자료구조
    - 인덱스(index)를 이용해 각 요소에 빠르게 접근 가능
    - 알고리즘 문제에서 가장 기본이 되는 자료구조
- 배열의 핵심 특징
  - 인덱스를 통한 빠른 접근
    - 원리  
      - 배열은 메모리에 연속 저장되기 때문에  
        시작 주소 + (인덱스 × 자료형 크기)로 바로 위치 계산 가능
    - 시간 복잡도: **O(1)**
    ```py
    arr = [10, 20, 30, 40]
    print(arr[2])
    # 출력: 30
    ```
  - 연속된 메모리 구조
    - 장점: 탐색 속도가 빠름
    - 단점: 중간 삽입/삭제가 느림 (뒤 요소들을 이동해야 함)
- 배열의 주요 연산과 시간 복잡도

    | 연산 | 설명 | 시간 복잡도 |
    |------|------|--------------|
    | 인덱스 접근 | arr[i] | O(1) |
    | 끝에 추가 | append() | O(1) (평균) |
    | 끝에서 삭제 | pop() | O(1) |
    | 중간 삽입 | insert(i, x) | O(N) |
    | 중간 삭제 | del arr[i] | O(N) |
    | 탐색 | 값 찾기 | O(N) |
- 왜 중간 삽입/삭제가 느릴까?
  ```py
  arr = [1, 2, 3, 4]
  arr.insert(1, 99)
  # 결과: [1, 99, 2, 3, 4]
  ```
  - 원리  
    - 삽입 위치 뒤에 있는 요소들을 한 칸씩 뒤로 이동해야 함
    - 요소가 많을수록 오래 걸림 → O(N)
- 배열 vs 연결 리스트

  | 구분 | 배열 | 연결 리스트 |
  |------|------|-------------|
  | 메모리 구조 | 연속 | 흩어짐 |
  | 접근 속도 | 빠름 O(1) | 느림 O(N) |
  | 삽입/삭제 | 느림 O(N) | 빠름 O(1) (위치 알고 있을 때) |
- 파이썬 리스트는 배열일까?
  - 파이썬 리스트는 내부적으로 **동적 배열(dynamic array)** 구조
  - 필요할 때 메모리를 늘리며 크기 확장
  - 그래서 append는 평균 O(1)이지만, 가끔 O(N)이 발생할 수 있음
- 알고리즘에서 배열이 자주 쓰이는 이유
  - 빠른 인덱스 접근이 필요할 때
  - DP(동적 계획법) 테이블 저장
  - 정렬 문제
  - 완전 탐색(브루트포스)에서 데이터 저장
  
- 🔁 2차원 배열 순회 방식
  
  - 개념
    - 2차원 배열은 **행(row)과 열(column)** 로 이루어진 표 형태의 자료구조다.
    - 순회란 이 표 안의 모든 칸을 어떤 순서로 방문하는지를 의미한다.
    - 문제에 따라 순회 방향이 달라지며, 이것이 알고리즘의 핵심이 되기도 한다.
  - 1️⃣ 행 우선 순회 (Row-wise Traversal)
    - 설명  
      - 한 행을 왼쪽 → 오른쪽으로 다 본 뒤  
        다음 행으로 내려가는 방식
    - 순서 느낌  
      ```
      (0,0) (0,1) (0,2)
      (1,0) (1,1) (1,2)
      (2,0) (2,1) (2,2)
      ```
    - 예시 코드
      ```python
      arr = [
          [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
      ]
  
      for r in range(len(arr)):          # 행
          for c in range(len(arr[0])):   # 열
              print(arr[r][c], end=' ')
  
      # 실행 결과: 1 2 3 4 5 6 7 8 9
      ```
    - 특징  
      - 가장 기본이 되는 순회 방식  
      - 대부분의 2차원 배열 문제의 기본 틀
  - 2️⃣ 열 우선 순회 (Column-wise Traversal)
    - 설명  
      - 한 열을 위 → 아래로 다 본 뒤  
        다음 열로 이동하는 방식
    - 순서 느낌  
      ```
      (0,0) (1,0) (2,0)
      (0,1) (1,1) (2,1)
      (0,2) (1,2) (2,2)
      ```
    - 예시 코드
      ```python
      arr = [
          [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
      ]
  
      for c in range(len(arr[0])):   # 열
          for r in range(len(arr)):  # 행
              print(arr[r][c], end=' ')
  
      # 실행 결과: 1 4 7 2 5 8 3 6 9
      ```
    - 특징  
      - 행 우선과 반복문의 순서만 바뀐다  
      - 전치 행렬, 세로 방향 탐색 문제에 사용
  - 3️⃣ 지그재그 순회 (Zigzag Traversal)
    - 설명  
      - 한 행은 왼쪽 → 오른쪽  
        다음 행은 오른쪽 → 왼쪽으로 번갈아 가며 순회
    - 순서 느낌  
      ```
      → → →
            ← ← ←
      → → →
      ```
    - 예시 코드
      ```python
      arr = [
          [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
      ]
  
      for r in range(len(arr)):
          if r % 2 == 0:  # 짝수 행 → 정방향
              for c in range(len(arr[0])):
                  print(arr[r][c], end=' ')
          else:           # 홀수 행 → 역방향
              for c in range(len(arr[0]) - 1, -1, -1):
                  print(arr[r][c], end=' ')
  
      # 실행 결과: 1 2 3 6 5 4 7 8 9
      ```
    - 특징  
      - 방향 전환이 있는 순회  
      - 그래픽, 시뮬레이션 문제에서 자주 등장
  - 4️⃣ 상하좌우 탐색 (델타 탐색, 4방향 탐색)
    - 설명  
      - 한 칸에서 **위/아래/왼쪽/오른쪽 이웃 칸**을 탐색하는 방식  
      - BFS, DFS, 미로 문제의 기본
    - 이동 방향 정의
      ```python
      dr = [-1, 1, 0, 0]  # 상, 하
      dc = [0, 0, -1, 1]  # 좌, 우
      ```
    - 예시 코드
      ```python
      r, c = 1, 1  # 현재 위치 (가운데)
  
      for d in range(4):
          nr = r + dr[d]
          nc = c + dc[d]
          print(nr, nc)
  
      # 실행 결과:
      # 0 1
      # 2 1
      # 1 0
      # 1 2
      ```
    - 특징  
      - 그래프 탐색의 시작점  
      - 경계 체크와 함께 사용됨
  - 5️⃣ 대각선 순회 (Diagonal Traversal)
    - 설명  
      - 대각선 방향으로 이동하며 순회하는 방식  
      - (r+c)가 같은 칸들이 같은 대각선에 위치
    - 예시 코드 (좌상단 → 우하단 방향)
      ```python
      arr = [
          [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
      ]
  
      n = len(arr)
  
      for s in range(2 * n - 1):  # 대각선 번호
          for r in range(n):
              c = s - r
              if 0 <= c < n:
                  print(arr[r][c], end=' ')
  
      # 실행 결과: 1 2 4 3 5 7 6 8 9
      ```
    - 특징  
      - DP, 행렬 문제에서 자주 등장  
      - 인덱스 규칙을 이해하는 연습에 좋음
    
  - 함수를 통한 순회
    - 공통 유틸 함수(경계 체크)
      ```python
      def in_range(r, c, n, m):
          """좌표 (r, c)가 n*m 격자 범위 안이면 True"""
          return 0 <= r < n and 0 <= c < m
    
    
      # 간단 테스트
      n, m = 3, 4
      print(in_range(2, 3, n, m))  # True
      print(in_range(3, 0, n, m))  # False
      ```
    - 델타 탐색(4방향) 이웃 좌표 생성 함수
      - 설명
        - 현재 위치 (r, c)에서 상/하/좌/우로 이동한 좌표를 만들어준다
        - 범위를 벗어나는 좌표는 제외한다
      ```python
      # 4방향(상, 하, 좌, 우)
      DR4 = [-1, 1, 0, 0]
      DC4 = [0, 0, -1, 1]
    
      def neighbors_4(r, c, n, m):
          """(r, c)의 4방향 유효 이웃 좌표 리스트 반환"""
          res = []
          for d in range(4):
              nr = r + DR4[d]
              nc = c + DC4[d]
              if in_range(nr, nc, n, m):
                  res.append((nr, nc))
          return res
    
      # 예시
      n, m = 3, 3
      r, c = 1, 1
      print(neighbors_4(r, c, n, m))
      # 출력: [(0, 1), (2, 1), (1, 0), (1, 2)]
      ```
    - 대각선 탐색(4방향) 이웃 좌표 생성 함수
      - 설명
        - 현재 위치 (r, c)에서 4개의 대각선 방향으로 이동한 좌표를 만든다
        - 범위를 벗어나는 좌표는 제외한다
    
      ```python
      # 4대각선(좌상, 우상, 좌하, 우하)
      DRD = [-1, -1, 1, 1]
      DCD = [-1, 1, -1, 1]
    
      def neighbors_diag(r, c, n, m):
          """(r, c)의 대각선(4방향) 유효 이웃 좌표 리스트 반환"""
          res = []
          for d in range(4):
              nr = r + DRD[d]
              nc = c + DCD[d]
              if in_range(nr, nc, n, m):
                  res.append((nr, nc))
          return res
    
    
      # 예시
      n, m = 3, 3
      r, c = 1, 1
      print(neighbors_diag(r, c, n, m))
      # 출력: [(0, 0), (0, 2), (2, 0), (2, 2)]
      ```
    - 8방향(4방향 + 대각선) 이웃 좌표 생성 함수
      - 설명
        - 8방향은 격자 BFS/DFS에서 자주 등장한다
        - “상하좌우 + 대각선”을 한 번에 다루고 싶을 때 사용
      ```python
      DR8 = [-1, 1, 0, 0, -1, -1, 1, 1]
      DC8 = [0, 0, -1, 1, -1, 1, -1, 1]
    
      def neighbors_8(r, c, n, m):
          """(r, c)의 8방향 유효 이웃 좌표 리스트 반환"""
          res = []
          for d in range(8):
              nr = r + DR8[d]
              nc = c + DC8[d]
              if in_range(nr, nc, n, m):
                  res.append((nr, nc))
          return res
    
    
      # 예시
      n, m = 3, 3
      r, c = 1, 1
      print(neighbors_8(r, c, n, m))
      # 출력: [(0, 1), (2, 1), (1, 0), (1, 2), (0, 0), (0, 2), (2, 0), (2, 2)]
      ```
    - “값까지” 같이 꺼내는 패턴 (좌표 + 값)
      - 설명
        - 이웃 좌표만 뽑는 게 아니라, 그 칸의 값도 같이 쓰는 경우가 많다
        - 그래서 (nr, nc, grid[nr][nc]) 형태로 반환하면 편하다
    
      ```python
      def neighbors_4_with_value(grid, r, c):
          n, m = len(grid), len(grid[0])
          res = []
          for d in range(4):
              nr = r + DR4[d]
              nc = c + DC4[d]
              if in_range(nr, nc, n, m):
                  res.append((nr, nc, grid[nr][nc]))
          return res
    
    
      grid = [
          [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
      ]
      print(neighbors_4_with_value(grid, 1, 1))
      # 출력: [(0, 1, 2), (2, 1, 8), (1, 0, 4), (1, 2, 6)]
      ```
  - ⏱ 시간 복잡도
    - 대부분의 2차원 배열 전체 순회는 **O(N × M)**  
      (행 개수 N, 열 개수 M)
      
## 정렬(Sorting)
- 정렬이란?
  - 내용, 설명  
    - 데이터를 일정한 기준(오름차순/내림차순)에 따라 순서대로 나열하는 것
    - 알고리즘 문제 해결 전 **전처리 단계**로 매우 자주 사용됨
    - 정렬을 하면 탐색, 비교, 중복 제거 등이 쉬워짐
  - 정렬이 중요한 이유 (APS 관점)
    - 시간 복잡도 비교 문제가 자주 출제됨
    - 정렬 후 투포인터, 이분 탐색, 그리디 알고리즘 등에 활용됨
    - 입력 크기에 따라 어떤 정렬을 써야 하는지 판단해야 함
- 카운팅 정렬 (Counting Sort)
  - 개념  
    - 값을 직접 비교하지 않고, **각 값이 몇 번 나왔는지(빈도)** 를 세어서 정렬하는 방식
    - “비교 기반 정렬”이 아니라 “빈도 기반 정렬”
    - 값의 범위가 작을수록 매우 빠름 (범위가 크면 메모리 낭비)

    ```py
    arr = [4, 2, 2, 8, 3, 3, 1]

    # 1) 최댓값 기준으로 count 배열 준비
    max_val = max(arr)
    count = [0] * (max_val + 1)

    # 2) 빈도 세기
    for num in arr:
        count[num] += 1

    # 3) 누적합(각 값의 "마지막 위치" 정보 만들기)
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # 4) 결과 배열에 채우기 (뒤에서부터 채우면 안정 정렬)
    result = [0] * len(arr)
    for num in reversed(arr):
        count[num] -= 1
        result[count[num]] = num

    print(result)
    # 출력: [1, 2, 2, 3, 3, 4, 8]
    ```
    - 프로세스 (배열: [4, 2, 2, 8, 3, 3, 1])
      - count(빈도) 만들기
        - 1은 1번, 2는 2번, 3은 2번, 4는 1번, 8은 1번
      - count(누적합) 만들기
        - “각 값이 정렬된 배열에서 끝나는 위치”를 알 수 있음
      - 뒤에서부터 result에 채우기
        - 같은 값이 여러 개 있을 때 **원래 순서를 최대한 유지(안정 정렬)** 하기 위함
  - DAT(Data Address Table) 이란?
    - DAT는 말 그대로 **"값을 바로 찾아가기 위한 표"** 이다.
    - 인덱스를 값처럼 사용해서, **그 값이 몇 번 등장했는지 저장하는 배열**이다.
    - 쉽게 말해:  
      👉 "값 = 주소(인덱스)" 로 쓰는 특별한 배열
  
    - 예를 들어 숫자 범위가 0~9라면  
      길이 10짜리 배열을 만들어서 이렇게 사용한다:
  
      | 인덱스 | 의미 |
      |--------|------|
      | 0 | 숫자 0의 개수 |
      | 1 | 숫자 1의 개수 |
      | 2 | 숫자 2의 개수 |
      | ... | ... |
  
  - 시간 복잡도: **O(N + K)**
    - N: 데이터 개수
    - K: 값의 범위(0 ~ max_val)
  - 특징
    - 장점
      - 값 범위가 작으면 매우 빠름 (비교 없이 정렬 가능)
      - 안정 정렬 구현 가능(누적합 + 뒤에서 채우기)
    - 단점
      - 값 범위(K)가 크면 메모리 사용량이 커짐
      - 정수(또는 정수로 매핑 가능한 값)에서만 쓰기 쉬움
    - 사용 조건(실전 체크)
      - 입력 값이 “정수”이고, 최댓값 범위가 충분히 작을 때 유리

- 버블 정렬 (Bubble Sort)
  - 개념  
    - 인접한 두 값을 비교하여 순서가 틀리면 교환(swap)하는 방식
    - 한 바퀴(1패스) 돌 때마다 **가장 큰 값이 맨 뒤로 이동**
    - “큰 값이 거품처럼 뒤로 떠오른다”는 느낌

    ```py
    arr = [5, 3, 2, 4]
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(arr)
    # 출력: [2, 3, 4, 5]
    ```

    - 프로세스 (배열: [5, 3, 2, 4])
      - 1패스 (맨 뒤 최댓값 확정)
        - (5,3) 교환 → [3, 5, 2, 4]
        - (5,2) 교환 → [3, 2, 5, 4]
        - (5,4) 교환 → [3, 2, 4, 5]  ← 5가 맨 뒤로 이동(확정)
      - 2패스 (뒤에서 2번째 확정)
        - (3,2) 교환 → [2, 3, 4, 5]
        - (3,4) 유지  → [2, 3, 4, 5]
      - 3패스 이후
        - 이미 정렬되어 변화 없음

  - 시간 복잡도: **O(N²)**
    - 평균/최악: O(N²)
    - 최선(이미 정렬된 경우): 보통 O(N²)  
      (※ swap이 한 번도 없으면 종료하는 최적화를 넣으면 O(N) 가능)

  - 특징
    - 장점
      - 구현이 가장 단순해서 정렬 원리 학습에 좋음
    - 단점
      - 교환(swap)이 매우 많아 데이터가 커지면 비효율적
    - 안정성
      - **안정 정렬(Stable)**  
        - 같은 값끼리는 순서가 유지됨 (조건이 `>`일 때)

- 선택 정렬 (Selection Sort)
  - 개념  
    - 매 단계마다 “현재 위치(i)에 들어갈 값”을 정하기 위해
      **남은 구간에서 최솟값(또는 최댓값)을 선택**해서 i 위치와 교환하는 방식
    - 한 번의 패스에서 교환은 최대 1번만 발생 (교환 횟수는 적음)
    - 대신 최솟값을 찾기 위해 매번 끝까지 훑으므로 비교 횟수는 많음

    ```py
    arr = [5, 3, 2, 4]
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print(arr)
    # 출력: [2, 3, 4, 5]
    ```

    - 프로세스 (배열: [5, 3, 2, 4])
      - i=0: [5, 3, 2, 4] 중 최솟값 2(인덱스 2) 선택 → 0번과 교환
        - 결과: [2, 3, 5, 4]  ← 0번 자리 확정
      - i=1: [3, 5, 4] 중 최솟값 3(인덱스 1) 선택 → 1번과 교환(변화 없음)
        - 결과: [2, 3, 5, 4]  ← 1번 자리 확정
      - i=2: [5, 4] 중 최솟값 4(인덱스 3) 선택 → 2번과 교환
        - 결과: [2, 3, 4, 5]  ← 2번 자리 확정
      - i=3: 마지막은 자동 확정

  - 시간 복잡도: **O(N²)**
    - 최선/평균/최악 모두 O(N²)
    - 이유: 매 i마다 남은 구간을 끝까지 훑어서 최솟값을 찾음(비교가 항상 많음)

  - 특징
    - 장점
      - 교환 횟수가 적음 (각 패스 최대 1번 교환)
      - 구현이 직관적이고 단순
    - 단점
      - 비교 횟수가 많아 큰 데이터에서는 느림
      - 이미 정렬된 상태여도 비교를 끝까지 해서 이득이 거의 없음
    - 안정성
      - **불안정 정렬(Unstable)** 인 경우가 많음  
        - 최솟값을 찾아 앞과 교환하는 과정에서 같은 값의 상대 순서가 바뀔 수 있음

- 삽입 정렬 (Insertion Sort)
  - 개념  
    - 앞쪽 구간을 “이미 정렬된 영역”이라고 가정하고,
      현재 값(key)을 그 정렬된 영역의 **올바른 위치에 끼워 넣는 방식**
    - 카드 정리하듯이 “한 장씩 뽑아 알맞은 자리로 넣는다”는 느낌
    - key보다 큰 값들은 한 칸씩 오른쪽으로 밀어서 자리를 만든 뒤 삽입

    ```py
    arr = [5, 3, 2, 4]
    n = len(arr)

    for i in range(1, n):
        key = arr[i]     # 이번에 끼워 넣을 값
        j = i - 1        # 정렬된 영역의 끝 인덱스

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # 큰 값들을 오른쪽으로 밀기
            j -= 1

        arr[j + 1] = key  # key를 최종 위치에 삽입

    print(arr)
    # 출력: [2, 3, 4, 5]
    ```

    - 프로세스 (배열: [5, 3, 2, 4])
      - i=1, key=3 (정렬된 영역: [5])
        - 5 > 3 이므로 5를 오른쪽으로 밀기 → [5, 5, 2, 4]
        - key=3을 삽입 → [3, 5, 2, 4]
      - i=2, key=2 (정렬된 영역: [3, 5])
        - 5 > 2 → 밀기 → [3, 5, 5, 4]
        - 3 > 2 → 밀기 → [3, 3, 5, 4]
        - key=2 삽입 → [2, 3, 5, 4]
      - i=3, key=4 (정렬된 영역: [2, 3, 5])
        - 5 > 4 → 밀기 → [2, 3, 5, 5]
        - 3 > 4 ? 아니오 → 멈춤
        - key=4 삽입 → [2, 3, 4, 5]

  - 시간 복잡도: **O(N²)**
    - 평균/최악: O(N²)
      - 이유: key를 삽입할 때 큰 값들을 많이 밀어야 할 수 있음 (역순에 가까울수록 최악)
    - 최선(거의 정렬된 경우): **O(N)**
      - 이유: while이 거의 실행되지 않아서 “한 번씩 확인만” 하고 끝남

  - 특징
    - 장점
      - 거의 정렬된 데이터에서 매우 빠름
      - 구현이 간단하고, 작은 입력에서는 효율적
    - 단점
      - 역순(내림차순) 데이터에서는 매우 느림 (많이 밀어야 함)
    - 안정성
      - **안정 정렬(Stable)**  
        - 비교 조건이 `arr[j] > key`인 경우 같은 값은 밀지 않아서 순서가 유지됨

- 병합 정렬 (Merge Sort)
  - 개념  
    - 데이터를 **절반씩 나누고(Divide)**, 각각을 정렬한 뒤 **합쳐서(Merge)** 전체를 정렬하는 방식
    - 대표적인 **분할 정복(Divide & Conquer)** 알고리즘
    - “쪼개서 정렬 → 정렬된 것끼리 합치기”의 반복

    ```py
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result


    arr = [5, 3, 2, 4]
    print(merge_sort(arr))
    # 출력: [2, 3, 4, 5]
    ```

    - 프로세스 (배열: [5, 3, 2, 4])
      - 1단계: 반으로 나누기
        - [5, 3, 2, 4] → [5, 3] | [2, 4]
      - 2단계: 더 나누기
        - [5, 3] → [5] | [3]
        - [2, 4] → [2] | [4]
      - 3단계: 작은 단위부터 정렬하며 합치기
        - [5] + [3] → [3, 5]
        - [2] + [4] → [2, 4]
      - 4단계: 두 정렬된 배열 병합
        - [3, 5] + [2, 4] → [2, 3, 4, 5]

  - 시간 복잡도: **O(N log N)**
    - 배열을 log N 단계로 나누고,
    - 각 단계에서 전체 N개를 병합 → N log N

  - 특징
    - 장점
      - 항상 일정하게 빠름 (최선/평균/최악 모두 O(N log N))
      - **안정 정렬(Stable)** (같은 값의 순서 유지)
    - 단점
      - 추가 메모리 필요 (병합할 때 새로운 배열 사용)
      - 재귀 호출로 인해 함수 호출 비용 존재
    - 사용 포인트
      - 데이터 크기가 크고, 안정 정렬이 필요할 때 유리
      - 연결 리스트 정렬에도 적합 (배열보다 병합이 자연스러움)

- 퀵 정렬 (Quick Sort)
  - 개념  
    - 기준값(pivot)을 하나 정하고,
      pivot보다 작은 값은 왼쪽, 큰 값은 오른쪽으로 **분할(partition)** 한 뒤
      왼쪽/오른쪽을 다시 같은 방식으로 정렬하는 **분할 정복(Divide & Conquer)** 정렬
    - 평균적으로 매우 빠른 편이라 “퀵” 정렬이라고 부름

    ```py
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]

        left = [x for x in arr if x < pivot]
        mid = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return quick_sort(left) + mid + quick_sort(right)


    arr = [5, 3, 2, 4]
    print(quick_sort(arr))
    # 출력: [2, 3, 4, 5]
    ```

    - 프로세스 (배열: [5, 3, 2, 4])
      - pivot 선택 (예: 가운데 값 2)
        - pivot = 2
      - 분할
        - left  = [ ]        (2보다 작은 값)
        - mid   = [2]        (2와 같은 값)
        - right = [5, 3, 4]  (2보다 큰 값)
      - right에 대해 다시 퀵정렬
        - pivot = 3 (예시)
        - left = [ ] , mid = [3], right = [5, 4]
      - [5, 4]에 대해 다시 퀵정렬
        - pivot = 4
        - left = [ ] , mid = [4], right = [5]
      - 합치기(재귀가 끝나며)
        - [ ] + [2] + [3] + [4] + [5] → [2, 3, 4, 5]

  - 시간 복잡도: **평균 O(N log N), 최악 O(N²)**
    - 평균적으로는 분할이 균형 있게 일어나서 빠름
    - 최악은 pivot이 계속 한쪽으로 치우치는 경우(예: 이미 정렬된 배열에서 첫/끝을 pivot으로 잡는 경우)
      - 분할이 (N-1) + 0 처럼 되어 깊이가 N까지 늘어날 수 있음 → O(N²)

  - 특징
    - 장점
      - 평균적으로 매우 빠르고(실전에서 많이 쓰임), 캐시 효율도 좋은 편
      - 추가 메모리 사용이 상대적으로 적은 구현도 가능(in-place partition)
    - 단점
      - pivot 선택이 나쁘면 최악 O(N²)
      - 보통 **불안정 정렬(Unstable)** (같은 값의 상대 순서가 바뀔 수 있음)
    - 주의점 (코테 감각)
      - 이미 정렬된/거의 정렬된 데이터에서 최악을 피하려면
        - pivot을 랜덤으로 선택하거나
        - 가운데 값/median-of-three 같은 전략을 사용
      - 파이썬 실전에서는 대부분 `sort()`(Timsort)를 쓰고,
        퀵 정렬은 원리 이해가 목적
        
## 검색

- 개념
  - 검색이란 많은 데이터 속에서 **원하는 값을 찾아내는 과정**이다.
  - 일상에서 물건을 찾는 것처럼, 컴퓨터도 데이터 속에서 목표를 찾기 위해 다양한 방법을 사용한다.
  - 데이터의 상태(정렬 여부, 크기 등)에 따라 더 적절한 검색 방법이 달라진다.

- 선형 검색 (Linear Search)
  - 개념  
    - 앞에서부터 **하나씩 차례대로 확인하며 찾는 방법**
  
  - 설명  
    - 가장 단순한 검색 방법  
    - 데이터가 정렬되어 있지 않아도 사용할 수 있다  
    - 원하는 값을 찾거나 끝까지 갔는데 없으면 검색 종료  

  - 예시 코드
    ```python
    arr = [3, 8, 2, 7, 5]
    target = 7

    for i in range(len(arr)):
        if arr[i] == target:
            print("찾았다! 인덱스:", i)
            break

    # 실행 결과: 찾았다! 인덱스: 3
    ```

  - 동작 과정  
    1. 첫 번째 값부터 시작  
    2. 현재 값이 찾는 값인지 비교  
    3. 아니면 다음 값으로 이동  
    4. 찾거나 끝까지 가면 종료  

  - 시간 복잡도  
    - O(N)

  - 특징  
    - 구현이 매우 쉬움  
    - 정렬이 필요 없음  
    - 데이터가 많아질수록 느려짐  

- 이진 검색 (Binary Search)
  - 개념  
    - 가운데 값을 기준으로 **탐색 범위를 절반씩 줄여가는 검색 방법**

  - 설명  
    - 반드시 **데이터가 정렬되어 있어야 사용 가능**  
    - 한 번 비교할 때마다 탐색 범위가 절반으로 줄어든다  
    - 데이터가 많을수록 선형 검색보다 훨씬 빠르다  

  - 예시 코드
    ```python
    arr = [1, 3, 5, 7, 9, 11, 13]
    target = 7

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            print("찾았다! 인덱스:", mid)
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # 실행 결과: 찾았다! 인덱스: 3
    ```

  - 동작 과정  
    1. 중간 위치 선택  
    2. 중간 값과 목표 값 비교  
    3. 목표가 더 크면 오른쪽 절반 탐색  
    4. 더 작으면 왼쪽 절반 탐색  
    5. 찾거나 범위가 사라질 때까지 반복  

  - 시간 복잡도  
    - O(log N)

  - 특징  
    - 매우 빠른 검색 방법  
    - 정렬이 필수 조건  
    - 구현이 선형 검색보다 조금 더 복잡  

- 완전 검색 (Brute Force)
  - 개념  
    - 가능한 **모든 경우를 하나도 빠짐없이 전부 시도하는 방법**

  - 설명  
    - 정답이 나올 수 있는 모든 경우를 직접 만들어 확인  
    - 검색이라기보다 **모든 경우를 탐색하는 방식**  
    - 경우의 수가 적을 때 효과적  

  - 예시 코드
    ```python
    password = "42"

    for i in range(100):
        guess = str(i).zfill(2)
        if guess == password:
            print("비밀번호 찾음:", guess)
            break

    # 실행 결과: 비밀번호 찾음: 42
    ```

  - 동작 과정  
    1. 가능한 모든 경우 생성  
    2. 하나씩 정답인지 확인  
    3. 정답이면 종료, 아니면 계속 진행  

  - 시간 복잡도  
    - 경우의 수에 비례 (예: O(2^N), O(N!) 등)

  - 특징  
    - 반드시 정답을 찾을 수 있음  
    - 구현이 직관적  
    - 경우의 수가 많아지면 매우 느려짐  

- 해시 기반 검색 (Hash Search)
  - 개념  
    - 값을 바로 찾을 수 있도록 **미리 위치를 정해두는 검색 방법**

  - 설명  
    - 파이썬의 딕셔너리(Dictionary)가 대표적인 예  
    - 키(key)를 이용해 바로 값(value)의 위치를 찾음  
    - 거의 즉시 검색 가능  

  - 예시 코드
    ```python
    phone_book = {
        "엄마": "010-1234-5678",
        "철수": "010-2222-3333"
    }

    print(phone_book["엄마"])

    # 실행 결과: 010-1234-5678
    ```

  - 동작 과정  
    1. 키를 해시 함수에 넣어 위치 계산  
    2. 해당 위치에 바로 접근  
    3. 값 반환  

  - 시간 복잡도  
    - 평균 O(1)

  - 특징  
    - 매우 빠른 검색 속도  
    - 메모리를 더 사용함  
    - 해시 충돌이 발생할 수 있음

## 🥞 Stack (스택)

- 개념
  - 스택은 **나중에 들어온 것이 먼저 나가는 구조(LIFO: Last In First Out)**
  - 접시를 쌓아두는 구조와 비슷하다

- 기본 연산
  - push: 데이터 넣기
  - pop: 가장 위 데이터 꺼내기
  - top/peek: 맨 위 데이터 확인
  - isEmpty: 비었는지 확인

- 예시 코드

  ```python
  stack = []

  stack.append(10)  # push
  stack.append(20)
  stack.append(30)

  print(stack.pop())  # 30
  print(stack[-1])    # 20 (peek)
  ```

- 특징
  - 뒤로 가기(undo), 괄호 검사, DFS 등에 사용

- 🧠 Stack 기반 문제 해결 패턴

  - 대표 유형
    - 괄호 짝 맞추기
    - 이전/다음 큰 수 찾기
    - 문자열 뒤집기
    - DFS (재귀 대신 스택 사용)
  
  - 예시: 괄호 검사
  
    ```python
    def is_valid_parentheses(s):
        stack = []
  
        for ch in s:
            if ch == '(':
                stack.append(ch)
            else:
                if not stack:
                    return False
                stack.pop()
  
        return len(stack) == 0
  
  
    print(is_valid_parentheses("(())"))  # True
    print(is_valid_parentheses("(()"))   # False
    ```
## 🔁 재귀 호출 (Recursion)

- 개념
  - 함수가 자기 자신을 다시 호출하는 방식
  - 문제를 더 작은 문제로 쪼개 해결

- 필수 요소
  1. 종료 조건 (Base Case)
  2. 자기 자신 호출 (Recursive Case)

- 예시: 팩토리얼

  ```python
  def factorial(n):
      if n == 1:
          return 1
      return n * factorial(n - 1)

  print(factorial(5))  # 120
  ```

- 특징
  - 코드가 간결해진다
  - 스택 메모리를 사용한다
  - DFS, 백트래킹, 분할정복의 기반
  
- 🌳 DFS (Depth-First Search)

  - 개념
    - 한 방향으로 끝까지 탐색한 뒤 돌아오는 탐색 방식
    - 스택 구조 또는 재귀를 이용한다
  
  - 동작 방식
    1. 현재 노드 방문
    2. 갈 수 있는 곳 끝까지 탐색
    3. 더 이상 갈 곳 없으면 되돌아감
  
  - 재귀 구현 예시
  
    ```python
    def dfs(graph, node, visited):
        visited[node] = True
        print(node, end=' ')
  
        for next_node in graph[node]:
            if not visited[next_node]:
                dfs(graph, next_node, visited)
  
  
    graph = {
        1: [2, 3],
        2: [4],
        3: [],
        4: []
    }
  
    visited = {i: False for i in graph}
    dfs(graph, 1, visited)  # 1 2 4 3
    ```
  
  - 특징
    - 완전탐색에 사용
    - 재귀 구조와 매우 잘 어울림
    - 경로 찾기, 사이클 탐지 등에 활용

- 🧠 Memoization (메모이제이션)

  - 개념
    - 이미 계산한 결과를 저장해두고 다시 계산하지 않는 기법
    - 재귀 호출의 중복 계산을 줄이기 위해 사용된다
  
  - 왜 필요한가?
    - 재귀는 같은 계산을 여러 번 반복할 수 있다
    - 저장해두면 시간 복잡도를 크게 줄일 수 있다
  
  - 예시: 피보나치 수열 (메모이제이션 적용)
  
    ```python
    memo = {}
  
    def fib(n):
        if n in memo:
            return memo[n]
  
        if n <= 2:
            return 1
  
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]
  
  
    print(fib(10))  # 55
    ```
  
  - 특징
    - 재귀 + 저장(캐시)의 조합
    - Top-Down DP의 핵심 기술
    - 시간 복잡도를 지수 → 선형으로 줄일 수 있다


## 🧠 알고리즘 설계 전략

- 개념
  - 알고리즘 설계 전략이란 **문제를 해결하기 위한 전체적인 접근 방식(생각의 틀)** 이다.
  - 같은 문제라도 어떤 전략을 쓰느냐에 따라 코드 구조와 속도가 크게 달라진다.
  - 문제를 보면 "이건 어떤 전략 문제인가?"를 먼저 떠올리는 연습이 중요하다.

- 완전 탐색 (Brute Force)
  - 개념  
    - 가능한 **모든 경우를 전부 시도**해서 정답을 찾는 방법
  
  - 설명  
    - 가장 단순하고 확실한 방법  
    - 경우의 수가 적을 때 효과적  
    - 재귀, 순열, 조합, 부분집합 등이 여기에 포함된다  

  - 사용 느낌  
    - "일단 다 해보자"

  - 시간 복잡도 특징  
    - 보통 매우 큼 (O(2^N), O(N!) 등)

  - 대표 예시  
    - 비밀번호 모든 조합 찾기  
    - 부분집합 전부 구하기  
    - 문자 비교 ( 패턴 검색 )
  ```python
  def bruteforce(p, t):
    N = len(t)
    M = len(p)
    i = j = 0
    while i < N and j < M:
        if t[i] != p[j]:  # 다르면
            i = i - j + 1  # i - j 비교를 시작했던 위치
            j = 0
        else:  # 같으면
            i += 1
            j += 1
    if j == M:
        return i - j  # 패턴의 시작 인덱스
    else:
        return -1       # 패턴이 없는 경우

  t = 'TTTTTATTAATA'
  p = 'TTA'
  
  print(bruteforce(p, t))
  ```


- 탐욕 알고리즘 (Greedy Algorithm)
  
  - 개념
    - 탐욕 알고리즘은 **매 순간(지금 당장) 가장 좋아 보이는 선택**을 반복해서 정답을 만들려는 방법이다.
    - 포인트는 “미래까지 다 계산하지 않고”, **현재 기준으로 최선인 선택을 확정**해 나간다는 것.
    - 그래서 빠르고 구현이 쉬운 경우가 많지만, **항상 정답을 보장하지는 않는다.**
  
  - 왜 “탐욕(욕심)”이라고 부를까?
    - 눈앞에 가장 큰 이득을 먼저 챙기는 느낌이라서 “Greedy(욕심쟁이)”라는 이름이 붙었다.
    - 예시(감각적으로)
      - 케이크 조각이 여러 개 있으면 → “지금 제일 큰 조각부터 먹자!”
      - 동전으로 거스름돈을 줄 때 → “지금 가장 큰 동전부터 쓰자!”

  - 동작 방식 (프로세스)
    - 1) 문제에서 “선택”을 해야 하는 순간을 찾는다
    - 2) 그 순간에 **가장 좋아 보이는 규칙(기준)** 을 정한다  
         - 예: “가장 큰 동전부터”, “가장 빨리 끝나는 회의부터”
    - 3) 그 선택을 **확정**하고, 남은 문제를 더 작게 만든다
    - 4) 남은 문제에 대해 2~3을 반복한다

  - 탐욕 알고리즘이 ‘정답’이 되려면 (핵심 조건 감각)
    - 탐욕은 아무 문제에나 쓰면 위험하다.
    - 보통 아래 2가지 성질이 만족될 때 “탐욕이 정답이 된다”고 보는 편이다.
  
    - (1) 탐욕 선택 속성 (Greedy Choice Property)
      - “지금 한 선택이” 나중에 발목을 잡지 않고  
        **전체에서도 최선의 결과로 이어진다**는 성질
  
    - (2) 최적 부분 구조 (Optimal Substructure)
      - 전체 문제의 최적해가 **부분 문제의 최적해**로 이루어진다는 성질
      - 즉, 큰 문제를 줄여가도 “남은 문제도 같은 방식으로 최적”이어야 한다
  
    - ※ 중학생 버전으로 한 줄 요약
      - “지금 잘 고르면, 끝까지 계속 잘 고르게 되는 문제”에서 탐욕이 통한다.

  - 대표 예시 1) 거스름돈 문제 (탐욕이 잘 통하는 대표)
    - 문제
      - 860원을 거슬러 줄 때
      - 동전: 500원, 100원, 50원, 10원
      - 동전 개수를 최소로 하려면?
  
    - 탐욕 아이디어
      - “남은 돈보다 작거나 같은 동전 중 **가장 큰 것**부터 쓰자”
  
    - 손으로 따라가기
      - 860 → 500 사용 (남은 360)
      - 360 → 100 사용 3개 (남은 60)
      - 60 → 50 사용 1개 (남은 10)
      - 10 → 10 사용 1개 (남은 0)
      - 총 동전 개수 = 1 + 3 + 1 + 1 = 6개
  
    - 예시 코드
      ```python
      money = 860
      coins = [500, 100, 50, 10]  # 큰 동전부터
      cnt = 0
  
      for c in coins:
          use = money // c      # 이 동전을 몇 개 쓸지
          cnt += use
          money %= c            # 남은 돈
  
      print(cnt)
  
      # 실행 결과: 6
      ```
  
    - 특징
      - “큰 단위부터 쓰는 게 항상 손해가 아니다”가 보장되는 동전 체계(예: 한국 화폐)라서 탐욕이 잘 통한다.
  
  - 대표 예시 2) 회의실 배정 (탐욕의 ‘정렬 + 선택’ 느낌)
    - 문제(느낌)
      - 회의가 여러 개 있고, 각 회의는 (시작시간, 끝시간)이 있다
      - 한 회의실에서 겹치지 않게 회의를 최대 몇 개까지 할 수 있을까?
  
    - 탐욕 아이디어(가장 유명한 규칙)
      - “가장 빨리 끝나는 회의부터 선택하자”
      - 이유(감각)
        - 빨리 끝나는 회의를 먼저 잡으면 뒤에 회의를 더 많이 넣을 기회가 생김
  
    - 예시 데이터
      - meetings = [(1, 4), (2, 3), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
  
    - 선택 과정(요약)
      - 끝나는 시간 기준으로 정렬
      - 겹치지 않으면 선택
      - 선택한 회의의 끝시간을 기준으로 다음을 고름
  
    - 예시 코드
      ```python
      meetings = [(1, 4), (2, 3), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
  
      # (끝시간, 시작시간)으로 정렬하면 “끝이 빠른 순”이 됨
      meetings.sort(key=lambda x: x[1])
  
      count = 0
      end_time = -1
  
      for s, e in meetings:
          if s >= end_time:     # 안 겹치면 선택
              count += 1
              end_time = e
  
      print(count)
  
      # 실행 결과: 4
      # (예: (2,3) -> (3,5) -> (5,7) -> (8,9))
      ```
  
    - 특징
      - “정렬한 뒤, 조건을 만족하면 선택” 형태가 탐욕 문제에서 정말 자주 나온다.
  
  - 대표 예시 3) 최소 동전 개수 (탐욕이 실패할 수 있는 예)
    - 왜 실패 예가 필요할까?
      - 탐욕은 “항상 맞다”가 아니라 “맞는 문제에서만 맞다”
      - 그래서 실패 예를 1개 알고 있으면, 문제를 볼 때 더 안전해진다
  
    - 동전 체계가 이렇게 이상하다고 해보자
      - coins = [10, 6, 1]
      - 목표 money = 12
  
    - 탐욕 방식(가장 큰 동전부터)
      - 12에서 10을 먼저 씀 (남은 2)
      - 2는 1 + 1
      - 총 3개 (10 + 1 + 1)
  
    - 하지만 더 좋은 답이 있음
      - 6 + 6 = 2개  ✅
      - 탐욕은 정답(최소 개수)을 놓쳤다 ❌
  
    - 예시 코드(탐욕 결과 확인)
      ```python
      money = 12
      coins = [10, 6, 1]
      cnt = 0
  
      for c in coins:
          use = money // c
          cnt += use
          money %= c
  
      print(cnt)
  
      # 실행 결과: 3   (하지만 최적은 2)
      ```
  
    - 결론
      - “가장 큰 동전부터” 규칙이 항상 정답이 되는 건 아니다.
      - 문제에서 **탐욕이 통하는 구조(조건)** 가 있는지 확인해야 한다.
  
  - 탐욕 알고리즘 문제를 만났을 때 체크리스트 (혼공용)
    - 1) “매 순간 선택”이 존재하는 문제인가?
      - 예: 동전 선택, 회의 선택, 구간 선택, 물건 선택 등
  
    - 2) “좋아 보이는 기준”을 하나 정할 수 있는가?
      - 예: 가장 큰 값, 가장 작은 값, 가장 빨리 끝나는 것, 비율이 가장 큰 것 등
  
    - 3) 정렬이 필요한가?
      - 탐욕 문제는 정렬로 시작하는 경우가 많다. (O(N log N) 패턴)
  
    - 4) 반례가 있는지 떠올려보기
      - 작은 숫자로 직접 손으로 몇 케이스 해보면 반례가 금방 나올 때가 있다.
  
  - 시간 복잡도 (감각)
    - 탐욕은 보통
      - 정렬이 있으면: O(N log N)
      - 정렬이 없고 한 번 훑으면: O(N)
    - 완전탐색처럼 경우의 수 폭발을 피하는 게 큰 장점이다.
  
  - 특징 요약
    - 장점
      - 빠른 경우가 많다
      - 구현이 비교적 간단하다
      - 직관적으로 설계하기 쉬운 문제가 있다(회의실 배정, 거스름돈 등)
  
    - 단점
      - 항상 정답을 보장하지 않는다
      - “탐욕 기준”을 잘못 잡으면 틀린 답이 나올 수 있다
      - 반례가 존재하는지 검토가 필요하다


- 분할 정복 (Divide and Conquer)
  - 개념  
    - 문제를 **작은 문제로 나누고**, 각각 해결한 뒤 합치는 방법

  - 설명  
    - 같은 형태의 작은 문제를 반복해서 해결  
    - 재귀 구조로 구현되는 경우가 많다  

  - 사용 느낌  
    - "쪼개고 → 해결하고 → 합친다"

  - 시간 복잡도 특징  
    - O(N log N) 구조가 자주 등장

  - 대표 예시  
    - 병합 정렬 (Merge Sort)  
    - 퀵 정렬 (Quick Sort)
    - 선택 알고리즘
    - 이진 탐색  
  
  - 선택 알고리즘 (Selection Algorithm, Quick Select)

    - 개념
      - 전체를 정렬하지 않고 **k번째로 작은(또는 큰) 원소를 찾는 알고리즘**
      - 퀵 정렬과 같은 "피벗 기준 분할" 아이디어를 사용한다

    - 왜 필요한가?
      - 정렬하면 O(N log N)이 걸리지만  
        k번째 값 하나만 필요하면 더 빠르게 찾을 수 있다
      - 예:
        - 시험 점수 중 3등 점수 찾기
        - 데이터의 중앙값(Median) 찾기

    - 핵심 아이디어
      1. 배열에서 피벗(pivot) 하나 선택
      2. 피벗보다 작은 값은 왼쪽, 큰 값은 오른쪽으로 분할
      3. 피벗의 위치가 k와 같으면 정답
      4. k가 왼쪽에 있으면 왼쪽 부분만 다시 탐색
      5. k가 오른쪽에 있으면 오른쪽 부분만 탐색

      👉 전체를 정렬하지 않고 필요한 구간만 계속 줄여간다

    - 예시

      ```python
      arr = [7, 2, 1, 6, 8, 5, 3, 4]
      k = 3  # 3번째로 작은 수

      # 정렬하면: [1,2,3,4,5,6,7,8]
      # 정답: 3
      ```

    - 예시 코드 (Quick Select)

      ```python
      import random

      def quick_select(arr, k):
          if len(arr) == 1:
              return arr[0]

          pivot = random.choice(arr)

          left = [x for x in arr if x < pivot]
          mid = [x for x in arr if x == pivot]
          right = [x for x in arr if x > pivot]

          if k <= len(left):
              return quick_select(left, k)
          elif k <= len(left) + len(mid):
              return pivot
          else:
              return quick_select(right, k - len(left) - len(mid))


      arr = [7, 2, 1, 6, 8, 5, 3, 4]
      print(quick_select(arr, 3))  # 3
      ```

    - 시간 복잡도
      - 평균: O(N)
      - 최악: O(N²) (피벗이 계속 한쪽으로 치우칠 때)

    - 특징
      - 정렬 없이 순위 기반 값을 찾을 수 있다
      - 퀵 정렬과 구조가 매우 비슷하다
      - 중앙값 찾기 문제와 연결된다
      - "k번째"라는 말이 나오면 떠올려야 하는 알고리즘
  
- 동적 계획법 (Dynamic Programming, DP)

  - 개념
    - 큰 문제를 작은 문제로 나누어 해결하고,
      그 결과를 저장하여 다시 사용하지 않도록 하는 알고리즘 기법
  
  - 사용 조건
    1. **중복되는 부분 문제 (Overlapping Subproblems)**
    2. **최적 부분 구조 (Optimal Substructure)**
  
  - Memoization과의 차이
    
    | 구분 | Memoization | DP |
    |------|-------------|----|
    | 방식 | 재귀 기반 (Top-Down) | 반복문 기반 (Bottom-Up) |
    | 계산 순서 | 필요할 때 계산 | 작은 문제부터 차례로 계산 |
  
  - 예시 1: 피보나치 수열 (DP 방식)
  
  ```python
  def fib(n):
      dp = [0] * (n + 1)
      dp[1] = dp[2] = 1
  
      for i in range(3, n + 1):
          dp[i] = dp[i-1] + dp[i-2]
  
      return dp[n]
  
  
  print(fib(10))  # 55
  ```
  
  - 예시 2: 계단 오르기 문제
    - 한 번에 1칸 또는 2칸 오를 수 있을 때  
      n칸을 오르는 방법의 수 구하기
  
  ```python
  def climb(n):
      dp = [0] * (n + 1)
      dp[1], dp[2] = 1, 2
  
      for i in range(3, n + 1):
          dp[i] = dp[i-1] + dp[i-2]
  
      return dp[n]
  
  
  print(climb(5))  # 8
  ```
  
  - 시간 복잡도
    - 대부분 O(N) 또는 O(N²)
    - 중복 계산 제거가 핵심
  
  - 특징 요약
    - 재귀의 비효율을 해결한 기법
    - "최적해", "최소/최대", "경우의 수" 문제에 자주 등장
    - 메모이제이션과 같은 개념에서 출발하지만 구현 방식이 다름

- 백트래킹 (Backtracking)
  - 개념  
    - 완전탐색을 하되, **아닌 길은 중간에 되돌아오는 방법**

  - 설명  
    - 해가 될 가능성이 없는 경우는 더 이상 탐색하지 않음  
    - 가지치기(Pruning)를 통해 탐색 수를 줄인다  

  - 사용 느낌  
    - "가다가 아니면 돌아가자"

  - 시간 복잡도 특징  
    - 최악은 완전탐색과 비슷하지만, 실제론 훨씬 줄어듦

  - 대표 예시  
    - N-Queen 문제  
    - 스도쿠 풀이

- 그래프 탐색 (Graph Traversal)
  - 개념  
    - 그래프 구조에서 노드를 방문하며 탐색하는 방법

  - 설명  
    - 연결 관계를 따라가며 탐색  
    - 자료구조(스택, 큐)를 활용한다

  - 사용 느낌  
    - "연결된 곳을 따라가 보자"

  - 대표 알고리즘  
    - DFS (깊이 우선 탐색)  
    - BFS (너비 우선 탐색)
  - 위상정렬 (Topological Sort)
    - what?
      - 방향 그래프에서 “선후 관계(의존성)”를 지키면서 노드를 나열하는 방법
      - 반드시 **DAG (Directed Acyclic Graph)** 에서만 가능
      - 사이클이 존재하면 위상정렬 불가능
  
    - 언제 쓰나?
      - 선수 과목 문제
      - 작업 순서 결정
      - 빌드 순서
      - 이벤트 처리 순서
  
    - 핵심 개념
      - 진입차수 (in-degree)
        - 한 노드로 들어오는 간선 개수
        - 진입차수 0 → 지금 당장 수행 가능
      - 모든 선행 조건이 끝나야 다음 작업 가능
      - 진입차수 0이 여러 개면 여러 정답 존재 가능
  
    - 예시 그래프
      - 1 → 3
      - 2 → 3
      - 3 → 4
      - 2 → 5
      - 5 → 4
  
    - 코드 구현 (Kahn 알고리즘)
      ```py
      from collections import deque
  
      n = 5
      edges = [
          (1, 3),
          (2, 3),
          (3, 4),
          (2, 5),
          (5, 4)
      ]
  
      graph = [[] for _ in range(n + 1)]
      indegree = [0] * (n + 1)
  
      for a, b in edges:
          graph[a].append(b)
          indegree[b] += 1
  
      queue = deque()
  
      for i in range(1, n + 1):
          if indegree[i] == 0:
              queue.append(i)
  
      result = []
  
      while queue:
          now = queue.popleft()
          result.append(now)
  
          for next_node in graph[now]:
              indegree[next_node] -= 1
              if indegree[next_node] == 0:
                  queue.append(next_node)
  
      print(result)
      ```
  
      실행 결과:
      ```
      [1, 2, 3, 5, 4]
      ```
      (1과 2의 순서에 따라 다른 결과가 나올 수도 있음)
  
    - 사이클 판별
      ```py
      if len(result) != n:
          print("사이클 존재")
      ```
  
      예시 (사이클 존재하는 경우)
      ```py
      n = 3
      edges = [(1, 2), (2, 3), (3, 1)]
      ```
  
      실행 결과:
      ```
      []
      사이클 존재
      ```
  
    - 시간 복잡도
      - O(V + E)
        - V: 노드 개수
        - E: 간선 개수
  
    - 이해 포인트
      - 큐에는 항상 “지금 당장 가능한 것”이 들어간다
      - 부모 하나가 아니라 “모든 부모”가 끝나야 가능
      - 순서가 여러 개 존재할 수 있다
    
- 한눈에 비교

  | 전략 | 핵심 아이디어 | 대표 키워드 |
  |------|----------------|-------------|
  | 완전 탐색 | 전부 다 시도 | 순열, 조합 |
  | 탐욕 알고리즘 | 지금 최선 선택 | 정렬, 선택 |
  | 분할 정복 | 나눠서 해결 후 합침 | 재귀 |
  | 동적 계획법 | 결과 저장 후 재사용 | DP 테이블 |
  | 백트래킹 | 되돌아가기 | 가지치기 |
  | 그래프 탐색 | 연결 따라 탐색 | DFS, BFS |

# 라이브러리

## Numpy
- Numpy를 왜 쓰나?

  - 파이썬 리스트도 숫자 배열을 담을 수 있지만, Numpy는 **대량의 숫자 계산**을 빠르게 하기 위해 만들어졌어요.
    - 내부적으로 C로 최적화되어 있고, 벡터/행렬 연산이 강함
    - 데이터 분석/머신러닝에서 Pandas의 바닥 데이터로도 자주 쓰임

- Numpy란?
  - 내용, 설명  
    - 수치 계산을 빠르게 수행하기 위한 파이썬 라이브러리
    - 핵심 객체는 다차원 배열인 `ndarray`
    - 파이썬 리스트보다 메모리 사용이 효율적이고, 벡터 연산이 가능해 속도가 빠름
    - 데이터 과학, 머신러닝, 통계 계산의 기본 도구
- starting
  - Numpy 설치하기
    - 내용, 설명  
      - Numpy는 기본 파이썬에 포함되어 있지 않음
      - 한 번만 설치하면 이후 계속 사용 가능
    - 설치 명령어 (터미널에서 실행)
      ```bash
      pip install numpy
      ```
    - 설치 확인
      ```bash
      pip show numpy
      ```
  - Numpy 불러오기 (import)
    - 내용, 설명  
      - 설치한 라이브러리를 코드에서 사용하려면 `import` 필요
      - 보통 관례적으로 `np`라는 별칭을 사용
    - 예시 코드
      ```py
      import numpy as np
      ```
    - 왜 `np`라고 쓰는가?
      - 내용, 설명  
        - numpy를 계속 쓰기엔 길어서 줄여 쓰는 관례
        - 전 세계적으로 통용되는 표준 약속이라 그대로 따르는 게 좋음
  - 첫 번째 Numpy 배열 만들어보기
    - 내용, 설명  
      - 리스트를 numpy 배열로 바꾸는 것이 가장 기본 시작점
    - 예시 코드
      ```py
      import numpy as np

      arr = np.array([1, 2, 3, 4])
      print(arr)
      # 출력: [1 2 3 4]
      ```
    - 리스트와의 차이 확인
      ```py
      arr = np.array([1, 2, 3])
      print(arr * 2)
      # 출력: [2 4 6]  ← 리스트와 다르게 각 요소가 곱해짐
      ```
- advanced
  - 개념 
    - Numpy는 숫자 계산을 빠르게 하는 라이브러리
    - 반드시 `pip install numpy`로 설치 후 사용
    - 코드에서는 `import numpy as np`로 불러옴
    - 리스트 대신 `np.array()`를 쓰는 순간부터 Numpy 시작
  - 배열 생성
    - 내용, 설명  
      - 리스트와 달리 Numpy 배열은 모든 요소가 같은 자료형을 가지며, 연속된 메모리 공간에 저장됨
      - 이 구조 덕분에 대량 연산이 빠르게 수행됨
    - 리스트를 numpy 배열로 변환
      ```py
      import numpy as np

      arr = [1, 2, 3, 4, 5]
      np_arr = np.array(arr)
      print(np_arr)
      # 출력: [1 2 3 4 5]
      ```
    - 연속된 숫자 배열 생성
      ```py
      np.arange(10)          # 0~9
      np.arange(10, 30, 5)   # 10~25, 5씩 증가
      ```
    - 다차원 배열 생성
      ```py
      arr = np.arange(15).reshape(3, 5)
      print(arr)
      # 출력:
      # [[ 0  1  2  3  4]
      #  [ 5  6  7  8  9]
      #  [10 11 12 13 14]]
      ```
    - 특정 값으로 채운 배열
      ```py
      np.zeros((2, 3))   # 0으로 채움
      np.ones((2, 3))    # 1로 채움
      np.full((2, 3), 7) # 7로 채움
      ```
    - 균일 간격 수 생성
      ```py
      np.linspace(-5, 5, 5)
      # 출력: [-5.  -2.5  0.   2.5  5. ]
      ```
    - 난수 배열 생성
      ```py
      rng = np.random.default_rng()
      rng.random(3)
      rng.integers(0, 10, 5)
      ```
  - 배열 기본 속성
    - 내용, 설명  
      - Numpy 배열은 “모양(shape)”과 “차원(ndim)” 개념이 중요
      - 배열의 구조와 메모리 특성을 파악할 때 사용
    ```py
    arr = np.arange(12).reshape(3, 4)
    arr.shape      # (3, 4)
    arr.ndim       # 2
    arr.dtype      # 데이터 타입
    arr.size       # 전체 원소 개수
    arr.itemsize   # 한 원소 바이트 크기
    ```
  - Indexing & Slicing
    - 내용, 설명  
      - Numpy 배열은 다차원 인덱싱이 가능하며, 슬라이싱으로 부분 배열 추출 가능
      - 슬라이싱 결과는 “뷰(view)”인 경우가 많아 원본과 메모리를 공유할 수 있음

    ```py
    arr[1, 2]        # 2행 3열 값
    arr[:, :2]       # 모든 행, 앞 2열
    arr[1:3, ::2]    # 행 슬라이스 + 열 간격 슬라이스
    ```
  - 배열 복사
    - 내용, 설명  
      - 단순 대입은 같은 배열을 가리키는 참조 복사
      - `.copy()`를 사용해야 완전히 독립된 배열이 생성됨

    ```py
    arr2 = arr        # 얕은 복사 (같은 메모리 공유)
    arr3 = arr.copy() # 깊은 복사
    ```
  - 조건 처리와 필터링
    - 내용, 설명  
      - Numpy는 반복문 없이 조건 기반 연산을 수행하는 벡터화 연산이 강력함

    ```py
    a = np.array([1, 5, 0, -2])
    np.where(a == 0, 999, a)

    x = np.array([-5, 2, 10, 20])
    np.clip(x, 0, 10)

    a = np.array([3, 1, 4, 1, 5])
    a[a >= 4]
    ```
  - 통계 및 유틸리티 함수
    - 내용, 설명  
      - 결측치(NaN)를 포함한 데이터 처리를 위한 함수 제공
      - 데이터 분석에서 자주 사용

    ```py
    arr = np.array([1., 2., np.nan, 4.])
    np.nanmean(arr)

    labels = np.array(['A', 'B', 'A', 'C'])
    np.unique(labels, return_counts=True)
    ```
  - 배열 결합
    - 내용, 설명  
      - 여러 배열을 행 방향 또는 열 방향으로 합칠 수 있음

    ```py
    a = np.array([[1,2],[3,4]])
    b = np.array([[5,6],[7,8]])

    np.vstack((a,b))
    np.hstack((a,b))
    ```

## Pandas
- Pandas를 왜 쓰나?

  - Pandas는 **표 형태(엑셀 같은)** 데이터를 다루는 데 특화된 라이브러리예요.
    - `DataFrame`(표), `Series`(한 열) 중심
    - 결측치 처리, 그룹 연산, 시간 데이터 처리 등이 강점


- Pandas란?
  - 내용, 설명  
    - 표 형태의 데이터를 다루기 위한 파이썬 라이브러리
    - 엑셀과 비슷한 구조로 데이터를 분석할 수 있음
    - 핵심 자료형은 Series(1차원)와 DataFrame(2차원)


- 기초

  
  - Pandas 불러오기
    ```py
    import pandas as pd
    ```
  - Series 생성
    - 내용, 설명  
      - 1차원 데이터 구조
      - 인덱스 + 값 구조
    ```py
    s = pd.Series([10, 20, 30])
    print(s)
    # 출력:
    # 0    10
    # 1    20
    # 2    30
    # dtype: int64
    ```
    - 주의점  
      - 리스트와 다르게 인덱스가 함께 존재
  - DataFrame 생성
    - 내용, 설명  
      - 2차원 테이블 구조
      - 열(column)은 각각 Series로 구성됨
    ```py
    data = {"name": ["Alice", "Bob"], "age": [25, 30]}
    df = pd.DataFrame(data)
    print(df)
    # 출력:
    #     name  age
    # 0  Alice   25
    # 1    Bob   30
    ```
  - 데이터 확인 함수
    - 원리  
      - 데이터 구조와 상태를 빠르게 파악하기 위한 함수들
    ```py
    df.head()      # 상위 5행
    df.info()      # 데이터 타입과 결측치
    df.describe()  # 숫자형 통계 요약
    ```
  - 열 선택
    ```py
    df["name"]
    # 출력: name 열 Series
  
    df[["name","age"]]
    # 출력: 두 열로 구성된 DataFrame
    ```
    - 주의점  
      - 대괄호 2개 쓰면 DataFrame 유지
  - 행 선택 (loc vs iloc)
    - loc → 인덱스 기준 / iloc → 위치 기준
    ```py
    df.loc[0]
    df.iloc[0]
    ```
    - 주의점  
      - loc은 라벨, iloc은 숫자 위치
  - 조건 필터링
    ```py
    df[df["age"] > 25]
    # 출력: age가 25 초과인 행만 표시
    ```
    - 원리  
      - 조건식이 True인 행만 남김
  - 결측치 처리
    ```py
    df.isnull()
    df.dropna()
    df.fillna(0)
    ```
    - 주의점  
      - dropna()는 기본적으로 행 삭제

- 고급
  
  - 열 추가
    ```py
    df["age_plus_5"] = df["age"] + 5
    ```
    - 원리  
      - 벡터 연산으로 전체 열에 적용됨
  - 정렬
    ```py
    df.sort_values("age")
    ```
    - 주의점  
      - 원본 변경 안 됨 → 필요시 inplace=True
  - 그룹 연산 (groupby)
    - 원리  
      - 특정 기준으로 묶고 집계 수행
    ```py
    df.groupby("name")["age"].mean()
    ```
    - 출력: 이름별 평균 나이
  - 여러 집계
    ```py
    df.groupby("name")["age"].agg(["mean","max"])
    ```
  - 병합 (merge)
    - 원리  
      - SQL의 JOIN과 동일한 개념
    ```py
    pd.merge(df1, df2, on="id", how="inner")
    ```
  - 연결 (concat)
    ```py
    pd.concat([df1, df2])        # 행 방향
    pd.concat([df1, df2], axis=1) # 열 방향
    ```
  - 피벗 테이블
    ```py
    df.pivot_table(values="age", index="name", aggfunc="mean")
    ```
  - 문자열 처리
    ```py
    df["name"].str.upper()
    ```
  - 날짜 처리
    ```py
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year
    ```

## Matplotlib
- Matplotlib의 포인트
  - Matplotlib는 데이터 시각화(그래프)를 위한 기본 라이브러리예요.
    - 흐름: 데이터 준비 → `plt.plot/scatter/bar/...` → `plt.title/xlabel/ylabel` → `plt.show()`
    - 그래프가 안 뜨면(주로 노트북/환경 문제) `plt.show()` 호출 여부부터 체크

- Matplotlib란?
  - 내용, 설명  
    - 파이썬에서 그래프를 그리기 위한 시각화 라이브러리
    - 데이터 분석 결과를 시각적으로 표현할 때 사용
    - Pandas, Numpy와 함께 자주 사용됨
- 기초
  - 설치 및 import
    ```bash
    pip install matplotlib
    ```
    ```py
    import matplotlib.pyplot as plt
    ```
    - 설명  
      - `pyplot` 모듈을 `plt`라는 이름으로 사용하는 것이 관례
  - 기본 선 그래프 (Line Plot)
    - 원리  
      - x축과 y축 값을 선으로 연결하여 변화 흐름을 표현
    ```py
    x = [1, 2, 3, 4]
    y = [10, 20, 25, 30]

    plt.plot(x, y)
    plt.show()
    ```
    - 출력  
      - 점들이 선으로 연결된 그래프 표시
    - 주의점  
      - `plt.show()`를 호출해야 그래프가 화면에 나타남
  - 그래프 제목과 축 이름
    ```py
    plt.plot(x, y)
    plt.title("Sample Graph")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.show()
    ```
  - 범례(legend) 추가
    ```py
    y2 = [15, 18, 22, 28]

    plt.plot(x, y, label="Line A")
    plt.plot(x, y2, label="Line B")
    plt.legend()
    plt.show()
    ```
- 다양한 그래프 종류
  - 막대 그래프 (Bar Chart)
    - 원리  
      - 범주형 데이터 비교에 사용
    ```py
    categories = ["A", "B", "C"]
    values = [5, 7, 3]

    plt.bar(categories, values)
    plt.show()
    ```
  - 산점도 (Scatter Plot)
    - 원리  
      - 두 변수 간의 관계를 점으로 표현
    ```py
    x = [1,2,3,4,5]
    y = [2,3,5,7,11]

    plt.scatter(x, y)
    plt.show()
    ```
  - 히스토그램 (Histogram)
    - 원리  
      - 데이터 분포를 구간별 빈도로 표시

    ```py
    data = [1,2,2,3,3,3,4,4,5]
    plt.hist(data, bins=5)
    plt.show()
    ```
  - 파이 차트 (Pie Chart)
    ```py
    sizes = [30, 40, 20, 10]
    labels = ["A", "B", "C", "D"]

    plt.pie(sizes, labels=labels, autopct="%1.1f%%")
    plt.show()
    ```
- 스타일 설정
  - 선 스타일, 색상, 마커

    ```py
    plt.plot(x, y, color="red", linestyle="--", marker="o")
    plt.show()
    ```
  - 그래프 크기 조절

    ```py
    plt.figure(figsize=(6,4))
    plt.plot(x, y)
    plt.show()
    ```
- 여러 그래프 한 화면에
  - 서브플롯 (subplot)

    ```py
    plt.subplot(1,2,1)
    plt.plot(x, y)
    plt.title("Left")

    plt.subplot(1,2,2)
    plt.bar(categories, values)
    plt.title("Right")

    plt.show()
    ```
- 핵심 정리
  - Matplotlib은 데이터 시각화 도구
  - 기본은 `plt.plot()` + `plt.show()`
  - 그래프 종류에 따라 bar, scatter, hist, pie 사용
  - 제목, 축 이름, 범례를 넣으면 가독성이 좋아짐

## collections
- 파이썬 **표준 라이브러리** 모듈로, 자주 쓰는 자료구조를 더 편하게/빠르게 쓰기 위한 도구 모음
- 핵심 포인트
  - `Counter` : 요소 빈도(개수) 세기
  - `deque` : 양방향 큐(앞/뒤 삽입·삭제가 빠름) → BFS에서 자주 사용

- 예시
```py
from collections import Counter, deque

print(Counter("banana"))
# Counter({'a': 3, 'n': 2, 'b': 1})

dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(dq)
# deque([0, 1, 2, 3, 4])
```

## itertools
- 반복 가능한 객체(iterable)를 **조합/순열** 같은 패턴으로 다루는 표준 라이브러리 모듈
- 자주 쓰는 것
  - `permutations` : 순열(순서 O)
  - `combinations` : 조합(순서 X)

- 예시
```py
from itertools import permutations, combinations

print(list(permutations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

print(list(combinations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 3)]
```

## pathlib (Path)
- 파일/폴더 경로를 문자열로 다루지 않고, **객체로 안전하게** 다루는 표준 라이브러리
- 자주 하는 일
  - 존재 확인: `Path(...).exists()`
  - 경로 합치기: `/` 연산자
  - 확장자 확인: `.suffix`

- 예시
```py
from pathlib import Path

p = Path("data") / "input.txt"
print(p)           # data/input.txt
print(p.suffix)    # .txt
print(p.exists())  # True/False
```

## datetime
- 날짜/시간을 다루는 표준 라이브러리
- 자주 하는 일
  - 현재 시각: `datetime.now()`
  - 문자열 ↔ datetime 변환: `strptime` / `strftime`
  - 시간 차이 계산: `timedelta`

- 예시
```py
from datetime import datetime, timedelta

now = datetime.now()
print(now)

parsed = datetime.strptime("2026-02-10", "%Y-%m-%d")
print(parsed)

print((now + timedelta(days=7)).date())
```

## random
- 난수(랜덤)를 다루는 표준 라이브러리
- 자주 하는 일
  - 정수 뽑기: `randint(a, b)` (a~b 포함)
  - 섞기: `shuffle`
  - 샘플링: `sample`

- 예시
```py
import random

print(random.randint(1, 6))  # 1~6

arr = [1, 2, 3, 4, 5]
random.shuffle(arr)
print(arr)

print(random.sample([1, 2, 3, 4, 5], 2))
```

## logging
- `print()` 대신 **로그 레벨/형식**을 갖춘 기록을 남기는 표준 라이브러리
- 로그 레벨(대표)
  - DEBUG / INFO / WARNING / ERROR / CRITICAL

- 예시
```py
import logging

logging.basicConfig(level=logging.INFO)
logging.info("INFO 로그")
logging.warning("WARNING 로그")
```
