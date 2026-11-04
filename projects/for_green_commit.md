# Green Commit

## 한 줄 소개

오픈소스 기여가 처음인 개발자에게 적절한 repository와 issue를 안내하고 fork부터 PR까지 기여 흐름을 학습시키는 서비스의 **개인 MVP 프로토타입**입니다. 팀 프로젝트 [깃든 (Gitden)](gitden.md)의 아이디어를 먼저 혼자 구현해 검증했고, 이후 Apache 2.0 오픈소스로 전환해 깃든 팀이 실제 PR 흐름을 테스트하는 연습 저장소로 사용했습니다.

## 기본 정보

| 항목 | 내용 |
| --- | --- |
| GitHub | https://github.com/userofthefreedom/for_green_commit |
| 기간 | MVP 2026-07-18 ~ 07-20 / 오픈소스 전환 07-30 / 연습 저장소 운영 08-06 ~ 08-13 |
| 형태 | 깃든(2026-07-13 ~ 08-12)의 개인 프로토타입 → 오픈소스 기여 연습 저장소 |
| 라이선스 | Apache License 2.0 |
| 역할 | MVP 단독 개발(Phase 0~6), 문서화, 오픈소스 전환, 연습용 issue 설계와 PR 리뷰·병합 |
| 커밋 | 전체 76개 중 본인 계정 52개. 나머지는 깃든 팀원들이 연습 저장소에서 올린 PR |
| 주요 기술 | React, Vite, TypeScript / Java 21, Spring Boot, Spring Data JPA, Spring Batch / Python 3.12, FastAPI, Pydantic / PostgreSQL, pgvector, Redis, Neo4j, MinIO, Docker Compose |
| 기준 자료 | README, CONTRIBUTING.md, ARCHITECTURE.md, 공개 커밋·PR·Issue 기록 |

## 문제 정의

초보 개발자나 새 팀원이 GitHub 협업에 참여할 때 OAuth 설정, fork/clone, 브랜치, PR 등록 같은 흐름에서 막히기 쉽습니다. Green Commit은 이 과정을 화면과 자동화로 안내하는 MVP로 시작했습니다.

깃든 팀 프로젝트가 진행되는 동안 이 아이디어가 실제로 끝까지 동작하는지 혼자 먼저 확인하는 것이 1차 목적이었습니다. 이후에는 저장소 자체를 오픈소스로 전환해 "처음 기여하는 사람"이 실제로 fork → issue 선택 → PR까지 연습할 수 있는 `contribution-lab`을 제공하는 방향으로 확장했습니다.

## 주요 기능

- GitHub OAuth 로그인 게이트
- 18개 화면 기반 프론트엔드 라우팅
- 온보딩 및 튜토리얼 흐름
- 개인화된 repository/issue 추천 카드와 Journey overview
- PR 상태 추적(open/merged/closed)
- 실제 자동화 wiring과 question-coach(AI 코칭) 연동
- PR 등록과 MVP E2E 흐름
- `contribution-lab/`: 초보자용 연습 이슈(공백 정규화, 문자열 검사 함수, 용어집 보강 등) 제공
- RFP, IA, 세부 문서, 추적성 보강

## 오픈소스 전환 작업 (2026-07-30)

MVP 완성 이후, 외부 기여자를 받을 수 있도록 저장소 구조와 문서를 대대적으로 정비했습니다.

- `CONTRIBUTING.md`: fork/clone → upstream 연결 → `<type>/<issue-number>-<description>` 브랜치 → 범위 제한 수정 → 테스트(`npm test` / `./gradlew test` / `python -m pytest`) → conventional commit → PR 순서의 기여 워크플로 문서화
- `CODE_OF_CONDUCT.md`, `SECURITY.md` 추가: 커뮤니티 행동 강령과 취약점 보고 절차 정비
- `ARCHITECTURE.md` 추가: `app/frontend`, `app/backend`, `app/ai`, `app/infra`, `contribution-lab` 구조를 외부 공개용으로 문서화
- Issue/PR 템플릿 추가, `good first issue` 라벨을 단 초보자용 이슈 등록
- OAuth secret 예시를 안전한 placeholder로 교체, 내부 스펙/개발 단계(Phase) 언급과 설계 산출물 등 비공개성 정보 제거
- Python 캐시 파일 제외, Flyway migration 불변성 보존 등 오픈소스 저장소로서의 위생 작업
- 위 작업들은 `chore/open-source-conversion` 브랜치로 모아 PR #1로 병합

## 깃든 팀의 기여 연습 저장소로 운영 (2026-08-06 ~ 08-13)

오픈소스로 전환한 뒤에는 깃든 팀원들이 이 저장소에서 실제 fork → branch → PR → 리뷰 → merge 흐름을 연습하고, 깃든의 PR 상태 추적 기능을 실제 PR로 검증하는 용도로 사용했습니다.

