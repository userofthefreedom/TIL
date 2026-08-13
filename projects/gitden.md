# 깃든 (Gitden)

## 한 줄 소개

- 주니어 개발자에게 맞는 GitHub Repository·Issue를 추천하고, 근거 기반 AI 코칭과 실제 Git 실행 흐름(Fork → Clone → 학습 → Commit/PR → 상태 추적)을 통해 첫 오픈소스 기여를 완주하도록 돕는 AI 웹 서비스. SSAFY 15기 공통 프로젝트 수상작.

## 기본 정보

| 항목 | 내용 |
| --- | --- |
| GitHub | 비공개 (SSAFY 15기 소스코드 반출·공개 금지 규정) |
| 기간 | 2026-07-13 ~ 2026-08-12 (약 1개월) |
| 형태 | 팀 프로젝트 (SSAFY 15기 공통 프로젝트, 6인 팀) — 수상작 |
| 역할 | 팀장 · 기획 겸 풀스택(AI Service 초기 구현, Backend 정책, Frontend UX 개편, 문서 정합화, dev 브랜치 통합 리드) |
| 팀 구성 | 오세진(본인) + 팀원 5인 (FE, BE, AI, Infra, UI/UX 역할 분담) |
| 주요 기술 | React 19, Vite, TypeScript / Java 21, Spring Boot / Python 3.12, FastAPI / PostgreSQL, Redis / Docker Compose, Jenkins, Blue-Green 배포 |

## 문제 정의

- 오픈소스 기여 초심자는 (1) 어떤 저장소·이슈가 자신 수준에 맞는지, (2) 찾은 뒤 Fork/Clone/Commit/PR을 어떤 순서로 진행해야 하는지, 두 가지 장벽을 동시에 겪는다.
- 인기 저장소의 `good first issue`는 노출되자마자 선점되는 구조라, "많이 추천"이 아니라 저장소 스타 상한·이슈 기간 창으로 후보 자체를 좁혀 "입문자가 실제로 잡을 수 있는" 이슈만 남기는 큐레이션을 핵심 원칙으로 삼았다.
- AI가 정답 코드를 대신 작성해 주는 대신, 근거(Evidence)와 질문·Hint로 사용자 스스로 판단하게 만들어 "학습이 남는 기여"를 지향했다.

![일반 AI, 깃든, 결과의 차이를 비교하는 랜딩 페이지 카드](../etc/gitden/home-compare.png)
*"코드 정답을 바로 준다"가 아니라 "질문·근거·검증을 함께"한다는 차별점을 랜딩 페이지에서부터 명시했다.*

## 주요 기능

- GitHub OAuth 로그인 및 온보딩 설문(6문항) 기반 프로필 확정
- 100점 만점 규칙 기반 스코어링으로 산출한 큐레이션 Issue/Repository 추천(상위 50건, Repo당 최대 2개로 다양화)
- Journey 실행 화면: Fork·Clone 가이드, Repo/Issue Brief, 질문형 AI Coach(대안 비교·Hint)
- Commit/PR 등록 보조(PR 설명 초안: What/Why/How tested/Fixes)
- PR 상태 Monitoring(진행 중엔 실시간에 가깝게, 이탈 후엔 배치 동기화)
- 성장 기록(XP·Level)과 "나의 기여" History
- Responsive Web + PWA(Lite 설치 지원), 모바일에서는 로컬 환경이 필요한 Clone·PR만 "PC에서 이어하기"로 안내

### 화면 미리보기

![GitHub OAuth 온보딩 화면, 요청 권한과 비공개 저장소는 건드리지 않는다는 안내](../etc/gitden/login.png)
*요청 권한과 "비공개 저장소는 건드리지 않는다"는 제한을 로그인 전에 먼저 보여준다.*

![Fork·Clone·Branch/Edit·Commit/Push·Pull Request·Review/Merge 6단계 Journey 스테퍼](../etc/gitden/journey-steps.png)
*Journey는 Fork부터 Review/Merge까지 6단계로 쪼개, 지금 어디에 있는지 항상 보여준다.*

