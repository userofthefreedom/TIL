# AI Building Permit Manager (R.E.D.)

## 한 줄 소개

사용자가 지도에서 대상 필지를 고르고 건축 계획을 입력하면 공공데이터, 룰엔진, RAG, LLM 문서 생성을 결합해 건축 인허가 **사전진단** 결과를 보여 주는 웹 서비스의 프로토타입입니다. 팀 해커톤 출전을 준비하며 팀장으로서 사흘 동안 만들었고, 해커톤에서는 아쉽게 탈락했습니다.

## 기본 정보

| 항목 | 내용 |
| --- | --- |
| GitHub | https://github.com/userofthefreedom/R.E.D. |
| 기간 | 2026-05-27 ~ 2026-05-29 (3일) |
| 형태 | 팀 해커톤 준비용 프로토타입 |
| 결과 | 해커톤 탈락 |
| 역할 | 팀장, 백엔드 개발, 프로토타입 개발 (저장소 커밋 9개 전체 담당: IA·wireframe·mockup, 백엔드 모델/DB·API, 지도 API 연결) |
| 주요 기술 | Vue 3, TypeScript, Vite, Pinia, OpenLayers / Python, FastAPI, SQLAlchemy 2, Alembic / PostgreSQL + PostGIS, Redis, Qdrant / Docker Compose / VWorld API |
| 기준 자료 | README, 공개 커밋 기록 |

## 문제 정의

건축 인허가는 필지 정보, 용도지역·지구단위계획 같은 공간 규제, 법령·조례, 신청 서식이 복잡하게 얽혀 있어 사용자가 "이 땅에서 이 계획이 가능한지, 어떤 절차가 필요한지"를 미리 파악하기 어렵습니다. 이 프로젝트는 그 판단을 돕는 사전진단 흐름을 빠르게 검증하는 것을 목표로 했습니다.

## 판단 원칙

README에 먼저 못 박아 둔 설계 원칙입니다. AI를 쓰더라도 판단 근거가 추적 가능해야 한다는 점을 중심에 뒀습니다.

- 주소 문자열이 아니라 `PNU`, 필지 Geometry, Parcel Profile, Building Profile, Action JSON을 기준으로 판단
- 인허가 판단의 1차 골격은 LLM이 아니라 **룰엔진**이 만듦
- RAG는 법령, 조례, 지구단위계획, 별표, 서식 근거를 찾아 **Evidence Trace**로 연결
- LLM은 판단자가 아니라 체크리스트, 사전협의 질문, 보고서 문장 생성 보조자
- 모든 결과에 Rule Trace, Evidence Trace, 데이터 기준일자, 수집 시각을 남김
- 최종 인허가 가능 여부는 관할 행정청의 판단 대상이며, 서비스는 참고자료만 제공

## 구현 상태 (마지막 커밋 기준)

**실제 지도/위치 API 일부 연결 + DB 저장형 진단 세로 흐름 + 최소 룰엔진** 단계까지 진행했습니다.

- **Frontend**: OpenLayers 지도 클릭/선택 UX, 건축 계획 입력 상태를 Action JSON으로 생성, 룰 결과와 Rule Trace 표시. `/dashboard`, `/projects`, `/projects/new`, `/projects/demo/diagnosis` 주요 흐름이 실제 백엔드 API 호출
- **Backend**: FastAPI 라우터, SQLAlchemy 모델, repository/service 계층, Project·대상지 프로파일 CRUD, DiagnosisRun/Result 최소 흐름
- **위치 확인**: 지도 클릭 좌표 → 백엔드 Location Resolve API → VWorld 역지오코딩 우선, 실패 시 mock 후보로 fallback
- **Infra / Migration**: PostgreSQL/PostGIS, Redis, Qdrant Docker Compose 구성, Alembic 초기 스키마 적용 확인
- **AI / Data**: RAG·LLM·문서 생성 폴더 구조와 초기 룰·메타데이터만 준비 (BGE-M3 임베딩, BM25, reranker, structured output, DOCX/PDF 보고서는 예정 단계)

## 기술 스택과 사용 이유