- `good first issue` / `beginner` 라벨이 붙은 연습 issue 14개 등록 (용어집 Rebase·Conflict·Squash Merge 설명, `isBlank()`·`capitalizeFirstLetter()`·`reverseWords()` 함수, `countWords` 엣지 케이스 테스트, `contributors.json`에 아이디 추가, README FAQ 등)
- issue를 기준으로 PR #5 ~ #45가 올라왔고(팀원 외 사용자의 PR 포함), 팀원들이 서로의 PR을 병합
- "#15 상태 추적 테스트 1~6차"처럼 README 마침표를 추가·제거하는 작은 PR을 반복으로 올려, PR이 열리고 병합되는 상태 변화를 깃든이 제대로 따라가는지 확인
- 마지막으로 contribution-lab FAQ를 추가(#45)하고 마무리

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

깃든 본 서비스와 같은 계열(React / Spring Boot / FastAPI / PostgreSQL·Redis)로 구성해, 프로토타입에서 확인한 흐름을 팀 프로젝트로 옮기기 쉽게 했습니다.

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
| 2026-07-30 | `5c766ca` ~ `f4dcb6e` | secret placeholder 교체, README 재작성, 라이선스·CONTRIBUTING·CODE_OF_CONDUCT·SECURITY·ARCHITECTURE·템플릿·contribution-lab 추가, 내부 정보 제거 |
| 2026-07-30 | `b99dec8` | PR #1(`chore/open-source-conversion`) 병합, 오픈소스 전환 완료 |
| 2026-08-06 | `6601386`, `c112bcb` | 연습 issue 기반 `isBlank()` 추가, 공백 정규화 테스트 보강 (PR #16, #22) |
| 2026-08-07 ~ 08-10 | PR #23 ~ #32 | 팀원들의 contributors 등록, 용어집 Conflict·Squash Merge, `capitalizeFirstLetter()` PR과 상호 리뷰·병합 |
| 2026-08-11 ~ 08-13 | PR #33 ~ #44 | `countWords` 엣지 케이스, "#15 상태 추적 테스트" 반복 PR |
| 2026-08-13 | `967b229` | contribution-lab FAQ 추가 (PR #45) |

## 내가 작업한 것

- 깃든 아이디어를 Phase 0~6으로 나눠 하루 만에 MVP E2E(OAuth → 온보딩 → 추천 → 자동화 → PR 등록)까지 단독 구현
- RFP, IA, plan/detail 문서 v1.2 작성으로 기능과 요구사항 추적성 정리
- 오픈소스 전환: 라이선스, 기여 가이드, 행동 강령, 보안 정책, 공개용 아키텍처 문서, Issue/PR 템플릿 작성과 비공개 정보 제거
- 난이도별 연습 issue 설계와 등록, 연습 저장소 운영과 PR 병합

## 어려웠던 점과 해결

- **비공개 정보가 섞인 저장소 공개**: MVP 단계 문서에는 내부 스펙·Phase 기록·OAuth secret 예시가 섞여 있었습니다. → 기능을 건드리기 전에 정보 제거와 placeholder 교체를 먼저 별도 커밋으로 처리하고, 이미 적용된 Flyway migration은 수정하지 않도록 보존했습니다.
- **PR 상태 추적 기능을 검증할 실제 PR이 필요함**: 실제 외부 저장소에 테스트 PR을 반복해 올릴 수는 없었습니다. → 직접 관리하는 연습 저장소에서 의미가 작은 PR(마침표 추가·제거)을 반복으로 열고 병합해 상태 변화를 확인했습니다.

## 배운 점

- 팀 개발 도구는 단순 기능보다 사용자가 막히는 순서를 따라가는 온보딩 설계가 중요하다는 점
- 팀 프로젝트 초반에 혼자 빠르게 프로토타입을 만들어 보면, 아이디어가 끝까지 동작하는지와 어디가 어려운지를 일찍 확인할 수 있다는 점
- Phase 단위로 API scaffold, 인증, 온보딩, 자동화, E2E를 쌓으면 진행 상황을 추적하기 쉽다는 점
- 오픈소스로 전환할 때는 기능 추가보다 "내부 전용 정보 제거 + 외부 기여자를 위한 문서/정책 정비"가 먼저라는 점
- `good first issue`처럼 난이도가 명확한 라벨과 `contribution-lab` 같은 연습 공간을 함께 제공하면 첫 기여 장벽을 크게 낮출 수 있다는 점

## 다음 개선 방향

- 남아 있는 open 연습 issue(`truncate`, `is_palindrome`, `count_vowels` 등)를 난이도별 학습 경로로 정리
- GitHub OAuth, fork/clone, PR 등록 실패 케이스별 안내 강화
- 자동화 흐름을 CI나 GitHub App 수준으로 확장할 수 있는지 검토
- 프로토타입과 깃든 본 서비스의 설계 차이(무엇을 유지하고 무엇을 바꿨는지)를 비교 정리
