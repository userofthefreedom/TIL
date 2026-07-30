# Green Commit

## 한 줄 소개

팀원이 GitHub 프로젝트에 더 쉽게 온보딩하고 기여할 수 있도록, OAuth 로그인, 튜토리얼, 추천 카드, 자동화 흐름을 실험한 팀 개발 프로토타입입니다.

## 기본 정보

| 항목 | 내용 |
| --- | --- |
| GitHub | https://github.com/userofthefreedom/for_green_commit |
| 형태 | 팀 개발을 위한 프로토타입 |
| 역할 | 확인 필요 |
| 주요 기술 | TypeScript, Java, CSS, Python, Docker, Shell |
| 기준 자료 | README, 공개 커밋 기록 |

## 문제 정의

초보 개발자나 새 팀원이 GitHub 협업에 참여할 때 OAuth 설정, fork/clone, 브랜치, PR 등록 같은 흐름에서 막히기 쉽습니다. 이 프로젝트는 팀 개발 참여 과정을 화면과 자동화로 안내하는 MVP를 만드는 데 초점을 둔 것으로 보입니다.

## 주요 기능

- GitHub OAuth 로그인 게이트
- 18개 화면 기반 프론트엔드 라우팅
- 온보딩 및 튜토리얼 흐름
- 카탈로그/추천 카드와 Journey overview
- 실제 자동화 wiring
- PR 등록과 MVP E2E 흐름
- RFP, IA, 세부 문서, 추적성 보강

## 기술 스택과 사용 이유

| 기술 | 사용한 이유 |
| --- | --- |
| TypeScript | 프론트엔드 화면과 상태 흐름을 안정적으로 구성 |
| Java | 백엔드 API 또는 서버 로직 구현에 사용된 것으로 추정 |
| Python | 보조 스크립트 또는 문서/자동화 작업에 사용된 것으로 추정 |
| Docker | 실행 환경 고정과 팀 개발 환경 재현 |

## 주요 커밋 흐름

| 날짜 | 커밋 | 작업 내용 |
| --- | --- | --- |
| 2026-07-18 | `49c50ba` | monorepo scaffold 구성 |
| 2026-07-18 | `a43c97e` | Phase 1: MVP entity/API scaffold, 18-screen routing |
| 2026-07-18 | `0112b95` | Phase 2: GitHub OAuth login gate |
| 2026-07-18 | `537b975` | Phase 3: onboarding과 tutorial branch 연결 |
| 2026-07-18 | `c25935e` | Phase 4: catalog/recommendation cards, Journey overview |
| 2026-07-18 | `4773f38` | Phase 5: automation wiring, question-coach port |
| 2026-07-18 | `2a978e0` | Phase 6: real PR registration, MVP E2E complete |
| 2026-07-19 | `e91bb73` | fork/clone 병합, time counting 등 세부 수정 |
| 2026-07-19 | `9865e71`, `bca70f5` | root README, setup, RFP, IA 문서 보강 |
| 2026-07-20 | `d9b2589`, `34a1de3` | plan/detail documents v1.2 정리 |

## 내가 작업한 것

- 확인 필요: 실제 담당 영역을 추가로 적어야 합니다.
- 커밋 흐름상 MVP 단계 분할, GitHub OAuth, 자동화, PR 등록, 문서 추적성 정리에 집중한 프로젝트입니다.

## 배운 점

- 팀 개발 도구는 단순 기능보다 사용자가 막히는 순서를 따라가는 온보딩 설계가 중요하다는 점
- Phase 단위로 API scaffold, 인증, 온보딩, 자동화, E2E를 쌓으면 진행 상황을 추적하기 쉽다는 점
- RFP, IA, README, plan 문서를 함께 관리하면 기능과 요구사항의 연결이 선명해진다는 점

## 다음 개선 방향

- 실제 사용자 테스트를 통해 온보딩 흐름에서 이탈 지점 수집
- GitHub OAuth, fork/clone, PR 등록 실패 케이스별 안내 강화
- 자동화 흐름을 CI나 GitHub App 수준으로 확장할 수 있는지 검토
