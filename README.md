[파이썬](#python-study-notes)

[cli](#cli-기본-명령어)

[git](#git-활용법-정리-기능--예시)

[markdown](#markdown--readme-작성법-정리)




---

## 목차
- [Python Study Notes](#python-study-notes)
  - [Basic](#basic)
  - [변수와 자료형](#변수와-자료형)
  - [조건문 (if / elif / else) + 중첩 조건문](#조건문-if--elif--else--중첩-조건문)
  - [반복문 (for / while / break / continue / pass)](#반복문-for--while--break--continue--pass)
  - [함수(Function) 기본: 정의/호출/return](#함수function-기본-정의호출return)
  - [함수 인자(Arguments) 종류 정리](#함수-인자arguments-종류-정리)
  - [스코프(Scope) \& 전역변수 global (LEGB Rule)](#스코프scope--전역변수-global-legb-rule)
  - [패킹/언패킹 (Packing / Unpacking)](#패킹언패킹-packing--unpacking)
  - [모듈 import 사용법 (import / from / as)](#모듈-import-사용법-import--from--as)
  - [내장함수: map / zip / filter / enumerate](#내장함수-map--zip--filter--enumerate)
    - [map](#map)
    - [zip](#zip)
    - [filter](#filter)
    - [enumerate](#enumerate)
  - [lambda (익명 함수)](#lambda-익명-함수)
  - [재귀(Recursion)](#재귀recursion)
  - [method](#method)
    - [method란?](#method란)
      - [정의](#정의)
      - [호출 방식](#호출-방식)
    - [공통 시퀀스 메서드](#공통-시퀀스-메서드)
      - [`.index()`](#index)
        - [설명](#설명)
        - [예시 코드](#예시-코드)
      - [`.count()`](#count)
        - [설명](#설명-1)
        - [예시 코드](#예시-코드-1)
    - [문자열 탐색 및 검증 메서드](#문자열-탐색-및-검증-메서드)
      - [`.find()`](#find)
      - [`.isupper()` / `.islower()`](#isupper--islower)
      - [`.isalpha()`](#isalpha)
    - [문자열 조작 메서드](#문자열-조작-메서드)
      - [`.replace()`](#replace)
      - [`.strip()`](#strip)
      - [`.split()`](#split)
      - [`.join()`](#join)
    - [리스트 값 추가 및 삭제 메서드](#리스트-값-추가-및-삭제-메서드)
      - [`.append()`](#append)
      - [`.extend()`](#extend)
      - [`.insert()`](#insert)
      - [`.remove()` / `.pop()` / `.clear()`](#remove--pop--clear)
    - [리스트 정렬 및 순서 변경](#리스트-정렬-및-순서-변경)
      - [`.reverse()`](#reverse)
      - [`.sort()`](#sort)
    - [메서드 체이닝](#메서드-체이닝)
      - [정의](#정의-1)
        - [예시 코드](#예시-코드-2)
      - [흔한 실수](#흔한-실수)
      - [올바른 방법](#올바른-방법)
    - [숫자 판별 메서드 비교](#숫자-판별-메서드-비교)
  - [Python으로 “클라이언트 → 서버 요청” 정리 (requests 중심)](#python으로-클라이언트--서버-요청-정리-requests-중심)
    - [0) 용어 한눈에 보기](#0-용어-한눈에-보기)
    - [1) requests 설치 및 기본 사용 흐름](#1-requests-설치-및-기본-사용-흐름)
    - [2) GET 요청: 서버에서 “조회”하기](#2-get-요청-서버에서-조회하기)
    - [3) POST 요청: 서버에 “생성/전송”하기 (JSON 바디)](#3-post-요청-서버에-생성전송하기-json-바디)
    - [4) POST 요청: form 데이터 전송 (`data=`)](#4-post-요청-form-데이터-전송-data)
    - [5) 헤더(headers): 인증/콘텐츠 타입/커스텀 헤더](#5-헤더headers-인증콘텐츠-타입커스텀-헤더)
    - [6) 상태코드와 에러 처리: raise\_for\_status()](#6-상태코드와-에러-처리-raise_for_status)
    - [7) 응답(response) 다루기: text / json / headers / encoding](#7-응답response-다루기-text--json--headers--encoding)
    - [8) timeout과 재시도(기본 전략)](#8-timeout과-재시도기본-전략)
    - [9) Session 사용: 쿠키/연결 재사용(성능/로그인 유지)](#9-session-사용-쿠키연결-재사용성능로그인-유지)
    - [10) 파일 다운로드/업로드 기초](#10-파일-다운로드업로드-기초)
      - [10-1) 다운로드(간단)](#10-1-다운로드간단)
      - [10-2) 업로드(파일 전송)](#10-2-업로드파일-전송)
    - [11) 실전 템플릿: 안전한 요청 함수 만들기](#11-실전-템플릿-안전한-요청-함수-만들기)
    - [참고 (연습용 테스트 API)](#참고-연습용-테스트-api)
- [CLI 기본 명령어](#cli-기본-명령어)
  - [1) `pwd`](#1-pwd)
  - [2) `ls`](#2-ls)
  - [3) `cd`](#3-cd)
  - [4) `mkdir`](#4-mkdir)
  - [5) `touch`](#5-touch)
  - [6) `cat`](#6-cat)
  - [7) `echo`](#7-echo)
  - [8) `cp`](#8-cp)
  - [9) `mv`](#9-mv)
  - [10) `rm`](#10-rm)
  - [11) `clear`](#11-clear)
  - [12) `history`](#12-history)
  - [추가 팁: 경로 기호 정리](#추가-팁-경로-기호-정리)
- [Git 활용법 정리 (기능 + 예시)](#git-활용법-정리-기능--예시)
  - [0) Git 작업 흐름 한눈에 보기](#0-git-작업-흐름-한눈에-보기)
  - [1) `git init` : Git 저장소 시작하기](#1-git-init--git-저장소-시작하기)
  - [2) `git status` : 현재 상태 확인](#2-git-status--현재-상태-확인)
  - [3) `git add` : 스테이징(커밋 후보 등록)](#3-git-add--스테이징커밋-후보-등록)
  - [4) `git commit` : 버전 저장(기록 남기기)](#4-git-commit--버전-저장기록-남기기)
  - [5) `git log` : 커밋 기록 보기](#5-git-log--커밋-기록-보기)
  - [6) `git diff` : 변경 내용 비교하기](#6-git-diff--변경-내용-비교하기)
  - [7) `git remote` / `git push` : 원격 저장소 연결 \& 업로드](#7-git-remote--git-push--원격-저장소-연결--업로드)
  - [8) `git pull` : 원격 변경](#8-git-pull--원격-변경)
  - [9) `git clone` : 원격 저장소 복제](#9-git-clone--원격-저장소-복제)
  - [10) 브랜치 기초: `git branch` / `git switch` / `git checkout`](#10-브랜치-기초-git-branch--git-switch--git-checkout)
  - [11) 병합: `git merge`](#11-병합-git-merge)
  - [12) 충돌(conflict) 해결 기본](#12-충돌conflict-해결-기본)
  - [13) 되돌리기(복구) 핵심: reset / revert / restore](#13-되돌리기복구-핵심-reset--revert--restore)
    - [13-1) `git restore`](#13-1-git-restore)
    - [13-2) `git reset`](#13-2-git-reset)
    - [13-3) `git revert`](#13-3-git-revert)
  - [14) `.gitignore` : 추적 제외 파일 설정](#14-gitignore--추적-제외-파일-설정)
- [Markdown / README 작성법 정리](#markdown--readme-작성법-정리)
  - [목차 (내부 링크)](#목차-내부-링크)
  - [내부링크](#내부링크)
  - [헤더적기](#헤더적기)
  - [순서 리스트 적기](#순서-리스트-적기)
  - [그냥 리스트 적기](#그냥-리스트-적기)
  - [체크 리스트 적기](#체크-리스트-적기)
  - [코드블럭](#코드블럭)
  - [링크걸기](#링크걸기)
  - [이미지걸기](#이미지걸기)
  - [텍스트 꾸미기](#텍스트-꾸미기)
    - [굵게 표현하기](#굵게-표현하기)
    - [기울임](#기울임)
    - [취소선](#취소선)
  - [수평선](#수평선)
  - [줄바꿈/구분](#줄바꿈구분)
  - [참고 링크](#참고-링크)

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
    b = a[:]
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
        <, <=, =>, >, ==, !=
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
      ```
      name = '홍길동'
      age = 25
      print(f'안녕하세요, {age}살 {name}입니다.")
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

## 조건문 (if / elif / else) + 중첩 조건문
- **내용, 설명**
  - 조건은 위에서부터 평가되므로 `elif` 순서가 매우 중요
  - 중첩 조건문으로 세부 조건 처리 가능
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
- **실수하기 쉬운 포인트**
  - 순서가 잘못되면 결과도 달라짐 (큰 조건을 먼저 체크!)


## 반복문 (for / while / break / continue / pass)
- **내용, 설명**
  - `break`: 반복 즉시 종료
  - `continue`: 현재 회차 스킵
  - `pass`: 문법적으로 자리를 채우는 용도 (아무 동작 없음)
- **예시**
```python
# break
for i in range(10):
    if i == 5:
        break
    print(i)

# continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```
- **실수하기 쉬운 포인트**
  - `while`은 종료 조건을 빼먹으면 무한 루프 가능


## 함수(Function) 기본: 정의/호출/return
- **내용, 설명**
  - `return` 만나면 함수 종료 + 값 반환
  - `print()`는 반환값이 없어서 `None` 반환
- **예시**
```python
def make_sum(x, y):
    return x + y

print(make_sum(100, 300))

resu = print(100)
print(resu)  # None
```
- **실수하기 쉬운 포인트**
  - return 아래 코드는 실행되지 않음
  - `print()`와 `return`을 혼동하지 않기


## 함수 인자(Arguments) 종류 정리
- **내용, 설명**
  1) Positional arguments  
  2) Default arguments  
  3) Keyword arguments  
  4) `*args`: 가변 위치 인자  
  5) `**kwargs`: 가변 키워드 인자
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
- **실수하기 쉬운 포인트**
  - 기본값 인자는 반드시 뒤에 위치해야 함
  - keyword 인자 뒤에 positional 인자 배치 불가


## 스코프(Scope) & 전역변수 global (LEGB Rule)
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
- **실수하기 쉬운 포인트**
  - `sum`, `list`, `dict`, `str` 같은 내장함수 이름을 변수명으로 쓰지 말기
  - global 선언 전 참조하면 SyntaxError 발생할 수 있음


## 패킹/언패킹 (Packing / Unpacking)
- **내용, 설명**
  - 패킹: 여러 값을 하나로 묶기
  - 언패킹: 여러 변수로 풀어내기
  - `*rest`로 남는 값 받기 가능
- **예시**
```python
packed_values = 1, 2, 3, 4, 5
a, b, *rest = packed_values
print(a, b, rest)  # 1 2 [3,4,5]
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


## 모듈 import 사용법 (import / from / as)
- **내용, 설명**
  - `import math` : 모듈 전체 사용
  - `from math import sqrt` : 특정 함수만
  - 단점: 이름 충돌 위험
  - `as`로 별칭 가능
- **예시**
```python
import math
print(math.sqrt(4))

from math import sqrt as msqrt
print(msqrt(16))
```
- **실수하기 쉬운 포인트**
  - `from math import *`는 충돌/가독성 문제로 비추천


## 내장함수: map / zip / filter / enumerate
### map
- **내용, 설명**: 요소에 함수를 적용한 결과를 map 객체로 반환
```python
numbers2 = list(map(int, input().split()))
```
- **실수하기 쉬운 포인트**
  - `map`은 한 번 소비하면 끝 → 다시 쓰려면 list로 변환해두기

### zip
- **내용, 설명**: 여러 iterable을 튜플로 묶음 (길이가 짧은 쪽 기준)
```python
arr = [[1,2,3],[4,5,6],[7,8,9]]
print(list(map(list, zip(*arr))))
```
- **실수하기 쉬운 포인트**
  - 길이가 다르면 긴 쪽은 잘려 나감

### filter
- **내용, 설명**: True인 값만 남김
```python
num = list(range(1, 8))
ret = filter(lambda x: x % 2 == 0, num)
print(list(ret))
```
- **실수하기 쉬운 포인트**
  - filter도 map처럼 iterator → 한 번만 사용 가능

### enumerate
- **내용, 설명**: (index, value) 제공
```python
for idx, fruit in enumerate(['apple', 'banana'], start=1):
    print(idx, fruit)
```

## lambda (익명 함수)
- **내용, 설명**
  - 한 줄로 간단한 함수 작성
  - `sorted(key=...)`, map/filter에 자주 사용
- **예시**
```python
students = [('지민', 25), ('서준', 20), ('민우', 30)]
result = sorted(students, key=lambda student: student[1])
print(result)
```
- **실수하기 쉬운 포인트**
  - 복잡한 로직은 lambda보다 def 함수가 더 가독성이 좋음


## 재귀(Recursion)
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

## method

### method란?

#### 정의
- **메서드(method)**는 특정 객체에 소속된 함수이다.
- `객체.메서드()` 형태로 호출한다.

#### 호출 방식

    # 함수
    def func():
        pass

    func()
    # 출력: None (아무것도 반환하지 않음)

    # 메서드
    numbers = [1, 2, 3]
    numbers.append(4)
    print(numbers)
    # 출력: [1, 2, 3, 4]

---

### 공통 시퀀스 메서드

#### `.index()`

##### 설명
- 특정 값이 **처음 등장하는 위치(인덱스)** 를 반환한다.
- 값이 없으면 `ValueError` 발생

##### 예시 코드

    text = 'banana'
    print(text.index('a'))
    # 출력: 1

    nums = [1, 2, 3]
    print(nums.index(2))
    # 출력: 1

---

#### `.count()`

##### 설명
- 특정 값이 **몇 번 등장하는지** 개수를 반환한다.

##### 예시 코드

    text = 'banana'
    print(text.count('a'))
    # 출력: 3

    nums = [1, 2, 2, 3]
    print(nums.count(2))
    # 출력: 2

---

### 문자열 탐색 및 검증 메서드

#### `.find()`
- 값이 없으면 `-1` 반환 (에러 없음)

    text = 'banana'
    print(text.find('a'))
    # 출력: 1

    print(text.find('z'))
    # 출력: -1

---

#### `.isupper()` / `.islower()`

    print('HELLO'.isupper())
    # 출력: True

    print('Hello'.islower())
    # 출력: False

---

#### `.isalpha()`

    print('Hello'.isalpha())
    # 출력: True

    print('123abc'.isalpha())
    # 출력: False

---

### 문자열 조작 메서드

#### `.replace()`

    text = 'Hello world world'
    print(text.replace('world', 'Python', 1))
    # 출력: Hello Python world

---

#### `.strip()`

    text = '   Hello World   '
    print(text.strip())
    # 출력: Hello World

---

#### `.split()`

    text = 'Hello   Python'
    print(text.split())
    # 출력: ['Hello', 'Python']

---

#### `.join()`

    words = ['Python', 'is', 'fun']
    print(' '.join(words))
    # 출력: Python is fun

---

### 리스트 값 추가 및 삭제 메서드

#### `.append()`
- **원본 리스트 변경**, 반환값은 `None`

    nums = [1, 2]
    result = nums.append(3)

    print(nums)
    # 출력: [1, 2, 3]

    print(result)
    # 출력: None

---

#### `.extend()`

    nums = [1, 2]
    nums.extend([4, 5])
    print(nums)
    # 출력: [1, 2, 4, 5]

---

#### `.insert()`

    nums = [1, 2, 3]
    nums.insert(1, 100)
    print(nums)
    # 출력: [1, 100, 2, 3]

---

#### `.remove()` / `.pop()` / `.clear()`

    nums = [1, 2, 3, 2]
    nums.remove(2)
    print(nums)
    # 출력: [1, 3, 2]

    item = nums.pop()
    print(item)
    # 출력: 2

    print(nums)
    # 출력: [1, 3]

    nums.clear()
    print(nums)
    # 출력: []

---

### 리스트 정렬 및 순서 변경

#### `.reverse()`

    nums = [1, 3, 2]
    nums.reverse()
    print(nums)
    # 출력: [2, 3, 1]

---

#### `.sort()`

    nums = [3, 1, 2]
    nums.sort()
    print(nums)
    # 출력: [1, 2, 3]

    nums.sort(reverse=True)
    print(nums)
    # 출력: [3, 2, 1]

> ⚠ `sort()`는 None 반환 → 체이닝 불가

---

### 메서드 체이닝

#### 정의
- 여러 메서드를 **연속해서 호출**하는 방식

##### 예시 코드

    text = 'heLLo'
    result = text.swapcase().replace('l', 'z')
    print(result)
    # 출력: HEzzO

---

#### 흔한 실수

    nums = [3, 1, 2]
    result = nums.sort()
    print(result)
    # 출력: None

---

#### 올바른 방법

    nums = [3, 1, 2]
    sorted_nums = sorted(nums)
    print(sorted_nums)
    # 출력: [1, 2, 3]


### 숫자 판별 메서드 비교

| 메서드 | 특징 |
|------|------|
| isdecimal | 가장 엄격 |
| isdigit | 지수 표현 허용 |
| isnumeric | 로마 숫자·분수까지 허용 |
```
    print('Ⅳ'.isnumeric())  # True
    print('Ⅳ'.isdigit())   # False
```
## Python으로 “클라이언트 → 서버 요청” 정리 (requests 중심)

- **내용, 설명**
  - 클라이언트(내 파이썬 코드)가 서버(API)에 요청(request)을 보내면, 서버는 응답(response)을 반환한다.
  - 보통 HTTP/HTTPS 프로토콜을 사용하며, 요청에는 **메서드(GET/POST/PUT/PATCH/DELETE)**, **URL**, **헤더**, **쿼리/바디**, **인증 정보** 등이 포함된다.
  - `requests` 라이브러리는 이 과정을 파이썬에서 쉽게 처리하게 해준다.

- **실수하기 쉬운 포인트**
  - “요청이 성공했다”는 건 단순히 통신이 됐다는 의미가 아니라, **상태코드(status code)** 를 반드시 확인해야 한다.
  - 응답이 JSON이라고 가정하고 `.json()`을 호출했는데 사실 HTML/텍스트면 에러가 날 수 있다.
  - 네트워크 요청은 언제든 실패할 수 있으니 **timeout**과 **예외 처리**는 기본이다.


### 0) 용어 한눈에 보기

- **내용, 설명**
  - **Endpoint**: 서버가 제공하는 API 주소(예: `/v1/users`)
  - **URL**: 전체 주소(프로토콜 + 도메인 + 경로 + 쿼리)
  - **Query String(쿼리스트링)**: URL 뒤 `?key=value&...` 형태
  - **Headers(헤더)**: 메타데이터(인증, 콘텐츠 타입 등)
  - **Body(바디)**: 요청 본문(POST/PUT/PATCH에서 주로 사용)
  - **Status Code**:
    - `2xx` 성공 (예: 200 OK, 201 Created)
    - `3xx` 리다이렉트
    - `4xx` 클라이언트 오류 (예: 400, 401, 403, 404)
    - `5xx` 서버 오류 (예: 500)

- **예시**

    URL 예시:
    https://api.example.com/v1/users?limit=10&page=2

    - 프로토콜: https
    - 도메인: api.example.com
    - 경로: /v1/users
    - 쿼리: limit=10&page=2

- **실수하기 쉬운 포인트**
  - `401`은 인증 실패(토큰/키 문제), `403`은 권한 없음, `404`는 경로 틀림 가능성.
  - “서버가 죽었다” 판단 전에 URL/인증/파라미터부터 점검하기.

### 1) requests 설치 및 기본 사용 흐름

- **내용, 설명**
  - `requests`는 표준 라이브러리가 아니라 설치가 필요할 수 있다.
  - 기본 흐름:
    1) 요청 보내기 (`requests.get/post/...`)
    2) 응답 객체 확인 (`status_code`, `headers`, `text`)
    3) 필요하면 JSON 파싱 (`.json()`)
    4) 예외 처리/타임아웃/재시도 고려

- **예시**

    pip install requests

    import requests

    r = requests.get("https://httpbin.org/get")
    print(r.status_code)
    print(r.text)

- **실수하기 쉬운 포인트**
  - `requests.get()`은 기본적으로 오래 기다릴 수 있음 → `timeout`을 주는 습관.


### 2) GET 요청: 서버에서 “조회”하기

- **내용, 설명**
  - GET은 주로 “데이터 조회”에 사용한다.
  - 파라미터는 보통 쿼리스트링으로 전달한다.
  - `params={...}`를 사용하면 requests가 URL 인코딩까지 처리한다.

- **예시**

    import requests

    url = "https://httpbin.org/get"
    params = {"q": "python", "page": 1}

    r = requests.get(url, params=params, timeout=5)
    print(r.url)          # 실제 요청된 URL 확인 가능
    print(r.status_code)

    data = r.json()
    print(data["args"])   # {"q": "python", "page": "1"}

- **실수하기 쉬운 포인트**
  - `params`를 문자열로 직접 붙이면 인코딩 문제/오타가 나기 쉽다 → `params` 사용 권장.
  - `r.json()`은 응답이 JSON일 때만 가능.

### 3) POST 요청: 서버에 “생성/전송”하기 (JSON 바디)

- **내용, 설명**
  - POST는 서버에 데이터를 생성하거나 전송할 때 사용한다.
  - JSON API는 보통 `json={...}`로 보내며, requests가 `Content-Type: application/json` 처리까지 해준다.

- **예시**

    import requests

    url = "https://httpbin.org/post"
    payload = {"name": "sejin", "role": "planner"}

    r = requests.post(url, json=payload, timeout=5)
    print(r.status_code)

    data = r.json()
    print(data["json"])  # {"name": "...", "role": "..."}

- **실수하기 쉬운 포인트**
  - `data=`와 `json=`은 다름:
    - `json=`: JSON으로 인코딩
    - `data=`: 보통 form 형태(또는 raw 문자열)
  - API 문서가 요구하는 형식(JSON vs form)을 확인해야 한다.


### 4) POST 요청: form 데이터 전송 (`data=`)

- **내용, 설명**
  - `application/x-www-form-urlencoded` 형태로 전송할 때 `data=`를 사용한다.
  - 로그인 폼 등 레거시 시스템에서 자주 사용.

- **예시**

    import requests

    url = "https://httpbin.org/post"
    form = {"username": "user1", "password": "pw1234"}

    r = requests.post(url, data=form, timeout=5)
    print(r.status_code)
    print(r.json()["form"])

- **실수하기 쉬운 포인트**
  - JSON API인데 `data=`로 보내면 서버가 바디를 해석 못 할 수 있다.


### 5) 헤더(headers): 인증/콘텐츠 타입/커스텀 헤더

- **내용, 설명**
  - 헤더는 요청에 대한 “부가 정보”를 담는다.
  - 대표적으로 인증 토큰(Authorization), 사용자 에이전트(User-Agent) 등이 있다.

- **예시**

    import requests

    url = "https://httpbin.org/headers"
    headers = {
      "Authorization": "Bearer YOUR_TOKEN",
      "User-Agent": "MyPythonClient/1.0",
    }

    r = requests.get(url, headers=headers, timeout=5)
    print(r.status_code)
    print(r.json())

- **실수하기 쉬운 포인트**
  - 토큰 앞에 `Bearer `가 필요한지(혹은 다른 스킴인지) API 문서 확인 필수.
  - 헤더 키 오타(Authorization vs Authorisation 등) 주의.


### 6) 상태코드와 에러 처리: raise_for_status()

- **내용, 설명**
  - 상태코드를 직접 체크하거나, `raise_for_status()`로 4xx/5xx를 예외로 처리할 수 있다.

- **예시**

    import requests

    try:
        r = requests.get("https://httpbin.org/status/404", timeout=5)
        r.raise_for_status()  # 4xx/5xx면 HTTPError 발생
        print("OK:", r.status_code)
    except requests.exceptions.HTTPError as e:
        print("HTTPError:", e)
    except requests.exceptions.Timeout:
        print("Timeout")
    except requests.exceptions.RequestException as e:
        print("RequestException:", e)

- **실수하기 쉬운 포인트**
  - `raise_for_status()`를 쓰면 실패를 놓치지 않아서 안정적인 코드가 된다.

### 7) 응답(response) 다루기: text / json / headers / encoding

- **내용, 설명**
  - `r.text`: 문자열(디코딩된 텍스트)
  - `r.content`: 바이트(이미지/파일 등)
  - `r.json()`: JSON 파싱
  - `r.headers`: 응답 헤더 딕셔너리
  - `r.encoding`: 텍스트 인코딩(필요 시 수동 설정)

- **예시**

    import requests

    r = requests.get("https://httpbin.org/get", timeout=5)
    print(r.status_code)
    print(r.headers.get("Content-Type"))
    print(r.text[:100])

    data = r.json()
    print(data.keys())

- **실수하기 쉬운 포인트**
  - 응답이 JSON이 아닐 때 `r.json()` 호출하면 ValueError가 날 수 있다.
  - 파일 다운로드는 `r.content`/`stream=True` 사용이 안전.

### 8) timeout과 재시도(기본 전략)

- **내용, 설명**
  - 네트워크 요청은 지연/실패가 발생할 수 있으므로 `timeout`은 필수.
  - 단순 재시도는 서버에 부담이 될 수 있어, 제한적으로 사용한다.

- **예시**

    import time
    import requests

    url = "https://httpbin.org/delay/2"

    for i in range(3):
        try:
            r = requests.get(url, timeout=1)  # 일부러 타임아웃 유도
            print("Success:", r.status_code)
            break
        except requests.exceptions.Timeout:
            print("Timeout, retry:", i + 1)
            time.sleep(1)

- **실수하기 쉬운 포인트**
  - timeout을 너무 짧게 잡으면 정상 요청도 실패할 수 있다.
  - 무한 재시도는 금지(서버/클라이언트 모두 위험).


### 9) Session 사용: 쿠키/연결 재사용(성능/로그인 유지)

- **내용, 설명**
  - `requests.Session()`을 쓰면:
    - 같은 서버에 여러 요청 시 연결 재사용(성능 향상)
    - 쿠키 유지(로그인 세션 유지 등)
    - 공통 헤더/파라미터 관리 용이

- **예시**

    import requests

    session = requests.Session()
    session.headers.update({"User-Agent": "MyClient/1.0"})

    r1 = session.get("https://httpbin.org/get", timeout=5)
    r2 = session.get("https://httpbin.org/get", timeout=5)

    print(r1.status_code, r2.status_code)

- **실수하기 쉬운 포인트**
  - 세션은 “상태”를 가지므로, 다른 계정/다른 토큰을 섞어 쓰지 않게 주의.

### 10) 파일 다운로드/업로드 기초

#### 10-1) 다운로드(간단)
- **내용, 설명**
  - 작은 파일은 `r.content`로 받아 저장 가능

- **예시**

    import requests

    r = requests.get("https://httpbin.org/image/png", timeout=5)
    with open("image.png", "wb") as f:
        f.write(r.content)

- **실수하기 쉬운 포인트**
  - 큰 파일은 `stream=True`로 나눠 받는 것이 안전.

#### 10-2) 업로드(파일 전송)
- **내용, 설명**
  - `files=` 파라미터로 multipart/form-data 업로드 가능

- **예시**

    import requests

    url = "https://httpbin.org/post"
    with open("image.png", "rb") as f:
        r = requests.post(url, files={"file": f}, timeout=10)

    print(r.status_code)

- **실수하기 쉬운 포인트**
  - 서버가 요구하는 필드명(예: file, upload 등)이 다를 수 있음 → API 문서 확인.

### 11) 실전 템플릿: 안전한 요청 함수 만들기

- **내용, 설명**
  - 자주 쓰는 패턴(타임아웃/에러처리/JSON 파싱)을 함수로 묶으면 실수가 줄어든다.

- **예시**

    import requests

    def get_json(url, params=None, headers=None, timeout=5):
        try:
            r = requests.get(url, params=params, headers=headers, timeout=timeout)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.Timeout:
            return {"error": "timeout"}
        except requests.exceptions.HTTPError as e:
            return {"error": "http_error", "detail": str(e), "status": r.status_code}
        except ValueError:
            return {"error": "not_json"}
        except requests.exceptions.RequestException as e:
            return {"error": "request_exception", "detail": str(e)}

    data = get_json("https://httpbin.org/get", params={"q": "python"})
    print(data)

- **실수하기 쉬운 포인트**
  - 실패 케이스를 먼저 설계하면(Timeout/HTTPError/Not JSON) 디버깅이 쉬워진다.

### 참고 (연습용 테스트 API)

- **내용, 설명**
  - 실제 서비스 API가 없어도 연습할 수 있는 공개 테스트 서버
  - 요청/응답 구조를 확인하기 좋다.

- **예시**

    https://httpbin.org/
    https://jsonplaceholder.typicode.com/

- **실수하기 쉬운 포인트**
  - 테스트 API는 실제 서비스와 인증/제한이 다를 수 있다.








---
# CLI 기본 명령어

CLI(Command Line Interface)는 터미널에서 명령어로 컴퓨터를 조작하는 방식이다.  
폴더 이동/파일 생성/삭제/복사 같은 작업을 빠르게 할 수 있다.

## 1) `pwd`

- **내용, 설명**
  - 현재 내가 위치한 폴더(경로)를 출력한다.

- **예시**

    pwd

- **실수하기 쉬운 포인트**
  - “어디 있는지 모르겠다” 싶으면 제일 먼저 `pwd`로 위치 확인!


## 2) `ls`

- **내용, 설명**
  - 현재 폴더에 있는 파일/폴더 목록을 출력한다.
  - 옵션을 붙이면 더 자세히 확인 가능

- **예시**

    ls
    ls -a      # 숨김 파일 포함
    ls -l      # 자세히 보기
    ls -al     # 숨김+자세히

- **실수하기 쉬운 포인트**
  - 숨김 파일은 기본 `ls`로 안 보이므로 `ls -a`를 자주 사용한다.

## 3) `cd`

- **내용, 설명**
  - 디렉토리를 이동하는 명령어

- **예시**

    cd 폴더이름
    cd ..     # 상위 폴더
    cd .      # 현재 폴더
    cd ~      # 홈 디렉토리
    cd /      # 루트 디렉토리

- **실수하기 쉬운 포인트**
  - `cd ..`와 `cd .` 헷갈리기 쉬움  
    - `..` = 상위 폴더  
    - `.` = 현재 폴더(변화 없음)

## 4) `mkdir`

- **내용, 설명**
  - 폴더(디렉토리)를 생성한다.
  - `-p` 옵션을 사용하면 중간 경로도 함께 생성 가능

- **예시**

    mkdir my_folder
    mkdir -p a/b/c

- **실수하기 쉬운 포인트**
  - 중간 폴더가 없으면 생성 실패 → `mkdir -p` 사용

## 5) `touch`

- **내용, 설명**
  - 파일이 없으면 빈 파일을 만들고, 있으면 수정 시간을 갱신한다.

- **예시**

    touch test.txt
    touch main.py

- **실수하기 쉬운 포인트**
  - 폴더는 만들 수 없음 → 폴더는 `mkdir`

## 6) `cat`

- **내용, 설명**
  - 텍스트 파일의 내용을 터미널에 출력한다.

- **예시**

    cat README.md
    cat test.txt

- **실수하기 쉬운 포인트**
  - 이미지/바이너리 파일에는 사용하지 말기 (깨진 출력 나옴)

## 7) `echo`

- **내용, 설명**
  - 문자열 출력
  - 리다이렉션(`>`, `>>`)으로 파일에 저장 가능

- **예시**

    echo "hello"
    echo "hello" > hello.txt     # 덮어쓰기
    echo "world" >> hello.txt    # 이어쓰기

- **실수하기 쉬운 포인트**
  - `>` 는 **덮어쓰기**, `>>`는 **이어쓰기** (자주 실수!)

## 8) `cp`

- **내용, 설명**
  - 파일/폴더를 복사한다.
  - 폴더는 `-r` 옵션이 필요하다.

- **예시**

    cp a.txt b.txt
    cp a.txt folder/
    cp -r my_folder backup/

- **실수하기 쉬운 포인트**
  - 폴더 복사할 때 `-r` 안 붙이면 실패

## 9) `mv`

- **내용, 설명**
  - 파일/폴더 이동 또는 이름 변경

- **예시**

    mv a.txt folder/          # 이동
    mv old.txt new.txt        # 이름 변경
    mv my_folder backup_folder

- **실수하기 쉬운 포인트**
  - 덮어쓰기 위험 있음 → 중요한 파일은 확인하고 실행

## 10) `rm`

- **내용, 설명**
  - 파일/폴더 삭제
  - 삭제는 보통 휴지통으로 가지 않아서 복구가 어렵다.

- **예시**

    rm a.txt
    rm -r folder/
    rm -rf folder/   # ⚠ 위험: 강제 전체 삭제

- **실수하기 쉬운 포인트**
  - `rm -rf`는 매우 위험함 (실수로 큰 폴더 삭제 가능)

## 11) `clear`

- **내용, 설명**
  - 터미널 화면을 깨끗하게 정리

- **예시**

    clear

- **실수하기 쉬운 포인트**
  - 기록 자체를 삭제하진 않음 → 단지 화면만 정리

## 12) `history`

- **내용, 설명**
  - 이전에 입력했던 명령어 기록을 보여준다.

- **예시**

    history

- **실수하기 쉬운 포인트**
  - 이전 명령이 기억 안 날 때 `history`로 찾아서 복사하면 편함

## 추가 팁: 경로 기호 정리

- **내용, 설명**
  - CLI에서 경로는 아래 기호를 자주 사용한다.

- **예시**

    cd ../..      # 상위 폴더 2번 올라가기
    cd ~/Desktop  # 홈 디렉토리 → Desktop 이동

- **실수하기 쉬운 포인트**
  - `.` / `..` / `~` 의미 헷갈리지 않기


---
# Git 활용법 정리 (기능 + 예시)

Git은 **코드 변경 사항을 기록하고(버전 관리)**, 다른 사람과 **협업**할 수 있게 도와주는 도구다.  
프로젝트의 “저장(커밋)” 단위로 기록하며, 브랜치/병합을 통해 안전하게 작업을 나눌 수 있다.

## 0) Git 작업 흐름 한눈에 보기

- **내용, 설명**
  - Git은 보통 아래 순서로 작업한다.
    1) 작업(파일 수정)
    2) 스테이징(add)
    3) 커밋(commit)
    4) 원격 저장소에 푸시(push)

- **예시**

    git status
    git add .
    git commit -m "메시지"
    git push origin main

- **실수하기 쉬운 포인트**
  - `git add`를 하지 않으면 커밋에 변경 사항이 포함되지 않는다.

## 1) `git init` : Git 저장소 시작하기

- **내용, 설명**
  - 현재 폴더를 Git 저장소로 만든다.
  - `.git` 폴더가 생성되며 버전 관리가 시작된다.

- **예시**

    git init

- **실수하기 쉬운 포인트**
  - 이미 Git 저장소인 폴더에서 다시 init하면 꼬일 수 있음  
  - `.git` 폴더를 함부로 삭제하지 말기


## 2) `git status` : 현재 상태 확인

- **내용, 설명**
  - 변경된 파일 / 스테이징 여부 / 브랜치 상태를 확인한다.
  - Git이 “현재 무엇을 알고 있는지” 보는 가장 중요한 명령어

- **예시**

    git status

- **실수하기 쉬운 포인트**
  - 문제 생기면 무조건 `git status`부터 확인하면 해결이 빨라진다.

## 3) `git add` : 스테이징(커밋 후보 등록)

- **내용, 설명**
  - 커밋에 포함할 변경사항을 스테이징 영역에 올린다.

- **예시**

    git add 파일이름
    git add .          # 현재 폴더 기준 전체 변경사항 스테이징
    git add -A         # 삭제까지 포함해서 전체 반영

- **실수하기 쉬운 포인트**
  - `git add .`는 “변경사항 저장”이 아니라 “커밋 후보로 등록”이다.


## 4) `git commit` : 버전 저장(기록 남기기)

- **내용, 설명**
  - 스테이징된 변경사항을 하나의 버전으로 저장한다.
  - 커밋 메시지는 “무엇을 했는지” 명확히 적는다.

- **예시**

    git commit -m "Add CLI section to README"
    git commit -m "Fix input parsing bug"

- **실수하기 쉬운 포인트**
  - commit 메시지를 “수정”처럼 애매하게 쓰면 나중에 추적이 어려움  
  - 커밋 전에 `git status`로 add가 되었는지 확인하기


## 5) `git log` : 커밋 기록 보기

- **내용, 설명**
  - 지금까지 저장된 커밋(버전) 이력을 확인한다.

- **예시**

    git log
    git log --oneline
    git log --oneline --graph --decorate

- **실수하기 쉬운 포인트**
  - 해시값(커밋 ID)은 되돌리기/비교할 때 필요하니 익숙해지기

## 6) `git diff` : 변경 내용 비교하기

- **내용, 설명**
  - 커밋 전후로 “어떤 부분이 바뀌었는지” 확인한다.

- **예시**

    git diff            # add 하기 전 변경 내용
    git diff --staged   # add 후 스테이징된 변경 내용

- **실수하기 쉬운 포인트**
  - 커밋 전에 `git diff`로 확인하면 실수를 크게 줄일 수 있다.

## 7) `git remote` / `git push` : 원격 저장소 연결 & 업로드

- **내용, 설명**
  - GitHub 같은 원격 저장소(remote)에 연결하고 업로드(push)한다.

- **예시**

    git remote add origin https://github.com/유저명/레포명.git
    git remote -v
    git push origin main

- **실수하기 쉬운 포인트**
  - 원격 저장소 연결이 없으면 push 불가  
  - 기본 브랜치는 `main`인 경우가 많지만 레포마다 다를 수 있음


## 8) `git pull` : 원격 변경

- **내용, 설명**
  - 원격 저장소 최신 커밋을 내려받아 현재 브랜치에 반영한다.

- **예시**

    git pull origin main

- **실수하기 쉬운 포인트**
  - 협업 중에는 작업 시작 전에 `git pull` 먼저 하는 습관이 중요!


## 9) `git clone` : 원격 저장소 복제

- **내용, 설명**
  - 원격 저장소 내용을 내 컴퓨터로 통째로 복사한다.

- **예시**

    git clone https://github.com/유저명/레포명.git

- **실수하기 쉬운 포인트**
  - clone은 이미 remote까지 설정된 상태로 시작함 (`git remote -v` 확인 가능)


## 10) 브랜치 기초: `git branch` / `git switch` / `git checkout`

- **내용, 설명**
  - 브랜치는 “독립된 작업 공간”
  - 새 기능 개발/버그 수정은 브랜치에서 하고 완료되면 main에 합친다.

- **예시**

    git branch                 # 브랜치 목록
    git branch new-feature     # 브랜치 생성
    git switch new-feature     # 브랜치 이동
    git switch -c hotfix       # 생성 + 이동

- **실수하기 쉬운 포인트**
  - main에서 작업하다 꼬이면 힘들어짐 → 새 작업은 브랜치에서 진행!

## 11) 병합: `git merge`

- **내용, 설명**
  - 다른 브랜치 작업 내용을 현재 브랜치로 합친다.

- **예시**

    git switch main
    git merge new-feature

- **실수하기 쉬운 포인트**
  - merge 전에 항상 `git status`로 깨끗한 상태인지 확인
  - 충돌(conflict)이 나면 당황하지 말고 수정 → add → commit


## 12) 충돌(conflict) 해결 기본

- **내용, 설명**
  - 서로 다른 브랜치에서 같은 파일/같은 줄을 수정하면 충돌 발생 가능
  - Git이 자동으로 합치지 못해서 사람이 선택해야 함

- **예시**

    # 충돌 발생 시 파일에 아래 표시가 생김
    <<<<<<< HEAD
    내 변경 내용
    =======
    상대 변경 내용
    >>>>>>> branch-name

    # 수정 후
    git add .
    git commit -m "Resolve merge conflict"

- **실수하기 쉬운 포인트**
  - 충돌 표시(<<<<<<<, =======, >>>>>>>)를 반드시 제거하고 저장해야 함

## 13) 되돌리기(복구) 핵심: reset / revert / restore

### 13-1) `git restore`
- **내용, 설명**
  - 워킹 디렉토리의 변경 사항을 버린다(되돌림)

- **예시**

    git restore 파일이름
    git restore .

- **실수하기 쉬운 포인트**
  - 되돌린 변경 내용은 복구가 어려움 → 신중히 사용

### 13-2) `git reset`
- **내용, 설명**
  - 커밋을 과거로 “이동”하는 명령
  - 옵션에 따라 기록도 변경됨(주의!)

- **예시**

    git reset --soft HEAD~1    # 커밋만 취소(변경사항 유지)
    git reset --mixed HEAD~1   # add까지 취소(변경사항 유지)
    git reset --hard HEAD~1    # ⚠ 변경사항까지 삭제

- **실수하기 쉬운 포인트**
  - `--hard`는 복구 어려움 (진짜 조심)

### 13-3) `git revert`
- **내용, 설명**
  - 특정 커밋을 “취소하는 커밋”을 새로 만든다.
  - 협업(푸시된 기록)에서는 reset보다 안전

- **예시**

    git revert 커밋해시

- **실수하기 쉬운 포인트**
  - 협업 레포에서 reset으로 과거를 강제로 바꾸면 팀원 기록이 꼬일 수 있음  
  - 공유된 커밋은 보통 revert 사용 권장

## 14) `.gitignore` : 추적 제외 파일 설정

- **내용, 설명**
  - Git이 추적하지 않아야 할 파일(캐시, 비밀키, 빌드 결과물)을 등록한다.

- **예시**

    # .gitignore 예시
    __pycache__/
    *.pyc
    .env
    .vscode/

- **실수하기 쉬운 포인트**
  - 이미 추적 중인 파일은 `.gitignore`에 추가해도 계속 추적됨  
  - 해결:

    git rm -r --cached .
    git add .
    git commit -m "Apply .gitignore"

---
# Markdown / README 작성법 정리

  - 마크다운은 “렌더링되는 곳(README.md 미리보기)”에서만 제대로 보인다.
  - 메모장처럼 일반 텍스트에서는 서식이 안 보이는 게 정상이다.



## 목차 (내부 링크)

- **내용, 설명**
  - 문서 상단에 목차를 만들면 빠르게 원하는 위치로 이동할 수 있다.
  - 링크는 보통 `(#헤더이름)` 형태로 작성한다.
  - 영어는 소문자, 띄어쓰기는 `-` 로 변환된다.

- **예시**

    - [헤더](#헤더적기)
    - [순서 리스트](#순서-리스트-적기)
    - [그냥 리스트](#그냥-리스트-적기)
    - [체크 리스트](#체크-리스트-적기)
    - [코드 블럭](#코드블럭)
    - [링크 걸기](#링크걸기)
    - [이미지 걸기](#이미지걸기)
    - [텍스트 꾸미기](#텍스트-꾸미기)
    - [수평선](#수평선)
    - [참고 링크](#참고-링크)

- **실수하기 쉬운 포인트**
  - 내부 링크는 “헤더 이름”을 기준으로 자동 생성된다.
  - 띄어쓰기가 있으면 `-`로 바뀐다.

## 내부링크

- **내용, 설명**
  - 문서 안에서 특정 위치로 이동하는 링크를 말한다.
  - 기본 구조는 `[표시될 글자](#이동할-헤더)` 이다.
  - 이동할 헤더는 보통:
    - 영어는 소문자
    - 띄어쓰기는 `-` 처리

- **예시**

    [맨 위로 이동](#markdown--readme-작성법-정리)

- **실수하기 쉬운 포인트**
  - 링크 괄호 사이에 띄어쓰기 넣으면 동작이 깨질 수 있다.
  - 헤더 글자를 수정하면 내부 링크도 함께 수정해야 한다.

## 헤더적기

- **내용, 설명**
  - `#` 개수에 따라 제목 크기(레벨)가 달라진다.
  - 보통 문서 제목은 `#`, 큰 섹션은 `##`, 하위는 `###`로 구성한다.

- **예시**

    # 헤더 1
    ## 헤더 2
    ### 헤더 3
    #### 헤더 4
    ##### 헤더 5

- **실수하기 쉬운 포인트**
  - `#` 뒤에는 공백 한 칸이 있어야 한다.  
    (`#헤더` ❌ / `# 헤더` ✅)

## 순서 리스트 적기

- **내용, 설명**
  - 숫자 + `.` 을 붙이면 순서 리스트를 만들 수 있다.
  - `Tab` 키로 들여쓰기하면 하위 리스트를 만들 수 있다.

- **예시**

    1. 첫 번째
    2. 두 번째
       1. 두 번째-하위 1
       2. 두 번째-하위 2

- **실수하기 쉬운 포인트**
  - 하위 리스트는 들여쓰기 공백이 맞지 않으면 깨질 수 있다.
  - 줄바꿈을 많이 하면 리스트 구조가 풀릴 수 있다.

## 그냥 리스트 적기

- **내용, 설명**
  - 순서가 없는 리스트는 `-`, `*`, `+` 중 하나로 만들 수 있다.
  - 한 문서에서는 **한 가지 기호로 통일**하는 것이 좋다.

- **예시**

    - 순서가 없는 리스트
      - 엔터 후 탭을 한 번 누르면 하위 리스트 가능
        - 다시 돌아가려면 `Shift + Tab`

- **실수하기 쉬운 포인트**
  - 섞어 쓰면 에디터에서 경고가 뜨기도 한다.
  - 들여쓰기(탭/공백)가 깨지면 구조가 무너진다.

## 체크 리스트 적기

- **내용, 설명**
  - 작업 목록(todo) 정리에 자주 사용한다.
  - `- [ ]` : 미완료
  - `- [x]` : 완료

- **예시**

    - [x] 계란
    - [ ] 당근
    - [x] 우유
    - [ ] 과자

- **실수하기 쉬운 포인트**
  - `[ ]` 안의 공백이 빠지면 체크박스로 인식되지 않는다.
  - 반드시 대괄호 앞에 `-` 또는 `*`가 필요하다.


## 코드블럭

- **내용, 설명**
  - 코드 블럭은 백틱(`) 3개로 감싸서 만든다.
  - 언어를 함께 적으면 문법 하이라이팅이 된다.

- **예시**

    ```python
    print("안")
    ```

- **실수하기 쉬운 포인트**
  - 백틱 3개 시작/끝이 정확히 닫혀야 한다.
  - 중간에 닫히면 문서 아래가 전부 코드처럼 보일 수 있다.


## 링크걸기

- **내용, 설명**
  - `[링크이름](URL)` 형태로 링크를 작성한다.
  - README에서는 참고 자료 링크를 자주 붙인다.

- **예시**

    [네이버](https://www.naver.com)  
    [왕초보를 위한 Python](https://www.python.org)

- **실수하기 쉬운 포인트**
  - `[]()` 사이 순서가 바뀌면 링크가 깨진다.
  - URL에 공백이 있으면 동작이 안 한다.


## 이미지걸기

- **내용, 설명**
  - 이미지 문법은 링크와 비슷하지만 앞에 `!`가 붙는다.
  - `![이미지이름](이미지URL)`

- **예시**

    ![example](https://via.placeholder.com/150)

- **실수하기 쉬운 포인트**
  - 이미지 URL이 실제 이미지 파일 링크여야 한다.
  - 로컬 경로도 가능하지만 경로가 맞아야 한다.


## 텍스트 꾸미기

### 굵게 표현하기
- **내용, 설명**
  - `**굵게**` 또는 `__굵게__`

- **예시**

    **글자강조**
    __글자강조__

- **실수하기 쉬운 포인트**
  - 기호 사이에 공백이 있으면 적용이 깨질 수 있다.

### 기울임
- **내용, 설명**
  - `*기울임*` 또는 `_기울임_`
  - 별 또는 언더바 뒤에는 공백을 두지 않는다.

- **예시**

    *기울임*
    _기울임_

### 취소선
- **내용, 설명**
  - `~~취소선~~`

- **예시**

    ~~취소선~~

- **실수하기 쉬운 포인트**
  - `~~`와 글자 사이에 띄어쓰기 넣으면 이상해질 수 있다.

## 수평선

- **내용, 설명**
  - 문서 구분용 수평선을 넣을 수 있다.
  - `---` / `***` / `___` 모두 동일하게 동작한다(3개 이상)

- **예시**

    ---
    ***
    ___

- **실수하기 쉬운 포인트**
  - 에디터에서 안 보이면 README 미리보기로 확인해야 한다.

## 줄바꿈/구분

- **내용, 설명**
  - Markdown에서 줄바꿈은 방식이 여러 가지다.
  - `<br>` 태그를 쓰면 확실하게 줄바꿈 된다.

- **예시**

    첫 줄<br>
    둘째 줄

- **실수하기 쉬운 포인트**
  - 엔터만 누르면 줄바꿈이 안 되는 경우가 있어 `<br>`이 안전하다.

## 참고 링크

- **내용, 설명**
  - 마크다운 공식 문법 참고 사이트

- **예시**

    https://www.markdownguide.org/
