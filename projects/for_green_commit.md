# Green Commit

## 한 줄 소개

오픈소스 기여가 처음인 개발자에게 적절한 repository와 issue를 안내하고, fork부터 PR까지 기여 흐름을 학습시키는 팀 프로젝트입니다. 실제 서비스와 분리된 교육용 프로토타입이며, 팀 프로젝트 진행을 위해 오픈소스(Apache 2.0)로 전환했습니다.

## 기본 정보

| 항목 | 내용 |
| --- | --- |
| GitHub | https://github.com/userofthefreedom/for_green_commit |
| 형태 | 팀 개발 프로토타입 → 오픈소스 전환 (contribution-lab 운영) |
| 라이선스 | Apache License 2.0 |
| 역할 | 확인 필요 |
| 주요 기술 | React, Vite, TypeScript / Java 21, Spring Boot, Spring Data JPA, Spring Batch / Python 3.12, FastAPI, Pydantic / PostgreSQL, pgvector, Redis, Neo4j, MinIO, Docker Compose |
| 기준 자료 | README, CONTRIBUTING.md, ARCHITECTURE.md, 공개 커밋 기록, Issues |

## 문제 정의

초보 개발자나 새 팀원이 GitHub 협업에 참여할 때 OAuth 설정, fork/clone, 브랜치, PR 등록 같은 흐름에서 막히기 쉽습니다. Green Commit은 이 과정을 화면과 자동화로 안내하는 MVP로 시작했고, 이후 프로젝트 자체를 오픈소스로 전환해 "처음 기여하는 사람"이 실제로 fork → issue 선택 → PR까지 연습할 수 있는 `contribution-lab`을 함께 제공하는 방향으로 확장했습니다.

## 주요 기능

- GitHub OAuth 로그인 게이트
- 18개 화면 기반 프론트엔드 라우팅
- 온보딩 및 튜토리얼 흐름
- 개인화된 repository/issue 추천 카드와 Journey overview
- PR 상태 추적(open/merged/closed)
- 실제 자동화 wiring과 question-coach(AI 코칭) 연동
- PR 등록과 MVP E2E 흐름
- `contribution-lab/` — 초보자용 연습 이슈(공백 정규화, 문자열 검사 함수, 용어집 보강 등) 제공
- RFP, IA, 세부 문서, 추적성 보강

## 오픈소스 전환 작업 (2026-07-30)

MVP 완성 이후, 외부 기여자를 받을 수 있도록 저장소 구조와 문서를 대대적으로 정비했습니다.

- `CONTRIBUTING.md` — fork/clone → upstream 연결 → `<type>/<issue-number>-<description>` 브랜치 → 범위 제한 수정 → 테스트(`npm test` / `./gradlew test` / `python -m pytest`) → conventional commit → PR 순서의 기여 워크플로 문서화
- `CODE_OF_CONDUCT.md`, `SECURITY.md` 추가 — 커뮤니티 행동 강령과 취약점 보고 절차 정비
- `ARCHITECTURE.md` 추가 — `app/frontend`, `app/backend`, `app/ai`, `app/infra`, `contribution-lab` 구조를 외부 공개용으로 문서화
- Issue/PR 템플릿 추가, `good first issue` 라벨을 단 초보자용 이슈 3건 등록
- OAuth secret 예시를 안전한 placeholder로 교체, 내부 스펙/개발 단계(Phase) 언급과 설계 산출물 등 비공개성 정보 제거
- Python 캐시 파일 제외, Flyway migration 불변성 보존 등 오픈소스 저장소로서의 위생 작업
- 위 작업들은 `chore/open-source-conversion` 브랜치로 모아 PR #1로 병합

## 기술 스택과 사용 이유

| 기술 | 사용한 이유 |
| --- | --- |
| React, Vite, TypeScript | 18개 화면 라우팅과 온보딩/추천 카드 등 프론트엔드 상태 흐름을 안정적으로 구성 |
| Java 21, Spring Boot, Spring Data JPA, Spring Batch | 백엔드 API, 도메인 모델, 배치성 자동화 처리 |
| Python 3.12, FastAPI, Pydantic | AI 코칭(question-coach) 서비스와 추천 로직 |
| PostgreSQL, pgvector | repository/issue 추천을 위한 벡터 검색 기반 저장소 |
| Redis | 세션/캐시 처리 |
| Neo4j | repository·issue·contributor 간 관계 데이터 모델링 |
| MinIO | 오브젝트 스토리지 |
| Docker Compose | 프론트/백엔드/AI/인프라를 로컬에서 재현 가능한 환경으로 구성 |

