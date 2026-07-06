# Agent & Harness Study Notes

## 핵심 흐름
- Agentic AI를 잘 쓰는 핵심은 "코드 짜줘"가 아니라, AI가 안전하게 일할 수 있는 작업 구조를 먼저 만드는 것이다.
- Harness는 AI Agent가 따라야 할 문서, 규칙, 작업 단위, 검증 루프, 역할 분담, 완료 기준을 묶은 개발 운영 구조이다.
- Harness Engineering은 AI Agent가 실수하지 않고 개발할 수 있도록 작업 환경, 개발 절차, 검증 기준을 설계하는 방법이다.
- 개발자는 AI가 만든 결과를 그대로 믿는 사람이 아니라, AI가 일할 수 있는 구조를 만들고 결과를 검증하는 사람이어야 한다.

## 생성형 AI와 Agentic AI
- 생성형 AI
  - 문서 작성, 아이디어 정리, 요구사항 정리, 설계 초안 작성에 강하다.
  - PRD 초안, Spec 초안, 기능 아이디어, 화면 구조, 데이터 흐름을 정리할 때 유용하다.
- Agentic AI
  - 도구를 사용하고, 파일을 수정하고, 명령어를 실행하고, 결과를 검증하면서 작업한다.
  - 프로젝트 구조 분석, 구현 계획 작성, 코드 수정, 테스트 실행, 빌드 실행, 문서 업데이트에 적합하다.
- 좋은 흐름
  - 생성형 AI로 요구사항과 설계를 구체화한다.
  - Agentic AI로 구현과 검증을 수행한다.
  - 사람은 작업 범위, 품질, 최종 완료 여부를 검토한다.

## Harness Engineering 전체 흐름
```text
프로젝트 공통 규칙 정의
-> PRD 작성
-> Spec 작성
-> Harness Workflow 설계
   -> Phase 분할
   -> Verify Loop 설계
   -> Agent 역할 매핑
   -> 완료 기준 정의
-> Phase 단위 실행
-> 사람 리뷰
-> 문서 업데이트
-> 작은 단위 commit
-> 다음 Phase
```

- PRD
  - 무엇을 만들지 정의한다.
- Spec / SDD / Tech Spec
  - 어떻게 만들지 설계한다.
- Phase
  - 큰 기능을 구현 가능한 작은 작업 단위로 나눈다.
- Verify Loop
  - 각 Phase를 완료시키기 위한 검증 절차이다.
- Agent
  - Verify Loop의 각 단계를 수행하는 역할이다.
- Workflow
  - Phase, Verify Loop, Agent, 완료 기준을 묶은 Harness 구조이다.

## Claude Code CLI 설치 (Windows / Git Bash)
- Claude Code v2.1부터 네이티브 인스톨러를 지원한다.
- `install.sh`는 macOS, Linux, WSL 전용이다. Windows에서는 실행되지 않는다.
- Git Bash 터미널이 아닌 PowerShell에서 설치한다.
- 설치 후 Git Bash PATH에 수동으로 등록해야 `claude` 명령이 인식된다.

### 설치

```powershell
# PowerShell에서 실행
irm https://claude.ai/install.ps1 | iex
```

### Git Bash에서 PATH 등록

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### 실행 확인

```bash
claude --version
```

