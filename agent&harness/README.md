# Agent & Harness Study Notes

Agentic AI와 Harness Engineering을 활용해 AI Agent가 안전하게 일할 수 있는 개발 흐름을 정리합니다.

## Quick Navigation

- [핵심 흐름](#핵심-흐름)
- [생성형 AI와 Agentic AI](#생성형-ai와-agentic-ai)
- [Harness Engineering 전체 흐름](#harness-engineering-전체-흐름)
- [Claude Code CLI 설치 (Windows / Git Bash)](#claude-code-cli-설치-windows--git-bash)
- [프로젝트 공통 규칙](#프로젝트-공통-규칙)
- [팀 단위 Agent 운영 규칙](#팀-단위-agent-운영-규칙)
- [PRD 작성](#prd-작성)
- [Spec 작성](#spec-작성)
- [Phase 분할](#phase-분할)
- [Verify Loop](#verify-loop)
- [Agent 역할 매핑](#agent-역할-매핑)
- [Multi-Agent Orchestration](#multi-agent-orchestration)
- [Phase 실행 루프](#phase-실행-루프)
- [Claude Code 사용 팁](#claude-code-사용-팁)
- [문서 업데이트와 Commit](#문서-업데이트와-commit)
- [실전 체크리스트](#실전-체크리스트)
- [유의점과 교훈](#유의점과-교훈)

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

## 팀 단위 Agent 운영 규칙

개인 실습에서는 PRD, Spec, Phase만으로도 충분할 수 있다. 하지만 팀 프로젝트에서는 Agent가 코드만 잘 작성하는 것보다 **정해진 협업 흐름 안에서 안전하게 움직이는 것**이 더 중요하다.

### 규칙 문서 계층화
- 루트에는 모든 Agent와 팀원이 공통으로 따를 규칙을 둔다.
- 앱이나 도메인별 폴더에는 해당 영역 전용 규칙을 별도로 둔다.
- 하위 규칙 문서는 공통 규칙을 대체하지 않고, 공통 규칙을 먼저 참조한 뒤 자기 영역의 예외와 세부 관례만 적는다.

```text
root/
  AGENTS.md 또는 CLAUDE.md        # 공통 협업 규칙
  apps/
    frontend/CLAUDE.md           # 프론트 전용 규칙
    backend/CLAUDE.md            # 백엔드 전용 규칙
    worker/CLAUDE.md             # 작업 영역 전용 규칙
```

이 구조를 쓰면 Agent는 먼저 팀 전체 규칙을 읽고, 그 다음 현재 작업 영역의 구체적인 제약을 읽는다.

### 수정 가능 범위 제한
- Agent가 기본적으로 수정할 수 있는 경로를 문서에 명확히 적는다.
- 예외적으로 수정 가능한 공통 문서나 spec 경로도 함께 적는다.
- 범위 밖 파일을 고쳐야 할 때는 바로 수정하지 않고, 필요성과 변경 범위를 먼저 설명하고 승인받게 한다.

```text
이 Agent는 apps/worker/ 안의 코드와 문서만 수정한다.
예외적으로 docs/specs/ 안의 이번 작업 명세서는 수정할 수 있다.
그 외 파일 변경이 필요하면 먼저 이유와 범위를 설명하고 승인받는다.
```

경로 제한은 Agent의 추측성 수정을 줄이고, 다른 담당 영역의 결정을 임의로 바꾸지 않게 한다.

### Spec 승인 전 자체 검증
- Agent가 Spec을 작성한 뒤 곧바로 승인 요청하지 않게 한다.
- Spec에 적은 파일, API, schema, field, 테스트 명령이 실제 코드와 맞는지 먼저 대조한다.
- 검증 중 발견한 문제는 Spec에 반영한 뒤 승인 요청한다.

```text
Spec 작성
-> 실제 파일과 코드 패턴 확인
-> API/DTO/schema 이름 대조
-> 테스트 명령 실행 가능성 확인
-> Spec 보정
-> 사용자 승인 요청
-> 구현 시작
```

이 과정을 넣으면 보기 좋은 Spec이 아니라 **실행 가능한 Spec**을 만들 수 있다.

### Spec과 Phase 기록 분리
- Spec은 구현 전 설계 문서로 둔다.
- Phase 기록은 구현 후 결과 문서로 둔다.
- 하나의 Phase가 끝날 때마다 새 기록 파일을 만들고, 기존 기록은 덮어쓰지 않는다.
- Phase index 문서를 두어 완료한 Phase와 다음 착수 후보를 한눈에 볼 수 있게 한다.

```text
docs/specs/
  ISSUE-123-feature.md       # 어떻게 만들지

docs/phases/
  README.md                  # Phase 현황 index
  ISSUE-123-feature.md       # 무엇을 구현했고 무엇이 남았는지
```

Spec에는 계획과 범위를, Phase 기록에는 구현 내용, 테스트 결과, 리뷰 결과, 남은 위험, 다음 작업을 적는다.

### 외부 의존성 분리
- 다른 앱, 다른 팀, 외부 서비스가 결정해야 하는 내용은 Agent가 확정하지 않는다.
- 문서에는 `확인 필요(외부 의존성)`처럼 표시하고, 실제 조율과 의사결정은 사람에게 맡긴다.
- 다음 Agent에게 지시할 내용과 사람이 결정해야 할 내용을 섞지 않는다.

이 기준을 지키면 Agent가 자기 작업 범위를 넘어 다른 담당자의 백로그를 임의로 만들어 버리는 일을 줄일 수 있다.

### 생성물 수기 수정 금지
- OpenAPI SDK, 자동 생성 README, schema 산출물처럼 생성 명령으로 만들어지는 파일은 직접 고치지 않는다.
- 원본 계약이나 생성 스크립트를 고친 뒤 재생성한다.
- 재생성 결과는 `git diff`와 타입 검사로 확인한다.

```text
원본 계약 변경
-> 생성 명령 실행
-> git diff 확인
-> typecheck / test 실행
-> 호출부가 깨졌으면 호출부만 수정
```

생성물을 손으로 고치면 다음 재생성 때 사라지고, 실제 계약과 코드가 어긋날 수 있다.

### 협업 시스템까지 연결
- 브랜치명, 커밋 메시지, 이슈 번호, MR 제목과 본문 형식을 정해 둔다.
- 작업 시작 전 최신 통합 브랜치에서 새 브랜치를 만든다.
- MR 본문에는 변경 내용, 검증 결과, 보안 체크, 관련 이슈를 남긴다.
- main/dev 같은 통합 브랜치에는 직접 push하지 않는다.

Agent 운영은 코드 작성으로 끝나지 않는다. 팀 협업에서는 이슈, 브랜치, commit, MR까지 같은 규칙으로 이어져야 작업 이력이 추적 가능해진다.

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

## Multi-Agent Orchestration
- Multi-Agent Orchestration은 여러 AI Agent에게 작업을 나누어 맡기고, 각 Agent의 결과를 연결, 검증, 조정하는 구조를 설계하는 것이다.
- 중요한 점은 Agent의 수를 늘리는 것이 아니라, 역할과 책임을 명확히 나누는 것이다.
- Agent가 많아질수록 자동으로 품질이 좋아지는 것이 아니라, 중복 작업, 잘못된 합의, 검증 누락, 컨텍스트 오염이 생길 수 있다.
- 좋은 Orchestration은 "누가 계획하고, 누가 만들고, 누가 검토하고, 누가 최종 결정하는가"를 명확히 한다.

### 단일 Agent와 Multi-Agent의 차이
- 단일 Agent는 하나의 AI가 조사, 계획, 구현, 검증, 문서화를 모두 수행하는 방식이다.
- 작업 흐름이 단순하고 빠르지만, 스스로 만든 결과를 스스로 검증하기 때문에 오류를 놓칠 위험이 있다.
- Multi-Agent는 역할을 나누어 서로 다른 관점에서 작업을 수행하게 만드는 방식이다.
- 예를 들어 Planner는 범위를 정하고, Coder는 구현하고, Reviewer는 위험을 찾고, Tester는 실행 결과를 확인한다.
- Multi-Agent가 항상 더 좋은 것은 아니다. 작업이 작거나 기준이 명확하지 않다면 오히려 복잡도만 증가할 수 있다.
- Multi-Agent는 복잡한 작업을 안정적으로 나누고 검증해야 할 때 사용한다.

### Orchestration을 설계할 때 던질 질문
- 누가 작업을 계획하는가?
- 누가 실제 결과물을 만드는가?
- 누가 결과물을 검토하는가?
- 누가 테스트와 검증을 수행하는가?
- 누가 최종 결정을 내리는가?
- Agent 사이에서 어떤 정보를 넘길 것인가?
- 실패했을 때 어디로 되돌아갈 것인가?
- 사람은 어느 지점에서 개입할 것인가?

### 주요 역할

#### Orchestrator
- 입력: 사용자 요청, PRD, Spec, 현재 Phase, 이전 작업 기록
- 책임: 전체 작업 흐름을 조정하고 어떤 Agent에게 어떤 일을 맡길지 결정한다.
- 출력: 작업 순서, 역할 배정, 다음 행동 결정
- 금지: 모든 세부 구현을 직접 처리하려 하지 않는다.

#### Planner
- 입력: PRD, Spec, 현재 Phase, 프로젝트 구조
- 책임: 작업 범위, 구현 순서, 수정 대상 파일 후보, 검증 방법을 정한다.
- 출력: Plan, 작업 범위, 제외할 일, 예상 위험
- 금지: 직접 코드를 수정하지 않는다.

#### Researcher
- 입력: 기존 코드, 문서, 에러 로그, 외부 자료
- 책임: 구현 전에 필요한 맥락과 근거를 수집한다.
- 출력: 관련 파일 목록, 참고 문서, 조사 결과 요약
- 금지: 근거 없이 구현 방향을 확정하지 않는다.

#### Coder
- 입력: Plan, PRD, Spec, 현재 Phase
- 책임: 정해진 범위 안에서 실제 코드를 수정한다.
- 출력: 변경된 코드, 변경 이유, 영향 범위
- 금지: Plan에 없는 파일이나 기능을 임의로 확장하지 않는다.

#### Tester
- 입력: 변경된 코드, 테스트 명령어, Acceptance Criteria
- 책임: 테스트와 빌드를 실행하고 실패 원인을 분석한다.
- 출력: 테스트 결과, 실패 로그 요약, 재현 방법
- 금지: 실패를 단순히 무시하거나 성공처럼 보고하지 않는다.

#### Reviewer
- 입력: diff, Plan, PRD, Spec
- 책임: 코드 품질, 범위 초과, 회귀 위험, 누락된 테스트를 확인한다.
- 출력: 리뷰 코멘트, 위험 목록, 수정 제안
- 금지: 새 기능을 임의로 추가하지 않는다.

#### Verifier
- 입력: 구현 결과, 테스트 결과, Acceptance Criteria
- 책임: 이번 Phase가 실제로 완료되었는지 기준에 맞춰 판단한다.
- 출력: 완료 여부, 미충족 조건, 남은 작업
- 금지: Agent의 "완료" 선언만 보고 통과시키지 않는다.

#### Documenter
- 입력: 변경 결과, 테스트 결과, 결정 사항
- 책임: README, PROGRESS, TEST_RESULT, PHASE 같은 문서를 최신 상태로 만든다.
- 출력: 업데이트된 문서, 다음 세션을 위한 기록
- 금지: 실제 구현과 맞지 않는 기록을 남기지 않는다.

#### Decision Maker
- 입력: Plan, 구현 결과, 테스트 결과, 리뷰 결과, 검증 결과
- 책임: 통과, 재작업, 범위 축소, 사람 리뷰 요청 같은 다음 행동을 결정한다.
- 출력: 최종 결정, 다음 Phase, 남은 위험
- 금지: 불확실한 상태에서 완료로 처리하지 않는다.

### Orchestration 패턴

#### Sequential Pipeline
```text
Planner
-> Coder
-> Tester
-> Reviewer
-> Verifier
-> Documenter
-> Decision Maker
```

- 가장 기본적인 순차 처리 방식이다.
- 각 Agent가 이전 Agent의 산출물을 입력으로 받아 다음 단계로 넘긴다.
- 단계가 명확해서 학습과 문서화에 좋다.
- 단점은 앞 단계가 잘못되면 뒤 단계 전체가 영향을 받는다는 점이다.

#### Supervisor / Worker
```text
Supervisor
-> Worker A
-> Worker B
-> Worker C
-> Supervisor
```

- Supervisor가 작업을 나누고 Worker들이 세부 작업을 수행한다.
- 여러 독립 작업을 병렬로 처리할 때 유용하다.
- 예를 들어 문서 조사, 테스트 분석, 코드 구조 파악을 나누어 맡길 수 있다.
- Supervisor는 Worker 결과를 그대로 합치지 말고 충돌과 누락을 확인해야 한다.

#### Planner / Executor
```text
Planner
-> Executor
-> Planner or Verifier
```

- Planner는 계획만 세우고 Executor는 실행만 한다.
- 계획과 실행을 분리해 범위 초과를 줄일 수 있다.
- 구현 전 승인 절차가 필요한 프로젝트에 잘 맞는다.

#### Generator / Reviewer
```text
Generator
-> Reviewer
-> Generator
-> Verifier
```

- Generator가 초안을 만들고 Reviewer가 위험과 누락을 찾는다.
- 코드, 문서, 설계안, 테스트 케이스를 만들 때 모두 사용할 수 있다.
- Reviewer가 직접 고치기보다 문제를 명확히 지적하는 역할을 맡으면 책임 경계가 분명해진다.

#### Router Pattern
```text
User Request
-> Router
   -> Docs Agent
   -> Coding Agent
   -> Test Agent
   -> Research Agent
```

- 요청의 종류에 따라 적절한 Agent로 보내는 방식이다.
- "문서 정리", "버그 수정", "테스트 실패 분석"처럼 작업 유형이 명확할 때 유용하다.
- Router의 기준이 모호하면 잘못된 Agent에게 작업이 전달될 수 있다.

#### Blackboard Pattern
```text
Shared Board
<- Planner
<- Researcher
<- Coder
<- Tester
<- Reviewer
```

- 여러 Agent가 하나의 공유 작업판에 결과를 남기는 방식이다.
- 큰 문제를 여러 관점에서 점진적으로 해결할 때 유용하다.
- 공유 공간에는 사실, 결정, 열린 질문, 위험, 다음 행동을 구분해서 기록해야 한다.

#### Human-in-the-loop
```text
Agent Work
-> Human Review
-> Agent Work
-> Human Final Decision
```

- 중요한 결정 지점에 사람이 개입하는 방식이다.
- 요구사항 변경, 보안, 데이터 삭제, 대규모 구조 변경처럼 위험한 작업에서 필요하다.
- 사람은 모든 세부 작업을 직접 하지 않더라도 최종 기준과 책임을 가져야 한다.

### 상태 관리
- Shared Context
  - 모든 Agent가 공통으로 알아야 하는 프로젝트 규칙, PRD, Spec, 현재 Phase이다.
- Task State
  - 현재 작업이 조사, 계획, 구현, 테스트, 리뷰, 검증 중 어디에 있는지 나타낸다.
- Artifact
  - Agent가 만든 산출물이다. Plan, diff, 테스트 로그, 리뷰 코멘트, 문서 업데이트가 여기에 포함된다.
- Handoff
  - 한 Agent가 다음 Agent에게 넘기는 요약이다. 무엇을 했고, 무엇을 확인해야 하며, 무엇이 남았는지 포함한다.
- Checkpoint
  - 실패했을 때 되돌아갈 수 있는 기준점이다. commit, 문서 기록, 테스트 통과 상태가 될 수 있다.
- Memory
  - 장기적으로 유지해야 하는 학습과 결정 기록이다. 단순 대화 기록보다 문서화된 결정이 더 안정적이다.

### Handoff 템플릿
```md
## Handoff

### 완료한 일
- 

### 변경한 파일
- 

### 확인한 근거
- 

### 테스트 결과
- 

### 남은 위험
- 

### 다음 Agent가 해야 할 일
- 
```

### 검증 구조
- Self-check
  - Agent가 자신의 결과를 1차로 점검한다.
- Cross-review
  - 다른 역할의 Agent가 결과를 검토한다.
- Test-based verification
  - 테스트와 빌드처럼 실행 가능한 기준으로 확인한다.
- Acceptance Criteria verification
  - PRD와 Spec에 적힌 완료 기준을 하나씩 대조한다.
- Human final review
  - 최종 품질과 책임은 사람이 판단한다.

### 실패 패턴
- 역할 경계가 흐려진다.
  - Planner가 구현까지 하거나 Reviewer가 새 기능을 추가하면 책임이 섞인다.
- Agent끼리 서로의 오류를 강화한다.
  - 앞 Agent의 잘못된 가정을 뒤 Agent가 검증 없이 받아들이면 오류가 커진다.
- Context가 너무 커진다.
  - 모든 내용을 매번 넘기면 중요한 기준이 묻히고 비용이 증가한다.
- 최종 결정권이 사라진다.
  - 여러 Agent가 말했지만 아무도 완료 여부를 책임지지 않는 상태가 된다.
- 검증 없는 자동화가 된다.
  - 많은 Agent가 움직였지만 테스트, 리뷰, Acceptance Criteria 확인이 없다면 품질을 보장할 수 없다.
- 병렬 작업 결과가 충돌한다.
  - 여러 Agent가 같은 파일이나 같은 결정을 동시에 바꾸면 통합 비용이 커진다.

### 실전 예시: 게시판 CRUD Phase 분리
```text
User
-> Orchestrator: 이번 Phase는 게시글 목록 화면이다.
-> Planner: 목록 화면 구현 범위와 제외할 기능을 정한다.
-> Researcher: 기존 라우팅, 모델, 템플릿 구조를 조사한다.
-> Coder: 목록 화면에 필요한 코드만 구현한다.
-> Tester: 관련 테스트와 서버 실행을 확인한다.
-> Reviewer: 범위 초과, 구조 문제, 기존 기능 영향 여부를 검토한다.
-> Verifier: Acceptance Criteria 충족 여부를 확인한다.
-> Documenter: PROGRESS.md와 TEST_RESULT.md를 업데이트한다.
-> Decision Maker: 통과 또는 재작업을 결정한다.
```

### Multi-Agent Orchestration 체크리스트
- 이번 작업이 Multi-Agent를 쓸 만큼 복잡한가?
- 각 Agent의 입력, 책임, 출력, 금지사항이 명확한가?
- Agent 사이의 Handoff 형식이 정해져 있는가?
- 공유 Context와 개별 작업 Context를 구분했는가?
- 최종 결정을 내리는 역할이 정해져 있는가?
- 테스트와 Acceptance Criteria 검증이 포함되어 있는가?
- 사람이 개입해야 하는 위험 지점이 표시되어 있는가?
- 실패했을 때 어느 단계로 되돌아갈지 정했는가?

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
