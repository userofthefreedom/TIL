[파이썬](#python-study-notes)

[cli](#cli-기본-명령어)

[git](#git-활용법-정리-기능--예시)





# Python Study Notes

---

## 목차
- [Python Study Notes](#python-study-notes)
  - [목차](#목차)
  - [1. 변수와 자료형 (int / float / str / bool)](#1-변수와-자료형-int--float--str--bool)
  - [2. 문자열 (Slicing / 연산 / 메서드 / ord \& chr)](#2-문자열-slicing--연산--메서드--ord--chr)
  - [3. 리스트 / 튜플 / range](#3-리스트--튜플--range)
  - [4. 딕셔너리(dict) / 집합(set)](#4-딕셔너리dict--집합set)
  - [5. 조건문 (if / elif / else) + 중첩 조건문](#5-조건문-if--elif--else--중첩-조건문)
  - [6. 반복문 (for / while / break / continue / pass)](#6-반복문-for--while--break--continue--pass)
  - [7. 함수(Function) 기본: 정의/호출/return](#7-함수function-기본-정의호출return)
  - [8. 함수 인자(Arguments) 종류 정리](#8-함수-인자arguments-종류-정리)
  - [9. 스코프(Scope) \& 전역변수 global (LEGB Rule)](#9-스코프scope--전역변수-global-legb-rule)
  - [10. 패킹/언패킹 (Packing / Unpacking)](#10-패킹언패킹-packing--unpacking)
  - [11. 모듈 import 사용법 (import / from / as)](#11-모듈-import-사용법-import--from--as)
  - [12. 내장함수: map / zip / filter / enumerate](#12-내장함수-map--zip--filter--enumerate)
    - [map](#map)
    - [zip](#zip)
    - [filter](#filter)
    - [enumerate](#enumerate)
  - [13. lambda (익명 함수)](#13-lambda-익명-함수)
  - [14. 재귀(Recursion)](#14-재귀recursion)
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

---

## 1. 변수와 자료형 (int / float / str / bool)
- **내용, 설명**
  - 파이썬은 다양한 자료형을 사용하며, `type()`으로 자료형 확인 가능
  - 한 줄에 여러 변수 할당 가능 (`a, b = 1, 2`)
  - `bool()` 변환 시 `0`, `""`는 False, 그 외는 대부분 True
- **예시**
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

---

## 2. 문자열 (Slicing / 연산 / 메서드 / ord & chr)
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
- **실수하기 쉬운 포인트**
  - `s[1] = "x"` 같은 직접 변경은 불가능 (TypeError)
  - `s + 1`처럼 문자열과 숫자는 바로 더할 수 없음 → `s + str(1)`

---

## 3. 리스트 / 튜플 / range
- **내용, 설명**
  - 리스트(list): 순서 있음, 변경 가능
  - 튜플(tuple): 순서 있음, 변경 불가
  - range: 연속된 숫자 생성 (반복문에서 자주 사용)
- **예시**
```python
my_list = ['java', 'django', 'C++', 'HTML', 'python']
my_list[0] = 'python'
print(len(my_list))

tp = (1, 2, 3, 4, 5)
print(tp[1], len(tp))

print(list(range(3)))       # [0,1,2]
print(list(range(3,8,2)))   # [3,5,7]
```
- **실수하기 쉬운 포인트**
  - `range(3)`를 출력하면 range 객체가 보임 → `list(range(3))`로 확인
  - 튜플은 값 변경 불가: `tp[0] = 10` → 오류

---

## 4. 딕셔너리(dict) / 집합(set)
- **내용, 설명**
  - dict: `key:value` 형태, key 중복 불가
  - set: 중복 제거에 매우 유용, 합집합/교집합/차집합 가능
- **예시**
```python
di = {
  1: 3,
  2: {"ㄱ": "가자", "ㄴ": "나는"},
  3: "집",
  "교": [2, 3, 4]
}
print(di[2]["ㄱ"])

s1 = {1,2,3}
s2 = {3,6,9}
print(s1 | s2)  # 합집합
print(s1 & s2)  # 교집합
print(s1 - s2)  # 차집합
```
- **실수하기 쉬운 포인트**
  - dict 접근은 인덱스가 아니라 key 기반: `di[0]` 같은 접근 불가
  - set은 순서가 없음 → 인덱싱 불가 (`s[0]` 안됨)

---

## 5. 조건문 (if / elif / else) + 중첩 조건문
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

---

## 6. 반복문 (for / while / break / continue / pass)
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

---

## 7. 함수(Function) 기본: 정의/호출/return
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

---

## 8. 함수 인자(Arguments) 종류 정리
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

---

## 9. 스코프(Scope) & 전역변수 global (LEGB Rule)
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

---

## 10. 패킹/언패킹 (Packing / Unpacking)
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
- **실수하기 쉬운 포인트**
  - 언패킹 변수 개수가 안 맞으면 ValueError
  - `*`는 남는 값들을 리스트로 받는다

---

## 11. 모듈 import 사용법 (import / from / as)
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

---

## 12. 내장함수: map / zip / filter / enumerate
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

---

## 13. lambda (익명 함수)
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

---

## 14. 재귀(Recursion)
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

---








---
# CLI 기본 명령어

CLI(Command Line Interface)는 터미널에서 명령어로 컴퓨터를 조작하는 방식이다.  
폴더 이동/파일 생성/삭제/복사 같은 작업을 빠르게 할 수 있다.

---

## 1) `pwd`

- **내용, 설명**
  - 현재 내가 위치한 폴더(경로)를 출력한다.

- **예시**

    pwd

- **실수하기 쉬운 포인트**
  - “어디 있는지 모르겠다” 싶으면 제일 먼저 `pwd`로 위치 확인!

---

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

---

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

---

## 4) `mkdir`

- **내용, 설명**
  - 폴더(디렉토리)를 생성한다.
  - `-p` 옵션을 사용하면 중간 경로도 함께 생성 가능

- **예시**

    mkdir my_folder
    mkdir -p a/b/c

- **실수하기 쉬운 포인트**
  - 중간 폴더가 없으면 생성 실패 → `mkdir -p` 사용

---

## 5) `touch`

- **내용, 설명**
  - 파일이 없으면 빈 파일을 만들고, 있으면 수정 시간을 갱신한다.

- **예시**

    touch test.txt
    touch main.py

- **실수하기 쉬운 포인트**
  - 폴더는 만들 수 없음 → 폴더는 `mkdir`

---

## 6) `cat`

- **내용, 설명**
  - 텍스트 파일의 내용을 터미널에 출력한다.

- **예시**

    cat README.md
    cat test.txt

- **실수하기 쉬운 포인트**
  - 이미지/바이너리 파일에는 사용하지 말기 (깨진 출력 나옴)

---

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

---

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

---

## 9) `mv`

- **내용, 설명**
  - 파일/폴더 이동 또는 이름 변경

- **예시**

    mv a.txt folder/          # 이동
    mv old.txt new.txt        # 이름 변경
    mv my_folder backup_folder

- **실수하기 쉬운 포인트**
  - 덮어쓰기 위험 있음 → 중요한 파일은 확인하고 실행

---

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

---

## 11) `clear`

- **내용, 설명**
  - 터미널 화면을 깨끗하게 정리

- **예시**

    clear

- **실수하기 쉬운 포인트**
  - 기록 자체를 삭제하진 않음 → 단지 화면만 정리

---

## 12) `history`

- **내용, 설명**
  - 이전에 입력했던 명령어 기록을 보여준다.

- **예시**

    history

- **실수하기 쉬운 포인트**
  - 이전 명령이 기억 안 날 때 `history`로 찾아서 복사하면 편함

---

## 추가 팁: 경로 기호 정리

- **내용, 설명**
  - CLI에서 경로는 아래 기호를 자주 사용한다.

- **예시**

    cd ../..      # 상위 폴더 2번 올라가기
    cd ~/Desktop  # 홈 디렉토리 → Desktop 이동

- **실수하기 쉬운 포인트**
  - `.` / `..` / `~` 의미 헷갈리지 않기


---



---
# Git 활용법 정리 (기능 + 예시)

Git은 **코드 변경 사항을 기록하고(버전 관리)**, 다른 사람과 **협업**할 수 있게 도와주는 도구다.  
프로젝트의 “저장(커밋)” 단위로 기록하며, 브랜치/병합을 통해 안전하게 작업을 나눌 수 있다.

---

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

---

## 1) `git init` : Git 저장소 시작하기

- **내용, 설명**
  - 현재 폴더를 Git 저장소로 만든다.
  - `.git` 폴더가 생성되며 버전 관리가 시작된다.

- **예시**

    git init

- **실수하기 쉬운 포인트**
  - 이미 Git 저장소인 폴더에서 다시 init하면 꼬일 수 있음  
  - `.git` 폴더를 함부로 삭제하지 말기

---

## 2) `git status` : 현재 상태 확인

- **내용, 설명**
  - 변경된 파일 / 스테이징 여부 / 브랜치 상태를 확인한다.
  - Git이 “현재 무엇을 알고 있는지” 보는 가장 중요한 명령어

- **예시**

    git status

- **실수하기 쉬운 포인트**
  - 문제 생기면 무조건 `git status`부터 확인하면 해결이 빨라진다.

---

## 3) `git add` : 스테이징(커밋 후보 등록)

- **내용, 설명**
  - 커밋에 포함할 변경사항을 스테이징 영역에 올린다.

- **예시**

    git add 파일이름
    git add .          # 현재 폴더 기준 전체 변경사항 스테이징
    git add -A         # 삭제까지 포함해서 전체 반영

- **실수하기 쉬운 포인트**
  - `git add .`는 “변경사항 저장”이 아니라 “커밋 후보로 등록”이다.

---

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

---

## 5) `git log` : 커밋 기록 보기

- **내용, 설명**
  - 지금까지 저장된 커밋(버전) 이력을 확인한다.

- **예시**

    git log
    git log --oneline
    git log --oneline --graph --decorate

- **실수하기 쉬운 포인트**
  - 해시값(커밋 ID)은 되돌리기/비교할 때 필요하니 익숙해지기

---

## 6) `git diff` : 변경 내용 비교하기

- **내용, 설명**
  - 커밋 전후로 “어떤 부분이 바뀌었는지” 확인한다.

- **예시**

    git diff            # add 하기 전 변경 내용
    git diff --staged   # add 후 스테이징된 변경 내용

- **실수하기 쉬운 포인트**
  - 커밋 전에 `git diff`로 확인하면 실수를 크게 줄일 수 있다.

---

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

---

## 8) `git pull` : 원격 변경

- **내용, 설명**
  - 원격 저장소 최신 커밋을 내려받아 현재 브랜치에 반영한다.

- **예시**

    git pull origin main

- **실수하기 쉬운 포인트**
  - 협업 중에는 작업 시작 전에 `git pull` 먼저 하는 습관이 중요!

---

## 9) `git clone` : 원격 저장소 복제

- **내용, 설명**
  - 원격 저장소 내용을 내 컴퓨터로 통째로 복사한다.

- **예시**

    git clone https://github.com/유저명/레포명.git

- **실수하기 쉬운 포인트**
  - clone은 이미 remote까지 설정된 상태로 시작함 (`git remote -v` 확인 가능)

---

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

---

## 11) 병합: `git merge`

- **내용, 설명**
  - 다른 브랜치 작업 내용을 현재 브랜치로 합친다.

- **예시**

    git switch main
    git merge new-feature

- **실수하기 쉬운 포인트**
  - merge 전에 항상 `git status`로 깨끗한 상태인지 확인
  - 충돌(conflict)이 나면 당황하지 말고 수정 → add → commit

---

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

---

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

---

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