### VS Code에서 실행
- VS Code 통합 터미널(Ctrl+`)을 열고 작업 폴더에서 `claude`를 입력한다.
- Claude Code는 현재 열린 폴더를 프로젝트 컨텍스트로 인식한다.
- 처음 실행하면 브라우저 로그인 창이 뜬다.
- VS Code를 완전히 재시작해야 새로 등록한 PATH가 반영된다.

## 프로젝트 공통 규칙
- Agent가 프로젝트를 일관되게 이해하도록 공통 규칙 파일을 둔다.
- Claude Code에서는 `CLAUDE.md`, 여러 Agentic Coding Tool을 고려하면 `AGENTS.md`를 사용할 수 있다.
- 이 파일은 모든 문서를 넣는 곳이 아니라, 매 세션마다 반드시 알아야 하는 규칙과 문서 참조를 적는 곳이다.
- 반드시 차단해야 하는 행동은 문서 지침만으로 막기보다 permission rule이나 hook 같은 실행 통제를 함께 고려한다.

### 공통 규칙에 넣을 내용
- 프로젝트 개요
- 기술 스택
- 설치, 실행, 테스트, 빌드 명령어
- 코드 스타일과 컨벤션
- 인증키와 `.env` 관리 방법
- 구현 전에 읽어야 할 문서
- 한 번에 하나의 Phase만 구현한다는 규칙
- 테스트와 빌드 없이 완료로 보지 않는다는 규칙
- 기존 기능을 수정해야 할 때는 먼저 이유를 설명하고 승인받는다는 규칙

### 예시
```md
# Project Rules

## Must Read Before Coding
- Read docs/PRD.md before implementation.
- Read docs/SPEC.md before implementation.
- Read docs/PHASE.md before implementation.

## Workflow Rules
- Implement only the current phase.
- Write a plan before coding.
- Run tests and build after implementation.
- Record changed files and verification results.
- Do not modify unrelated files.
```

## PRD 작성
- PRD는 Product Requirements Document의 약자이다.
- 요구사항 문서이며, "무엇을 만들 것인가"를 정리한다.
- AI가 추측하지 않도록 기능의 범위와 제외할 일을 명확하게 적는다.

### PRD에 포함할 내용
- 무엇을 만들 것인가?
- 누가 사용할 것인가?
- 사용자는 어떤 행동을 할 수 있어야 하는가?
- 어떤 기능이 필요한가?
- 이번 단계에서 제외할 기능은 무엇인가?
- 성공 기준은 무엇인가?

### 나쁜 요청과 좋은 요구사항
```text
나쁜 요청:
게시판 만들어줘.

좋은 요구사항:
사용자는 게시글 목록을 볼 수 있다.
각 게시글에는 제목, 작성자, 작성일이 표시된다.
게시글 제목을 클릭하면 상세 페이지로 이동한다.
게시글이 없으면 "게시글이 없습니다" 메시지를 보여준다.
이번 단계에서는 작성, 수정, 삭제 기능은 제외한다.
```

## Spec 작성
- PRD가 "무엇을 만들지"라면 Spec은 "어떻게 만들지"를 정리하는 문서이다.
- SDD 또는 Tech Spec이라고도 부른다.
- Brainstorming은 아이디어와 요구사항을 질문과 대화로 Spec 수준까지 구체화하는 단계로 볼 수 있다.

### Spec에 포함할 내용
- 어떤 화면이 필요한가?
- 어떤 API가 필요한가?
- 데이터 구조는 어떻게 되는가?
- 어떤 파일을 만들거나 수정할 것인가?
- 어떤 라이브러리를 사용할 것인가?
- 예외 상황은 무엇인가?
- 완료 기준은 무엇인가?

### Acceptance Criteria 예시
```md
## Acceptance Criteria
- 사용자는 게시글 목록을 볼 수 있다.
- 각 게시글에는 제목, 작성자, 작성일이 표시된다.
- 제목을 클릭하면 상세 페이지로 이동한다.
- 게시글이 없으면 "게시글이 없습니다" 메시지를 보여준다.
- 이번 Phase에서는 작성, 수정, 삭제 기능은 구현하지 않는다.
```

## Phase 분할
- Phase는 큰 기능을 구현 가능한 작은 작업 단위로 나눈 것이다.
- Agent에게 한 번에 많은 기능을 맡기면 범위가 커지고, 검증도 어려워진다.
- 핵심 원칙은 WIP = 1이다.
- 한 번에 하나의 Phase만 구현한다.

### 나쁜 방식
```text
게시판 CRUD 전체를 한 번에 구현한다.
```

### 좋은 방식
```text
Phase 1: 게시글 목록 화면
Phase 2: 게시글 상세 화면
Phase 3: 게시글 작성 기능
Phase 4: 게시글 수정 기능
Phase 5: 게시글 삭제 기능
Phase 6: 예외 처리와 유효성 검사
```

### Phase 검토 기준
- 하나의 Phase가 너무 크지 않은가?
- 하나의 Phase에 여러 기능이 섞여 있지 않은가?
- 테스트 가능한 단위인가?
- 기존 기능에 불필요한 영향을 주지 않는가?
- 완료 기준이 명확한가?

## Verify Loop
- Verify Loop는 각 Phase를 완료시키는 검증 절차이다.
- Agent가 "구현 완료"라고 말해도 실제 완료가 아니다.
- 완료는 테스트, 빌드, 리뷰, Acceptance Criteria 검증으로 판단한다.

```text
Coding
-> Test
-> Review
-> Verify
-> Synthesize / Decide
```

- Coding
  - 현재 Phase에 해당하는 기능만 구현한다.
  - 관련 없는 파일은 수정하지 않는다.
- Test
  - 변경 범위와 관련된 테스트를 실행한다.
  - 필요하면 전체 테스트와 빌드를 실행한다.
- Review
  - 코드 품질, 범위 초과, 구조 문제, 기존 기능 영향 여부를 확인한다.
- Verify
  - PRD, Spec, Acceptance Criteria를 기준으로 완료 여부를 확인한다.
- Synthesize / Decide
  - 앞 단계 결과를 종합해 통과, 재작업, 범위 조정, 문서 업데이트 여부를 결정한다.

## Agent 역할 매핑
- Agent는 반드시 별도의 AI 인스턴스라는 뜻이 아니다.
- 실제로는 Subagent, Skill, 역할 기반 프롬프트, 별도 세션, 사람 리뷰를 조합할 수 있다.
- 역할을 분리하면 AI가 스스로 작성한 코드를 무비판적으로 통과시키는 위험을 줄일 수 있다.

| Loop 단계 | 담당 역할 | 하는 일 |
| --- | --- | --- |
| Coding | Coding Agent | PRD, Spec, Plan을 읽고 하나의 Phase만 구현한다. |
| Test | Test Agent | 테스트와 빌드를 실행하고 실패 원인을 분석한다. |
| Review | Review Agent | 코드 품질, 범위 초과, 구조 문제를 확인한다. |
| Verify | Verify Agent | Acceptance Criteria 충족 여부를 확인한다. |
| Decide | Decision Agent | 결과를 종합해 다음 행동을 결정한다. |

## Phase 실행 루프
```text
1. 조사
2. Plan 작성
3. 구현
4. Verify Loop 실행
5. 사람 리뷰
6. 문서 업데이트
7. Commit
```

### 1. 먼저 조사시킨다
- 바로 구현시키지 않는다.
- 프로젝트 구조, 관련 문서, 기존 코드 스타일, 수정 후보 파일을 먼저 조사하게 한다.

```text
아직 코드는 수정하지 마.
먼저 PRD, Spec, Phase 문서를 확인하고,
현재 프로젝트 구조와 관련 파일 목록을 조사해줘.
이 Phase에서 수정해야 할 파일 후보와 이유만 먼저 알려줘.
```

### 2. 구현 전에 Plan을 작성시킨다
- Agent가 코드를 쓰기 전에 어떤 파일을 왜 바꿀지 설명해야 한다.
- 개발자는 Plan을 읽고 이해한 뒤 구현을 승인한다.

```text
조사한 내용을 바탕으로 PLAN.md를 작성해줘.

포함할 내용:
1. 구현 목표
2. 수정할 파일 목록
3. 각 파일을 수정하는 이유
4. 구현 순서
5. 테스트 방법
6. 예상 리스크
7. 이번 Phase에서 하지 않을 일
```

### 3. 하나의 Phase만 구현시킨다
```text
PLAN.md에 작성한 내용대로 구현해줘.

규칙:
1. 이번 Phase는 게시글 목록 화면만 구현한다.
2. 작성, 수정, 삭제 기능은 구현하지 않는다.
3. PLAN.md에 없는 파일은 수정하지 않는다.
4. 꼭 수정이 필요하면 먼저 이유를 설명하고 승인을 받아라.
5. 구현 후 어떤 파일을 왜 바꿨는지 설명해줘.
```

### 4. 구현 후 검증시킨다
```text
관련 테스트를 실행해줘.
빌드 명령어를 실행해줘.
에러가 있으면 원인을 분석하고 수정해줘.
이번 기능을 위해 추가된 코드만 수정해줘.
기존 기능을 수정해야 한다면 먼저 이유와 수정 방법을 설명하고 승인을 받아줘.
최종 결과와 남은 리스크를 알려줘.
```

## Claude Code 사용 팁

### 세션 내 슬래시 명령어

| 명령어 | 설명 |
| --- | --- |
| `/usage` | 현재 세션의 토큰 사용량과 플랜 한도 확인 |
| `/context` | 컨텍스트 창 사용량 확인 |
| `/compact` | 긴 대화를 요약해서 압축 |

- Claude Code는 5시간 단위 롤링 윈도우로 토큰 한도가 적용된다.
- 작업 중간에 `/usage`로 남은 토큰을 확인하는 습관을 들인다.
- 대화가 길어지면 `/compact`로 컨텍스트를 줄이고 계속 작업할 수 있다.

### 세션 이어가기

```bash
# 가장 최근 세션을 이어서 시작
claude --continue

# 세션 목록에서 선택해서 이어가기
claude --resume
```

### 다음 세션에서 이어가기
- 세션을 종료하기 전에 `PROGRESS.md`에 오늘 완료한 것과 다음에 할 것을 기록한다.
- 세션 기록보다 문서 기반으로 이어가는 것이 컨텍스트가 흐려지는 문제를 방지한다.
- 새 세션 시작 시 문서를 먼저 읽게 한 뒤 진행한다.

```text
PROGRESS.md, PLAN.md, SPEC.md를 읽고 현재 진행 상황을 파악해줘.
Phase N부터 이어서 진행할 거야.
```

## 문서 업데이트와 Commit
- 기능 구현과 검증이 끝나면 기록을 남긴다.
- 기록은 다음 Agent 세션의 Harness가 된다.

### 매 Phase마다 업데이트하기 좋은 문서
- `PROGRESS.md`
- `TEST_RESULT.md`
- `PHASE.md`

### 필요할 때 업데이트하는 문서
- `PRD.md`
  - 요구사항이 바뀐 경우
- `SPEC.md`
  - 설계가 바뀐 경우
- `PLAN.md`
  - 구현 계획이 바뀐 경우

### 기록할 내용
- 무엇을 구현했는가?
- 어떤 파일을 수정했는가?
- 어떤 테스트를 실행했는가?
- 테스트 결과는 무엇인가?
- 리뷰 결과는 무엇인가?
- 남은 작업은 무엇인가?
- 다음 Phase는 무엇인가?

### Commit 원칙
- 하나의 commit에는 하나의 Phase만 포함한다.
- 테스트가 실패한 상태로 commit하지 않는다.
- 관련 없는 변경은 commit하지 않는다.

```bash
git status
git diff
git add -p
git commit -m "feat: implement post list page"
```

## 실전 체크리스트
- 구현 전에 공통 규칙 파일을 만들었는가?
- PRD에 기능 범위와 제외 범위를 적었는가?
- Spec에 화면, API, 데이터 구조, 수정 파일, 완료 기준을 적었는가?
- 큰 기능을 작은 Phase로 나눴는가?
- 이번 작업의 WIP가 1인가?
- Agent에게 먼저 조사와 Plan 작성을 시켰는가?
- Plan에 없는 파일을 수정하지 않도록 제한했는가?
- 테스트와 빌드를 실행했는가?
- Acceptance Criteria를 기준으로 검증했는가?
- 사람이 최종 리뷰했는가?
- 문서와 commit을 작은 단위로 남겼는가?

## 유의점과 교훈
- AI Agent에게 모호하게 요청하면 Agent가 많은 것을 추측한다.
- 추측이 많아질수록 범위 초과, 불필요한 수정, 검증 누락이 생긴다.
- PRD와 Spec은 Agent의 자유도를 낮추는 문서가 아니라, 좋은 결과를 안정적으로 만들기 위한 기준이다.
- Phase를 작게 나누면 구현, 테스트, 리뷰, 롤백이 쉬워진다.
- Agent의 완료 선언보다 테스트, 빌드, 리뷰, 문서 기준이 더 중요하다.
- AI 테스트도 필요하지만 최종 품질 책임은 개발자에게 있다.
- 좋은 Agentic AI 사용법은 더 많이 맡기는 것이 아니라, 더 명확한 구조 안에서 맡기는 것이다.
