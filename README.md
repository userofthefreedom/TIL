
[Python](#python-study-notes) | [CLI](#cli-기본-명령어) | [Git](#git-활용법-정리) | [Markdown](#markdown--readme-작성법) | [Numpy](#numpy) | [Pandas](#pandas) | [matplotlib](#matplotlib) | [알고리즘](#알고리즘algorithm-기초)

_정리 스타일: 대목차는 #, 핵심 개념 구분만 ## 사용, 나머지는 - 들여쓰기_  
_최종 수정: 2026-02-10_


# Python Study Notes

## Basic 개념

- 실행 과정
  - 컴퓨터는 기계어만 이해한다
  - 사람이 작성한 코드는 인터프리터가 한 줄씩 번역하고 실행한다
  - 즉, **코드를 쓰는 것 = 컴퓨터에게 순서대로 명령을 내리는 것**

- 인터프리터
  - 코드를 위에서부터 한 줄씩 읽고 바로 실행
  - 실행 도중 에러가 나면 그 즉시 멈춘다
  - Python, JavaScript가 대표적인 인터프리터 언어

- 표현식 (Expression)
  - 하나의 값으로 평가될 수 있는 모든 코드
  ```python
  3 + 5        # 8
  x > 10       # True or False
  5 * 4        # 20
  ```

- 값 (Value)
  - 더 이상 계산되지 않는 최종 결과 데이터
  ```python
  3.14
  "hello"
  True
  ```

## 변수와 자료형

- 변수란?
  - 값을 저장하기 위한 이름표
  - 나중에 다시 사용하기 위해 값을 기억해 두는 공간

- 자료형(Data Type)
  - 값의 종류와 가능한 연산을 결정하는 속성
  - 같은 자료형끼리는 비슷한 연산이 가능하다

- 기본 사용 예
  ```python
  a = 1
  b = "1"
  c = True

  print(type(a), type(b), type(c))
  # <class 'int'> <class 'str'> <class 'bool'>
  ```

- bool 형 변환 규칙
  ```python
  print(bool(0))    # False
  print(bool(""))   # False
  print(bool(-1))   # True
  print(bool("A"))  # True
  ```
  - 숫자 0과 빈 문자열만 False

### Numeric types (숫자형)

- int (정수)
  ```python
  x = 10
  y = -5
  print(x + y)  # 5
  ```

- float (실수)
  ```python
  pi = 3.14
  print(pi * 2)  # 6.28
  ```

### Sequence types (순서 자료형)

- str (문자열)
- list (리스트)
- tuple (튜플)
- range (범위)

---

# CLI 기본 명령어

## 자주 사용하는 명령어

- 현재 위치 확인
  ```bash
  pwd
  ```

- 파일 목록 보기
  ```bash
  ls
  ```

- 폴더 이동
  ```bash
  cd folder_name
  ```

---

# Git 활용법 정리

## 기본 흐름

```bash
git init
git add .
git commit -m "message"
git push
```

- 현재 상태 확인
```bash
git status
```

- 변경 사항 비교
```bash
git diff
```

---

# Markdown / README 작성법

## 기본 문법

- 코드 블럭
```markdown
```python
print("Hello")
```
```

- 리스트
```markdown
- 항목1
  - 하위 항목
```

---

# Numpy

## 배열 생성

```python
import numpy as np

arr = np.array([1, 2, 3])
print(arr)  # [1 2 3]
```

---

# Pandas

## 데이터 프레임 생성

```python
import pandas as pd

df = pd.DataFrame({"A": [1,2], "B": [3,4]})
print(df)
```

## 문자열 처리

```python
df["name"].str.upper()
```

## 날짜 처리

```python
df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
```

---

# matplotlib

## 기본 그래프

```python
import matplotlib.pyplot as plt

x = [1,2,3]
y = [10,20,15]

plt.plot(x, y)
plt.title("Simple Graph")
plt.show()
```

---

# 알고리즘(Algorithm) 기초

## 알고리즘이란?

- 문제를 해결하기 위한 절차적 방법
- 입력 → 처리 → 출력의 구조를 가진다
- 효율적인 알고리즘일수록 실행 시간이 짧다

## 시간 복잡도

- 알고리즘 성능을 나타내는 지표
- O(1), O(N), O(N log N), O(N²) 등으로 표현

## 대표 알고리즘 유형

- 완전 탐색
- 탐욕 알고리즘
- 분할 정복
- 동적 계획법(DP)
