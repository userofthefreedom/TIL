## 📚 목차

- [Python](#python)
- [CLI 기본 명령어](#cli-기본-명령어)
- [Git 활용법 정리 (기능 + 예시)](#git-활용법-정리-기능--예시)
- [Markdown / README 작성법 정리](#markdown--readme-작성법-정리)
- [Algorithm](#algorithm)
- [라이브러리](#라이브러리)
  - [Numpy](#numpy)
  - [Pandas](#pandas)
  - [Matplotlib](#matplotlib)
  - [collections](#collections)
  - [itertools](#itertools)
  - [pathlib (Path)](#pathlib-path)
  - [datetime](#datetime)
  - [random](#random)
  - [logging](#logging)
- [WEB](#web)

# Python

Python 학습 정리는 [python/README.md](python/README.md)로 이동했습니다.

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

# Algorithm

알고리즘 학습 정리는 [algorithm/README.md](algorithm/README.md)로 이동했습니다.

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
---
---

# WEB

WEB 학습 정리는 [web/README.md](web/README.md)로 이동했습니다.