![이슈 추천 점수 구성: 기술스택·난이도·이슈정보충실도 등 8개 항목 가중합](../etc/gitden/recommend-score.png)
*추천 점수를 숨기지 않고 8개 항목 가중합을 그대로 노출해, 왜 이 이슈가 추천됐는지 근거를 준다.*

![AI가 이슈를 쉬운 말로 요약하고 지금 문제·기대 결과·완료 기준으로 정리한 Brief 카드](../etc/gitden/ai-brief.png)
*Repo/Issue Brief는 원문 이슈를 "지금 문제 · 기대 결과 · 완료 기준"으로 구조화해 보여준다.*

![코치가 오답 이유를 근거와 함께 설명하는 피드백 박스](../etc/gitden/ai-coach-feedback.png)
*AI Coach는 정답만 알려주지 않고, 오답을 골랐을 때도 근거를 들어 다시 생각해보게 한다.*

![GitHub PR URL을 붙여넣어 리뷰·CI·머지 상태 추적을 등록하는 카드](../etc/gitden/pr-register.png)
*PR을 등록하면 그 이후 리뷰·CI·머지 상태를 계속 추적할 수 있다.*

![PR 등록됨 → 리뷰 대기 → 결과로 이어지는 진행 타임라인](../etc/gitden/pr-monitoring.png)
*진행 타임라인으로 지금 PR이 어느 단계인지 한눈에 보여준다.*

![PR이 머지되어 축하 메시지와 캐릭터 성장 단계가 표시되는 결과 화면](../etc/gitden/result-celebrate.png)
*첫 기여가 머지되면 캐릭터가 성장하는 축하 화면으로 마무리된다.*

![알 → 부화 → 병아리 → 닭으로 이어지는 성장 단계 트랙](../etc/gitden/my-contribution.png)
*"나의 기여" 페이지는 누적 기여를 알에서 닭까지 이어지는 성장 단계로 시각화한다.*

## 아키텍처

모노레포 구조로 `apps/{frontend, backend, ai-service}`와 `infra/`를 함께 관리했다.

![Blue/Green 배포와 Frontend/Backend/AI Service/Observability로 구성된 전체 아키텍처 다이어그램](../etc/gitden/architecture.png)
*Stage/Prod를 Blue-Green 페어로 분리하고, Edge(Traefik)가 트래픽을 무중단으로 전환한다. 실제 배포 포트 번호는 반출 규정에 따라 가렸다.*

- **Frontend (React 19 + Vite + TypeScript)**: 18개 화면, react-router-dom v7 + TanStack Query, 백엔드 OpenAPI 스펙에서 API 클라이언트를 자동 생성하는 파이프라인을 구성해 스펙과 프론트 호출부의 드리프트를 줄였다.
- **Backend (Java 21 + Spring Boot)**: 도메인 주도로 인증/추천/Journey/PR/AI연동/게이미피케이션 등 14개 도메인을 수직 분할. GitHub OAuth는 Access Token이 아닌 GitHub 사용자 ID를 기준으로 회원을 식별하도록 설계했고, Prometheus/Grafana/Loki/Tempo로 관측성을 갖췄다.
- **AI Service (Python 3.12 + FastAPI)**: Brief/Coach/Hint/추천 reasoning/PR 작성 보조를 담당하는 순수 텍스트 생성 계층. Fork/Clone/PR 같은 부작용(side effect)은 절대 직접 실행하지 않고 전부 Backend가 통제하도록 책임을 분리했다. 배포 LLM 제공자는 SSAFY 교육 인프라의 게이트웨이 하나를 사용했고, 장애 시 정적 Fallback으로 전환해 AI 없이도 핵심 여정이 완주되도록 설계했다.
- **Infra**: Docker Compose를 데이터/앱/Edge/Observability 스택으로 분리하고, Blue/Green 무중단 배포 파이프라인(헬스체크 → 트래픽 전환 → 라이브 smoke test, 실패 시 자동 롤백)을 Jenkins CI/CD와 연동했다.

## 기술 스택과 사용 이유

