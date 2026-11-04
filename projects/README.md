# Projects

GitHub에 공개한 프로젝트를 돌아보며, 어떤 문제를 풀려고 했고 어떤 기술을 사용했는지, 주요 커밋 흐름에서 무엇을 구현했는지 정리합니다.

## Quick Navigation

- [씬크루 (SceneCrew)](scenecrew.md)
- [깃든 (Gitden)](gitden.md)
- [Pickage](pickage.md)
- [FirstHome Navigator AI](FirstHome_Navigator_AI.md)
- [Green Commit](for_green_commit.md)
- [AI 쇼핑 어시스턴트](shopping_with_ai.md)
- [채용 공고 수집 + 자소서 초안 도구](job_find.md)
- [AI Building Permit Manager](R.E.D.md)
- [프로젝트 분석 템플릿](PROJECT_TEMPLATE.md)

## 작성 기준

- 프로젝트 README와 공개 GitHub 커밋·PR·Issue 기록을 기준으로 작성합니다.
- 저장소만으로 확정하기 어려운 내용은 `확인 필요`로 남깁니다.
- 단순 기능 목록보다 문제 정의, 구현 과정, 배운 점, 다음 개선 방향을 함께 기록합니다.
- 기술 스택은 GitHub language 통계와 README 내용을 함께 참고합니다.

## 프로젝트 요약

| 프로젝트 | 성격 | 주요 기술 | 프로젝트 상태 | 회고 정리도 |
| --- | --- | --- | --- | --- |
| 씬크루 (SceneCrew) | 콘서트 운영 팀의 계획·업무 배정·장비·안전·현장 보고를 AI 제안과 총괄 승인으로 조정하는 WEB/Android 서비스, SSAFY 15기 자율 프로젝트 (소스 비공개) | React 19/Capacitor Android, Spring Boot, FastAPI·LangGraph, PostgreSQL, WebSocket·SSE·FCM, Python 장비 수집기 | 진행 중 (2026-11-18 시연 예정) | 보강 |
| 깃든 (Gitden) | 오픈소스 첫 기여 온보딩 AI 서비스, SSAFY 15기 공통 프로젝트 (소스 비공개) | React 19, Java/Spring Boot, Python/FastAPI, PostgreSQL, Redis, Docker, Blue-Green | 완료 · **우수상** | 완성 |
| Pickage | npm 패키지를 생태계·기능·커뮤니티로 비교하고 PDF·에이전트용 Markdown으로 내보내는 서비스, SSAFY 15기 빅데이터 분산 트랙 공통 프로젝트 (소스 비공개) | Java 21/Spring Boot 4, React 19/Vite, Python(ONNX·Spark·DuckDB), FastAPI RAG, PostgreSQL, MinIO | 완료 (2026-09-28 발표) | 완성 |
| FirstHome Navigator AI | 청약 추천, 자금 계획, AI 코치 서비스, SSAFY 15기 관통 프로젝트 | Django, DRF, Vue, Pinia, Axios, PDF 분석, LLM | 완료 · **우수상** | 보강 |
| Green Commit | 깃든의 개인 MVP 프로토타입 → 오픈소스 기여 연습 저장소 (Apache 2.0) | React/TS, Java·Spring Boot, Python·FastAPI, Docker | 완료 (오픈소스 공개) | 보강 |
| AI 쇼핑 어시스턴트 | 상품 사진 기반 탐지·유사 상품 추천·챗봇, SSAFY AI 과정 과제 | Python, YOLOv8, CLIP, ChromaDB, LangChain, Gradio, Docker | 완료 | 보강 |
| 채용 공고 수집 + 자소서 초안 도구 | 3개 채용 사이트 수집·관련성 랭킹·AI 자소서 초안 개인 CLI 도구 | Python, sentence-transformers, Claude/OpenAI, DART API | 운영 중 (실사용) | 보강 |
| AI Building Permit Manager | 팀 해커톤 준비용 건축 인허가 사전진단 프로토타입 | Vue 3/TS, OpenLayers, FastAPI, PostgreSQL/PostGIS, Qdrant | 프로토타입 (해커톤 탈락) | 보강 |

### 상태 표기 기준

**프로젝트 상태**: 프로젝트 자체가 어디까지 진행됐는지 나타냅니다.

| 값 | 의미 |
| --- | --- |
| 완료 | 제출·발표·과제 마감 등 목표 시점까지 끝낸 프로젝트 |
| 진행 중 | 아직 개발 중이며 제출·발표 전인 프로젝트 |
| 운영 중 | 지금도 직접 사용하면서 개선하고 있는 프로젝트 |
| 프로토타입 | 아이디어 검증 단계까지만 진행하고 멈춘 프로젝트 |

**회고 정리도**: 이 TIL 회고 문서를 얼마나 다듬었는지 나타냅니다.

| 값 | 의미 |
| --- | --- |
| 초안 | README·커밋 메시지만 보고 빠르게 만든 문서. 추측성 문장이나 `확인 필요`가 남아 있음 |
| 보강 | 저장소 README·커밋·PR 기록과 본인 확인으로 사실관계를 검증한 문서. 설계 결정과 회고 문장은 더 다듬을 여지가 있음 |
| 완성 | 설계 의사결정, 트러블슈팅, 화면, 수치 근거까지 정리한 포트폴리오 수준의 문서 |

## 다음에 보완할 것

- 씬크루: 2026-11-18 시연 후 결과·최종 수치 반영, 실제 장비·Android 실기기 사진 추가

- 보강 단계 문서에 대표 화면 캡처 추가 (`etc/<프로젝트>/`)
- 프로젝트마다 가장 어려웠던 문제 1~2개를 깃든·Pickage처럼 "문제 → 판단 → 결과" 구조로 깊게 서술
- 프로젝트별 회고를 포트폴리오 문장으로 다듬기
