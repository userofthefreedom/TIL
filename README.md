## 📚 목차

- [Python](#python)
- [CLI 기본 명령어](#cli-기본-명령어)
- [Git 활용법 정리 (기능 + 예시)](#git-활용법-정리-기능--예시)
- [Markdown / README 작성법 정리](#markdown--readme-작성법-정리)
- [알고리즘](#알고리즘)
  - [알고리즘 사고 방식](#알고리즘-사고-방식)
  - [기본 자료구조 기반 알고리즘](#기본-자료구조-기반-알고리즘)
  - [탐색 알고리즘](#탐색-알고리즘)
  - [배열 기반 알고리즘](#배열-기반-알고리즘)
  - [정렬 알고리즘](#정렬-알고리즘)
  - [그래프 알고리즘](#그래프-알고리즘)
  - [알고리즘 기법](#알고리즘-기법)
  - [자료구조 기반 알고리즘](#자료구조-기반-알고리즘)
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
  - [HTML](#html)
  - [CSS](#css)
  - [Layout](#layout)
  - [Bootstrap](#bootstrap)

## 🚀 Algorithm Quick Navigation

- [알고리즘 사고 방식](#알고리즘-사고-방식)
  - [알고리즘 기본 개념](#알고리즘-기본-개념)
  - [시간 복잡도](#시간-복잡도)

- [기본 자료구조 기반 알고리즘](#기본-자료구조-기반-알고리즘)
  - Stack
  - Recursion
  - Tree
  - Binary Tree
  - Binary Search Tree
  - 2D 배열 순회

- [탐색 알고리즘](#탐색-알고리즘)
  - DFS
  - BFS
  - Grid BFS
  - 완전 탐색
  - 선형 탐색

- [배열 기반 알고리즘](#배열-기반-알고리즘)
  - Two Pointer
  - Sliding Window
  - Prefix Sum
  - Binary Search

- [정렬 알고리즘](#정렬-알고리즘)
  - Selection Sort
  - Bubble Sort
  - Insertion Sort
  - Merge Sort
  - Quick Sort

- [그래프 알고리즘](#그래프-알고리즘)
  - Graph 개념
  - Union Find
  - MST
    - Kruskal
    - Prim
  - Shortest Path
    - Dijkstra
  - DAG
    - Topological Sort

- [알고리즘 기법](#알고리즘-기법)
  - Greedy
  - Backtracking
  - Divide and Conquer
  - Dynamic Programming
  - Bit Manipulation

- [자료구조 기반 알고리즘](#자료구조-기반-알고리즘)
  - Priority Queue
  - Segment Tree
  - Fenwick Tree
  - Trie

---

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

# 알고리즘

## 알고리즘 사고 방식
- 알고리즘 기본 개념
  - 알고리즘이란
    - 문제를 해결하기 위한 절차적 방법(순서 있는 해결 과정)
    - 입력(Input)을 받아 원하는 출력(Output)을 만드는 일련의 단계
    - 컴퓨터가 이해할 수 있도록 논리적으로 구성된 해결 방법
  - 예시
    - 라면 끓이기 알고리즘

        ```
        물 끓이기 → 면 넣기 → 스프 넣기 → 완성
        ```

  - 알고리즘 특징
    - 명확성
      - 단계가 모호하지 않아야 한다
    - 유한성
      - 반드시 끝나야 한다
    - 입력 / 출력 존재
      - 입력 데이터가 존재하고 결과 출력이 있어야 한다

- 알고리즘 공부의 큰 흐름
  - 정확성
    - 답이 맞는가
    - 반례가 없는가
  - 시간 복잡도
    - 입력 크기가 커질 때 실행 시간이 얼마나 증가하는가
  - 공간 복잡도
    - 알고리즘이 사용하는 메모리 양

- 알고리즘 문제 해결 과정
  - 문제 읽기
  - 설계
  - 구현
  - 디버깅

- 디버깅
  - 디버깅 개념
    - 프로그램 실행 과정에서 발생하는 오류를 찾고 수정하는 과정
  - IDE 디버깅 단축키
    - Ctrl + F8
      - breakpoint 설정
    - Shift + F9
      - 디버깅 시작
    - F8
      - Step Over
    - F7
      - Step Into
    - Ctrl + F2
      - 디버깅 종료

- 시간 복잡도
  - 시간 복잡도 개념
    - 입력 크기 N이 증가할 때 알고리즘 실행 시간이 얼마나 증가하는지를 나타내는 척도
  - 왜 중요한가
    - 같은 문제라도 알고리즘에 따라 실행 시간이 크게 달라질 수 있다
  - 예시
    - 리스트에서 최대값 찾기
      - 방법 1 : 정렬 후 최대값 찾기
        - 예시 코드

            ```python
            arr = [5,1,9,3,7]
            arr.sort()
            max_val = arr[-1]
            print(max_val)
            ```

        - 실행 결과

            ```
            9
            ```

        - 시간 복잡도

            ```
            O(N log N)
            ```

      - 방법 2 : 한 번 순회
        - 예시 코드

            ```python
            arr = [5,1,9,3,7]

            max_val = arr[0]

            for x in arr:
                if x > max_val:
                    max_val = x

            print(max_val)
            ```

        - 실행 결과

            ```
            9
            ```

        - 시간 복잡도

            ```
            O(N)
            ```

  - Big-O 표기법
    - 개념
      - 알고리즘의 시간 복잡도를 표현하는 방법
      - 입력 크기 N이 매우 커질 때 가장 큰 영향만 남기고 나머지는 무시한다
    - 시간 복잡도 증가 순서

        ```
        O(1) < O(log N) < O(N) < O(N log N) < O(N²) < O(N³) < O(2ⁿ) < O(N!)
        ```

    - 주요 시간 복잡도
      - O(1)
        - 의미
          - 상수 시간
          - 입력 크기와 관계없이 항상 일정한 시간
        - 예시
          - 예시 코드

              ```python
              arr = [10,20,30,40,50]
              print(arr[3])
              ```

          - 실행 결과

              ```
              40
              ```

      - O(log N)
        - 의미
          - 로그 시간
          - 문제 크기가 절반씩 줄어드는 구조
        - 예시 : 이진 탐색
          - 예시 코드

              ```python
              arr = [1,3,5,7,9,11,13]
              target = 9

              left = 0
              right = len(arr) - 1

              while left <= right:
                  mid = (left + right) // 2

                  if arr[mid] == target:
                      print(mid)
                      break
                  elif arr[mid] < target:
                      left = mid + 1
                  else:
                      right = mid - 1
              ```

          - 실행 결과

              ```
              4
              ```

      - O(N)
        - 의미
          - 선형 시간
          - 데이터를 한 번 전체 순회
        - 예시
          - 예시 코드

              ```python
              arr = [5,1,9,3,7]

              max_val = arr[0]

              for x in arr:
                  if x > max_val:
                      max_val = x

              print(max_val)
              ```

          - 실행 결과

              ```
              9
              ```

      - O(N log N)
        - 의미
          - 정렬 알고리즘에서 자주 등장하는 시간 복잡도
        - 예시
          - 예시 코드

              ```python
              arr = [5,1,9,3,7]
              arr.sort()
              print(arr)
              ```

          - 실행 결과

              ```
              [1,3,5,7,9]
              ```

      - O(N²)
        - 의미
          - 이중 반복문에서 자주 발생
        - 예시
          - 예시 코드

              ```python
              for i in range(n):
                  for j in range(n):
                      print(i, j)
              ```

      - O(N³)
        - 의미
          - 삼중 반복문 구조
        - 예시
          - 예시 코드

              ```python
              for i in range(n):
                  for j in range(n):
                      for k in range(n):
                          print(i, j, k)
              ```

      - O(2ⁿ)
        - 의미
          - 부분집합과 같은 완전 탐색에서 자주 등장
        - 예시
          - 예시 코드

              ```python
              arr = [1,2,3]
              n = len(arr)

              def subset(idx):
                  if idx == n:
                      return

                  subset(idx + 1)
                  subset(idx + 1)

              subset(0)
              ```

          - 왜 O(2ⁿ)인가
            - 각 원소마다 두 가지 선택이 존재한다

                ```
                선택 / 선택 안 함
                ```

            - 따라서 전체 경우의 수는 다음과 같다

                ```
                2 × 2 × 2 ... = 2ⁿ
                ```

      - O(N!)
        - 의미
          - 순열 탐색에서 자주 등장
        - 예시
          - 예시 코드

              ```python
              from itertools import permutations

              arr = [1,2,3]

              for p in permutations(arr):
                  print(p)
              ```

          - 실행 결과

              ```
              (1, 2, 3)
              (1, 3, 2)
              (2, 1, 3)
              (2, 3, 1)
              (3, 1, 2)
              (3, 2, 1)
              ```

  - 시간 복잡도 계산 규칙
    - 상수 제거

        ```
        O(2N) → O(N)
        ```

    - 가장 큰 항만 남김

        ```
        O(N² + N) → O(N²)
        ```

    - 중첩 반복문은 곱

        ```
        for i in N
            for j in N

        → O(N²)
        ```

## 기본 자료구조 기반 알고리즘

- 배열 (Array)
  - 개념
    - 같은 타입의 데이터를 연속된 메모리 공간에 저장하는 자료구조
    - 각 요소는 인덱스(index)를 이용해 접근할 수 있다
    - 알고리즘 문제에서 가장 기본적으로 사용되는 자료구조

  - 특징
    - 인덱스를 이용한 접근

        ```
        O(1)
        ```

    - 데이터가 연속된 메모리에 저장된다

  - 예시
    - 예시 코드

        ```python
        arr = [10,20,30,40,50]

        print(arr[0])
        print(arr[3])
        ```

    - 실행 결과

        ```
        10
        40
        ```

  - 배열 주요 연산 시간 복잡도

      ```
      접근   O(1)
      탐색   O(N)
      삽입   O(N)
      삭제   O(N)
      ```

  - 삽입이 느린 이유
    - 설명
      - 중간에 삽입하면 뒤에 있는 모든 데이터를 이동해야 한다

    - 예시 코드

        ```python
        arr = [1,2,3,4]

        arr.insert(1,99)

        print(arr)
        ```

    - 실행 결과

        ```
        [1, 99, 2, 3, 4]
        ```

- 2차원 배열
  - 개념
    - 행(row)과 열(column)로 구성된 배열
    - 표 형태 데이터를 표현할 때 사용된다

  - 예시
    - 예시 코드

        ```python
        arr = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]

        print(arr[1][2])
        ```

    - 실행 결과

        ```
        6
        ```

  - 2차원 배열 순회
    - 행 우선 순회
      - 예시 코드

        ```python
        arr = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]

        for r in range(len(arr)):
            for c in range(len(arr[0])):
                print(arr[r][c], end=" ")
        ```

      - 실행 결과

        ```
        1 2 3 4 5 6 7 8 9
        ```

    - 열 우선 순회
      - 예시 코드

        ```python
        arr = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]

        for c in range(len(arr[0])):
            for r in range(len(arr)):
                print(arr[r][c], end=" ")
        ```

      - 실행 결과

        ```
        1 4 7 2 5 8 3 6 9
        ```

  - 델타 탐색 (4방향 탐색)
    - 개념
      - 격자에서 상하좌우 이동을 처리하는 방법

    - 예시 코드

        ```python
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]

        r, c = 1, 1

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            print(nr, nc)
        ```

    - 실행 결과

        ```
        0 1
        2 1
        1 0
        1 2
        ```
  - 지그재그 순회
    - 개념
      - 한 행은 왼쪽 → 오른쪽
      - 다음 행은 오른쪽 → 왼쪽

    - 예시 코드

        ```python
        arr = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]

        for r in range(len(arr)):

            if r % 2 == 0:

                for c in range(len(arr[0])):
                    print(arr[r][c], end=" ")

            else:

                for c in range(len(arr[0])-1,-1,-1):
                    print(arr[r][c], end=" ")
        ```

    - 실행 결과

        ```
        1 2 3 6 5 4 7 8 9
        ```

  - 대각선 순회
    - 개념
      - 배열을 대각선 방향으로 순회

    - 예시 코드

        ```python
        arr = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]

        n = len(arr)

        for d in range(n*2-1):

            for r in range(n):

                c = d - r

                if 0 <= c < n:
                    print(arr[r][c], end=" ")
        ```

  - 경계 체크 함수
    - 예시 코드

        ```python
        def in_range(r,c,n,m):

            return 0 <= r < n and 0 <= c < m
        ```

  - 4방향 이웃 탐색

      ```python
      def neighbors_4(r,c,n,m):

          dr = [-1,1,0,0]
          dc = [0,0,-1,1]

          for d in range(4):

              nr = r + dr[d]
              nc = c + dc[d]

              if 0 <= nr < n and 0 <= nc < m:
                  yield nr,nc
      ```

  - 대각선 이웃 탐색

      ```python
      def neighbors_diag(r,c,n,m):

          dr = [-1,-1,1,1]
          dc = [-1,1,-1,1]

          for d in range(4):

              nr = r + dr[d]
              nc = c + dc[d]

              if 0 <= nr < n and 0 <= nc < m:
                  yield nr,nc
      ```

  - 8방향 탐색

      ```python
      def neighbors_8(r,c,n,m):

          dr = [-1,-1,-1,0,0,1,1,1]
          dc = [-1,0,1,-1,1,-1,0,1]

          for d in range(8):

              nr = r + dr[d]
              nc = c + dc[d]

              if 0 <= nr < n and 0 <= nc < m:
                  yield nr,nc
      ```

  - 특정 값 탐색

      ```python
      def neighbors_with_value(arr,r,c,value):

          n = len(arr)
          m = len(arr[0])

          for nr,nc in neighbors_4(r,c,n,m):

              if arr[nr][nc] == value:
                  return True

          return False
      ```

  - 2차원 배열 시간 복잡도

      ```
      N × M 배열 전체 순회

      O(N × M)
      ```

- Stack
  - 개념
    - LIFO 구조
    - Last In First Out
    - 마지막에 들어온 데이터가 먼저 나온다

  - 주요 연산

      ```
      push
      pop
      peek
      ```

  - 예시
    - 예시 코드

        ```python
        stack = []

        stack.append(10)
        stack.append(20)
        stack.append(30)

        print(stack.pop())
        print(stack[-1])
        ```

    - 실행 결과

        ```
        30
        20
        ```

  - 활용 예 : 괄호 검사
    - 예시 코드

        ```python
        def check_parentheses(s):

            stack = []

            for ch in s:

                if ch == "(":
                    stack.append(ch)

                else:

                    if not stack:
                        return False

                    stack.pop()

            return len(stack) == 0


        print(check_parentheses("(())"))
        print(check_parentheses("(()"))
        ```

    - 실행 결과

        ```
        True
        False
        ```

- Recursion
  - 개념
    - 함수가 자기 자신을 다시 호출하는 방식

  - 필수 요소

      ```
      Base Case
      Recursive Case
      ```

  - 예시 : 팩토리얼
    - 예시 코드

        ```python
        def factorial(n):

            if n == 1:
                return 1

            return n * factorial(n-1)


        print(factorial(5))
        ```

    - 실행 결과

        ```
        120
        ```

- Tree
  - 개념
    - 부모와 자식 관계로 연결된 계층 구조 자료구조
  - 왜 트리가 필요한가
    - 데이터가 계층 구조를 가질 때 자연스럽게 표현할 수 있다
    - 선형 구조(배열, 연결 리스트)로 표현하기 어려운 관계를 나타낼 수 있다

    - 대표 예시

        ```
        파일 시스템
        조직도
        HTML DOM
        의사결정 구조
        ```
  - 특징

      ```
      사이클이 없다
      하나의 루트 노드가 존재한다
      부모는 하나
      자식은 여러 개 가능
      ```

  - 트리 용어

 

  - 트리 표현
    - 배열 기반 표현
      - 예시 코드

        ```python
        tree = " ABCDEFG"
        ```

      - 트리 구조 예

        ```
              A
            /   \
           B     C
          / \   / \
         D   E F   G
        ```

  - 트리 순회 (Tree Traversal)
    - 개념
      - 트리 순회(traversal)는 트리의 모든 노드를 한 번씩 방문하는 방법이다
      - 어떤 순서로 방문하느냐에 따라 결과가 달라진다

    - 대표 순회 방식

        ```
        DFS 기반 순회
        Preorder
        Inorder
        Postorder

        BFS 기반 순회
        레벨 순회
        ```

    - 트리 DFS 설명
      - DFS는 한 방향으로 최대한 깊게 내려간 뒤 다시 올라오는 방식이다
      - 트리에서는 재귀로 구현하는 경우가 많다

    - 트리 BFS 설명
      - BFS는 루트부터 같은 높이(depth)의 노드를 먼저 방문하는 방식이다
      - 트리에서는 Queue를 사용하여 구현한다
    - Preorder
      - 방문 순서

        ```
        Root → Left → Right
        ```

      - 예시 코드

        ```python
        tree = " ABCDEFG"

        def preorder(node):

            if node >= len(tree):
                return

            if tree[node] == " ":
                return

            print(tree[node], end=" ")

            preorder(node*2)
            preorder(node*2+1)


        preorder(1)
        ```

      - 실행 결과

        ```
        A B D E C F G
        ```

    - Inorder
      - 방문 순서

        ```
        Left → Root → Right
        ```

      - 예시 코드

        ```python
        tree = " ABCDEFG"

        def inorder(node):

            if node >= len(tree):
                return

            if tree[node] == " ":
                return

            inorder(node*2)

            print(tree[node], end=" ")

            inorder(node*2+1)


        inorder(1)
        ```

      - 실행 결과

        ```
        D B E A F C G
        ```

    - Postorder
      - 방문 순서

        ```
        Left → Right → Root
        ```

      - 예시 코드

        ```python
        tree = " ABCDEFG"

        def postorder(node):

            if node >= len(tree):
                return

            if tree[node] == " ":
                return

            postorder(node*2)
            postorder(node*2+1)

            print(tree[node], end=" ")


        postorder(1)
        ```

      - 실행 결과

        ```
        D E B F G C A
        ```

  - LCA (Lowest Common Ancestor)

    - 개념
      - 트리에서 두 노드의 **가장 가까운 공통 조상**

    - 예시

        ```
              1
            /   \
          2     3
          / \
        4   5
        ```

        ```
        LCA(4,5) = 2
        ```

    - 예시 코드

        ```python
        parent = [0,0,1,1,2,2]

        def lca(a,b):

            visited = set()

            while a:

                visited.add(a)
                a = parent[a]

            while b:

                if b in visited:
                    return b

                b = parent[b]

        print(lca(4,5))
        ```

    - 실행 결과

        ```
        2
        ```

    - Euler Tour Technique

      - 개념
        - 트리를 DFS 순회하여 **선형 배열로 변환하는 방법**

      - 활용

          ```
          Subtree Query
          LCA
          Segment Tree
          ```

      - 핵심 아이디어

          ```
          노드 방문 시간을 기록
          ```

      - 예시 코드

          ```python
          graph = {
              1:[2,3],
              2:[4,5],
              3:[],
              4:[],
              5:[]
          }

          start = {}
          end = {}

          order = []
          time = 0

          def dfs(v):

              global time

              start[v] = time
              order.append(v)

              time += 1

              for nxt in graph[v]:
                  dfs(nxt)

              end[v] = time-1


          dfs(1)

          print(order)
          print(start)
          print(end)
          ```

      - 실행 결과

          ```
          [1,2,4,5,3]
          {1: 0, 2: 1, 4: 2, 5: 3, 3: 4}
          {4: 2, 5: 3, 2: 3, 3: 4, 1: 4}
          ```

  - Binary Search Tree
    - 개념

        ```
        왼쪽 자식 < 부모 < 오른쪽 자식
        ```

    - 특징

        ```
        평균 탐색 O(log N)
        ```
    - 삽입
      - 개념
        - BST 규칙에 맞는 위치를 찾아 노드를 삽입한다

      - 예시 코드

        ```python
        arr = [0]*20
        data = [4,2,9,7,15,1,3]

        def insert(x):

            now = 1

            while True:

                if arr[now] == 0:
                    arr[now] = x
                    return

                if arr[now] < x:
                    now = now*2 + 1
                else:
                    now = now*2

        for x in data:
            insert(x)
        ```

    - 탐색
      - 개념
        - BST의 규칙을 이용하여 값을 빠르게 찾는다

      - 예시 코드

        ```python
        def search(target):

            now = 1

            while True:

                if now >= 20:
                    return False

                if arr[now] == target:
                    return True

                if arr[now] < target:
                    now = now*2 + 1
                else:
                    now = now*2
        ```

    - 삭제
      - 개념
        - BST에서 특정 값을 제거하는 연산
        - 삭제 후에도 BST 규칙은 유지되어야 한다

      - 삭제 케이스

        ```
        1. 자식 없음
        2. 자식 1개
        3. 자식 2개
        ```

      - 자식이 없는 경우
        - 그냥 노드를 삭제한다

      - 자식이 하나인 경우
        - 삭제할 노드를 없애고 자식을 부모와 연결한다

      - 자식이 두 개인 경우
        - inorder successor를 이용한다

      - inorder successor
        - 오른쪽 서브트리에서 가장 작은 값

## 탐색 알고리즘

- 탐색 (Search)
  - 개념
    - 데이터 집합에서 원하는 값을 찾는 과정
    - 알고리즘 문제에서 매우 자주 등장한다

  - 대표 탐색 방법

      ```
      선형 탐색
      이진 탐색
      DFS
      BFS
      완전 탐색
      ```

- 선형 탐색 (Linear Search)
  - 개념
    - 데이터를 처음부터 하나씩 확인하면서 찾는 방법

  - 특징

      ```
      구현이 쉽다
      정렬이 필요 없다
      데이터가 많으면 느리다
      ```

  - 시간 복잡도

      ```
      O(N)
      ```

  - 예시
    - 예시 코드

        ```python
        arr = [5,8,3,9,2]
        target = 9

        for i in range(len(arr)):

            if arr[i] == target:
                print("index:",i)
                break
        ```

    - 실행 결과

        ```
        index: 3
        ```

- 이진 탐색 (Binary Search)
  - 개념
    - 탐색 범위를 절반씩 줄여가며 탐색하는 방법

  - 특징

      ```
      반드시 정렬된 데이터여야 한다
      매우 빠른 탐색
      ```

  - 시간 복잡도

      ```
      O(log N)
      ```

  - 예시
    - 예시 코드

        ```python
        arr = [1,3,5,7,9,11,13]
        target = 9

        left = 0
        right = len(arr)-1

        while left <= right:

            mid = (left + right)//2

            if arr[mid] == target:
                print("index:",mid)
                break

            elif arr[mid] < target:
                left = mid + 1

            else:
                right = mid - 1
        ```

    - 실행 결과

        ```
        index: 4
        ```
  - Lower Bound / Upper Bound

    - 개념
      - Lower Bound : 처음으로 target 이상이 되는 위치
      - Upper Bound : 처음으로 target 초과가 되는 위치

    - 예시 코드

        ```python
        import bisect

        arr = [1,2,2,2,3,4]

        print(bisect.bisect_left(arr,2))
        print(bisect.bisect_right(arr,2))
        ```

    - 실행 결과

        ```
        1
        4
        ```

  - Binary Search on Answer

    - 개념
      - 정답의 범위를 이진 탐색으로 줄여가는 방법
      - 정답이 숫자 범위 안에 있을 때 사용된다

    - 대표 문제

        ```
        최소 시간
        최대 길이
        가능한 최소값
        ```

    - 핵심 아이디어

        ```
        mid 값이 가능한지 검사
        ```

    - 예시 문제
      - 랜선 자르기

    - 예시 코드

        ```python
        cables = [802,743,457,539]
        target = 11

        left = 1
        right = max(cables)

        answer = 0

        while left <= right:

            mid = (left + right) // 2

            pieces = 0

            for c in cables:
                pieces += c // mid

            if pieces >= target:

                answer = mid
                left = mid + 1

            else:

                right = mid - 1

        print(answer)
        # 200
        ```

    - 시간 복잡도

        ```
        O(N log M)

        N = 배열 길이
        M = 탐색 범위
        ```    

- DFS (Depth First Search)
  - 개념
    - 깊이 우선 탐색
    - 한 방향으로 갈 수 있을 때까지 끝까지 탐색

  - 특징

      ```
      스택 구조
      재귀 구현 가능
      경로 탐색에 유리
      ```

  - 탐색 예

      ```
          A
          / \
        B   C
        / \
      D   E

      DFS 탐색 순서
      A → B → D → E → C
      ```

  - 예시
    - 예시 코드

        ```python
        graph = [
            [],
            [2,3],
            [1,4,5],
            [1],
            [2],
            [2]
        ]

        visited = [False]*6

        def dfs(v):

            visited[v] = True
            print(v,end=" ")

            for nxt in graph[v]:

                if not visited[nxt]:
                    dfs(nxt)

        dfs(1)
        ```

    - 실행 결과

        ```
        1 2 4 5 3
        ```

- BFS (Breadth First Search)
  - 개념
    - 너비 우선 탐색
    - 가까운 노드부터 탐색

  - 특징

      ```
      큐(queue) 사용
      최단 거리 문제에 자주 사용
      ```

  - 탐색 예

      ```
          A
          / \
        B   C
        / \
      D   E

      BFS 탐색 순서
      A → B → C → D → E
      ```

  - 예시
    - 예시 코드

        ```python
        from collections import deque

        graph = [
            [],
            [2,3],
            [1,4,5],
            [1],
            [2],
            [2]
        ]

        visited = [False]*6

        def bfs(start):

            q = deque([start])
            visited[start] = True

            while q:

                v = q.popleft()

                print(v,end=" ")

                for nxt in graph[v]:

                    if not visited[nxt]:

                        visited[nxt] = True
                        q.append(nxt)

        bfs(1)
        ```

    - 실행 결과

        ```
        1 2 3 4 5
        ```

  - Grid BFS

    - 개념
        - 2차원 격자에서 BFS를 이용해 탐색하는 방법
        - 주로 **최단 거리 문제**에서 사용된다

    - 대표 문제

        ```
        미로 탐색
        최단 거리
        섬 개수
        ```

    - 핵심 아이디어

        ```
        상하좌우 이동
        Queue 사용
        방문 체크
        ```

    - 이동 방향

        ```python
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]
        ```

    - 예시 문제
        - 시작점에서 목표 지점까지 최단 거리 찾기

    - 예시 코드

        ```python
        from collections import deque

        grid = [
            [1,1,0],
            [0,1,1],
            [0,0,1]
        ]

        n = len(grid)
        m = len(grid[0])

        dr = [-1,1,0,0]
        dc = [0,0,-1,1]

        def bfs(sr,sc):

            q = deque()
            q.append((sr,sc,0))

            visited = [[False]*m for _ in range(n)]
            visited[sr][sc] = True

            while q:

                r,c,d = q.popleft()

                if (r,c) == (2,2):
                    return d

                for k in range(4):

                    nr = r + dr[k]
                    nc = c + dc[k]

                    if 0 <= nr < n and 0 <= nc < m:

                        if grid[nr][nc] == 1 and not visited[nr][nc]:

                            visited[nr][nc] = True
                            q.append((nr,nc,d+1))

        print(bfs(0,0))
        ```

    - 실행 결과

        ```
        4
        ```

    - 시간 복잡도

        ```
        O(N × M)
        ```

  - Multi Source BFS

    - 개념
      - 여러 시작점에서 동시에 BFS를 시작하는 방법

    - 대표 문제

        ```
        토마토 문제
        전염 확산
        최단 거리 확산
        ```

    - 핵심 아이디어

        ```
        시작점 여러 개를
        Queue에 모두 넣는다
        ```

    - 예시 코드

        ```python
        from collections import deque

        grid = [
            [1,0,0],
            [0,0,0],
            [0,0,1]
        ]

        n = len(grid)
        m = len(grid[0])

        q = deque()

        for r in range(n):
            for c in range(m):

                if grid[r][c] == 1:
                    q.append((r,c))

        dr = [-1,1,0,0]
        dc = [0,0,-1,1]

        while q:

            r,c = q.popleft()

            for k in range(4):

                nr = r + dr[k]
                nc = c + dc[k]

                if 0 <= nr < n and 0 <= nc < m:

                    if grid[nr][nc] == 0:

                        grid[nr][nc] = grid[r][c] + 1
                        q.append((nr,nc))

        print(grid)
        # [[1, 2, 3], [2, 3, 2], [3, 2, 1]]
        ```

- Flood Fill

  - 개념
    - 특정 위치에서 시작하여 **같은 영역을 모두 탐색하는 알고리즘**
    - DFS 또는 BFS로 구현할 수 있다

  - 대표 문제

      ```
      그림 영역 찾기
      섬 개수
      영역 크기 계산
      ```

  - 핵심 아이디어

      ```
      같은 값이면 계속 탐색
      방문 체크
      ```

  - 예시 코드

      ```python
      grid = [
          [1,1,0],
          [1,0,0],
          [0,0,1]
      ]

      n = len(grid)
      m = len(grid[0])

      visited = [[False]*m for _ in range(n)]

      dr = [-1,1,0,0]
      dc = [0,0,-1,1]

      def dfs(r,c):

          visited[r][c] = True
          count = 1

          for k in range(4):

              nr = r + dr[k]
              nc = c + dc[k]

              if 0 <= nr < n and 0 <= nc < m:

                  if grid[nr][nc] == 1 and not visited[nr][nc]:

                      count += dfs(nr,nc)

          return count


      areas = []

      for r in range(n):
          for c in range(m):

              if grid[r][c] == 1 and not visited[r][c]:

                  areas.append(dfs(r,c))

      print(areas)
      ```

  - 실행 결과

      ```
      [3,1]
      ```

  - 시간 복잡도

      ```
      O(N × M)
      ```

- DFS vs BFS 비교

    ```
    DFS
    깊게 탐색
    스택
    경로 문제

    BFS
    가까운 노드부터
    큐
    최단 거리 문제
    ```

- 완전 탐색 (Brute Force)
  - 개념
    - 가능한 모든 경우를 확인하는 방법

  - 특징

      ```
      구현이 단순하다
      항상 정답을 찾는다
      경우의 수가 많으면 느리다
      ```
  - 문자열 패턴 검색 (Brute Force)

    - 개념
      - 텍스트 문자열에서 특정 패턴을 찾는 가장 단순한 방법
      - 가능한 모든 위치에서 패턴을 비교한다

    - 아이디어

        ```
        텍스트의 각 위치에서
        패턴과 하나씩 비교한다
        ```

    - 예시

        ```
        text = "ABCABCAB"
        pattern = "CAB"
        ```

    - 예시 코드

        ```python
        def bruteforce(pattern, text):

            M = len(pattern)
            N = len(text)

            for i in range(N-M+1):

                j = 0

                while j < M and text[i+j] == pattern[j]:
                    j += 1

                if j == M:
                    return i

            return -1


        text = "ABCABCAB"
        pattern = "CAB"

        print(bruteforce(pattern, text))
        ```

    - 실행 결과

        ```
        2
        ```

    - 시간 복잡도

        ```
        O(N × M)

        N = 텍스트 길이
        M = 패턴 길이
        ```

  - 순열 탐색
    - 개념
        - 가능한 모든 순서를 탐색

    - 시간 복잡도

        ```
        O(N!)
        ```

    - 예시
        - 예시 코드

            ```python
            arr = [1,2,3]

            used = [False]*3

            def perm(path):

                if len(path) == 3:
                    print(path)
                    return

                for i in range(3):

                    if used[i]:
                        continue

                    used[i] = True
                    perm(path+[arr[i]])
                    used[i] = False

            perm([])
            ```

        - 실행 결과

            ```
            [1, 2, 3]
            [1, 3, 2]
            [2, 1, 3]
            [2, 3, 1]
            [3, 1, 2]
            [3, 2, 1]
            ```

  - 부분집합 (Subsets)

    - 개념
      - 어떤 집합에서 원소를 선택하거나 선택하지 않는 모든 경우를 의미한다
      - 원소가 N개이면 부분집합의 개수는 다음과 같다

          ```
          2^N
          ```

    - 예시

        ```
        arr = [1,2,3]

        부분집합

        []
        [1]
        [2]
        [3]
        [1,2]
        [1,3]
        [2,3]
        [1,2,3]
        ```

    - 시간 복잡도

        ```
        O(2^N)
        ```

    - 부분집합 생성 방법

        ```
        1. 백트래킹
        2. 비트마스크
        ```

    - 백트래킹 방식

      - 아이디어
        - 각 원소마다 선택 / 선택하지 않음 두 가지 경우가 있다

            ```
            선택
            선택 안함
            ```

      - 예시 코드

          ```python
          arr = [1,2,3]

          path = []

          def subset(idx):

              if idx == len(arr):
                  print(path)
                  return

              path.append(arr[idx])
              subset(idx+1)

              path.pop()
              subset(idx+1)

          subset(0)
          ```

      - 실행 결과

          ```
          [1, 2, 3]
          [1, 2]
          [1, 3]
          [1]
          [2, 3]
          [2]
          [3]
          []
          ```

    - 비트마스크 방식

      - 아이디어
        - 비트를 이용하여 선택 여부를 표현한다

      - 예시

          ```
          arr = [1,2,3]

          mask = 5

          5 = 101 (binary)

          1 선택
          2 선택 안함
          3 선택
          ```

      - 예시 코드

          ```python
          arr = [1,2,3]

          n = len(arr)

          for mask in range(1<<n):

              subset = []

              for i in range(n):

                  if mask & (1<<i):
                      subset.append(arr[i])

              print(subset)
          ```

      - 실행 결과

          ```
          []
          [1]
          [2]
          [1, 2]
          [3]
          [1, 3]
          [2, 3]
          [1, 2, 3]
          ```
  
    - 응용
  
      - 조건 문제 예시

        - 부분집합의 합이 K가 되는 경우

        - 예시 코드

            ```python
            arr = [1,2,3,4]
            K = 5

            count = 0

            def subset(idx, s):

                global count

                if idx == len(arr):

                    if s == K:
                        count += 1

                    return

                subset(idx+1, s + arr[idx])
                subset(idx+1, s)

            subset(0,0)

            print(count)
            ```

        - 실행 결과

            ```
            2
            ```

      - pruning

        - 개념
          - 불필요한 탐색을 미리 차단하는 기법

        - 예시

            ```
            현재 합 > K
            ```

          이 경우 더 탐색할 필요가 없다

## 배열 기반 알고리즘

- Two Pointer
  - 개념
    - 두 개의 포인터를 사용하여 배열을 탐색하는 알고리즘 기법
    - 주로 **정렬된 배열**에서 많이 사용된다

  - 특징

      ```
      O(N) 시간에 해결 가능
      정렬된 배열에서 매우 강력
      ```

  - 대표 문제
    - 두 수의 합
    - 구간 합
    - 중복 제거

  - 예시 : 두 수의 합
    - 문제
      - 정렬된 배열에서 두 수의 합이 특정 값이 되는 쌍 찾기

    - 예시 코드

        ```python
        arr = [1,2,3,4,6,8,9]
        target = 10

        left = 0
        right = len(arr)-1

        while left < right:

            s = arr[left] + arr[right]

            if s == target:
                print(arr[left], arr[right])
                break

            elif s < target:
                left += 1

            else:
                right -= 1
        ```

    - 실행 결과

        ```
        1 9
        ```

- Sliding Window
  - 개념
    - 일정 크기의 구간(window)을 이동하면서 값을 계산하는 방법

  - 특징

      ```
      구간 문제에 매우 강력
      O(N)으로 해결 가능
      ```

  - 예시 : 최대 구간 합
    - 문제
      - 길이가 k인 구간 중 합이 가장 큰 값을 찾기

    - 예시 코드

        ```python
        arr = [2,1,5,1,3,2]
        k = 3

        window_sum = sum(arr[:k])
        max_sum = window_sum

        for i in range(k, len(arr)):

            window_sum += arr[i]
            window_sum -= arr[i-k]

            max_sum = max(max_sum, window_sum)

        print(max_sum)
        ```

    - 실행 결과

        ```
        9
        ```

- Prefix Sum
  - 개념
    - 배열의 누적 합을 미리 계산해 두는 방법

  - 특징

      ```
      구간 합 계산을 빠르게 할 수 있다
      ```

  - 예시

      ```
      arr = [1,2,3,4,5]

      prefix
      [0,1,3,6,10,15]
      ```

  - 예시 코드

      ```python
      arr = [1,2,3,4,5]

      prefix = [0]*(len(arr)+1)

      for i in range(len(arr)):
          prefix[i+1] = prefix[i] + arr[i]

      print(prefix)
      ```

    - 실행 결과

      ```
      [0,1,3,6,10,15]
      ```

  - 구간 합 계산
    - 공식

        ```
        sum(l,r) = prefix[r] - prefix[l-1]
        ```

    - 예시 코드

        ```python
        arr = [1,2,3,4,5]

        prefix = [0]*(len(arr)+1)

        for i in range(len(arr)):
            prefix[i+1] = prefix[i] + arr[i]

        l = 2
        r = 4

        print(prefix[r] - prefix[l-1])
        ```

    - 실행 결과

        ```
        9
        ```

- Kadane Algorithm

  - 개념
    - 배열에서 **연속된 부분 배열의 최대 합**을 찾는 알고리즘

  - 대표 문제

      ```
      Maximum Subarray
      ```

  - 핵심 아이디어

      ```
      현재까지의 합이 음수가 되면 버린다
      ```

  - 예시

      ```
      arr = [-2,1,-3,4,-1,2,1,-5,4]
      ```

  - 예시 코드

      ```python
      arr = [-2,1,-3,4,-1,2,1,-5,4]

      current = arr[0]
      best = arr[0]

      for i in range(1,len(arr)):

          current = max(arr[i], current + arr[i])
          best = max(best, current)

      print(best)
      ```

  - 실행 결과

      ```
      6
      ```

  - 설명

      ```
      최대 부분 배열
      [4,-1,2,1]
      ```

  - 시간 복잡도

      ```
      O(N)
      ```

- Monotonic Stack

  - 개념
    - 스택을 이용해 **값이 단조 증가 또는 감소하도록 유지하는 방법**

  - 대표 문제

      ```
      Next Greater Element
      Stock Span
      ```

  - 핵심 아이디어

      ```
      현재 값보다 작은 값들을 스택에서 제거
      ```

  - 예시 문제
    - 다음 큰 수 찾기

  - 예시 코드

      ```python
      arr = [2,1,2,4,3]

      stack = []
      result = [-1]*len(arr)

      for i in range(len(arr)):

          while stack and arr[stack[-1]] < arr[i]:

              idx = stack.pop()
              result[idx] = arr[i]

          stack.append(i)

      print(result)
      ```

  - 실행 결과

      ```
      [4,2,4,-1,-1]
      ```

  - 시간 복잡도

      ```
      O(N)
      ```
- Interval Algorithms
  
  - Interval Merge

    - 개념
      - 겹치는 구간(interval)을 하나로 합치는 알고리즘

    - 대표 문제

        ```
        Merge Intervals
        Meeting Rooms
        ```

    - 핵심 아이디어

        ```
        구간을 시작점 기준으로 정렬
        ```

    - 예시

        ```
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        ```

    - 예시 코드

        ```python
        intervals = [[1,3],[2,6],[8,10],[15,18]]

        intervals.sort()

        merged = [intervals[0]]

        for start,end in intervals[1:]:

            last_end = merged[-1][1]

            if start <= last_end:

                merged[-1][1] = max(last_end,end)

            else:

                merged.append([start,end])

        print(merged)
        ```

    - 실행 결과

        ```
        [[1,6],[8,10],[15,18]]
        ```

    - 시간 복잡도

        ```
        O(N log N)
        ```
  - Sweep Line

    - 개념
      - 시간이나 좌표 축을 따라 **이벤트를 순서대로 처리하는 알고리즘**

    - 대표 문제

        ```
        Meeting Rooms
        구간 겹침
        선분 교차
        ```

    - 핵심 아이디어

        ```
        시작 / 끝 이벤트 정렬
        ```

    - 예시 코드
  
        ```python
        intervals = [(1,4),(2,5),(7,9)]
  
        events = []
  
        for s,e in intervals:
  
            events.append((s,1))
            events.append((e,-1))
  
        events.sort()
  
        count = 0
        max_count = 0
  
        for time,val in events:
  
            count += val
            max_count = max(max_count,count)
  
        print(max_count)
        ```

    - 실행 결과

        ```
        2
        ```
  - Meeting Rooms

    - 개념
      - 여러 회의 일정이 있을 때 필요한 최소 회의실 수를 구하는 문제

    - 핵심 아이디어

        ```
        시작 시간 정렬
        끝나는 시간 비교
        ```

    - 예시 코드

        ```python
        import heapq

        meetings = [(0,30),(5,10),(15,20)]

        meetings.sort()

        heap = []

        for start,end in meetings:

            if heap and heap[0] <= start:
                heapq.heappop(heap)

            heapq.heappush(heap,end)

        print(len(heap))
        ```

    - 실행 결과

        ```
        2
        ```

## 정렬 알고리즘

  - 정렬이란
    - 데이터를 특정 기준에 따라 순서대로 나열하는 과정
  - 정렬이 중요한 이유

    - 많은 알고리즘 문제에서 정렬이 전처리 역할을 한다

    - 예시

        ```
        Two Pointer
        Binary Search
        Greedy
        ```

    - 예를 들어 두 수의 합 문제를 생각해보자

        ```
        배열이 정렬되어 있지 않다면

        O(N²)
        ```

        하지만 정렬을 먼저 하면

        ```
        O(N log N) + O(N)
        ```

        으로 줄일 수 있다

    - 그래서 실제 코딩테스트에서는

        ```
        문제 → 정렬 → 알고리즘 적용
        ```

        이런 패턴이 매우 자주 등장한다
  - 대표 정렬

      ```
      Bubble Sort
      Selection Sort
      Insertion Sort
      Merge Sort
      Quick Sort
      Counting Sort
      ```
  - Stable Sort (안정 정렬)

    - 개념
      - 같은 값을 가진 데이터의 **기존 순서를 유지하는 정렬**

    - 예시

        ```
        (점수, 이름)

        (90, A)
        (80, B)
        (90, C)
        ```

        점수 기준으로 정렬하면

        ```
        (80, B)
        (90, A)
        (90, C)
        ```

        A와 C의 순서가 유지된다

    - Stable Sort 예시

        ```
        Merge Sort
        Counting Sort
        Python sort()
        ```

    - Stable Sort가 아닌 정렬

        ```
        Selection Sort
        Quick Sort (기본 구현)
        ```
  - Bubble Sort
    - 개념
      - 인접한 두 값을 비교하면서 큰 값을 뒤로 보내는 방식

    - 시간 복잡도

        ```
        O(N²)
        ```

    - 예시 코드

        ```python
        arr = [5,2,9,1,7]

        n = len(arr)

        for i in range(n):
            for j in range(n-1-i):

                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]

        print(arr)
        ```

      - 실행 결과

          ```
          [1,2,5,7,9]
          ```

  - Selection Sort
    - 개념
      - 가장 작은 값을 찾아 앞에 배치하는 방식

    - 시간 복잡도

        ```
        O(N²)
        ```

    - 예시 코드

        ```python
        arr = [5,2,9,1,7]

        n = len(arr)

        for i in range(n):

            min_idx = i

            for j in range(i+1,n):

                if arr[j] < arr[min_idx]:
                    min_idx = j

            arr[i],arr[min_idx] = arr[min_idx],arr[i]

        print(arr)
        ```

      - 실행 결과

          ```
          [1,2,5,7,9]
          ```

  - Insertion Sort
    - 개념
      - 정렬된 부분에 새로운 값을 삽입하는 방식

    - 시간 복잡도

        ```
        평균 O(N²)
        최선 O(N)
        ```

    - 예시 코드

        ```python
        arr = [5,2,9,1,7]

        for i in range(1,len(arr)):

            key = arr[i]
            j = i-1

            while j >= 0 and arr[j] > key:

                arr[j+1] = arr[j]
                j -= 1

            arr[j+1] = key

        print(arr)
        ```

      - 실행 결과

          ```
          [1,2,5,7,9]
          ```
  - Counting Sort

    - 개념
      - 값의 등장 횟수를 세어 정렬하는 방법

    - 특징

        ```
        시간 복잡도 O(N + K)

        K = 값의 범위
        ```

    - 예시

        ```
        arr = [3,1,2,3,2]
        ```

        등장 횟수

        ```
        1 → 1
        2 → 2
        3 → 2
        ```

    - 예시 코드

        ```python
        arr = [3,1,2,3,2]

        max_val = max(arr)

        count = [0]*(max_val+1)

        for x in arr:
            count[x] += 1

        result = []

        for i in range(len(count)):

            for _ in range(count[i]):
                result.append(i)

        print(result)
        ```

    - 실행 결과

        ```
        [1,2,2,3,3]
        ```
  - DAT (Direct Address Table)

    - 개념
      - 값을 배열의 인덱스로 사용하는 방법

    - 아이디어

        ```
        값 = 주소
        ```

    - 예시

        ```python
        arr = [3,1,2,3,2]

        dat = [0]*10

        for x in arr:
            dat[x] = 1

        for i in range(len(dat)):
            if dat[i]:
                print(i)
        ```

    - 실행 결과

        ```
        1
        2
        3
        ```

## 그래프 알고리즘

- Graph
  - 개념
    - 정점(Vertex)과 간선(Edge)으로 이루어진 자료구조
    - 정점은 데이터 하나를 의미한다
    - 간선은 정점 간 연결 관계를 의미한다
  - 그래프 종류

    - 무방향 그래프 (Undirected Graph)
      - 간선에 방향이 없는 그래프
      - 두 정점이 서로 연결되어 있으면 양쪽 모두 이동할 수 있다

        ```
        A --- B
        ```

      - 예시
        - 친구 관계
        - 양방향 도로

    - 방향 그래프 (Directed Graph)
      - 간선에 방향이 있는 그래프
      - 한쪽 방향으로만 이동할 수 있다

        ```
        A → B
        ```

      - 예시
        - 선수 과목 관계
        - 작업 순서
        - 단방향 도로

    - 가중치 그래프 (Weighted Graph)
      - 간선마다 비용, 거리, 시간 같은 값이 붙어 있는 그래프

        ```
        A --3-- B
        A --5-- C
        ```

      - 예시
        - 지도에서의 거리
        - 네트워크 전송 비용
        - 이동 시간
  - 특징

      ```
      사이클이 존재할 수 있다
      연결이 끊어질 수 있다
      방향 그래프 / 무방향 그래프 존재
      ```

- 그래프 표현

  - 인접 행렬 (Adjacency Matrix)
    - 개념
      - 2차원 배열로 연결 여부 표현

    - 예시 코드

        ```python
        graph = [
            [0,1,1,0],
            [1,0,1,1],
            [1,1,0,0],
            [0,1,0,0]
        ]

        print(graph[0][1])
        ```

    - 실행 결과

        ```
        1
        ```

  - 인접 리스트 (Adjacency List)
    - 개념
      - 각 정점에서 연결된 정점만 저장

    - 예시 코드

        ```python
        graph = [
            [],
            [2,3],
            [1,4],
            [1],
            [2]
        ]

        print(graph[1])
        ```

    - 실행 결과

        ```
        [2, 3]
        ```

- Union Find (Disjoint Set)

  - 개념
    - 서로소 집합을 관리하는 자료구조
    - 두 노드가 같은 집합인지 빠르게 확인할 수 있다

  - 핵심 연산

      ```
      find
      union
      ```

  - 예시 코드

      ```python
      parent = [i for i in range(6)]

      def find(x):

          if parent[x] != x:
              parent[x] = find(parent[x])

          return parent[x]

      def union(a,b):

          rootA = find(a)
          rootB = find(b)

          if rootA != rootB:
              parent[rootB] = rootA

      union(1,2)
      union(2,3)

      print(find(1))
      print(find(3))
      ```

    - 실행 결과

        ```
        1
        1
        ```

  - 최적화
    - Path Compression

      - 개념
        - find 연산을 수행할 때 **루트까지 올라가는 경로를 한 번에 압축하는 기법**
        - 이후 같은 노드를 다시 찾을 때 매우 빠르게 동작한다

      - 아이디어

          ```
          find 수행 중

          parent[x] = find(parent[x])
          ```

        이렇게 하면 **경로에 있는 모든 노드가 바로 루트를 가리키게 된다**

      - 예시 코드

          ```python
          parent = [i for i in range(6)]

          def find(x):

              if parent[x] != x:
                  parent[x] = find(parent[x])

              return parent[x]
          ```

      - 효과

          ```
          트리 높이를 줄인다
          find 연산 속도 개선
          ```

    - Union by Rank

      - 개념
        - 트리의 높이를 최소화하기 위해 **높이가 작은 트리를 큰 트리 아래에 붙이는 방법**

      - 아이디어

          ```
          rank 배열 사용
          ```

      - 예시 코드

          ```python
          parent = [i for i in range(6)]
          rank = [0]*6

          def find(x):

              if parent[x] != x:
                  parent[x] = find(parent[x])

              return parent[x]


          def union(a,b):

              rootA = find(a)
              rootB = find(b)

              if rootA == rootB:
                  return

              if rank[rootA] < rank[rootB]:
                  parent[rootA] = rootB

              elif rank[rootA] > rank[rootB]:
                  parent[rootB] = rootA

              else:
                  parent[rootB] = rootA
                  rank[rootA] += 1
          ```

      - 효과

          ```
          트리 높이를 최소화
          union 연산 효율 개선
          ```
            
  - Cycle Detection (Union Find)

    - 개념
      - 간선을 추가할 때 **두 정점이 이미 같은 집합이면 사이클**

    - 핵심 아이디어

        ```
        find(u) == find(v)
        ```

    - 예시 코드

        ```python
        edges = [
            (1,2),
            (2,3),
            (3,1)
        ]

        parent = [0,1,2,3]

        def find(x):

            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(a,b):

            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return True

            parent[rootB] = rootA
            return False

        for u,v in edges:

            if union(u,v):
                print("cycle detected")
                break
        ```
          
- MST (Minimum Spanning Tree)

  - 개념
    - 모든 정점을 연결하면서
    - 사이클이 없고
    - 간선 가중치 합이 최소인 트리

  - 특징

      ```
      간선 수 = 정점 수 - 1
      사이클 없음
      ```

  - 대표 알고리즘

      ```
      Kruskal
      Prim
      ```

  - Kruskal Algorithm
    - 개념
      - 간선을 가중치 기준으로 정렬
      - 사이클이 생기지 않는 간선만 선택

    - 예시 코드

        ```python
        edges = [
            (0,1,1),
            (2,3,2),
            (1,2,3),
            (1,3,4)
        ]

        parent = [0,1,2,3]

        def find(x):

            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(a,b):

            rootA = find(a)
            rootB = find(b)

            if rootA != rootB:
                parent[rootB] = rootA

        edges.sort(key=lambda x:x[2])

        total = 0

        for u,v,w in edges:

            if find(u) != find(v):

                union(u,v)
                total += w

        print(total)
        ```

    - 실행 결과

        ```
        6
        ```

  - Prim Algorithm
    - 개념
      - 하나의 정점에서 시작하여
      - 가장 작은 간선을 선택하면서 트리를 확장

    - 특징

        ```
        Priority Queue 사용
        ```

    - 예시 코드

        ```python
        import heapq

        graph = {
            0:[(1,1),(2,3)],
            1:[(0,1),(2,1),(3,4)],
            2:[(0,3),(1,1),(3,1)],
            3:[(1,4),(2,1)]
        }

        visited = set()
        pq = [(0,0)]

        total = 0

        while pq:

            cost,node = heapq.heappop(pq)

            if node in visited:
                continue

            visited.add(node)
            total += cost

            for nxt,w in graph[node]:
                if nxt not in visited:
                    heapq.heappush(pq,(w,nxt))

        print(total)
        ```

    - 실행 결과

        ```
        3
        ```

- Shortest Path

  - 개념
    - 시작 정점에서 다른 정점까지 최소 거리

  - 대표 알고리즘

      ```
      Dijkstra
      ```

  - Dijkstra Algorithm

    - 특징

        ```
        음수 간선 불가
        Priority Queue 사용
        ```

    - 예시 코드

        ```python
        import heapq

        graph = {
            1:[(2,2),(3,5)],
            2:[(3,1),(4,2)],
            3:[(4,3)],
            4:[]
        }

        dist = {v:float('inf') for v in graph}
        dist[1] = 0

        pq = [(0,1)]

        while pq:

            d,v = heapq.heappop(pq)

            for nxt,w in graph[v]:

                nd = d + w

                if nd < dist[nxt]:

                    dist[nxt] = nd
                    heapq.heappush(pq,(nd,nxt))

        print(dist)
        ```

    - 실행 결과

        ```
        {1:0, 2:2, 3:3, 4:4}
        ```

  - 0-1 BFS

    - 개념
      - 간선 가중치가 **0 또는 1**일 때 사용하는 최단 거리 알고리즘
      - Priority Queue 대신 **Deque**를 사용한다

    - 특징

        ```
        가중치 0 → 앞에 삽입
        가중치 1 → 뒤에 삽입
        ```

    - 시간 복잡도

        ```
        O(V + E)
        ```

    - 예시 코드

        ```python
        from collections import deque

        graph = {
            0: [(1,0),(2,1)],
            1: [(3,1)],
            2: [(3,0)],
            3: []
        }

        INF = float('inf')
        dist = [INF]*4
        dist[0] = 0

        dq = deque([0])

        while dq:

            v = dq.popleft()

            for nxt,w in graph[v]:

                nd = dist[v] + w

                if nd < dist[nxt]:

                    dist[nxt] = nd

                    if w == 0:
                        dq.appendleft(nxt)
                    else:
                        dq.append(nxt)

        print(dist)
        ```

    - 실행 결과

        ```
        [0,0,1,1]
        ```

  - Bellman-Ford Algorithm

    - 개념
      - 음수 간선이 있어도 사용할 수 있는 최단 경로 알고리즘

    - 특징

        ```
        음수 간선 허용
        음수 사이클 탐지 가능
        ```

    - 시간 복잡도

        ```
        O(V × E)
        ```

    - 예시 코드

        ```python
        edges = [
            (1,2,4),
            (1,3,5),
            (2,3,-3)
        ]

        n = 3
        INF = float('inf')

        dist = [INF]*(n+1)
        dist[1] = 0

        for _ in range(n-1):

            for u,v,w in edges:

                if dist[u] != INF and dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w

        print(dist)
        ```

    - 실행 결과

        ```
        [inf,0,4,1]
        ```

  - Floyd-Warshall Algorithm

    - 개념
      - 모든 정점 쌍 사이의 최단 경로를 구하는 알고리즘

    - 특징

        ```
        모든 정점 → 모든 정점
        DP 기반
        ```

    - 시간 복잡도

        ```
        O(N³)
        ```

    - 예시 코드

        ```python
        INF = float('inf')

        graph = [
            [0,3,INF],
            [INF,0,1],
            [INF,INF,0]
        ]

        n = 3

        for k in range(n):
            for i in range(n):
                for j in range(n):

                    graph[i][j] = min(
                        graph[i][j],
                        graph[i][k] + graph[k][j]
                    )

        for row in graph:
            print(row)
        ```

    - 실행 결과

        ```
        [0,3,4]
        [inf,0,1]
        [inf,inf,0]
        ```

- DAG (Directed Acyclic Graph)

  - 개념
    - 방향 그래프
    - 사이클이 없는 그래프

  - 사용 예

      ```
      작업 순서
      선수 과목
      빌드 시스템
      ```

  - Topological Sort

    - 개념
      - DAG에서 가능한 정점 순서를 찾는 알고리즘

    - 핵심 아이디어

        ```
        진입차수 0 노드부터 처리
        ```

    - 예시 코드

        ```python
        from collections import deque

        graph = [
            [],
            [2,3],
            [4],
            [4],
            []
        ]

        indegree = [0]*5

        for i in range(1,5):
            for v in graph[i]:
                indegree[v]+=1

        q = deque()

        for i in range(1,5):
            if indegree[i]==0:
                q.append(i)

        while q:

            now = q.popleft()
            print(now,end=" ")

            for nxt in graph[now]:

                indegree[nxt]-=1

                if indegree[nxt]==0:
                    q.append(nxt)
        ```

    - 실행 결과

        ```
        1 2 3 4
        ```

  - Tarjan SCC

    - 개념
      - 그래프에서 **Strongly Connected Component**를 찾는 알고리즘
      - 하나의 SCC는 **서로 왕복 가능한 정점들의 집합**이다

    - 특징

        ```
        DFS 기반
        스택 사용
        O(V + E)
        ```

    - 예시 코드

        ```python
        graph = {
            0:[1],
            1:[2],
            2:[0,3],
            3:[4],
            4:[]
        }

        stack = []
        on_stack = set()

        ids = {}
        low = {}

        id_counter = 0
        sccs = []

        def dfs(v):

            global id_counter

            ids[v] = id_counter
            low[v] = id_counter
            id_counter += 1

            stack.append(v)
            on_stack.add(v)

            for nxt in graph[v]:

                if nxt not in ids:
                    dfs(nxt)
                    low[v] = min(low[v], low[nxt])

                elif nxt in on_stack:
                    low[v] = min(low[v], ids[nxt])

            if ids[v] == low[v]:

                scc = []

                while True:

                    node = stack.pop()
                    on_stack.remove(node)

                    scc.append(node)

                    if node == v:
                        break

                sccs.append(scc)


        for v in graph:

            if v not in ids:
                dfs(v)

        print(sccs)
        ```

    - 실행 결과

      ```
      [[4],[3],[0,2,1]]
      ```
          
  - Kosaraju SCC

    - 개념
      - 그래프에서 Strongly Connected Component를 찾는 알고리즘
      - **DFS를 두 번 수행**한다

    - 알고리즘 과정

        ```
        1️⃣ DFS로 종료 순서 기록
        2️⃣ 그래프 방향 뒤집기
        3️⃣ 종료 순서 역순 DFS
        ```

    - 시간 복잡도

        ```
        O(V + E)
        ```

    - 예시 코드

        ```python
        graph = {
            0:[1],
            1:[2],
            2:[0,3],
            3:[4],
            4:[]
        }

        visited = set()
        order = []

        def dfs(v):

            visited.add(v)

            for nxt in graph[v]:

                if nxt not in visited:
                    dfs(nxt)

            order.append(v)


        for v in graph:

            if v not in visited:
                dfs(v)

        rev = {v:[] for v in graph}

        for u in graph:
            for v in graph[u]:
                rev[v].append(u)

        visited.clear()

        def dfs2(v, comp):

            visited.add(v)
            comp.append(v)

            for nxt in rev[v]:

                if nxt not in visited:
                    dfs2(nxt, comp)


        sccs = []

        for v in reversed(order):

            if v not in visited:

                comp = []
                dfs2(v, comp)
                sccs.append(comp)

        print(sccs)
        ```

## 알고리즘 기법

- Greedy Algorithm
  - 개념
    - 매 순간 가장 좋아 보이는 선택을 하는 알고리즘 기법

  - 특징

      ```
      현재 선택이 전체 최적해로 이어져야 한다
      구현이 간단하다
      매우 빠르다
      ```

  - 대표 문제

      ```
      거스름돈 문제
      회의실 배정
      MST
      ```

  - 예시 : 거스름돈 문제
    - 문제
      - 가장 적은 동전으로 금액을 만드는 문제

    - 예시 코드

        ```python
        coins = [500,100,50,10]
        money = 1260

        count = 0

        for coin in coins:

            count += money // coin
            money %= coin

        print(count)
        ```

    - 실행 결과

        ```
        6
        ```

- Backtracking
  - 개념
    - 가능한 모든 경우를 탐색하다가
    - 조건에 맞지 않으면 되돌아가는 탐색 방법

  - 특징

      ```
      DFS 기반
      가지치기(pruning)
      ```

  - 대표 문제

      ```
      N-Queen
      부분집합
      순열
      ```

  - 예시 : 부분집합 탐색
    - 예시 코드

        ```python
        arr = [1,2,3]

        def backtrack(idx, path):

            if idx == len(arr):
                print(path)
                return

            backtrack(idx+1, path + [arr[idx]])
            backtrack(idx+1, path)

        backtrack(0, [])
        ```

    - 실행 결과

        ```
        [1, 2, 3]
        [1, 2]
        [1, 3]
        [1]
        [2, 3]
        [2]
        [3]
        []
        ```

- Divide and Conquer
  - 개념
    - 문제를 작은 문제로 나누고 해결한 뒤 다시 합치는 방식

  - 구조

      ```
      Divide
      Conquer
      Combine
      ```

  - 대표 알고리즘

      ```
      Merge Sort
      Quick Sort
      Binary Search
      ```

  - 예시 : 이진 탐색
    - 예시 코드

        ```python
        def binary_search(arr, target):

            left = 0
            right = len(arr)-1

            while left <= right:

                mid = (left + right)//2

                if arr[mid] == target:
                    return mid

                elif arr[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return -1


        arr = [1,3,5,7,9]

        print(binary_search(arr,7))
        ```

    - 실행 결과

        ```
        3
        ```

- Dynamic Programming
  - 개념
    - 큰 문제를 작은 문제로 나누고
    - 이미 계산한 결과를 저장하여 재사용하는 방법

  - 특징

      ```
      Overlapping Subproblem
      Optimal Substructure
      ```

  - 대표 문제

      ```
      피보나치
      배낭 문제
      LIS
      ```

  - 예시 : 피보나치
    - 예시 코드

        ```python
        memo = {}

        def fib(n):

            if n in memo:
                return memo[n]

            if n <= 1:
                return n

            memo[n] = fib(n-1) + fib(n-2)

            return memo[n]


        print(fib(10))
        ```

    - 실행 결과

        ```
        55
        ```
  - Knapsack Problem

    - 개념
      - 제한된 무게 안에서 최대 가치를 얻는 문제

    - 예시

        ```
        weight = [2,1,3]
        value  = [4,2,3]
        capacity = 4
        ```

    - 핵심 아이디어

        ```
        DP[i][w]

        i번째 물건까지 고려
        w 무게에서 최대 가치
        ```

    - 예시 코드

        ```python
        weight = [2,1,3]
        value = [4,2,3]

        capacity = 4
        n = len(weight)

        dp = [[0]*(capacity+1) for _ in range(n+1)]

        for i in range(1,n+1):

            for w in range(capacity+1):

                dp[i][w] = dp[i-1][w]

                if w >= weight[i-1]:

                    dp[i][w] = max(
                        dp[i][w],
                        dp[i-1][w-weight[i-1]] + value[i-1]
                    )

        print(dp[n][capacity])
        ```

    - 실행 결과

        ```
        6
        ```

  - LIS (Longest Increasing Subsequence)

    - 개념
      - 가장 긴 증가 부분 수열을 찾는 문제

    - 예시

        ```
        arr = [10,9,2,5,3,7,101,18]
        ```

    - 예시 코드

        ```python
        arr = [10,9,2,5,3,7,101,18]

        n = len(arr)

        dp = [1]*n

        for i in range(n):

            for j in range(i):

                if arr[j] < arr[i]:

                    dp[i] = max(dp[i], dp[j]+1)

        print(max(dp))
        ```

    - 실행 결과

        ```
        4
        ```

    - 시간 복잡도

        ```
        O(N²)
        ```

- Bit Manipulation
  - 개념
    - 비트 단위 연산을 이용하는 알고리즘 기법
    - 정수를 2진수로 생각하고 연산한다
  - 비트 기본 개념

    - 컴퓨터는 모든 데이터를 2진수로 표현한다

        ```
        5  = 101
        10 = 1010
        ```

    - 각 자리의 값을 **비트(bit)** 라고 한다

        ```
        101

        1 → 2^2
        0 → 2^1
        1 → 2^0
        ```

    - 비트 연산은 이 2진수 단위로 계산한다

  - 비트 연산자

      ```
      AND  &
      OR   |
      XOR  ^
      NOT  ~
      SHIFT LEFT  <<
      SHIFT RIGHT >>
      ```

    - AND

        ```
        1 & 1 = 1
        1 & 0 = 0
        ```

    - OR

        ```
        1 | 0 = 1
        0 | 0 = 0
        ```

    - XOR

        ```
        1 ^ 1 = 0
        1 ^ 0 = 1
        ```

  - 자주 사용하는 비트 연산 패턴

    - i번째 비트 확인

        ```python
        mask & (1 << i)
        ```

    - i번째 비트 켜기

        ```python
        mask | (1 << i)
        ```

    - i번째 비트 끄기

        ```python
        mask & ~(1 << i)
        ```

    - i번째 비트 토글

        ```python
        mask ^ (1 << i)
        ```

  - 비트마스크 예시

      ```
      mask = 5
      ```

    - 이 값을 2진수로 보면

        ```
        5 = 101
        ```

    - 의미

        ```
        첫 번째 원소 선택
        두 번째 원소 선택 안함
        세 번째 원소 선택
        ```

    - 예시 코드

        ```python
        mask = 5

        for i in range(3):

            if mask & (1<<i):
                print(i, "선택")
        ```

  - 비트 연산 예시
    - 예시 코드

        ```python
        a = 5
        b = 3

        print(a & b)
        print(a | b)
        print(a ^ b)
        ```

    - 실행 결과

        ```
        1
        7
        6
        ```

  - 비트마스크 활용 : 부분집합
    - 예시 코드

        ```python
        arr = [1,2,3]
        n = len(arr)

        for mask in range(1<<n):

            subset = []

            for i in range(n):

                if mask & (1<<i):
                    subset.append(arr[i])

            print(subset)
        ```

    - 실행 결과

        ```
        []
        [1]
        [2]
        [1, 2]
        [3]
        [1, 3]
        [2, 3]
        [1, 2, 3]
        ```

  - Bitmask DP

    - 개념
      - 상태를 비트마스크로 표현하는 동적 계획법

    - 대표 문제

        ```
        Traveling Salesman Problem
        방문 상태 관리
        ```

    - 핵심 아이디어

        ```
        dp[mask][i]

        mask 상태에서
        i 위치
        ```

    - 예시 코드

        ```python
        n = 3

        dp = [[False]*(n+1) for _ in range(1<<n)]

        dp[1][1] = True

        for mask in range(1<<n):

            for i in range(n):

                if mask & (1<<i):

                    for j in range(n):

                        if not (mask & (1<<j)):

                            dp[mask | (1<<j)][j] = True

        print(dp)
        ```
          
## 자료구조 기반 알고리즘

- Priority Queue (우선순위 큐)
  - 개념
    - 일반적인 Queue는 FIFO(First In First Out) 구조이다
    - Priority Queue는 우선순위가 높은 데이터가 먼저 나오는 자료구조이다

  - 특징

      ```
      삽입      O(log N)
      삭제      O(log N)
      최소값    O(1)
      ```

  - 파이썬 구현
    - `heapq` 모듈 사용
    - 기본적으로 Min Heap 구조

  - 예시
    - 예시 코드

        ```python
        import heapq

        pq = []

        heapq.heappush(pq, 3)
        heapq.heappush(pq, 1)
        heapq.heappush(pq, 5)
        heapq.heappush(pq, 2)

        while pq:
            print(heapq.heappop(pq))
        ```

    - 실행 결과

        ```
        1
        2
        3
        5
        ```
  - Top K Elements

    - 개념
      - 데이터 중 **상위 K개 요소**를 찾는 문제
      - Priority Queue(Heap)을 이용하면 효율적으로 해결할 수 있다

    - 대표 문제

        ```
        Top K Frequent Elements
        K번째 큰 수
        ```

    - 핵심 아이디어

        ```
        Min Heap 유지
        크기가 K를 넘으면 제거
        ```

    - 예시 코드

        ```python
        import heapq

        arr = [5,1,9,3,7,8]
        k = 3

        heap = []

        for num in arr:

            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        print(heap)
        ```

    - 실행 결과

        ```
        [7,8,9]
        ```

    - 시간 복잡도

        ```
        O(N log K)
        ```

- Segment Tree

  - 개념
    - 배열의 구간 정보를 트리 구조로 저장하는 자료구조
    - 구간 합, 구간 최소값, 구간 최대값 문제에 사용된다

  - 특징

      ```
      구간 질의   O(log N)
      업데이트   O(log N)
      ```

  - 예시 배열

      ```
      arr = [1,3,5,7,9,11]
      ```

  - Segment Tree 생성
    - 예시 코드

        ```python
        arr = [1,3,5,7,9,11]
        n = len(arr)

        tree = [0]*(4*n)

        def build(node,start,end):

            if start == end:
                tree[node] = arr[start]
                return

            mid = (start+end)//2

            build(node*2,start,mid)
            build(node*2+1,mid+1,end)

            tree[node] = tree[node*2] + tree[node*2+1]


        build(1,0,n-1)

        print(tree[:15])
        ```

    - 실행 결과

        ```
        [0,36,9,27,4,5,16,11,1,3,5,7]
        ```

  - 구간 합 계산
    - 예시 코드

        ```python
        def query(node,start,end,left,right):

            if right < start or end < left:
                return 0

            if left <= start and end <= right:
                return tree[node]

            mid = (start+end)//2

            return query(node*2,start,mid,left,right) + \
                   query(node*2+1,mid+1,end,left,right)


        print(query(1,0,n-1,1,3))
        ```

    - 실행 결과

        ```
        15
        ```
  - Sparse Table

    - 개념
      - **정적 배열에서 구간 최소값 / 최대값을 빠르게 구하는 자료구조**

    - 특징

        ```
        전처리 O(N log N)
        쿼리 O(1)
        ```

    - 대표 문제

        ```
        Range Minimum Query
        ```

    - 예시 코드

        ```python
        import math

        arr = [4,6,1,5,7,3]
        n = len(arr)

        k = int(math.log2(n)) + 1

        st = [[0]*n for _ in range(k)]

        for i in range(n):
            st[0][i] = arr[i]

        j = 1

        while (1<<j) <= n:

            for i in range(n-(1<<j)+1):

                st[j][i] = min(
                    st[j-1][i],
                    st[j-1][i + (1<<(j-1))]
                )

            j += 1

        print(st)
        ```

- Fenwick Tree (Binary Indexed Tree)

  - 개념
    - 구간 합을 효율적으로 계산하기 위한 자료구조
    - Segment Tree보다 구현이 단순하다

  - 특징

      ```
      업데이트   O(log N)
      prefix sum O(log N)
      ```

  - Fenwick Tree 생성
    - 예시 코드

        ```python
        n = 5
        tree = [0]*(n+1)

        def update(i,val):

            while i <= n:

                tree[i] += val
                i += i & -i


        def prefix_sum(i):

            s = 0

            while i > 0:

                s += tree[i]
                i -= i & -i

            return s


        arr = [1,2,3,4,5]

        for i,v in enumerate(arr,1):
            update(i,v)

        print(prefix_sum(3))
        ```

    - 실행 결과

        ```
        6
        ```

  - 구간 합 계산
    - 예시 코드

        ```python
        def range_sum(l,r):

            return prefix_sum(r) - prefix_sum(l-1)


        print(range_sum(2,4))
        ```

    - 실행 결과

        ```
        9
        ```

- Trie

  - 개념
    - 문자열을 효율적으로 저장하고 검색하기 위한 트리 자료구조
    - 문자열 검색 및 자동완성 문제에서 자주 사용된다

  - 특징

      ```
      문자열 길이를 L이라 하면
      삽입 O(L)
      탐색 O(L)
      ```

  - Trie 노드 정의
    - 예시 코드

        ```python
        class TrieNode:

            def __init__(self):

                self.children = {}
                self.end = False
        ```

  - Trie 삽입
    - 예시 코드

        ```python
        class Trie:

            def __init__(self):

                self.root = TrieNode()

            def insert(self,word):

                node = self.root

                for ch in word:

                    if ch not in node.children:
                        node.children[ch] = TrieNode()

                    node = node.children[ch]

                node.end = True
        ```

  - Trie 탐색
    - 예시 코드

        ```python
            def search(self,word):

                node = self.root

                for ch in word:

                    if ch not in node.children:
                        return False

                    node = node.children[ch]

                return node.end


        trie = Trie()

        trie.insert("cat")
        trie.insert("car")

        print(trie.search("cat"))
        print(trie.search("cap"))
        ```

    - 실행 결과

        ```
        True
        False
        ```

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

- WEB이란?

  - 정의
    - 인터넷을 통해 문서(페이지)를 제공하고, 사용자가 브라우저로 접근하여 보는 시스템이다.
    - “웹(Web)”은 흔히 “인터넷(Internet)”과 같이 말하지만 둘은 다르다.
      - 인터넷: 전 세계 컴퓨터가 연결된 네트워크 자체
      - 웹: 인터넷 위에서 동작하는 서비스(문서/페이지 제공 시스템)

  - 왜 웹을 배우나
    - 웹은 대부분의 서비스가 제공되는 플랫폼이다.
    - HTML/CSS/JS를 배우면 “화면(페이지)을 만들고, 꾸미고, 움직이게” 할 수 있다.


- Web Site / Web Page

  - Web Site
    - 정의
      - 여러 Web Page가 모여 하나의 사이트(서비스)를 이룬다.
    - 예시
      - 네이버(사이트) 안에는: 메인 페이지, 로그인 페이지, 검색 결과 페이지 등 여러 페이지가 존재한다.

  - Web Page
    - 정의
      - 브라우저에서 보이는 “한 화면” 단위를 의미한다.
      - 보통 하나의 HTML 문서를 중심으로 구성된다.
    - 특징
      - 페이지는 HTML(구조) + CSS(스타일) + JS(동작)로 완성된다.


- Browser(브라우저)

  - 정의
    - 웹 페이지를 받아서 해석하고, 화면에 렌더링(Rendering)하는 프로그램이다.
  - 예시
    - Chrome, Edge, Safari, Firefox
  - 브라우저가 하는 일(핵심)
    - HTML을 해석하여 구조를 만든다.
    - CSS를 적용하여 모양(색, 크기, 위치)을 결정한다.
    - Javascript를 실행하여 동작을 처리한다.


- WEB의 3대 구성 요소

  - HTML
    - 역할
      - 웹 페이지의 “구조”를 만든다.
    - 예시(무엇을 올릴지)
      - 제목(h1), 문단(p), 이미지(img), 링크(a), 목록(ul/li) 등

  - CSS
    - 역할
      - 웹 페이지의 “스타일(디자인)”을 만든다.
    - 예시(어떻게 보일지)
      - 색상(color), 크기(font-size, width), 간격(margin/padding), 배치(display) 등

  - Javascript
    - 역할
      - 웹 페이지의 “동작”을 만든다.
    - 예시(무엇을 하게 할지)
      - 버튼 클릭 처리, 입력값 검증, 애니메이션, 서버 통신 등

- WEB 동작 과정(요청/응답 흐름)

  - 핵심 개념
    - 사용자가 브라우저로 “요청(Request)”을 보내면
    - 서버가 “응답(Response)”을 반환하고
    - 브라우저가 화면을 만든다(Rendering)

  - 1 단계: 주소 입력(URL)
    - 사용자가 주소를 입력한다.

          https://example.com

    - URL은 “어디에 요청할지”를 나타낸다.

  - 2 단계: 브라우저가 서버에 요청(Request)
    - 브라우저가 서버에게 “페이지 주세요”라고 요청한다.
    - 이 요청을 HTTP Request라고 부른다.

  - 3 단계: 서버가 응답(Response)
    - 서버는 보통 HTML 문서를 응답으로 보낸다.
    - 필요하다면 CSS/JS/이미지 파일도 추가로 받게 된다.
    - 이 응답을 HTTP Response라고 부른다.

  - 4 단계: 브라우저가 화면 생성(Rendering)
    - 브라우저는 보통 다음 순서로 화면을 만든다.
      - HTML 해석 → 구조 생성
      - CSS 적용 → 모양 결정
      - Javascript 실행 → 동작 처리

  - 중요한 포인트
    - “웹은 파일을 열어보는 것”이 아니라, 대부분 “서버와 통신해서 문서를 받는 것”이다.
    - 단, 개발 초반에는 로컬의 html 파일을 브라우저로 열어도 학습이 가능하다.

- (입문 보강) Client / Server

  - Client(클라이언트)
    - 정의
      - 서비스를 요청하는 쪽
    - 예시
      - 브라우저(Chrome)가 대표적인 클라이언트이다.

  - Server(서버)
    - 정의
      - 요청을 받아서 응답을 보내주는 쪽
    - 예시
      - 웹 서버(페이지 제공), API 서버(데이터 제공) 등

  - 요약
    - Client(브라우저) → Request → Server
    - Server → Response(HTML/CSS/JS/데이터) → Client(브라우저)

- Rendering이란?

  - 정의
    - 브라우저가 HTML/CSS/JS를 바탕으로 화면을 만들어 사용자에게 보여주는 과정이다.
  - 초보자가 자주 착각하는 점
    - “HTML을 작성하면 곧바로 화면이 된다”가 아니라
    - 브라우저가 HTML을 해석하고 스타일을 계산해서 “그려주는 과정”이 필요하다.

## HTML

- HTML이란

  - 정의
    - 웹 페이지의 구조를 만드는 언어이다.
    - 웹 페이지에 어떤 요소가 있는지를 정의한다.
    - 제목, 문단, 이미지, 링크 등을 표현할 수 있다.

  - 특징
    - 프로그래밍 언어가 아니라 문서 구조 언어이다.
    - 태그(Tag)를 사용하여 문서를 구성한다.
    - 브라우저가 해석하여 화면으로 보여준다.

  - HTML과 CSS의 차이

    - HTML
      - 구조를 만든다.
      - 무엇이 있는지 정의한다.

    - CSS
      - 디자인을 만든다.
      - 어떻게 보일지 정의한다.

    - 예시

          <h1>Hello</h1>

      - HTML은 "제목이다" 라는 의미를 만든다.
      - 크기나 색상은 CSS가 담당한다.


- HyperText

  - 정의
    - 문서와 문서를 연결하는 기능이다.
    - 링크(Link)를 통해 다른 페이지로 이동할 수 있다.

  - 예시

        <a href="https://google.com">
        Google
        </a>

    - 클릭하면 다른 페이지로 이동한다.

- Markup Language

  - 정의
    - 태그(Tag)를 이용하여 문서 구조를 표현하는 언어이다.

  - 특징
    - 꺾쇠괄호 < > 를 사용한다.

          <p>Hello</p>

    - 태그를 이용해 의미를 표현한다.

  - 예시

        <h1>Title</h1>
        <p>Hello</p>

    - h1은 제목을 의미한다.
    - p는 문단을 의미한다.

- HTML 기본 구조

  - 기본 구조

        <!DOCTYPE html>
        <html>

        <head>
            <title>Page Title</title>
        </head>

        <body>

        </body>

        </html>

  - DOCTYPE

        <!DOCTYPE html>

    - HTML 문서라는 것을 브라우저에 알려준다.
    - HTML5 문서라는 것을 의미한다.
    - 표준 모드(Standard Mode)로 동작하도록 한다.
    - 없으면 브라우저가 비표준 모드로 동작할 수 있다.

  - html 태그

        <html>
        </html>

    - HTML 문서 전체를 감싸는 태그이다.
    - HTML 문서의 루트(root) 요소이다.
    - 모든 HTML 요소는 html 태그 안에 들어간다.

  - head 태그

        <head>
        </head>

    - 문서 설정 정보를 넣는 영역이다.
    - 화면에는 표시되지 않는다.

    - 예시 내용
      - title
      - CSS 연결
      - 문자 인코딩 설정

  - title 태그

        <title>Page Title</title>

    - 브라우저 탭 이름이 된다.

    - 예시

      - Chrome 탭에 표시된다.

  - body 태그

        <body>
        </body>

    - 실제 화면에 표시되는 내용을 넣는다.
    - 대부분의 HTML 코드는 body 안에 작성한다.

- HTML 태그(Tag)

  - 정의
    - 꺾쇠괄호 < > 로 이루어진 명령어이다.

  - 시작 태그

        <p>

  - 종료 태그

        </p>

  - 특징
    - 대부분 시작 태그와 종료 태그가 존재한다.

        <p>Hello</p>

  - 규칙
    - 먼저 열린 태그는 나중에 닫혀야 한다.

          <div>
              <p>Hello</p>
          </div>

    - 잘못된 예

          <div>
              <p>Hello
          </div>
          </p>

- HTML 요소(Element)

  - 정의
    - 시작 태그 + 내용 + 종료 태그 전체를 요소(Element)라고 한다.

          <p>Hello</p>

  - 구성

        <p> + Hello + </p>

  - Tag와 Element 차이

    - Tag

          <p>

    - Element

          <p>Hello</p>

    - 태그는 요소의 일부이다.

- HTML 구조 (중첩 구조)

  - 정의
    - 요소는 다른 요소 안에 들어갈 수 있다.

  - 예시

        <div>

            <p>Hello</p>

        </div>

  - 구조

        div
         └ p

    - div는 부모 요소이다.
    - p는 자식 요소이다.

  - 특징
    - HTML은 트리 구조(Tree Structure)를 가진다.

- HTML 속성(Attribute)

  - 정의
    - 태그에 추가 정보를 제공한다.

  - 구조

        name="value"

  - 위치
    - 시작 태그 안에 작성한다.

      ```html
      <a href="google.com">
      ```

  - 여러 속성 사용

        <a href="google.com" target="_blank">

  - 주요 속성

    - href

          <a href="google.com">

      - 링크 주소를 지정한다.

    - src

          <img src="image.png">

      - 이미지 파일 위치를 지정한다.

    - class

          <p class="menu">

      - CSS 적용 대상을 지정한다.
      - 여러 요소에 사용할 수 있다.

    - id

          <div id="header">

      - 특정 요소 하나를 지정한다.
      - 보통 하나만 사용한다.

- HTML 텍스트 구조

  - Heading

        <h1>Title</h1>

    - 제목을 나타낸다.
    - h1 ~ h6까지 존재한다.
    - h1이 가장 중요하다.

    - 구조 예시

          <h1>Book</h1>
          <h2>Chapter</h2>
          <h3>Section</h3>

  - Paragraph

        <p>Hello world</p>

    - 문단을 나타낸다.
    - 자동으로 줄바꿈이 된다.

    - 예시

          <p>Hello</p>
          <p>World</p>

  - Lists

        <ul>
            <li>Apple</li>
            <li>Banana</li>
        </ul>

    - 순서 없는 목록이다.

  - Ordered Lists

        <ol>
            <li>One</li>
            <li>Two</li>
        </ol>

    - 순서가 있는 목록이다.

  - li 태그

        <li>Apple</li>

    - 목록 항목을 나타낸다.
    - ul 또는 ol 안에 들어간다.

  - Emphasis

        <em>important</em>

    - 강조를 나타낸다.
    - 보통 기울임꼴로 표시된다.
    - 의미적으로 강조를 표현한다.

  - Strong

        <strong>important</strong>

    - 중요한 내용을 나타낸다.
    - 보통 굵게 표시된다.
    - 의미적으로 중요함을 나타낸다.

- div 태그

  - 정의
    - 영역을 나누는 태그이다.
    - 여러 요소를 묶는 역할을 한다.

  - 특징
    - 의미가 없는 일반적인 태그이다.
    - Layout 구성에 자주 사용된다.

  - 예시

        <div class="menu">
            <p>Home</p>
            <p>About</p>
        </div>

- span 태그

  - 정의
    - 텍스트 일부를 묶는 태그이다.

  - 특징
    - 문장 안에서 특정 부분만 선택할 때 사용한다.

  - 예시

        Price : <span>$10</span>

- Block 요소

  - 특징
    - 줄 전체를 차지한다.
    - 자동 줄바꿈이 된다.

  - 대표 요소

        div
        p
        h1
        ul

  - 예시

        <p>Hello</p>
        <p>World</p>

- Inline 요소

  - 특징
    - 줄 안에 표시된다.
    - 자동 줄바꿈이 없다.

  - 대표 요소

        span
        a
        em
        strong

  - 예시

        Hello <span>world</span>

## CSS

- CSS란

  - 정의
    - HTML 요소의 스타일을 지정하는 언어이다.
    - 웹 페이지의 디자인을 담당한다.
    - 색상, 크기, 위치 등을 지정할 수 있다.

  - 역할

    - HTML
      - 구조를 만든다.
      - 무엇이 있는지 정의한다.

    - CSS
      - 디자인을 만든다.
      - 어떻게 보일지 정의한다.

  - 예시

        <p>Hello</p>

        p {
            color:red;
        }

    - p 태그 글자가 빨간색이 된다.

- CSS 적용 방법

  - Inline 방식

        <p style="color:red;">
        Hello
        </p>

    - HTML 태그 안에 CSS를 작성하는 방식이다.
    - 특정 요소 하나에 스타일을 적용할 때 사용한다.
    - 관리가 어렵기 때문에 많이 사용하지 않는다.

  - Internal 방식

        <style>

        p {
            color:red;
        }

        </style>

    - HTML 파일 안에 CSS를 작성하는 방식이다.
    - head 태그 안에 작성한다.
    - 작은 프로젝트에서 사용한다.

  - External 방식

        <link rel="stylesheet" href="style.css">

    - CSS 파일을 따로 만들어 연결하는 방식이다.
    - 가장 많이 사용하는 방식이다.
    - 여러 HTML 파일에서 사용할 수 있다.

  - 파일 구조 예시

        index.html
        style.css

- CSS 구문(Syntax)

        p {

            color:red;

        }

  - Selector

        p

    - 스타일을 적용할 HTML 요소를 선택한다.

  - Property

        color

    - 변경할 속성을 의미한다.

  - Value

        red

    - 속성 값을 의미한다.

- CSS 선택자(Selector)

  - Tag 선택자

        p {
            color:red;
        }

    - 특정 태그 전체에 스타일을 적용한다.
    - 예시에서는 모든 p 태그 글자를 빨간색으로 만든다.
    - 가장 기본적인 선택자이다.

    - 적용 예시

          <p>A</p>
          <p>B</p>
          <p>C</p>

    - 결과
      - A B C 모두 빨간색이 된다.

  - Class 선택자

        .menu {
            color:red;
        }

    - class 속성을 가진 요소를 선택한다.
    - 가장 많이 사용하는 선택자이다.
    - 여러 요소에 적용할 수 있다.

    - HTML 예시

          <p class="menu">A</p>
          <p class="menu">B</p>

    - 결과
      - A B가 빨간색이 된다.

  - ID 선택자

        #header {
            color:red;
        }

    - id 속성을 가진 요소를 선택한다.
    - 보통 하나의 요소에만 사용한다.

    - HTML 예시

          <div id="header">
          </div>

  - Tag + Class 선택자

        p.menu {
            color:red;
        }

    - p 태그 중 class가 menu인 요소를 선택한다.

    - HTML 예시

          <p class="menu">A</p>
          <div class="menu">B</div>

    - 결과
      - A만 적용된다.

  - Attribute 선택자

        input[type="text"] {

        }

    - 특정 속성을 가진 요소를 선택한다.

    - HTML 예시

          <input type="text">
          <input type="password">

    - Attribute 값 선택

          [type="text"] {

          }

      - type이 text인 요소 선택한다.

    - 시작 선택

          [href^="https"]

      - https로 시작하는 요소 선택한다.

    - 끝 선택

          [src$=".png"]

      - png로 끝나는 요소 선택한다.

    - 포함 선택

          [class*="menu"]

      - menu를 포함하는 요소 선택한다.

- Cascade

  - 정의
    - 여러 CSS 규칙 중 어떤 스타일이 적용될지 결정하는 규칙이다.

  - 특징
    - 같은 선택자라면 아래쪽 CSS가 적용된다.

  - 예시

        p {
            color:blue;
        }

        p {
            color:red;
        }

    - 결과
      - 빨간색 적용된다.

- Specificity

  - 정의
    - 선택자 우선순위를 결정하는 규칙이다.

  - 우선순위

        Inline > ID > Class > Tag

  - 설명
    - Inline style이 가장 강하다.
    - ID 선택자가 Class보다 강하다.
    - Class 선택자가 Tag보다 강하다.

  - 예시

        p {
            color:blue;
        }

        .menu {
            color:red;
        }

    - 결과
      - 빨간색 적용된다.

  - !important

          color:red !important;

    - 우선순위를 강제로 높인다.

    - 특징
      - 다른 CSS보다 우선 적용된다.
      - 남용하면 관리가 어려워진다.

- CSS 단위(Unit)

  - px

        width:200px;

    - 고정 크기 단위이다.
    - 가장 많이 사용하는 단위이다.

  - %

        width:50%;

    - 부모 요소 기준 단위이다.

  - em

        font-size:2em;

    - 부모 font-size 기준 단위이다.
    - 중첩되면 계산이 어려워질 수 있다.

  - rem

        font-size:2rem;

    - html font-size 기준 단위이다.
    - 실무에서 많이 사용한다.

  - vw

        width:50vw;

    - 화면 너비 기준 단위이다.
    - 1vw는 화면 너비의 1%이다.

  - vh

        height:100vh;

    - 화면 높이 기준 단위이다.
    - 1vh는 화면 높이의 1%이다.

- CSS 상속과 값 제어 (Inheritance / inherit / initial / unset)

  - CSS 상속(Inheritance)이란

    - 정의
      - 부모 요소에 적용된 스타일이 자식 요소에 전달되는 현상이다.
      - HTML 요소는 부모-자식 구조를 가지므로 스타일이 전달될 수 있다.

    - 구조 예시

          <div>

              Hello
              <p>World</p>

          </div>

      - div는 부모 요소이다.
      - p는 자식 요소이다.

    - 상속 예시

          div {

              color:red;

          }

      - 결과
        - div 안의 모든 글자가 빨간색이 된다.
        - p 태그도 빨간색이 된다.

    - 특징
      - 모든 속성이 상속되는 것은 아니다.
      - 일부 속성만 상속된다.

  - 상속이 일어나는 이유

    - 목적
      - 문서 전체 스타일을 쉽게 적용하기 위해서이다.

    - 예시

          body {

              font-family:Arial;
              color:black;

          }

      - 결과
        - 페이지 전체 글자가 Arial 글꼴이 된다.
        - 대부분의 텍스트가 검은색이 된다.

    - 특징
      - 보통 body나 html에 기본 스타일을 설정한다.

  - 대표적으로 상속되는 속성

    - 특징
      - 텍스트 관련 속성은 대부분 상속된다.

    - color

          div {
              color:red;
          }

      - 자식 요소 글자도 빨간색이 된다.

    - font-size

          div {
              font-size:20px;
          }

      - 자식 요소도 20px이 된다.

    - font-family

          body {
              font-family:Arial;
          }

      - 전체 글꼴이 Arial이 된다.

    - font-weight

          div {
              font-weight:bold;
          }

      - 자식 글자도 굵어진다.

    - line-height

          div {
              line-height:2;
          }

      - 자식 요소도 적용된다.

    - text-align

          div {
              text-align:center;
          }

      - 자식 텍스트도 가운데 정렬된다.

    - visibility

          div {
              visibility:hidden;
          }

      - 자식 요소도 보이지 않는다.

    - 대표 속성 정리

          color
          font-size
          font-family
          font-weight
          line-height
          text-align
          visibility

  - 대표적으로 상속되지 않는 속성

    - 특징
      - Layout과 크기 관련 속성은 대부분 상속되지 않는다.

    - margin

          div {
              margin:20px;
          }

      - 자식 margin은 적용되지 않는다.

    - padding

          div {
              padding:20px;
          }

      - 자식 padding은 적용되지 않는다.

    - border

          div {
              border:1px solid black;
          }

      - 자식 border는 없다.

    - width

          div {
              width:200px;
          }

      - 자식 width는 자동이다.

    - height

          div {
              height:200px;
          }

      - 자식 height는 자동이다.

    - background

          div {
              background:red;
          }

      - 자식 background는 없다.
      - 부모 배경이 보일 뿐이다.

    - display

          div {
              display:flex;
          }

      - 자식 요소는 flex가 아니다.

    - position

          div {
              position:relative;
          }

      - 자식 요소는 relative가 아니다.

    - 대표 속성 정리

          margin
          padding
          border
          width
          height
          background
          display
          position

  - inherit

    - 정의
      - 부모 요소의 값을 그대로 사용한다.
      - 부모 값이 바뀌면 자식 값도 함께 바뀐다.
      - 자동 상속이 아닌 속성도 상속할 수 있다.

    - 예시 (color)

          .parent {
              color:red;
          }

          .child {
              color:inherit;
          }

      - 결과
        - child도 빨간색이 된다.

    - 예시 (border)

          .parent {
              border:1px solid black;
          }

          .child {
              border:inherit;
          }

      - 결과
        - child에도 border가 생긴다.

    - 특징
      - 부모 값을 그대로 따라간다.
      - 강제 상속을 만들 수 있다.

  - initial

    - 정의
      - 브라우저 기본값으로 되돌린다.
      - 부모 값과 관계없이 기본값을 사용한다.

    - 예시

          div {
              color:red;
          }

          p {
              color:initial;
          }

      - 결과
        - p는 기본 글자색이 된다.

    - 특징
      - 상속을 끊고 기본값으로 돌아간다.

  - unset

    - 정의
      - 상황에 따라 inherit 또는 initial처럼 동작한다.

    - 동작 규칙

          상속 속성 → inherit

          비상속 속성 → initial

    - 예시 (상속 속성)

          div {
              color:red;
          }

          p {
              color:unset;
          }

      - 결과
        - p는 빨간색이 유지된다.

    - 예시 (비상속 속성)

          div {
              margin:20px;
          }

          p {
              margin:unset;
          }

      - 결과
        - p margin은 기본값이 된다.

  - inherit vs initial vs unset 비교

        inherit → 부모값 사용

        initial → 기본값 사용

        unset → 자동 판단

  - 실무 예시

    - 링크 색상 부모와 동일하게 만들기

          a {
              color:inherit;
          }

      - 링크 색상이 부모와 같아진다.

    - 버튼 기본 스타일 제거

          button {
              all:unset;
          }

      - 모든 스타일이 제거된다.

## Layout

- Layout이란

  - 정의
    - 웹 페이지에서 요소들의 위치와 크기를 결정하는 것이다.
    - 요소를 어디에 배치할지 결정하는 작업이다.

  - 예시
    - 메뉴 영역
    - 본문 영역
    - 사이드바 영역

  - 특징
    - HTML은 구조를 만든다.
    - CSS Layout은 위치를 만든다.

- Block vs Inline

  - Block 요소

    - 특징
      - 줄 전체를 차지한다.
      - 자동으로 줄바꿈이 된다.
      - width 설정 가능하다.
      - height 설정 가능하다.
      - margin 설정 가능하다.
      - padding 설정 가능하다.

    - 대표 요소

          div
          p
          h1
          ul
          li

    - 예시

          <div>A</div>
          <div>B</div>

    - 결과

          A
          B

    - 세로로 배치된다.

  - Inline 요소

    - 특징
      - 줄 안에 표시된다.
      - 자동 줄바꿈이 없다.
      - 내용(content) 크기만큼만 공간을 차지한다.
      - width 설정이 제한된다.
      - height 설정이 제한된다.

    - 대표 요소

          span
          a
          em
          strong

    - 예시

          Hello <span>world</span>

    - 결과

          Hello world

    - 한 줄에 표시된다.

- Box Model

  - 정의
    - 모든 HTML 요소는 사각형(Box) 형태를 가진다.
    - 요소의 크기는 Box Model로 계산된다.

  - 구조

        Margin
        Border
        Padding
        Content

  - 설명

    - Content
      - 실제 내용이 들어가는 영역이다.

    - Padding
      - Content와 Border 사이의 공간이다.
      - 내부 여백이다.

    - Border
      - 요소의 테두리이다.

    - Margin
      - 요소 바깥 공간이다.
      - 다른 요소와의 거리를 만든다.

  - width

        width:200px;

    - Content 영역 크기이다.
    - 전체 크기가 아니다.

  - 예시

        div {

            width:200px;
            padding:20px;
            border:5px solid black;

        }

    - 전체 크기 계산

          200 + 20 + 20 + 5 + 5

    - 결과

          250px

  - padding

        padding:20px;

    - 내부 여백이다.

  - margin

        margin:20px;

    - 외부 여백이다.

  - border

        border:1px solid black;

    - 테두리이다.

  - box-sizing

        box-sizing:border-box;

    - width에 padding과 border를 포함한다.

    - 예시

          div {

              width:200px;
              padding:20px;
              box-sizing:border-box;

          }

    - 전체 크기가 200px로 유지된다.

- Display

  - 정의
    - 요소가 화면에 표시되는 방식을 결정하는 속성이다.
    - 요소의 배치 방법을 변경할 수 있다.
    - 태그의 기본 동작을 변경할 수 있다.

    - 예시

          div {
              display:inline;
          }

    - div를 inline처럼 사용할 수 있다.

  - block

        display:block;

    - 특징
      - 줄 전체를 차지한다.
      - 자동 줄바꿈이 된다.
      - width 설정 가능하다.
      - height 설정 가능하다.

    - 예시

          div {
              display:block;
          }

  - inline

        display:inline;

    - 특징
      - 줄 안에 표시된다.
      - 자동 줄바꿈이 없다.
      - width 설정이 제한된다.
      - height 설정이 제한된다.

    - 예시

          span {
              display:inline;
          }

  - inline-block

        display:inline-block;

    - 특징
      - 줄 안에 표시된다.
      - width 설정 가능하다.
      - height 설정 가능하다.
      - block과 inline의 특징을 함께 가진다.

    - 예시

          div {
              display:inline-block;
              width:100px;
              height:50px;
          }

    - 결과
      - 가로로 배치되면서 크기를 지정할 수 있다.

  - none

        display:none;

    - 특징
      - 요소가 화면에서 사라진다.
      - 공간도 함께 사라진다.

    - 예시

          .menu {
              display:none;
          }

- Position

  - 정의
    - 요소의 “위치 배치 방식”을 결정하는 속성이다.
    - display가 “줄 배치 방식(block/inline)”을 정한다면,
      - position은 “특정 좌표(top/left 등)로 옮길 수 있는지 / 무엇을 기준으로 옮기는지”를 정한다.
    - position은 보통 top / left / right / bottom 과 함께 사용된다.

  - position 종류
    - static
    - relative
    - absolute
    - fixed
    - sticky

  - top / left / right / bottom 기본 개념
    - 숫자를 주면 “이동”하는 게 아니라 “해당 방향에서 떨어진 거리”를 의미한다.
    - 그래서 헷갈릴 수 있다.

    - top: 20px
      - “위에서 20px 떨어져라” 라는 뜻
      - 결과적으로 아래로 내려간 것처럼 보인다.

    - left: 20px
      - “왼쪽에서 20px 떨어져라”
      - 결과적으로 오른쪽으로 이동한 것처럼 보인다.

  - position: static (기본값)

    - 특징
      - 모든 요소의 기본값이다.
      - 문서의 기본 흐름(위에서 아래, 왼쪽에서 오른쪽)에 따라 배치된다.
      - top/left/right/bottom이 적용되지 않는다.

    - 예시

          .box {
              position:static;
              top:50px;      /* 적용되지 않음 */
              left:50px;     /* 적용되지 않음 */
          }

    - 결과
      - 화면 변화가 없다.

  - position: relative

    - 정의
      - “원래 있어야 할 위치(기본 흐름에서의 위치)”를 기준으로 이동한다.

    - 특징
      - top/left/right/bottom이 적용된다.
      - 이동해도 “원래 자리(공간)”가 유지된다.
        - 겉으로는 이동하지만, 주변 요소는 원래 자리 기준으로 배치된 것처럼 남아있다.

    - 예시

          <div>A</div>
          <div class="box">B</div>
          <div>C</div>

          .box {
              position:relative;
              left:40px;
              top:10px;
          }

    - 결과
      - B가 오른쪽/아래로 이동한다.
      - 하지만 B의 원래 공간은 유지되어 A와 C의 위치는 크게 바뀌지 않는다.

    - 매우 중요한 용도(실무 핵심)
      - absolute의 기준점(부모)을 만들기 위해 사용한다.
      - 즉, “부모를 relative로 만든다”는 패턴이 매우 흔하다.

  - position: absolute (가장 중요)

    - 정의
      - “문서 흐름에서 빠져나와서” 특정 기준점에 붙어서 배치된다.

    - 특징 1 : 공간을 차지하지 않는다
      - absolute를 주면 요소가 흐름에서 빠져나간다.
      - 즉, 주변 요소는 그 요소가 없는 것처럼 배치된다.
      - 그래서 요소가 겹쳐 보일 수 있다.

    - 특징 2 : 기준점이 필요하다
      - absolute는 “가장 가까운 position이 설정된 조상 요소”를 기준으로 한다.
      - 여기서 position이 설정된 조상 요소란 보통 relative인 부모를 말한다.

    - 기준점 규칙(초보 핵심)
      - 가까운 조상 중에서 position이 static이 아닌 요소를 기준으로 한다.
      - 대부분 이렇게 만든다.

            .parent {
                position:relative;
            }

            .child {
                position:absolute;
            }

      - 만약 기준점이 없으면(조상에 position 설정이 없으면)
        - 브라우저 화면(문서 전체)을 기준으로 배치되는 것처럼 보인다.

    - 예시 1 : 부모 기준으로 배치하기 (정석)

          <div class="parent">
              <div class="child">BOX</div>
          </div>

          .parent {
              position:relative;
              width:300px;
              height:200px;
              border:1px solid black;
          }

          .child {
              position:absolute;
              top:20px;
              left:30px;
              width:80px;
              height:40px;
              border:1px solid black;
          }

    - 결과
      - child는 parent 내부의 (top:20, left:30) 위치에 배치된다.

    - 예시 2 : absolute는 공간이 사라진다 (겹침)

          <div>A</div>
          <div class="box">B</div>
          <div>C</div>

          .box {
              position:absolute;
              top:0;
              left:0;
          }

    - 결과
      - B는 문서 흐름에서 빠져나가며 A, C는 “B가 없는 것처럼” 배치된다.
      - B는 화면 좌상단 근처로 이동하며 다른 요소와 겹칠 수 있다.

    - 언제 쓰나(대표 예시)
      - 뱃지(badge) 붙이기: “NEW”, “HOT”
      - 카드 이미지 위 텍스트 올리기
      - 모달, 드롭다운 같은 떠있는 UI
      - 특정 영역의 한쪽 모서리에 요소 고정(부모 기준)

  - position: fixed

    - 정의
      - 브라우저 화면(Viewport)을 기준으로 고정된다.

    - 특징
      - 스크롤을 내려도 같은 위치에 유지된다.
      - absolute처럼 흐름에서 빠져나와 공간을 차지하지 않는다.

    - 예시

          .chat {
              position:fixed;
              right:20px;
              bottom:20px;
              width:60px;
              height:60px;
              border:1px solid black;
          }

    - 결과
      - 화면 오른쪽 아래에 고정된 버튼처럼 보인다.
      - 스크롤해도 위치가 유지된다.

    - 언제 쓰나(대표 예시)
      - “맨 위로” 버튼
      - 채팅 버튼
      - 고정 상단/하단 바(단, 요즘은 sticky도 자주 사용)

  - position: sticky

    - 정의
      - 기본은 문서 흐름에 따라 움직이지만,
      - 특정 위치(top 등)에 도달하면 그 자리에서 고정된다.

    - 필수 조건(중요)
      - 보통 top 값을 같이 써야 동작한다.

            position:sticky;
            top:0;

    - 예시

          .menu {
              position:sticky;
              top:0;
              border:1px solid black;
          }

    - 결과
      - 스크롤 전에는 일반 요소처럼 있다가,
      - 스크롤로 top:0 위치에 닿으면 상단에 붙어서 고정된다.

    - fixed와 차이
      - fixed는 항상 고정
      - sticky는 “닿을 때만” 고정

  - z-index (겹침 순서)

    - 정의
      - 요소가 겹칠 때 “누가 위에 보일지”를 결정한다.
      - position이 static이 아닌 요소(또는 특정 상황)에서 의미가 커진다.

    - 예시

          .a {
              position:absolute;
              z-index:1;
          }

          .b {
              position:absolute;
              z-index:2;
          }

    - 결과
      - z-index가 큰 요소가 위에 보인다.

    - 주의
      - z-index는 “같은 기준(같은 stacking context)”에서 비교된다.
      - 초보 단계에서는 “숫자가 크면 위”라고 이해해도 충분하다.

- Flexbox

  - 정의
    - 요소들을 가로나 세로 방향으로 정렬하는 Layout 방식이다.
    - 부모 요소(Container)에 display:flex를 적용하면 자식 요소(Item)들이 flex 방식으로 배치된다.
    - 요소 정렬(Layout)을 만들 때 가장 많이 사용하는 방법이다.

  - 기본 사용 방법

        .container {
            display:flex;
        }

    - 부모 요소가 Flex Container가 된다.
    - 자식 요소들이 Flex Item이 된다.

  - 기본 예시

        <div class="container">

            <div>A</div>
            <div>B</div>
            <div>C</div>

        </div>


        .container {
            display:flex;
        }

    - 결과
      - A B C 가 가로로 배치된다.
      - 기본 block 요소는 세로로 배치되지만 flex에서는 가로 배치된다.

  - Container와 Item

    - Container
      - display:flex가 적용된 부모 요소이다.

            .container {
                display:flex;
            }

    - Item
      - Container 안에 들어있는 자식 요소이다.

            <div class="container">

                <div>A</div>
                <div>B</div>

            </div>

    - 구조

            Container
              ├ Item
              ├ Item
              └ Item

  - Flex 축 개념 (매우 중요)

    - Main Axis
      - 아이템이 배치되는 기본 방향이다.

    - Cross Axis
      - Main Axis와 수직 방향이다.

    - 기본 상태

            display:flex;

    - 구조

            Main Axis → 가로 방향

            Cross Axis ↓ 세로 방향


    - 결과

            A B C

  - flex-direction

    - 정의
      - Main Axis 방향을 결정한다.

    - row (기본값)

            .container {
                display:flex;
                flex-direction:row;
            }

      - Main Axis = 가로
      - Cross Axis = 세로

      - 결과

            A B C

    - column

            .container {
                display:flex;
                flex-direction:column;
            }

      - Main Axis = 세로
      - Cross Axis = 가로

      - 결과

            A
            B
            C


    - 매우 중요한 특징
      - column이 되면 justify-content와 align-items 방향이 바뀐다.

  - justify-content

    - 정의
      - Main Axis 방향 정렬을 결정한다.

    - center

            justify-content:center;

      - 가운데 정렬

            A B C

    - flex-start

            justify-content:flex-start;

      - 시작 위치 정렬

    - flex-end

            justify-content:flex-end;

      - 끝 위치 정렬

    - space-between

            justify-content:space-between;

      - 양 끝 정렬 + 사이 공간 동일

            A     B     C

    - space-around

            justify-content:space-around;

      - 양쪽 공간 포함 균등 분배

  - align-items

    - 정의
      - Cross Axis 방향 정렬을 결정한다.

    - center

            align-items:center;

      - 세로 가운데 정렬

    - flex-start

            align-items:flex-start;

      - 위쪽 정렬

    - flex-end

            align-items:flex-end;

      - 아래쪽 정렬

  - justify-content vs align-items (핵심)

    - row일 때

      - justify-content
        - 가로 정렬

      - align-items
        - 세로 정렬

    - column일 때

      - justify-content
        - 세로 정렬

      - align-items
        - 가로 정렬

  - gap

    - 정의
      - Flex Item 사이 간격을 만든다.

    - 예시

            .container {

                display:flex;
                gap:20px;

            }

      - 결과

            A   B   C


    - 특징
      - Item 사이 간격만 생긴다.
      - 가장자리에는 간격이 생기지 않는다.
      - margin보다 관리가 쉽다.

  - flex-wrap

    - 정의
      - 줄바꿈 허용 여부를 결정한다.

    - nowrap (기본값)

            flex-wrap:nowrap;

      - 줄바꿈이 발생하지 않는다.

    - wrap

            flex-wrap:wrap;

      - 줄바꿈이 발생한다.

      - 결과

            A B C
            D E F


    - 대표 사용 예
      - 카드 Layout
      - 상품 목록

  - align-content

    - 정의
      - 여러 줄이 있을 때 줄 전체 정렬을 결정한다.

    - 특징
      - flex-wrap:wrap 상태에서만 동작한다.

    - 예시

            .container {

                display:flex;
                flex-wrap:wrap;
                height:300px;

                align-content:center;

            }

      - 결과
        - 여러 줄이 가운데 정렬된다.

  - flex-grow

    - 정의
      - 남는 공간을 얼마나 차지할지 결정한다.

    - 예시

            .container {
                display:flex;
                width:400px;
            }

            .a {
                flex-grow:1;
            }

            .b {
                flex-grow:1;
            }

      - 결과
        - 같은 크기로 확장된다.

    - 비율 예시

            .a {
                flex-grow:1;
            }

            .b {
                flex-grow:2;
            }

      - 결과
        - b가 a보다 2배 넓어진다.

  - flex-shrink

    - 정의
      - 공간이 부족할 때 얼마나 줄어들지 결정한다.

    - 기본값

            flex-shrink:1;

      - 줄어든다.

    - 줄어들지 않게

            flex-shrink:0;

      - 크기가 유지된다.

  - flex-basis

    - 정의
      - Flex Item의 기본 크기를 결정한다.

    - 예시

            flex-basis:200px;

      - 기본 크기가 200px이 된다.

  - flex (축약형)

    - 정의
      - flex-grow, flex-shrink, flex-basis를 한번에 설정한다.

    - 예시

            flex:1;

      - 의미

            flex-grow:1
            flex-shrink:1
            flex-basis:0

    - 대표 사용 방법

            .box {

                flex:1;

            }

      - 모든 아이템이 같은 크기가 된다.

- Grid

  - 정의
    - 행(Row)과 열(Column)을 이용해 요소를 배치하는 Layout 방식이다.
    - Flexbox와 달리 2차원 Layout을 만들 수 있다.
    - 페이지 전체 구조를 만들 때 많이 사용된다.

  - Flexbox와 Grid 차이

    - Flexbox
      - 한 방향 Layout이다.
      - 가로나 세로 중 한 방향 정렬에 사용한다.

            A B C

      - 메뉴 정렬이나 버튼 정렬에 적합하다.

    - Grid
      - 두 방향 Layout이다.
      - 행과 열을 동시에 제어할 수 있다.

            A B C
            D E F

      - 페이지 Layout에 적합하다.

  - 기본 사용 방법

        .container {

            display:grid;

        }

    - 부모 요소가 Grid Container가 된다.
    - 자식 요소가 Grid Item이 된다.

  - 기본 예시

        <div class="container">

            <div>A</div>
            <div>B</div>
            <div>C</div>

        </div>


        .container {

            display:grid;

        }


    - 결과

            A
            B
            C

    - 기본 배치는 세로 방향이다.

  - grid-template-columns

    - 정의
      - 열(Column)의 개수와 크기를 결정한다.

    - 예시

        grid-template-columns:100px 100px 100px;


    - 결과

            A B C


    - 특징
      - 값의 개수만큼 열이 생성된다.

    - 예시

        grid-template-columns:200px 100px;


    - 결과

            A B
            C D
            E F

    - 열은 2개가 된다.

  - grid-template-rows

    - 정의
      - 행(Row)의 높이를 결정한다.


    - 예시

        grid-template-rows:100px 200px;


    - 결과
      - 첫 번째 행 높이는 100px
      - 두 번째 행 높이는 200px

    - 예시

        .container {

            display:grid;

            grid-template-columns:1fr 1fr;
            grid-template-rows:100px 200px;

        }

  - fr 단위

    - 정의
      - 남은 공간을 비율로 나누는 단위이다.

    - 예시

        grid-template-columns:1fr 1fr;


    - 결과
      - 두 열이 같은 크기가 된다.

    - 예시

        grid-template-columns:1fr 2fr;


    - 결과
      - 두 번째 열이 두 배 넓어진다.

  - px와 fr 차이

    - px

        grid-template-columns:200px 200px;

      - 고정 크기이다.

    - fr

        grid-template-columns:1fr 1fr;

      - 화면 크기에 따라 변한다.

  - gap

    - 정의
      - Grid Item 사이 간격을 만든다.

    - 예시

        .container {

            display:grid;

            grid-template-columns:1fr 1fr;

            gap:20px;

        }


    - 결과

            A   B
            C   D


    - 특징
      - 요소 사이 간격만 생긴다.
      - 가장자리에는 간격이 생기지 않는다.

  - Grid 자동 배치

    - 정의
      - Grid는 자동으로 요소를 배치한다.

    - 예시

        grid-template-columns:1fr 1fr;


        A B C D E F


    - 결과

            A B
            C D
            E F

  - Grid 선(Line) 개념

    - 특징
      - Grid는 칸이 아니라 선 번호 기준으로 동작한다.


    - 예시

        grid-template-columns:1fr 1fr 1fr;


    - 구조

            1   2   3   4
            | A | B | C |


    - 열이 3개이면 선은 4개이다.

  - grid-column

    - 정의
      - 요소가 차지하는 열 범위를 지정한다.


    - 예시

        .box {

            grid-column:1 / 3;

        }


    - 결과

            A A B
            C D E


    - 설명
      - 1번 선부터 3번 선까지 사용한다.
      - 두 칸을 차지한다.

  - grid-row

    - 정의
      - 요소가 차지하는 행 범위를 지정한다.


    - 예시

        .box {

            grid-row:1 / 3;

        }


    - 결과

            A B
            A C


    - 설명
      - 세로 방향으로 확장된다.

  - span

    - 정의
      - 몇 칸을 차지할지 지정한다.

    - 예시

        .box {

            grid-column:span 2;

        }


    - 결과

            A A B
            C D E


    - 특징
      - 현재 위치 기준으로 확장된다.

  - grid-column과 span 차이

    - grid-column:1 / 3

      - 1번 선에서 3번 선까지 이동한다.

    - grid-column:span 2

      - 현재 위치에서 2칸 차지한다.

  - grid-column + grid-row

    - 예시

        .box {

            grid-column:1 / 3;
            grid-row:1 / 3;

        }


    - 결과

            A A B
            A A C
            D E F

    - 특징
      - 2 x 2 영역을 차지한다.

  - 실전 Layout 예시

    - 구조

            Header Header
            Menu   Content
            Footer Footer

    - CSS

        .container {

            display:grid;

            grid-template-columns:200px 1fr;

            grid-template-rows:80px 1fr 80px;

            gap:10px;

        }


        .header {

            grid-column:1 / 3;

        }


        .menu {

            grid-column:1;

        }


        .content {

            grid-column:2;

        }


        .footer {

            grid-column:1 / 3;

        }

    - 결과

            Header Header
            Menu   Content
            Footer Footer

- overflow

  - 개념
    - 요소(box)의 크기보다 내용이 더 클 때 **넘친 부분을 어떻게 처리할지 결정하는 CSS 속성**
    - 박스보다 내용이 크면 overflow가 발생함
    - 레이아웃 제어에서 매우 자주 사용되는 속성

  - 기본 구조

    overflow: 값;

    대표 값:

    overflow: visible;
    overflow: hidden;
    overflow: scroll;
    overflow: auto;


  - 동작 원리

    box 크기 > 내용 크기
    → 정상 표시

    box 크기 < 내용 크기
    → overflow 발생

    overflow는 반드시 **크기(width 또는 height)가 있어야 작동함**

    예시:

    height: 200px;
    overflow: auto;


  - overflow: visible

    - 기본값 (default)
    - 내용이 넘쳐도 그대로 표시됨
    - 박스 밖으로 내용이 튀어나옴

    예시:

    div {
        width: 200px;
        height: 100px;
        overflow: visible;
    }


  - overflow: hidden

    - 넘친 부분을 잘라서 숨김
    - 박스 영역 밖의 내용은 보이지 않음
    - 레이아웃 정리에 자주 사용됨

    예시:

    div {
        width: 200px;
        height: 100px;
        overflow: hidden;
    }

    사용 예:

    - 이미지 자르기
    - 둥근 모서리 처리

    예:

    border-radius: 20px;
    overflow: hidden;


  - overflow: scroll

    - 항상 스크롤바가 생성됨
    - 내용이 넘치지 않아도 스크롤 표시됨
    - 실무에서는 거의 사용하지 않음

    예시:

    div {
        width: 200px;
        height: 100px;
        overflow: scroll;
    }


  - overflow: auto

    - 내용이 넘칠 때만 스크롤 생성
    - 넘치지 않으면 스크롤 없음
    - 실무에서 가장 많이 사용됨

    예시:

    div {
        width: 200px;
        height: 100px;
        overflow: auto;
    }


  - 방향별 overflow

    가로 스크롤

    overflow-x: auto;

    - 가로 방향만 스크롤 생성

    세로 스크롤

    overflow-y: auto;

    - 세로 방향만 스크롤 생성


  - overflow가 작동하는 조건 (중요 ⭐)

    overflow는 반드시 크기가 있어야 동작함

    예:

    overflow: auto;

    → 아무 일도 안 일어남

    반드시:

    height: 200px;
    overflow: auto;

    또는:

    width: 300px;
    overflow: auto;


  - 실무 사용 패턴

    1) 스크롤 박스

    height: 300px;
    overflow: auto;

    사용 예:

    - 채팅창
    - 리스트
    - 메뉴


    2) 이미지 자르기

    overflow: hidden;

    사용 예:

    - 카드 UI
    - 프로필 이미지


    3) 가로 스크롤

    overflow-x: auto;

    사용 예:

    - 테이블
    - 코드 영역

## Bootstrap

- Bootstrap

  - 정의
    - 웹사이트 디자인을 빠르게 만들기 위한 CSS + JavaScript 라이브러리이다.
    - 버튼, 메뉴, 카드, 팝업창 같은 UI를 class만으로 만들 수 있다.
    - CSS를 직접 작성하지 않아도 기본 디자인이 적용된다.
    - 실무에서 매우 많이 사용되는 프레임워크이다.

  - CDN

    - 정의
      - Bootstrap 파일을 인터넷에서 바로 가져오는 방식이다.
      - Bootstrap을 설치하지 않고 사용할 수 있다.

    - Bootstrap CSS 연결

          <link href="https://cdn.jsdelivr.net/npm/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">

      - Bootstrap 디자인을 적용하기 위해 필요하다.

    - Bootstrap JavaScript 연결

          <script src="https://cdn.jsdelivr.net/npm/bootstrap/dist/js/bootstrap.bundle.min.js"></script>

      - Bootstrap 기능을 사용하기 위해 필요하다.

    - JavaScript가 필요한 기능

      - Navbar 버튼
      - Dropdown
      - Carousel
      - Modal

  - 기본 사용 방법

    - Bootstrap은 class 중심 구조이다.

          태그 class="bootstrap-class"

    - class를 추가하면 디자인이 적용된다.

    - 예시

          <button class="btn btn-primary">버튼</button>

    - Bootstrap 사용 순서

      1 Bootstrap 연결
      2 HTML 작성
      3 class 추가

  - Reset CSS

    - 정의
      - 브라우저 기본 스타일을 초기화하는 것이다.

    - 브라우저 기본 스타일 예

      - h1 → 큰 글자
      - p → margin 존재
      - ul → 들여쓰기 존재

    - Bootstrap 특징

      - 폰트 통일
      - margin 정리
      - 줄 간격 통일

    - Bootstrap은 Reset CSS가 포함되어 있다.

  - 활용 영역

    - Typography
      - 글자 스타일을 설정하는 기능이다.

    - Colors
      - 글자색과 배경색을 설정하는 기능이다.

    - Component
      - 완성된 UI 부품이다.

  - Typography

    - 정의
      - 글자의 크기와 스타일을 설정하는 기능이다.

    - Display 글자 크기

          <h1 class="display-1">Display 1</h1>

      - display-1 → 가장 큰 글자
      - display-6 → 작은 글자

      - 사이트 제목에 많이 사용된다.

    - 글자 스타일 태그

      - 형광펜

            <mark>text</mark>

      - 취소선

            <del>text</del>

      - 밑줄

            <ins>text</ins>

      - 굵은 글씨

            <strong>text</strong>

      - 기울임

            <em>text</em>

  - Colors

    - 정의
      - Bootstrap에서 제공하는 색상 시스템이다.

    - 글자 색상

          class="text-primary"

      - primary → 파랑
      - success → 초록
      - danger → 빨강
      - warning → 노랑
      - info → 하늘색
      - dark → 검정
      - light → 밝은색

    - 배경 색상

          class="bg-dark"

    - 사용 예

          class="text-warning bg-dark"

      - 글자색 노랑
      - 배경색 검정

    - 특징

      - 색상 이름만 기억하면 사용할 수 있다.

  - Component

    - 정의
      - Bootstrap에서 제공하는 완성된 UI 부품이다.

    - Navbar

      - 정의
        - 웹사이트 상단 메뉴이다.

      - 구성 요소

        - 로고
        - 메뉴
        - 검색창

    - Alert

      - 정의
        - 알림 메시지를 표시하는 Component이다.

      - 종류

        - alert-success
        - alert-danger
        - alert-warning
        - alert-info

    - Badge

      - 정의
        - 작은 표시를 나타내는 Component이다.

      - 사용 예

        - NEW 표시
        - 공지 표시

    - Card

      - 정의
        - 정보를 박스 형태로 표시하는 Component이다.

      - 사용 예

        - 상품 표시
        - 게시글 표시

      - 구성 요소

        - 이미지
        - 제목
        - 설명
        - 버튼

    - Carousel

      - 정의
        - 이미지를 슬라이드 형태로 표시하는 Component이다.

      - 사용 예

        - 쇼핑몰 배너
        - 메인 화면 이미지

    - Modal

      - 정의
        - 팝업창을 표시하는 Component이다.

      - 사용 예

        - 로그인 창
        - 회원가입 창

- Bootstrap Layout

  - 정의
    - 웹페이지 요소를 화면에 배치하는 방법이다.

  - 기본 구조

        container
          row
            col

    - Bootstrap Layout의 기본 구조이다.

  - Container

    - 정의
      - 내용을 가운데 정렬하고 폭을 제한하는 영역이다.

    - 형식

          <div class="container">

    - 특징

      - 가운데 정렬
      - 좌우 여백 생성
      - 최대 폭 제한

    - container-fluid

          <div class="container-fluid">

      - 화면 전체 폭 사용

  - Row

    - 정의
      - 가로 한 줄을 만드는 요소이다.

    - 형식

          <div class="row">

  - Column

    - 정의
      - 한 줄 안에서 칸을 나누는 요소이다.

    - 형식

          <div class="col">

  - Grid 시스템

    - 정의
      - Bootstrap은 화면을 12칸으로 나누어 Layout을 만든다.

    - 특징

      - 한 줄 = 12칸

    - col-6

          <div class="col-6">

      - 화면 반반 분할

    - col-4

          <div class="col-4">

      - 화면 3칸 분할

  - 핵심 구조

        container → 영역
        row → 줄
        col → 칸
