[파이썬](#python-study-notes)

[cli](#cli-기본-명령어)

[git](#git-활용법-정리-기능--예시)

[markdown](#markdown--readme-작성법-정리)




---

## 목차
- [Python Study Notes](#python-study-notes)
  - [Basic](#basic)
  - [변수와 자료형](#변수와-자료형)
  - [함수(Function)](#함수function)
  - [모듈](#모듈)
  - [제어문](#제어문)
  - [method](#method)
  - [class](#클래스)
  - [상속](#상속-inheritance)
  - [Python으로 “클라이언트 → 서버 요청” 정리 (requests 중심)](#python으로-클라이언트--서버-요청-정리-requests-중심)
- [CLI 기본 명령어](#cli-기본-명령어)
- [Git 활용법 정리 (기능 + 예시)](#git-활용법-정리-기능--예시)
- [Markdown / README 작성법 정리](#markdown--readme-작성법-정리)

---
# Python Study Notes

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
    - 변수는 특정 객체를 가리치는 이름표
  - 재할당 : 변수가 가리키는 대상을 새로운 값으로 변경하는 행위
    ```python
    number = 10
    double = 2*number
    print(double) # 20

    number = 5
    print(double) # 20
    ```
    - 즉 , 객체란 실제 사람, 메모리 주소는 사람이 사는 주소, 변수는 사람의 주소록 상 이름표
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

  - Data type : 값의 종류와 그 값으로 할 수 있는 동작(연산) 결정 속성
    - numeric type : int, float. complex
    - text sequence type : str
    - sequence type : list tuple, range
    - non-sequence type : set, dict
    - others : Boolean, None, Functions

## 변수와 자료형
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
        ```
        1 apple
        2 banana
        ```
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
      ```py
      $ pip install requests

      import requests

      url = "사이트 주소"
      response = requests.get(url).json()
      print(response)
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
        if % 2 == 0 :
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
      ```python
      def func():
          pass

      func()
      # 출력: None (아무것도 반환하지 않음)
      ```
      - 메서드
      ```py
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
          ```py
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
    def wapping(v):
        print('shine'*3)
        func(v)
        print('화이팅'*3)
    return wapping

    @deco
    def call_name(name):
        print(name)
        
    @deco
    def call_age(age):
        print(age)

    call_name('세진')
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

---
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

---
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


---
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
      ```python
      print("hello")
      ```
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