| 기술 | 사용한 이유 |
| --- | --- |
| Vue 3 / TypeScript / Pinia | 4단계 진단 Wizard 화면과 건축 계획 상태 관리 |
| OpenLayers + VWorld | 지도 클릭 기반 필지 선택과 역지오코딩 |
| FastAPI / SQLAlchemy / Alembic | 진단 API, 도메인 모델, 스키마 마이그레이션 |
| PostgreSQL + PostGIS | 필지 Geometry 같은 공간 데이터 저장 |
| Qdrant | 법령·조례 근거 검색용 벡터 DB (RAG 예정) |
| YAML/JSON Rule Set + Python Rule Engine | LLM이 아닌 규칙으로 1차 판단 |
| Docker Compose | DB·캐시·벡터 DB 실행 환경 재현 |

## 주요 커밋 흐름

| 날짜 | 커밋 | 작업 내용 |
| --- | --- | --- |
| 2026-05-27 | `ca373f6`, `f2a4334` | 프로젝트 시작, 모노레포 구조 구성 |
| 2026-05-27 | `0f4cfa7` | IA, wireframe, gitignore 작성 |
| 2026-05-27 | `97fbd1f`, `2996d3c` | mockup v1.0, 문서 수정 |
| 2026-05-28 | `0508819` | prototype 구현 |
| 2026-05-29 | `25b8a9f` | 프론트 minor patch, backend model/db structure |
| 2026-05-29 | `7f79ef1` | 실제 지도 API 연결, v2.0 |
| 2026-05-29 | `44f2351` | 발표용 이미지 자료 추가 |

## 내가 작업한 것

- 팀장으로서 해커톤 아이디어를 하루 만에 IA → wireframe → mockup으로 전환
- 판단 원칙(룰엔진 우선, LLM은 보조, Trace 기록)을 README에 먼저 정의
- 백엔드 담당으로 FastAPI 라우터·SQLAlchemy 모델·DB 구조를 설계하고, 프론트 mockup과 진단 세로 흐름을 연결
- 지도 클릭 → VWorld 역지오코딩 → mock fallback 위치 확인 흐름 구현 (v2.0)
- Bash 기준 실행 준비, 인프라 실행, 테스트·검증 명령, 자주 나는 문제를 README에 정리

## 어려웠던 점과 해결

- **사흘 안에 끝까지 동작하는 흐름 만들기**: 전국 실데이터나 전체 법령 RAG까지 하려면 시간이 턱없이 부족했습니다. → MVP 1차 목표를 "샘플 필지와 샘플 법령 근거로 진단 플로우가 끝까지 도는 세로 흐름"으로 좁혔습니다.
- **외부 지도 API의 불안정성**: VWorld 지적도 geometry 권한·응답이 안정적이지 않았습니다. → 역지오코딩을 우선 시도하고 실패 시 mock 후보로 fallback해 시연 흐름이 끊기지 않게 했습니다.

## 배운 점

- 해커톤 프로토타입은 기획 산출물과 실행 가능한 mockup을 빠르게 연결하는 것이 중요하다는 점
- 법·규제처럼 틀리면 안 되는 영역에서는 LLM에 판단을 맡기지 않고, 룰엔진과 근거 추적을 먼저 설계해야 한다는 점
- 지도 API 같은 외부 API는 mock 단계와 실제 API 연결 단계의 차이를 명확히 관리해야 한다는 점
- 짧은 기간의 프로젝트일수록 README의 실행 순서와 문제 해결 가이드가 중요하다는 점

## 다음 개선 방향

README에 정리해 둔 다음 작업 목록입니다.

- Project CRUD에 인증 사용자 소유권 연결
- VWorld 지적도 geometry 안정화와 PNU 생성 로직 고도화
- 건축HUB, 토지이용계획, 공간규제 레이어 API 연결
- 최소 룰엔진을 YAML RuleLoader/RuleEvaluator 구조로 확장하고 실행 Trace를 DB에 저장
- 샘플 법령 chunk 기반 RAG 검색과 Evidence panel 실제 연결
- 체크리스트와 보고서 HTML/DOCX 생성