| 기술 | 사용한 이유 |
| --- | --- |
| React 19, Vite, TypeScript | 18개 화면의 라우팅과 추천/Journey/Monitoring 등 복잡한 상태 흐름을 타입 안정적으로 구성 |
| Java 21, Spring Boot, JPA | 14개 도메인 REST API, 인증, 스케줄링 등 서비스 핵심 로직 구현 |
| Python 3.12, FastAPI, Pydantic | AI 텍스트 생성(Brief/Coach/Hint/추천 reasoning)을 Backend와 분리된 계층으로 독립 운영 |
| PostgreSQL, Redis | 정규화된 도메인 데이터 저장과 세션·캐시·분산락 처리 |
| Docker Compose, Jenkins | 로컬 재현 가능한 개발 환경과 Blue/Green 기반 무중단 배포 자동화 |

## 프로젝트 규모

| 지표 | 값 |
| --- | --- |
| 총 커밋 수 | 1,303건 (팀 전체) |
| 개발 기간 | 약 1개월 (2026-07-13 ~ 2026-08-12) |
| 팀 인원 | 6명 |
| Backend REST 엔드포인트 | 68개 (14개 도메인, 테스트 클래스 214개) |
| Frontend 화면 | 18개 |
| 본인 커밋 비중 | 팀 내 약 31%(402/1,303건, 여러 커밋 계정 합산) — 팀 내 최다 기여자 |
| 본인 dev 브랜치 통합(merge) 비중 | 전체 merge 515건 중 약 29%(147건) |

## 주요 작업 흐름

| 시기 | 단계 | 작업 내용 |
| --- | --- | --- |
| 07-13 ~ 07-21 | 팀장·기획 | 팀 주제 선정 리드, MVP 범위 제안, 초기 기획서·요구사항정의서·IA·화면정의서 등 정본 문서 체계 수립 |
| 07-22 ~ 07-28 | AI Service 초기 구현 | Brief·Coach/Hint·Seed Extraction·추천 reasoning 라우터 구현, Backend 추천 스코어링 로직 구현 |
| 전 기간 반복 | 문서·스펙 정합화 | 기획서-구현 간 불일치를 주기적으로 재점검하고 DB 스키마·TODO를 정본 상태로 유지 |
| 08-06 ~ 08-09 | Frontend UX 개편 | Coach 학습 보조/문제풀이 패널 위계 정리, Tutorial 설명 보강, PR CTA 강조, 코멘트 모아보기 UI 등 |
| 전 기간 | Backend 정책 | PR 등록 시 Journey slot 해제, PR 머지 대기 저장소 보호 등 도메인 정책 구현 |
| 전 기간 | 통합 리드 | feature 브랜치를 dev로 병합하는 게이트키퍼 역할을 지속 수행 |

## 내가 작업한 것

- 팀장으로서 주제 선정과 MVP 범위 확정을 리드하고, 서비스기획서·요구사항정의서 등 정본 문서 체계를 만들었다.
- AI Service 초기 라우터(Brief/Coach·Hint/Seed Extraction/추천 reasoning)와 Backend 추천 스코어링 로직 구현에 관여했다.
- 개발 기간 내내 기획-구현 간 불일치를 점검·정리해 문서를 "정본" 상태로 유지하는 역할을 반복 수행했다.
- Frontend UX 개편(Coach/Tutorial 패널 위계, PR CTA, 코멘트 UI 등)과 Backend PR·Journey 관련 정책 구현에 참여했다.
- feature 브랜치의 dev 통합을 지속적으로 담당해 팀 전체 merge의 약 29%를 처리했다.
- 파일 경로 기준으로는 Backend > Frontend > AI Service > 문서 순으로 고르게 관여해, 특정 레이어에 국한되지 않는 풀스택 + PM성 기여를 했다.

## 인상 깊었던 기술적 설계

