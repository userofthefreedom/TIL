# AI Building Permit Manager

## 한 줄 소개

건축 인허가 업무를 AI와 데이터 파이프라인으로 보조하는 해커톤 대비 프로토타입입니다.

## 기본 정보

| 항목 | 내용 |
| --- | --- |
| GitHub | https://github.com/userofthefreedom/R.E.D. |
| 형태 | 해커톤 대비 프로토타입 |
| 역할 | 확인 필요 |
| 주요 기술 | Python, Vue, TypeScript, CSS, FastAPI, Docker |
| 기준 자료 | README, 공개 커밋 기록 |

## 문제 정의

건축 인허가 업무는 문서, 지도, 법규, 신청 정보가 복잡하게 얽혀 있어 사용자가 현재 상태와 필요한 절차를 파악하기 어렵습니다. 이 프로젝트는 해커톤을 대비해 건축 인허가 관리 흐름을 빠르게 검증하는 프로토타입으로 보입니다.

## 주요 기능

- 프론트엔드 mockup
- FastAPI 기반 백엔드 구조
- AI/Data Pipeline 영역 설계
- 지도 API 연동
- backend model/db structure 구성
- Docker 기반 인프라 실행
- 테스트와 검증, 실행 문제 해결 가이드

## 기술 스택과 사용 이유

| 기술 | 사용한 이유 |
| --- | --- |
| Vue / TypeScript | 빠른 프론트엔드 mockup과 화면 흐름 구현 |
| Python / FastAPI | API 서버와 데이터 파이프라인 구현 |
| Docker | 인프라 실행과 개발 환경 재현 |
| 지도 API | 위치 기반 인허가 정보 표현 |

## 주요 커밋 흐름

| 날짜 | 커밋 | 작업 내용 |
| --- | --- | --- |
| 2026-05-27 | `ca373f6` | 프로젝트 시작 |
| 2026-05-27 | `f2a4334` | 프로젝트 구조 구성 |
| 2026-05-27 | `0f4cfa7` | IA, wireframe, gitignore 작성 |
| 2026-05-27 | `97fbd1f` | mockup v1.0 |
| 2026-05-28 | `0508819` | prototype 구현 |
| 2026-05-29 | `25b8a9f` | 프론트 minor patch, backend model/db structure |
| 2026-05-29 | `7f79ef1` | real API(map), v2.0 |
| 2026-05-29 | `44f2351` | 이미지 자료 추가 |

## 내가 작업한 것

- 해커톤 대비 아이디어를 빠르게 IA, wireframe, mockup, prototype으로 전환
- 프론트 mockup과 백엔드 모델/DB 구조를 함께 검토
- 지도 API를 실제 API로 연결해 v2.0 수준까지 확장
- 실행 준비, 인프라, 테스트/검증, 자주 나는 문제를 README에 정리

## 배운 점

- 해커톤 프로토타입은 기획 산출물과 실행 가능한 mockup을 빠르게 연결하는 것이 중요하다는 점
- 지도 API 같은 외부 API는 mock 단계와 실제 API 연결 단계의 차이를 명확히 관리해야 한다는 점
- 짧은 기간의 프로젝트일수록 README의 실행 순서와 문제 해결 가이드가 중요하다는 점

## 다음 개선 방향

- 실제 인허가 데이터 모델과 API 명세 구체화
- AI/Data Pipeline이 어떤 입력을 받아 어떤 판단을 보조하는지 명확히 분리
- 사용자 유형별 화면 흐름과 권한 체계 보강
- 실제 사용 시나리오 기반 데모 데이터 추가
