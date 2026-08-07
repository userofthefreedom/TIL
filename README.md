# TIL

프로그래밍 및 AI를 학습하며 정리한 내용을 모아 둔 TIL 저장소입니다.

## Quick Navigation

- [폴더별 학습 정리](#폴더별-학습-정리)
- [프로젝트 회고](#프로젝트-회고)
- [학습 운영 방식](#학습-운영-방식)
- [작성 템플릿과 체크리스트](#작성-템플릿과-체크리스트)
- [공통 메모](#공통-메모)
  - [CLI 기본 명령어](#cli-기본-명령어)
  - [Git 활용법](#git-활용법)
  - [Markdown / README 작성법](#markdown--readme-작성법)

## 학습 운영 방식

이 저장소는 단순히 배운 내용을 쌓아 두는 곳이 아니라, 나중에 다시 꺼내 쓰기 위한 개인 지식 베이스로 관리합니다.

### 정리 원칙

- **개념**: 용어를 내 말로 설명합니다.
- **흐름**: 어떤 순서로 동작하는지 단계로 정리합니다.
- **예시**: 바로 실행하거나 응용할 수 있는 최소 코드를 남깁니다.
- **주의점**: 헷갈렸던 부분, 자주 나는 오류, 실수 방지 기준을 기록합니다.
- **연결**: 다른 주제와 이어지는 부분은 관련 폴더 링크를 남깁니다.

### 추천 작성 흐름

```text
학습
-> 핵심 개념 3~5개 추리기
-> 예시 코드 작성
-> 실수/오류 기록
-> 관련 문서 링크 연결
-> README 목차 갱신
```

### 노트 성숙도

| 상태 | 의미 |
| --- | --- |
| Draft | 강의나 실습 중 빠르게 적은 메모 |
| Reviewed | 한 번 다시 읽고 구조를 정리한 문서 |
| Applied | 문제 풀이, 프로젝트, 실습에 실제로 사용한 내용 |

## 작성 템플릿과 체크리스트

- [TIL 작성 템플릿](docs/TIL_TEMPLATE.md)
- [학습 노트 리뷰 체크리스트](docs/REVIEW_CHECKLIST.md)

## 프로젝트 회고

GitHub에 공개한 프로젝트 repo를 분석해 구현 흐름, 주요 커밋, 사용 기술, 배운 점을 정리합니다.

- [프로젝트 회고 인덱스](projects/README.md)
- [프로젝트 분석 템플릿](projects/PROJECT_TEMPLATE.md)

## 폴더별 학습 정리

### [Python](python/README.md)

Python 기본 문법과 객체지향, 예외 처리, 모듈, 라이브러리 활용을 정리했습니다. `Counter`, `deque`, 순열/조합, `requests`처럼 알고리즘과 웹 요청에서 자주 쓰는 도구도 함께 다룹니다.

### [Algorithm](algorithm/README.md)

알고리즘 문제 풀이를 위한 사고 방식과 자료구조 기반 풀이를 정리했습니다. 탐색, 배열, 정렬, 그래프, DP, 그리디, Union-Find, BFS/DFS 등 문제 풀이 과정에서 반복해서 쓰이는 패턴을 중심으로 구성했습니다.

### [WEB](web/README.md)

HTML, CSS, 레이아웃, Bootstrap, 반응형 웹 기초를 정리했습니다. HTML 태그 구조, CSS 선택자와 박스 모델, flex/grid, Bootstrap component와 utility, 웹 학습 시 공식 문서와 검색을 활용하는 태도까지 담았습니다.

### [JavaScript](javascript/README.md)

JavaScript 기본 문법, 함수, 객체, `this`, 배열 helper method, DOM/BOM, Event, 비동기 처리, Promise, Axios와 Ajax 실습 흐름을 정리했습니다. 좋아요/팔로우 Ajax 구현처럼 Django와 연결되는 프론트엔드 흐름도 포함합니다.

### [Vue](vue/README.md)

Vue 프로젝트 생성, Vite, Single File Component, `ref`, `v-model`, directive, computed/watch/lifecycle, component 분리, props/emit, Vue Router, dynamic/nested routes, navigation guard를 정리했습니다.

### [DB](db/README.md)

관계형 데이터베이스와 SQL 기본 문법, 테이블 조작, 조회 흐름, JOIN, Django ORM과 모델 관계를 정리했습니다. Django CRUD, 인증, M:N 관계, 좋아요/팔로우, fixture, CSV, hashtag 구현 흐름도 함께 다룹니다.

### [Django](django/README.md)

Django 프로젝트 구조와 URL, View, Template, DTL, namespace, variable routing, GET/POST/CSRF, Model/Migration/Admin, ORM, QuerySet, CRUD, Form/ModelForm, static/media file까지 정리했습니다.

### [AI](ai/README.md)

AI 학습을 위한 Python, 수학 기초, 머신러닝, EDA, Scikit-learn, PyTorch, NLP, LLM prompting, 데이터 생성, 컴퓨터 비전, 이미지 파운데이션 모델, 멀티모달, LangChain과 RAG를 정리했습니다.

### [Agent & Harness](agent&harness/README.md)

Agentic AI와 Harness Engineering을 활용한 개발 흐름을 정리했습니다. PRD, Spec, Phase 분할, Verify Loop, Agent 역할 매핑, 사람 리뷰, 문서 업데이트와 작은 단위 commit까지 AI Agent가 안전하게 일할 수 있는 구조를 다룹니다.

## 공통 메모

여러 학습 과정에서 공통으로 반복해서 쓰이는 도구와 문서 작성 기준입니다.

## CLI 기본 명령어

CLI(Command Line Interface)는 터미널에서 명령어로 컴퓨터를 조작하는 방식입니다. 폴더 이동, 파일 생성, 삭제, 복사, 내용 확인을 빠르게 수행할 수 있습니다.

### 현재 위치와 파일 목록

```bash
pwd
ls
ls -a
ls -l
ls -al
```

- `pwd`: 현재 위치 출력
- `ls`: 현재 폴더의 파일/폴더 목록 출력
- `ls -a`: 숨김 파일 포함
- `ls -l`: 자세히 보기

위치가 헷갈릴 때는 먼저 `pwd`와 `ls`를 확인합니다.

### 폴더 이동

```bash
cd 폴더이름
cd ..
cd .
cd ~
cd /
```

- `..`: 상위 폴더
- `.`: 현재 폴더
- `~`: 홈 디렉터리
- `/`: 루트 디렉터리

### 파일과 폴더 생성

```bash
mkdir my_folder
mkdir -p a/b/c
touch test.txt
```

- `mkdir`: 폴더 생성
- `mkdir -p`: 중간 경로까지 한 번에 생성
- `touch`: 파일이 없으면 생성, 있으면 수정 시간 갱신

### 파일 내용 확인과 출력

```bash
cat README.md
echo "hello"
echo "hello" > hello.txt
echo "world" >> hello.txt
```

- `cat`: 텍스트 파일 내용 출력
- `echo`: 문자열 출력
- `>`: 덮어쓰기
- `>>`: 이어쓰기

### 복사와 이동

```bash
cp a.txt b.txt
cp a.txt folder/
cp -r my_folder backup/
mv old.txt new.txt
mv a.txt folder/
```

- `cp`: 파일/폴더 복사
- `cp -r`: 폴더 복사
- `mv`: 파일/폴더 이동 또는 이름 변경

### 삭제와 터미널 정리

```bash
rm a.txt
rm -r folder/
clear
history
```

- `rm`: 파일 삭제
- `rm -r`: 폴더 삭제
- `clear`: 터미널 화면 정리
- `history`: 이전 명령어 기록 확인

`rm -rf`는 매우 위험하므로 삭제 대상 경로를 반드시 확인한 뒤 사용합니다.

## Git 활용법

Git은 코드 변경 사항을 기록하는 버전 관리 도구입니다. 기본 흐름은 수정, add, commit, push입니다.

### 저장소 시작과 복제

```bash
git init
git clone https://github.com/username/repository.git
```

- `git init`: 현재 폴더를 Git 저장소로 초기화
- `git clone`: 원격 저장소를 로컬로 복제

`.git` 폴더는 저장소의 변경 이력을 담고 있으므로 함부로 삭제하지 않습니다.

### 상태 확인과 변경 내용 보기

```bash
git status
git diff
git diff --staged
git log --oneline --graph --decorate
```

- `git status`: 변경 파일과 staging 상태 확인
- `git diff`: 아직 staging하지 않은 변경 비교
- `git diff --staged`: staging된 변경 비교
- `git log`: commit 기록 확인

### 변경 사항 저장

```bash
git add 파일이름
git add .
git add -A
git commit -m "commit message"
```

- `git add`: commit할 변경 사항을 staging
- `git commit`: staging된 변경을 하나의 버전으로 저장

commit message는 나중에 변경 이유를 이해할 수 있도록 작성합니다.

### 원격 저장소 동기화

```bash
git remote -v
git remote add origin URL
git push origin main
git pull origin main
```

- `git remote`: 원격 저장소 확인/등록
- `git push`: 로컬 commit을 원격 저장소에 업로드
- `git pull`: 원격 저장소의 최신 내용을 가져와 병합

로컬과 원격에서 같은 파일을 다르게 수정했다면 conflict가 발생할 수 있습니다.

### 브랜치

```bash
git branch
git branch feature/login
git switch feature/login
git switch -c feature/articles
```

- `branch`: 특정 commit을 가리키는 이름
- `git branch`: 브랜치 목록 확인 또는 생성
- `git switch`: 다른 브랜치로 이동
- `git switch -c`: 브랜치를 만들면서 이동

작업 중인 변경 사항이 있을 때 브랜치를 이동하면 충돌하거나 이동이 막힐 수 있으므로, 이동 전 `git status`를 확인합니다.

### 병합과 충돌

```bash
git switch main
git merge feature/login
git branch -d feature/login
```

- `git merge`: 다른 브랜치의 작업을 현재 브랜치에 병합
- `git branch -d`: 병합이 끝난 브랜치 삭제

충돌이 발생하면 파일 안에 conflict marker가 생깁니다.

```text
<<<<<<< HEAD
main branch content
=======
feature branch content
>>>>>>> feature/login
```

충돌 부분을 직접 수정한 뒤 다시 `git add`와 `git commit`을 진행합니다.

### Pull Request 협업 흐름

```text
main
-> feature branch 생성
-> 기능 구현
-> commit
-> push
-> Pull Request
-> review
-> merge
```

협업 시에는 main 브랜치에서 직접 작업하기보다 기능별 브랜치를 만들고, Pull Request를 통해 리뷰와 병합을 진행합니다. PR 제목과 설명에는 변경 내용과 확인한 내용을 남깁니다.

## Markdown / README 작성법

Markdown은 문서를 구조화하고, GitHub README처럼 렌더링되는 환경에서 보기 좋게 표시하기 위한 문법입니다.

### 제목과 문서 구조

```md
# 제목1
## 제목2
### 제목3
```

`#` 뒤에는 공백을 넣습니다. 긴 문서는 `#`, `##`, `###` 계층을 유지하면 읽기 쉽습니다.

### 목차와 내부 링크

```md
- [Git 활용법](#git-활용법)
```

내부 링크는 heading 텍스트를 소문자화하고, 띄어쓰기를 `-`로 바꾼 형태를 사용합니다. 한글 heading도 GitHub에서 내부 링크로 사용할 수 있습니다.

### 리스트

```md
- 항목
  - 하위 항목

1. 첫 번째
2. 두 번째

- [x] 완료
- [ ] 미완료
```

한 문서 안에서는 리스트 스타일을 가능하면 통일합니다.

### 코드

````md
```python
print("hello")
```
````

문장 안에서 명령어나 파일명을 강조할 때는 backtick을 사용합니다.

```md
`git status`를 실행한다.
```

### 링크와 이미지

```md
[Python 정리](python/README.md)
![이미지 설명](image.png)
```

링크는 `[텍스트](주소)`, 이미지는 앞에 `!`를 붙입니다.

### 텍스트 강조와 구분선

```md
**굵게**
*기울임*
~~취소선~~
---
```