- **AI와 부작용(side effect)의 책임 분리**: AI Service는 텍스트만 생성하고 Fork/Clone/PR 같은 실제 GitHub 액션은 전혀 실행하지 않도록 아키텍처 레벨에서 강제했다. LLM이 이상 동작해도 실제 GitHub 조작으로 번지지 않는 구조적 안전장치였다.
- **Webhook 대신 이중 Polling으로 PR 상태 추적**: 외부 오픈소스 저장소에는 자체 GitHub App을 설치할 수 없어 Webhook을 1차 이벤트 원천으로 쓸 수 없었다. 화면 활성 중 짧은 주기 클라이언트 Polling과, 이탈 후 배치 동기화를 병행하는 이중 구조로 이 제약을 풀었다.
- **AI 호출 비용·신뢰성 관리**: 원본 데이터 변경 여부를 해시로 감지해 불필요한 LLM 호출을 막고, 장애 시 정적 Fallback으로 전환해 "AI 없이도 핵심 여정이 완주 가능"하도록 설계했다. 모든 AI 출력에는 근거 출처 태그를 붙여 추정과 사실을 구분했다.
- **추천 큐레이션 철학을 규칙으로 명문화**: "많이 보여주고 고르게 하기"가 아니라 수집 단계에서부터 후보를 좁혀 "입문자가 실제로 잡을 수 있는 것만 남기기"를 스코어링 규칙으로 못박았다.
- **문서-코드 동기화 자동화**: 아키텍처 문서를 소스 코드에서 자동 생성하고 pre-commit 훅과 CI 검증을 이중으로 걸어, 문서와 코드가 항상 같은 커밋에 있도록 강제했다.

## 배운 점

- 팀장으로서 기획-구현 간 정합성을 지속적으로 관리하는 것이 기능 구현 자체보다 더 많은 노력이 든다는 점, 그리고 정본 문서 체계를 초반에 세워두면 반복 점검 비용이 크게 줄어든다는 점.
- AI를 서비스에 통합할 때는 "무엇을 할 수 있는가"보다 "무엇을 하지 못하게 막을 것인가"(부작용 차단, Fallback, 근거 태깅)를 먼저 설계해야 신뢰할 수 있는 제품이 된다는 점.
- 외부 시스템(GitHub) 연동에서 이상적인 이벤트 기반 설계가 항상 가능한 것은 아니며, 제약을 인정하고 Polling 같은 대안을 조합하는 절충이 실무적으로 더 중요할 때가 많다는 점.
- 6인 팀에서 기획·AI·Backend·Frontend·통합을 넘나들며 작업하니, 한 레이어 전문성보다 전체 흐름을 조율하는 역할의 가치를 체감했다.

## 어려웠던 점과 해결

- 기획서와 실제 구현이 시간이 지나며 계속 벌어지는 문제 → 정본 문서 체계를 만들고 프로젝트 전 기간에 걸쳐 정기적으로 재점검하는 프로세스로 대응했다.
- PR 상태를 실시간처럼 보여주고 싶은데 외부 저장소에는 Webhook을 걸 수 없는 제약 → 화면 활성 중 클라이언트 Polling과 이탈 후 배치 동기화를 병행하는 이중 경로로 해결했다.
- AI 응답의 신뢰성과 호출 비용을 동시에 관리해야 하는 문제 → 원본 변경 감지(해시 비교)로 불필요한 호출을 막고, 장애 시 정적 Fallback으로 전환하는 구조를 도입했다.

## 다음 개선 방향

- 실사용자 테스트를 통해 온보딩·추천 단계에서의 이탈 지점을 구체적으로 수집
- GitHub App 설치가 가능한 저장소 범위를 넓혀 Webhook 기반 실시간성을 일부 보완
- Knowledge Graph 기반 추천, Orchestrator 고도화 등 대회 기간 내 미루었던 확장 계획 검토
- FE→BE→AI 전체 분산 추적(Observability) 계측을 앱 레벨까지 확장

## 비고

- 이 프로젝트는 SSAFY 15기 공통 프로젝트로 소스코드 저장소의 반출·공개가 규정상 금지되어 있어, 이 문서는 실제 코드 대신 문제 정의·아키텍처 개념·기술 스택·본인 역할과 배운 점을 중심으로 서술했다.
