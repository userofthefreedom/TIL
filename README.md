[맛보기](#사전-학습-맛보기)
[git](#git)
[TIP](#tip)

# 사전 학습 (맛보기)

[점프투파이썬](https://wikidocs.net/book/1)

1. 파이썬이란? 설치법 등
2. 자료형
    - 숫자형, 문자형, 리스트 (range), 튜플, 딕셔너리, 집합, 불
3. 제어문
    - if / while / for
4. 입출력
    - input과 print 함수
5. 클래스

# GIT
- 로컬 기초
  - git은 working directory, staging area, repository로 구성되어 있다
    - working directory : 실제 작업중 파일 위치
    - staging area : 워킹에서 변경된 파일 중 다음 버전 포함 시킬 파일 선택, 대기 시키는 중간 준비 영역
    - repository : 버전 이력과 파일들이 영구 저장되는 곳
- Commit
  - 커밋은 버전으로, 변경된 파일을 저장하는 행위

# TIP
- ord()로 아스키코드화, chr()으로 다시 글으로
  - 아스키 코드 기준 
    - 48 <= x <= 57: 숫자
    - 65 <= x <= 90: 대문자
    - 97 <= x <= 122: 소문자
```
alphab = input()
wrong_list = []
x = "A"
while ord(x) <= ord(alphab) :
    wrong_list.append(x)
    x = chr(ord(x)+1)

print("".join(wrong_list))
```
- isdigit() 숫자인지 판별
```
ch_list = list(map(str,input().split()))
check_list = 0
for i in ch_list:
    if i.isdigit():
        check_list += 1

if check_list == 0:
    print("숫자미발견")
else:
    print(f"숫자{check_list}개발견")
```
- python 패키지

![readme_pic]
