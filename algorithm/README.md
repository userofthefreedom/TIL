# Algorithm

## 🚀 Algorithm Quick Navigation

- [알고리즘 사고 방식](#알고리즘-사고-방식)
  - [알고리즘 기본 개념](#알고리즘-기본-개념)
  - [시간 복잡도](#시간-복잡도)
  - 알고리즘 입출력 패턴

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
  - 2D Grid Direction
  - 완전 탐색
  - 선형 탐색

- [배열 기반 알고리즘](#배열-기반-알고리즘)
  - String Matching
  - Palindrome
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
  - Permutation / Combination / Subset
  - Implementation / Simulation
  - Divide and Conquer
  - Dynamic Programming
  - Bit Manipulation

- [자료구조 기반 알고리즘](#자료구조-기반-알고리즘)
  - Priority Queue
  - Segment Tree
  - Fenwick Tree
  - Trie

---


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

- 알고리즘 입출력 패턴
  - 개념
    - 알고리즘 문제는 입력 형식이 고정되어 있으므로 빠르고 안정적으로 입력을 읽는 방식이 중요하다
    - 로컬에서 여러 테스트 케이스를 확인할 때는 `input.txt`를 연결해서 실행하면 편하다
    - 온라인 저지에 제출할 때는 파일 입력 연결 코드를 제거하거나 주석 처리해야 한다

  - 기본 입력
    - 예시 코드

        ```python
        n = int(input())
        arr = list(map(int, input().split()))
        ```

  - 여러 줄 입력
    - 예시 코드

        ```python
        n, m = map(int, input().split())
        grid = [list(map(int, input().split())) for _ in range(n)]
        ```

  - 로컬 테스트 입력
    - 예시 코드

        ```python
        import sys
        sys.stdin = open("input.txt", "r")

        T = int(input())
        for tc in range(1, T + 1):
            n = int(input())
            arr = list(map(int, input().split()))
        ```

    - 주의
      - `input.txt`는 로컬 테스트용 파일이다
      - 공개 기록으로 남길 때는 문제 입력 파일 자체보다 입력 형식과 풀이 아이디어를 기록하는 편이 좋다
      - 제출 환경에서는 `sys.stdin = open(...)` 줄이 실패할 수 있으므로 제거한다

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

  - 2D Grid Direction

    - 개념
      - 2차원 배열 문제에서 현재 좌표 `(r, c)`를 기준으로 다음 좌표를 만드는 패턴
      - BFS, DFS, 완전 탐색, 구현/시뮬레이션 문제에서 반복적으로 사용한다
      - 방향 배열과 범위 체크를 분리하면 실수를 줄일 수 있다

    - 상하좌우 4방향

        ```python
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if not (0 <= nr < row and 0 <= nc < col):
                continue
        ```

    - 8방향

        ```python
        dirs = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1),
        ]

        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc
        ```

    - 방향 제약이 있는 경우
      - 전차, RC카, 터널, 파이프처럼 현재 상태나 칸의 종류에 따라 이동 가능한 방향이 달라질 수 있다
      - 이때는 방향을 dictionary로 관리하면 조건 분기가 줄어든다

        ```python
        dirs = {
            "U": (-1, 0),
            "D": (1, 0),
            "L": (0, -1),
            "R": (0, 1),
        }

        dr, dc = dirs[heading]
        nr = r + dr
        nc = c + dc
        ```

    - 주의
      - `row`, `col` 범위 체크를 먼저 한다
      - 방문 체크와 이동 가능 조건을 분리해서 생각한다
      - 문제마다 좌표가 `(row, col)`인지 `(x, y)`인지 먼저 통일한다

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

- String Matching
  - 개념
    - 긴 문자열 `text` 안에서 특정 패턴 `pattern`이 등장하는 위치나 횟수를 찾는 문제
    - 문자열도 인덱스로 접근할 수 있는 시퀀스이므로 배열 문제처럼 생각할 수 있다

  - Brute Force
    - 개념
      - 가능한 모든 시작 위치에서 패턴을 직접 비교하는 방식
      - 구현이 단순하지만 최악의 경우 느릴 수 있다

    - 시간 복잡도

        ```text
        O(N * M)
        ```

    - 예시 코드

        ```python
        def brute_force(text, pattern):
            n = len(text)
            m = len(pattern)

            for start in range(n - m + 1):
                matched = True

                for i in range(m):
                    if text[start + i] != pattern[i]:
                        matched = False
                        break

                if matched:
                    return start

            return -1
        ```

  - KMP
    - 개념
      - 이미 비교한 정보를 활용해 불필요한 비교를 줄이는 문자열 탐색 알고리즘
      - `LPS(Longest Prefix Suffix)` 배열을 만들어 패턴이 어디까지 일치했는지 재사용한다

    - 시간 복잡도

        ```text
        O(N + M)
        ```

    - LPS 생성

        ```python
        def build_lps(pattern):
            lps = [0] * len(pattern)
            length = 0
            i = 1

            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                elif length != 0:
                    length = lps[length - 1]
                else:
                    i += 1

            return lps
        ```

    - 탐색

        ```python
        def kmp(text, pattern):
            lps = build_lps(pattern)
            i = j = 0
            result = []

            while i < len(text):
                if text[i] == pattern[j]:
                    i += 1
                    j += 1

                    if j == len(pattern):
                        result.append(i - j)
                        j = lps[j - 1]
                elif j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

            return result
        ```

- Palindrome
  - 개념
    - 앞에서 읽어도 뒤에서 읽어도 같은 문자열이나 배열
    - 회문 검사, 가장 긴 회문, 격자 안 회문 찾기 문제에서 자주 사용한다

  - 기본 검사

      ```python
      def is_palindrome(text):
          return text == text[::-1]
      ```

  - 양끝 포인터 검사

      ```python
      def is_palindrome(text):
          left = 0
          right = len(text) - 1

          while left < right:
              if text[left] != text[right]:
                  return False
              left += 1
              right -= 1

          return True
      ```

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

- Permutation / Combination / Subset
  - 개념
    - 백트래킹에서 가장 자주 등장하는 경우의 수 생성 패턴
    - 순열은 순서가 중요하고, 조합은 선택한 원소의 집합만 중요하다
    - 부분집합은 각 원소를 선택하거나 선택하지 않는 모든 경우를 만든다

  - 순열

      ```python
      arr = [1, 2, 3]
      visited = [False] * len(arr)

      def perm(path):
          if len(path) == len(arr):
              print(path)
              return

          for i in range(len(arr)):
              if visited[i]:
                  continue

              visited[i] = True
              perm(path + [arr[i]])
              visited[i] = False

      perm([])
      ```

  - 조합

      ```python
      arr = [1, 2, 3, 4]
      r = 2

      def comb(start, path):
          if len(path) == r:
              print(path)
              return

          for i in range(start, len(arr)):
              comb(i + 1, path + [arr[i]])

      comb(0, [])
      ```

  - 부분집합

      ```python
      arr = [1, 2, 3]

      def subset(idx, path):
          if idx == len(arr):
              print(path)
              return

          subset(idx + 1, path + [arr[idx]])
          subset(idx + 1, path)

      subset(0, [])
      ```

  - 주의
    - 중복 원소가 있는 경우 같은 결과가 여러 번 나올 수 있다
    - 문제 조건에 따라 `visited`, `start`, 정렬, 중복 건너뛰기 처리가 필요하다

- Implementation / Simulation
  - 개념
    - 특별한 알고리즘보다 문제 조건을 정확히 코드로 옮기는 유형
    - 격자 이동, 방향 전환, 상태 변화, 명령 처리, 중력, 회전, 충돌 처리 같은 구현 요소가 자주 등장한다

  - 접근 순서

      ```text
      1. 상태를 어떤 자료구조로 표현할지 정한다
      2. 명령 또는 시간 흐름에 따라 상태를 갱신한다
      3. 범위 체크와 예외 조건을 먼저 처리한다
      4. 작은 예제로 직접 시뮬레이션하며 검증한다
      ```

  - 방향 전환 예시

      ```python
      # 0: up, 1: right, 2: down, 3: left
      dr = [-1, 0, 1, 0]
      dc = [0, 1, 0, -1]

      direction = 0
      direction = (direction + 1) % 4  # 오른쪽 회전
      direction = (direction - 1) % 4  # 왼쪽 회전
      ```

  - 격자 상태 갱신 예시

      ```python
      nr = r + dr[direction]
      nc = c + dc[direction]

      if 0 <= nr < row and 0 <= nc < col and board[nr][nc] != "#":
          r, c = nr, nc
      ```

  - 주의
    - 문제에서 말하는 좌표 기준과 배열 인덱스 기준을 맞춘다
    - 상태 변경 순서가 답을 바꾸는 경우가 많으므로 조건을 순서대로 기록한다
    - 구현 문제는 코드가 길어지기 쉬우므로 기능을 작은 단계로 나누어 확인한다

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