## 주요 커밋 흐름

| 날짜 | 커밋 | 작업 내용 |
| --- | --- | --- |
| 2026-07-18 | `49c50ba` | monorepo scaffold 구성 (Phase 0) |
| 2026-07-18 | `a43c97e` | Phase 1: MVP entity/API scaffold, 18-screen routing |
| 2026-07-18 | `0112b95` | Phase 2: GitHub OAuth login gate |
| 2026-07-18 | `537b975` | Phase 3: onboarding과 tutorial branch 연결 |
| 2026-07-18 | `c25935e` | Phase 4: catalog/recommendation cards, Journey overview |
| 2026-07-18 | `4773f38` | Phase 5: automation wiring, question-coach port |
| 2026-07-18 | `2a978e0` | Phase 6: real PR registration, MVP E2E complete |
| 2026-07-19 | `e91bb73` | fork/clone 병합, time counting 등 세부 수정 |
| 2026-07-19 | `9865e71`, `bca70f5` | root README, setup, RFP, IA 문서 보강 |
| 2026-07-20 | `d9b2589`, `34a1de3` | plan/detail documents v1.2 정리 |
| 2026-07-30 | `5c766ca` | OAuth secret 예시를 안전한 placeholder로 교체 |
| 2026-07-30 | `4520632` | README를 오픈소스 프로토타입 소개로 재작성 |
| 2026-07-30 | `29988ee` | Apache 2.0 라이선스 추가 |
| 2026-07-30 | `94672d5` | CONTRIBUTING.md 추가 |
| 2026-07-30 | `34ce0b4` | CODE_OF_CONDUCT, SECURITY 정책 추가 |
| 2026-07-30 | `7ab5035` | 공개용 ARCHITECTURE 문서 추가 |
| 2026-07-30 | `6eb2634` | Issue/PR 템플릿 추가 |
| 2026-07-30 | `388f474` | 초보자용 contribution-lab 추가 |
| 2026-07-30 | `bf3d3a2`, `7709b3b`, `f4dcb6e` | 내부 Phase/스펙 참조 등 비공개 정보 제거 |
| 2026-07-30 | `b99dec8` | PR #1(`chore/open-source-conversion`) 병합, 오픈소스 전환 완료 |

## 내가 작업한 것

- 확인 필요: 실제 담당 영역을 추가로 적어야 합니다.
- MVP 단계에서는 Phase 분할, GitHub OAuth, 자동화, PR 등록, 문서 추적성 정리에 집중했고, 오픈소스 전환 단계에서는 기여 가이드/정책 문서와 초보자용 이슈 정리에 집중한 프로젝트입니다.

## 배운 점

- 팀 개발 도구는 단순 기능보다 사용자가 막히는 순서를 따라가는 온보딩 설계가 중요하다는 점
- Phase 단위로 API scaffold, 인증, 온보딩, 자동화, E2E를 쌓으면 진행 상황을 추적하기 쉽다는 점
- RFP, IA, README, plan 문서를 함께 관리하면 기능과 요구사항의 연결이 선명해진다는 점
- 오픈소스로 전환할 때는 기능 추가보다 "내부 전용 정보 제거 + 외부 기여자를 위한 문서/정책 정비"가 먼저라는 점 (CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, ARCHITECTURE, 라이선스, secret placeholder 교체 등)
- `good first issue`처럼 난이도가 명확한 라벨과 `contribution-lab` 같은 연습 공간을 함께 제공하면 첫 기여 장벽을 크게 낮출 수 있다는 점

## 다음 개선 방향

- 실제 사용자 테스트를 통해 온보딩 흐름에서 이탈 지점 수집
- GitHub OAuth, fork/clone, PR 등록 실패 케이스별 안내 강화
- 자동화 흐름을 CI나 GitHub App 수준으로 확장할 수 있는지 검토
- 오픈소스 전환 이후 실제 외부 기여자의 PR/issue 대응 흐름과 리뷰 기준 정리
- `contribution-lab`의 연습 이슈를 난이도별로 확장하고, 완료 후 다음 이슈로 이어지는 학습 경로 설계
