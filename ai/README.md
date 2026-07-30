# AI Study Notes

AI 학습에 필요한 Python, 수학 기초, 머신러닝, 딥러닝, NLP, LLM, 컴퓨터 비전, RAG 흐름을 정리합니다.

## Quick Navigation

- [핵심 흐름](#핵심-흐름)
- [학습 환경](#학습-환경)
- [AI를 위한 Python](#ai를-위한-python)
- [AI 수학 기초](#ai-수학-기초)
- [머신러닝 기초](#머신러닝-기초)
- [선형 회귀와 로지스틱 회귀](#선형-회귀와-로지스틱-회귀)
- [EDA와 Scikit-learn](#eda와-scikit-learn)
- [딥러닝과 PyTorch](#딥러닝과-pytorch)
- [NLP 기초](#nlp-기초)
- [LLM과 텍스트 파운데이션 모델](#llm과-텍스트-파운데이션-모델)
- [AI를 이용한 데이터 생성](#ai를-이용한-데이터-생성)
- [컴퓨터 비전](#컴퓨터-비전)
- [이미지 파운데이션 모델과 멀티모달](#이미지-파운데이션-모델과-멀티모달)
- [LangChain과 RAG](#langchain과-rag)
- [유의점과 교훈](#유의점과-교훈)

## 핵심 흐름
- AI, ML, Deep Learning의 관계
  - AI(Artificial Intelligence)
    - 사람이 지능적으로 수행하는 인지, 학습, 추론, 계획, 행동을 컴퓨터로 구현하려는 넓은 영역이다.
  - ML(Machine Learning)
    - AI의 한 분야로, 사람이 규칙을 직접 모두 작성하지 않고 데이터에서 패턴과 규칙을 학습한다.
  - Deep Learning
    - 머신러닝 중에서도 인공신경망을 여러 층으로 깊게 쌓아 특징 추출과 예측을 함께 학습하는 방식이다.
  - Foundation Model
    - 대규모 데이터로 사전학습한 뒤, 여러 하위 작업에 zero-shot, few-shot, fine-tuning 등으로 빠르게 적응하는 범용 모델이다.
- AI 학습의 큰 흐름
  - 데이터 준비
    - feature와 label을 구분하고, 학습에 필요한 형태로 데이터를 정리한다.
  - 모델 선택
    - 회귀, 분류, 생성, 검색, 탐지 등 문제 유형에 맞는 모델 구조를 선택한다.
  - 학습
    - 예측값과 정답의 차이를 손실 함수로 계산하고, 손실을 줄이는 방향으로 파라미터를 갱신한다.
  - 평가
    - 학습 데이터가 아니라 검증/테스트 데이터에서 일반화 성능을 확인한다.
  - 활용
    - 예측, 분류, 생성, 검색 증강 생성(RAG), 멀티모달 처리 등 실제 작업에 연결한다.

## 학습 환경
- Python / Jupyter Lab
  - Jupyter Notebook은 코드, 출력, 설명을 하나의 문서에서 함께 관리할 수 있어 AI 실습에 적합하다.
  - 셀 단위 실행이 가능하므로 데이터 확인, 모델 학습, 시각화 결과를 단계별로 점검하기 좋다.
  - 셀 실행 순서가 꼬이면 결과가 달라질 수 있으므로 위에서 아래로 다시 실행해 상태를 정리하는 습관이 필요하다.
- WSL / Docker
  - WSL은 Windows에서 Linux 기반 개발 환경을 쓰기 위한 기반이다.
  - Docker는 실행 환경을 이미지와 컨테이너로 고정해, 의존성 차이로 인한 문제를 줄인다.
  - JupyterLab을 Docker에서 띄우면 Python 버전, 패키지, 실행 환경을 더 일관되게 맞출 수 있다.
- 의존성 파일
  - `requirements.txt`
    - Python 패키지 목록을 기록하는 파일이다.
  - `Dockerfile`
    - 어떤 기반 이미지에서 어떤 패키지를 설치하고 어떤 명령으로 실행할지 정의한다.
  - `docker-compose.yml`
    - 컨테이너 실행 옵션, 포트, 볼륨, 서비스 구성을 묶어서 관리한다.
- 환경 설계에서 배운 점
  - PyTorch, CUDA, JupyterLab, HuggingFace, LangChain, Chroma 같은 의존성이 많아질수록 로컬 환경 차이가 커진다.
  - Dockerfile은 베이스 이미지, 시스템 패키지, Python 패키지, 실행 명령을 고정한다.
  - docker-compose는 포트, volume, GPU 사용, 환경 변수를 한 번에 관리한다.
  - `verify_env.sh`처럼 환경 검증 스크립트를 두면 GPU 인식, 주요 패키지 버전, JupyterLab 설치 여부를 빠르게 확인할 수 있다.
- 고급 학습 환경 의존성
  - `bitsandbytes`
    - 양자화와 메모리 효율 학습에 사용한다.
  - `Unsloth`
    - LLM fine-tuning을 더 빠르고 가볍게 하기 위한 도구이다.
  - `PEFT`
    - LoRA처럼 일부 파라미터만 학습하는 효율적 fine-tuning 방식에 사용한다.
  - `TRL`
    - SFT, preference tuning처럼 LLM 학습 후반부 정렬/튜닝 실습에 연결된다.
  - `hf_transfer`
    - HuggingFace 모델/데이터 다운로드 속도를 높이는 데 사용한다.

## AI를 위한 Python
- 기본 문법
  - 변수는 값을 가리키는 이름이다.
  - 조건문은 상황에 따라 다른 흐름을 선택한다.
  - 반복문은 같은 처리를 여러 번 수행한다.
  - 함수는 반복되는 로직을 이름 붙여 재사용한다.
  - 클래스는 데이터와 동작을 묶어 객체 단위로 관리한다.
- 컬렉션과 반복 도구
  - `list`
    - 순서가 있는 여러 값을 저장한다.
  - `dict`
    - key와 value를 묶어 저장한다.
  - `set`
    - 중복 없는 값을 다룬다.
  - `tuple`
    - 변경하지 않을 값 묶음에 적합하다.
  - `Counter`
    - 값의 빈도를 빠르게 센다.
  - `defaultdict`
    - key가 없을 때 기본값을 자동으로 만들어준다.
  - `itertools`
    - 순열, 조합, 곱집합, 누적합 같은 반복 패턴을 다룬다.
- AI 실습에서 자주 쓰는 라이브러리
  - NumPy
    - 수치 계산과 배열 연산의 기반이다.
    - 벡터, 행렬, 브로드캐스팅, 난수, 통계 계산을 빠르게 처리한다.
  - Pandas
    - 표 형태의 데이터를 `Series`와 `DataFrame`으로 다룬다.
    - 데이터 확인, 결측치 처리, 컬럼 선택, 그룹화, 병합에 자주 사용한다.
  - Matplotlib / Seaborn
    - 데이터 분포, 관계, 모델 결과를 시각화한다.
    - 회귀선, 산점도, 히스토그램, heatmap, pairplot 등 EDA에서 많이 사용한다.
- 예시: NumPy 배열과 행렬 곱
  - AI 모델의 입력은 대부분 숫자 배열이다.
  - 행렬 곱은 feature를 다른 표현 공간으로 바꾸는 기본 연산이다.
  - `@` 연산자는 NumPy에서 행렬 곱을 수행한다.
  ```python
  import numpy as np

  # 3개의 샘플, 2개의 feature
  X = np.array([
      [1.0, 2.0],
      [2.0, 1.0],
      [3.0, 4.0],
  ])

  # 2차원 feature를 3차원 표현으로 바꾸는 가중치 행렬
  W = np.array([
      [2.0, 0.5, -1.0],
      [1.0, 1.5,  0.0],
  ])

  b = np.array([0.1, 0.2, 0.3])
  Z = X @ W + b

  print(Z.shape)  # (3, 3)
  ```

## AI 수학 기초
- 벡터와 행렬
  - 벡터는 여러 숫자를 순서 있게 묶은 값이다.
  - 행렬은 2차원 숫자 배열이며, 여러 feature를 한 번에 표현하기 좋다.
  - 모델 입력은 보통 행렬 형태로 구성된다.
    - 행: sample
    - 열: feature
- 스칼라 곱과 선형 변환
  - 스칼라 곱은 벡터나 행렬의 크기 방향을 조절하는 연산이다.
  - 선형 변환은 입력 벡터를 다른 공간의 벡터로 바꾸는 연산이다.
  - 신경망의 `Linear` 계층도 본질적으로 행렬 곱과 bias 추가로 이해할 수 있다.
- 미분과 기울기
  - 미분은 함수의 순간 변화량이다.
  - 손실 함수의 기울기는 파라미터를 어느 방향으로 얼마나 바꿔야 할지 알려준다.
  - 경사하강법은 손실이 작아지는 방향으로 weight와 bias를 반복적으로 갱신한다.
- 손실 함수
  - 손실은 모델 예측이 정답과 얼마나 다른지 수치화한 값이다.
  - 회귀에서는 MAE, MSE를 자주 사용한다.
  - 분류에서는 Cross Entropy, Binary Cross Entropy를 자주 사용한다.
- 시각화로 이해한 포인트
  - 행렬 표현, 스칼라 곱, 선형 변환을 도식으로 확인했다.
  - `matplotlib`, `seaborn`으로 선 그래프, 산점도, iris 품종 분포를 시각화했다.
  - 수식만 볼 때보다 그래프를 함께 보면 벡터 공간, 변환, 분포의 의미가 더 명확해진다.

## 머신러닝 기초
- 데이터 구성
  - Feature
    - 모델이 입력으로 사용하는 정보이다.
  - Label / Target
    - 모델이 맞추려는 정답이다.
  - 학습은 feature와 label 사이의 관계를 설명하는 함수를 찾는 과정이다.
- 지도학습
  - 정답이 있는 데이터로 학습한다.
  - 대표 문제는 회귀와 분류이다.
- 회귀
  - 연속적인 숫자 값을 예측한다.
  - 예: 집값, 온도, 점수, 매출
  - 주요 지표
    - MAE
      - 오차의 절댓값 평균이다.
      - 해석이 직관적이다.
    - MSE
      - 오차 제곱의 평균이다.
      - 큰 오차를 더 강하게 벌준다.
    - R2
      - 모델이 데이터 변동을 얼마나 설명하는지 나타낸다.
- 분류
  - 미리 정해진 범주 중 하나를 예측한다.
  - 예: 스팸/정상, 합격/불합격, 질병/정상
  - 이진 분류에서는 sigmoid로 0과 1 사이의 확률을 만든다.
  - 다중 분류에서는 softmax로 각 클래스 확률을 만든다.
- 모델, 학습, 추론
  - 모델은 입력을 출력으로 바꾸는 함수 구조이다.
  - 학습은 좋은 파라미터를 찾는 과정이다.
  - 추론은 학습된 모델로 새 입력의 결과를 예측하는 과정이다.
- 일반화
  - 학습 데이터에서만 성능이 좋은 모델은 실제 문제에서 실패할 수 있다.
  - train, validation, test 데이터를 나누어 과적합을 확인한다.
  - K-fold cross validation은 데이터를 여러 fold로 나누어 검증을 반복하는 방식이다.
  - LOOCV는 샘플 하나를 검증 데이터로 두는 극단적인 교차검증 방식이다.

## 선형 회귀와 로지스틱 회귀
- 선형 회귀
  - 입력과 출력이 선형 관계라고 가정한다.
  - 단순 선형 회귀는 하나의 feature로 예측한다.
  - 다중 선형 회귀는 여러 feature를 함께 사용한다.
  - 모델은 보통 다음 형태로 이해한다.
    ```text
    y_hat = w * x + b
    ```
  - 잔차는 실제값과 예측값의 차이다.
  - 최소제곱법은 잔차 제곱합이 가장 작아지는 계수를 찾는다.
  - 정규방정식은 해를 직접 계산할 수 있지만, feature가 많아지면 계산 비용이 커질 수 있다.
- 선형 회귀 결과 해석
  - 회귀계수
    - feature가 1 증가할 때 target이 평균적으로 얼마나 변하는지 나타낸다.
  - p-value
    - 특정 feature가 통계적으로 유의한지 판단할 때 사용한다.
  - R2
    - 모델이 target의 변동을 얼마나 설명하는지 나타낸다.
  - F-statistic
    - 개별 feature가 아니라 모델 전체가 유의한지 확인하는 지표이다.
  - OLS와 MLE
    - OLS는 잔차 제곱합을 최소화하는 관점이다.
    - MLE는 관측된 데이터가 나올 가능도를 최대화하는 관점이다.
    - 정규 오차를 가정하면 선형 회귀에서 OLS와 MLE는 같은 해로 이어질 수 있다.
- Gradient Descent
  - 손실 함수의 기울기를 이용해 파라미터를 조금씩 갱신한다.
  - learning rate가 너무 크면 발산하고, 너무 작으면 학습이 느리다.
  - SGD는 전체 데이터가 아니라 일부 샘플 또는 mini-batch로 기울기를 계산한다.
- 로지스틱 회귀
  - 이름은 회귀지만 분류에 사용하는 모델이다.
  - 선형 결합 결과를 sigmoid에 통과시켜 확률로 바꾼다.
  - 이진 분류에서 Binary Cross Entropy를 손실 함수로 사용한다.
  - decision boundary를 기준으로 클래스를 나눈다.
- Grid Search
  - 여러 후보 파라미터를 조합해 성능이 좋은 설정을 찾는 방법이다.
  - 단순하지만 후보가 많아질수록 비용이 커진다.
- 예시: 선형 회귀를 직접 구현하는 흐름
  - 예측식은 `y_hat = w * x + b`이다.
  - 손실은 예측값과 실제값의 차이를 평균낸다.
  - 기울기를 계산해 `w`, `b`를 조금씩 갱신한다.
  ```python
  import numpy as np

  x = np.array([1, 2, 3, 4, 5], dtype=float)
  y = np.array([3, 5, 7, 9, 11], dtype=float)

  w = 0.0
  b = 0.0
  lr = 0.01

  for epoch in range(1000):
      y_hat = w * x + b
      error = y_hat - y
      loss = np.mean(error ** 2)

      dw = np.mean(2 * error * x)
      db = np.mean(2 * error)

      w -= lr * dw
      b -= lr * db

  print(round(w, 2), round(b, 2), round(loss, 4))
  ```
- 예시: 로지스틱 회귀와 Binary Cross Entropy
  - 로지스틱 회귀는 선형 점수를 sigmoid에 통과시켜 확률로 바꾼다.
  - 확률이 0.5 이상이면 class 1, 아니면 class 0으로 분류할 수 있다.
  - `np.clip`은 `log(0)`이나 overflow를 막기 위한 안정화 장치이다.
  ```python
  import numpy as np

  def sigmoid(z):
      z = np.clip(z, -500, 500)
      return 1 / (1 + np.exp(-z))

  def binary_cross_entropy(y_true, y_prob):
      eps = 1e-8
      y_prob = np.clip(y_prob, eps, 1 - eps)
      return -np.mean(y_true * np.log(y_prob) + (1 - y_true) * np.log(1 - y_prob))

  X = np.array([[1.0, 2.0], [2.0, 1.0], [3.0, 4.0], [4.0, 3.0]])
  y = np.array([0, 0, 1, 1])

  W = np.zeros(X.shape[1])
  b = 0.0
  lr = 0.1

  for _ in range(300):
      prob = sigmoid(X @ W + b)
      loss = binary_cross_entropy(y, prob)

      grad = prob - y
      dW = X.T @ grad / len(X)
      db = np.mean(grad)

      W -= lr * dW
      b -= lr * db

  pred = (sigmoid(X @ W + b) >= 0.5).astype(int)
  print(pred, loss)
  ```
- 시각화로 이해한 포인트
  - 데이터 산점도 위에 회귀선을 올려 모델이 어떤 함수를 학습하는지 확인했다.
  - MAE/MSE 차이, 정규방정식, gradient descent의 손실 감소 방향을 그림으로 확인했다.
  - sigmoid curve와 cross entropy 형태를 시각화해 확률 기반 분류를 이해했다.

## EDA와 Scikit-learn
- EDA(Exploratory Data Analysis)
  - 데이터를 모델에 넣기 전에 구조, 분포, 관계, 이상치를 확인하는 과정이다.
  - 좋은 모델링은 데이터를 이해하는 데서 시작한다.
- 기본 확인
  - 데이터 크기
  - column 목록
  - 자료형
  - 결측치
  - 기초 통계량
  - target 분포
- 상관관계
  - 두 변수 사이의 선형적 관계를 확인한다.
  - 산점도와 heatmap으로 feature 간 관계를 시각화한다.
  - 상관관계가 높다고 해서 반드시 인과관계가 있는 것은 아니다.
- 분포 확인
  - 히스토그램, KDE, boxplot 등을 사용한다.
  - 분포를 보면 skew, outlier, class imbalance를 파악할 수 있다.
- 전처리
  - train/test split
    - 학습과 평가 데이터를 분리한다.
  - StandardScaler
    - 평균 0, 표준편차 1이 되도록 feature를 표준화한다.
  - 표준화는 거리 기반 모델, 선형 모델, 경사하강법 기반 학습에서 중요하다.
- 구체적인 전처리 패턴
  - IQR 기반 이상치 탐색
    - Q1, Q3, IQR을 이용해 하한/상한 밖의 값을 이상치 후보로 본다.
  - 회귀 target stratified split
    - 회귀 문제에서는 target을 구간화한 뒤 stratify에 사용하면 train/test의 target 분포를 더 비슷하게 유지할 수 있다.
    - `pd.qcut`은 연속형 target을 분위수 기반 구간으로 나눌 때 사용할 수 있다.
  - `pivot`
    - row에 있던 범주 값을 column 구조로 펼쳐 비교표를 만든다.
  - `pivot_table`
    - `pivot`과 비슷하지만 중복 조합이 있을 때 평균, 합계, 개수 같은 집계를 함께 수행할 수 있다.
  - `melt`
    - 여러 column을 하나의 변수 column과 값 column으로 길게 변환한다.
    - wide format을 long format으로 바꿀 때 사용한다.
- 예시: IQR, qcut, pivot, pivot_table, melt 전처리 패턴
  - `pivot`은 같은 지표를 범주별 column로 펼쳐 비교표를 만들 때 유용하다.
  - `pivot_table`은 같은 `index`와 `columns` 조합이 여러 번 등장할 때 집계 기준을 정해 비교표를 만든다.
  - `melt`는 반대로 여러 column에 흩어진 값을 하나의 column으로 모아 시각화나 groupby에 쓰기 좋게 만든다.
  - 회귀 target을 stratify하려면 `qcut`으로 target을 임시 구간화한 뒤 split에만 사용한다.
  ```python
  import pandas as pd
  from sklearn.model_selection import train_test_split

  df = pd.DataFrame({
      "region": ["Seoul", "Seoul", "Busan", "Busan", "Jeju", "Jeju"],
      "model": ["A", "B", "A", "B", "A", "B"],
      "score": [82, 91, 75, 84, 88, 79],
      "price": [120, 180, 90, 140, 130, 160],
  })

  # 1. pivot: 지역별 모델 점수 비교표 만들기
  score_table = df.pivot(index="region", columns="model", values="score")
  print(score_table)
  ```
  ```text
  model    A   B
  region
  Busan   75  84
  Jeju    88  79
  Seoul   82  91
  ```
  ```python
  # 2. pivot_table: 중복 조합이 있어도 집계 기준으로 비교표 만들기
  logs = pd.DataFrame({
      "region": ["Seoul", "Seoul", "Seoul", "Busan", "Busan", "Busan"],
      "model": ["A", "A", "B", "A", "B", "B"],
      "score": [80, 84, 91, 75, 82, 86],
  })

  avg_score_table = logs.pivot_table(
      index="region",
      columns="model",
      values="score",
      aggfunc="mean",
  )
  print(avg_score_table)
  ```
  ```text
  model     A     B
  region
  Busan  75.0  84.0
  Seoul  82.0  91.0
  ```
  ```python
  # 3. melt: wide table을 long table로 되돌리기
  long_score = score_table.reset_index().melt(
      id_vars="region",
      var_name="model",
      value_name="score",
  )

  # 4. IQR: 이상치 후보 확인
  q1 = df["price"].quantile(0.25)
  q3 = df["price"].quantile(0.75)
  iqr = q3 - q1
  lower = q1 - 1.5 * iqr
  upper = q3 + 1.5 * iqr
  outlier_candidates = df[(df["price"] < lower) | (df["price"] > upper)]

  # 5. qcut: 회귀 target을 임시 구간화해 stratified split에 사용
  target_bins = pd.qcut(df["score"], q=3, labels=False, duplicates="drop")
  train_df, test_df = train_test_split(
      df,
      test_size=0.5,
      random_state=42,
      stratify=target_bins,
  )
  ```
- Scikit-learn 기본 흐름
  - 모델 객체 생성
  - `fit()`으로 학습
  - `predict()`로 예측
  - metric으로 평가
  - 필요하면 scaler, split, pipeline을 함께 사용한다.
- 예시: EDA와 Scikit-learn 기본 파이프라인
  - 모델 학습 전에는 train/test split을 먼저 수행한다.
  - scaler는 train 데이터에만 `fit`하고, test 데이터에는 `transform`만 적용한다.
  ```python
  import pandas as pd
  import seaborn as sns
  from sklearn.model_selection import train_test_split
  from sklearn.preprocessing import StandardScaler
  from sklearn.linear_model import LinearRegression
  from sklearn.metrics import mean_squared_error, r2_score

  df = sns.load_dataset("mpg").dropna()
  X = df[["weight", "horsepower", "acceleration"]]
  y = df["mpg"]

  X_train, X_test, y_train, y_test = train_test_split(
      X, y, test_size=0.2, random_state=42
  )

  scaler = StandardScaler()
  X_train_scaled = scaler.fit_transform(X_train)
  X_test_scaled = scaler.transform(X_test)

  model = LinearRegression()
  model.fit(X_train_scaled, y_train)

  y_pred = model.predict(X_test_scaled)
  print(mean_squared_error(y_test, y_pred), r2_score(y_test, y_pred))
  ```
- 예시: 시각화로 모델 결과 확인하기
  - 숫자 metric만 보면 모델이 어디서 틀리는지 알기 어렵다.
  - 실제값과 예측값 산점도를 그리면 과소/과대 예측 경향을 확인할 수 있다.
  ```python
  import matplotlib.pyplot as plt
  import seaborn as sns

  sns.scatterplot(x=y_test, y=y_pred, alpha=0.7)
  plt.xlabel("Actual")
  plt.ylabel("Predicted")
  plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color="red")
  plt.show()
  ```
- 시각화로 이해한 포인트
  - 데이터 크기, 통계량, 상관관계 표를 시각 자료로 확인했다.
  - scatterplot, heatmap, histogram, pairplot으로 feature 관계와 분포를 살펴봤다.
  - 표준화 전후 모델 결과를 비교했다.

## 딥러닝과 PyTorch
- Tensor
  - PyTorch의 기본 데이터 단위이다.
  - NumPy 배열과 비슷하지만 GPU 연산과 자동 미분을 지원한다.
- Autograd
  - 연산 기록을 바탕으로 기울기를 자동 계산한다.
  - 학습할 때는 gradient 추적이 필요하다.
  - 평가나 추론할 때는 `no_grad`로 불필요한 gradient 계산을 막는다.
- 신경망 기본 구조
  - 입력층
    - 데이터를 받는다.
  - 은닉층
    - weight, bias, activation을 통해 표현을 변환한다.
  - 출력층
    - 회귀값, 확률, class score 등을 만든다.
- `nn.Linear`
  - 입력 벡터에 선형 변환을 적용한다.
  - 내부적으로 행렬 곱과 bias 덧셈으로 이해할 수 있다.
- 활성화 함수
  - 선형 변환만 쌓으면 전체 모델도 선형 모델에 머문다.
  - ReLU, sigmoid, tanh 같은 활성화 함수가 비선형성을 만든다.
- Sequential Model
  - 여러 계층을 순서대로 연결해 모델을 구성한다.
  - 작은 MLP를 빠르게 만들 때 유용하다.
- MLP
  - fully connected layer를 여러 층 쌓은 기본 신경망이다.
  - 이미지나 텍스트처럼 구조가 있는 데이터에는 CNN, RNN, Transformer가 더 적합할 수 있다.
- Dataset / DataLoader
  - Dataset은 샘플과 label을 제공한다.
  - DataLoader는 batch, shuffle, 병렬 로딩을 관리한다.
- Tensor shape
  - 딥러닝 코드는 값 자체보다 shape이 맞는지가 먼저 중요하다.
  - batch dimension, feature dimension, class dimension을 구분해야 한다.
- 학습 루프
  - forward
  - loss 계산
  - `zero_grad()`
  - backward
  - optimizer step
  - validation 평가
- 예시: PyTorch의 autograd 확인
  - `requires_grad=True`인 tensor는 연산 기록을 추적한다.
  - `backward()`를 호출하면 leaf tensor의 gradient가 계산된다.
  ```python
  import torch

  x = torch.tensor(2.0, requires_grad=True)
  y = x ** 2 + 3 * x + 1
  y.backward()

  print(x.grad)  # dy/dx = 2x + 3, x=2 -> 7
  ```
- 예시: Tensor shape와 `nn.Linear` 입출력
  - `nn.Linear(in_features, out_features)`는 마지막 차원을 `in_features`에서 `out_features`로 바꾼다.
  - batch 크기는 그대로 유지된다.
  ```python
  import torch
  import torch.nn as nn

  x = torch.randn(32, 4)  # batch_size=32, feature=4
  layer = nn.Linear(4, 3)

  logits = layer(x)

  print(x.shape)       # torch.Size([32, 4])
  print(logits.shape)  # torch.Size([32, 3])
  ```
- 예시: Custom Dataset으로 sample과 label 제공하기
  - Dataset은 `__len__`과 `__getitem__`을 구현한다.
  - DataLoader는 Dataset에서 sample을 꺼내 batch로 묶는다.
  ```python
  import torch
  from torch.utils.data import Dataset, DataLoader

  class ReviewDataset(Dataset):
      def __init__(self, features, labels):
          self.features = torch.tensor(features, dtype=torch.float32)
          self.labels = torch.tensor(labels, dtype=torch.long)

      def __len__(self):
          return len(self.labels)

      def __getitem__(self, idx):
          return self.features[idx], self.labels[idx]


  features = [
      [0.2, 0.8, 0.1],
      [0.9, 0.1, 0.4],
      [0.3, 0.4, 0.7],
  ]
  labels = [1, 0, 1]

  dataset = ReviewDataset(features, labels)
  loader = DataLoader(dataset, batch_size=2, shuffle=True)

  for xb, yb in loader:
      print(xb.shape, yb.shape)
  ```
- 예시: PyTorch MLP 학습 루프
  - 모델 정의, 손실 함수, optimizer, DataLoader가 기본 구성이다.
  - 학습 모드에서는 `model.train()`을 사용한다.
  - 평가 모드에서는 `model.eval()`과 `torch.no_grad()`를 함께 사용한다.
  ```python
  import torch
  import torch.nn as nn
  import torch.optim as optim
  from torch.utils.data import DataLoader, TensorDataset

  X = torch.randn(128, 4)
  y = (X[:, 0] + X[:, 1] > 0).long()

  loader = DataLoader(TensorDataset(X, y), batch_size=32, shuffle=True)

  class MLP(nn.Module):
      def __init__(self):
          super().__init__()
          self.net = nn.Sequential(
              nn.Linear(4, 16),
              nn.ReLU(),
              nn.Linear(16, 2),
          )

      def forward(self, x):
          return self.net(x)

  model = MLP()
  criterion = nn.CrossEntropyLoss()
  optimizer = optim.Adam(model.parameters(), lr=0.01)

  for epoch in range(20):
      model.train()
      for xb, yb in loader:
          pred = model(xb)
          loss = criterion(pred, yb)

          optimizer.zero_grad()
          loss.backward()
          optimizer.step()
  ```
- 예시: 평가 모드와 accuracy 계산
  - 평가 중에는 `model.eval()`로 dropout/batch norm의 동작을 고정한다.
  - `torch.no_grad()`를 사용하면 gradient 저장을 생략해 메모리를 아낄 수 있다.
  ```python
  correct = 0
  total = 0

  model.eval()
  with torch.no_grad():
      for xb, yb in loader:
          logits = model(xb)
          pred = logits.argmax(dim=1)

          correct += (pred == yb).sum().item()
          total += yb.size(0)

  accuracy = correct / total
  print(accuracy)
  ```
- 시각화로 이해한 포인트
  - `nn.Linear`의 입력/출력 차원과 행렬 변환 관계를 도식으로 확인했다.
  - 활성화 함수가 비선형 결정 경계를 만들 수 있음을 그래프로 확인했다.
  - MNIST sample 이미지를 출력해 이미지 데이터의 tensor 구조를 확인했다.

## NLP 기초
- 텍스트를 숫자로 바꾸는 이유
  - 모델은 문자열을 직접 이해하지 못한다.
  - 텍스트를 토큰으로 나누고, 토큰을 숫자 id 또는 벡터로 바꿔야 한다.
- Tokenizer
  - 문장을 모델이 처리할 수 있는 token 단위로 나눈다.
  - 단어, subword, character 단위 등 여러 방식이 있다.
  - BERT 계열 tokenizer는 subword 기반으로 낯선 단어도 부분 단위로 처리할 수 있다.
- BPE(Byte Pair Encoding)
  - 자주 함께 등장하는 문자 또는 subword 쌍을 반복적으로 병합해 vocabulary를 만든다.
  - 낯선 단어를 완전히 버리지 않고 부분 token으로 표현할 수 있게 해준다.
  - 단어 단위 tokenization보다 OOV 문제를 줄이는 데 도움이 된다.
- Vocabulary
  - token과 id의 대응표이다.
  - tokenizer는 vocabulary를 기준으로 token id를 만든다.
- One-hot Encoding
  - vocabulary 크기만큼의 벡터에서 해당 단어 위치만 1로 표시한다.
  - 단순하지만 sparse하고 단어 의미 유사성을 담지 못한다.
- Word Embedding
  - 단어를 dense vector로 표현한다.
  - 의미가 가까운 단어는 벡터 공간에서도 가깝게 위치하도록 학습한다.
- 임베딩 유사도
  - cosine similarity로 벡터 방향의 유사성을 비교할 수 있다.
  - PCA 같은 차원 축소를 사용하면 고차원 임베딩을 2D 평면에 시각화할 수 있다.
- Word2Vec
  - Skip-gram
    - 중심 단어로 주변 단어를 예측한다.
    - 희귀 단어 표현에 강하지만 학습이 느릴 수 있다.
  - CBOW
    - 주변 단어로 중심 단어를 예측한다.
    - 학습이 빠르고 빈번한 단어에 강하다.
- 순차 데이터
  - 순서가 의미에 중요한 데이터이다.
  - 텍스트, 음성, 시계열, 비디오가 대표적이다.
- RNN
  - 이전 시점의 hidden state를 다음 시점으로 넘기며 순차 데이터를 처리한다.
  - 장기 의존성, vanishing gradient, 병렬화 어려움이 한계이다.
- LSTM
  - gate와 cell state를 사용해 장기 의존성 문제를 완화한다.
- Encoder / Decoder
  - Encoder는 입력 시퀀스를 hidden representation으로 압축한다.
  - Decoder는 그 representation을 바탕으로 출력 시퀀스를 생성한다.
  - 번역, 요약, 질의응답처럼 입력과 출력의 길이가 달라질 수 있는 작업에서 중요하다.
- Attention
  - 현재 처리에 중요한 입력 위치에 더 큰 가중치를 주는 방식이다.
  - Query, Key, Value로 attention score를 계산한다.
- Self-Attention
  - 같은 문장 안의 token들이 서로를 참조한다.
  - Transformer의 핵심 구조이다.
- Masked Self-Attention
  - 다음 token을 예측할 때 미래 token을 보지 못하게 막는다.
  - GPT 계열 autoregressive 모델에서 중요하다.
- HuggingFace Transformers
  - tokenizer, pretrained model, pipeline을 불러와 NLP와 멀티모달 모델을 실습할 수 있다.
  - `AutoTokenizer`, `AutoModel`, `AutoModelForCausalLM`처럼 모델 종류에 맞는 자동 로더를 자주 사용한다.
  - 모델 허브의 checkpoint를 가져올 때는 입력 형식, output 구조, 라이선스를 함께 확인해야 한다.
- Padding / Truncation / Attention Mask
  - 길이가 다른 문장을 batch로 묶으려면 같은 길이가 되도록 padding한다.
  - 너무 긴 문장은 모델 최대 길이에 맞게 truncation한다.
  - attention mask는 실제 token과 padding token을 구분한다.
- Transformer 직접 구현 관점
  - Multi-Head Self-Attention
    - 하나의 attention이 아니라 여러 head가 서로 다른 관계를 학습하도록 한다.
  - Layer Normalization
    - 각 layer의 입력 분포를 안정화해 깊은 모델 학습을 돕는다.
  - Feed Forward Network
    - attention 이후 각 token 위치에 독립적으로 적용되는 MLP이다.
  - Residual Connection
    - 입력을 출력에 더해 gradient 흐름을 돕고 깊은 네트워크를 안정화한다.
  - Decoder Block
    - masked self-attention, normalization, feed forward를 묶어 다음 token 예측 구조를 만든다.
- 예시: Tokenizer와 token id 확인
  - tokenizer는 문장을 token으로 나누고 token id로 바꾼다.
  - 같은 단어라도 tokenizer 종류에 따라 분해 방식이 다를 수 있다.
  ```python
  from transformers import AutoTokenizer

  tokenizer = AutoTokenizer.from_pretrained("klue/bert-base")
  text = "토큰화는 문장을 모델 입력으로 바꾸는 과정이다."

  tokens = tokenizer.tokenize(text)
  ids = tokenizer.convert_tokens_to_ids(tokens)

  print(tokens)
  print(ids)
  ```
- 예시: padding, truncation, attention mask 확인
  - `input_ids`는 token id이고, `attention_mask`는 padding이 아닌 위치를 1로 표시한다.
  - batch 입력에서는 각 문장의 길이가 달라도 tensor shape를 맞춰야 한다.
  ```python
  from transformers import AutoTokenizer

  tokenizer = AutoTokenizer.from_pretrained("klue/bert-base")
  texts = [
      "짧은 문장",
      "조금 더 긴 문장을 tokenizer에 넣어 본다.",
  ]

  batch = tokenizer(
      texts,
      padding=True,
      truncation=True,
      max_length=12,
      return_tensors="pt",
  )

  print(batch["input_ids"].shape)
  print(batch["attention_mask"])
  print(tokenizer.convert_ids_to_tokens(batch["input_ids"][0]))
  ```
- 예시: 임베딩과 cosine similarity
  - 임베딩은 문장이나 단어를 벡터로 바꾼 표현이다.
  - cosine similarity는 두 벡터의 방향이 얼마나 비슷한지 측정한다.
  ```python
  import numpy as np

  def cosine_similarity(a, b):
      return (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))

  cat = np.array([0.9, 0.1, 0.2])
  dog = np.array([0.8, 0.2, 0.2])
  car = np.array([0.1, 0.9, 0.7])

  print(cosine_similarity(cat, dog))
  print(cosine_similarity(cat, car))
  ```
- 예시: Transformers pipeline으로 감정 분류 호출하기
  - `pipeline`은 tokenizer, model, 후처리를 묶어 빠르게 추론을 실행한다.
  - 학습보다는 pretrained model의 입력과 출력 형식을 익히는 데 좋다.
  ```python
  from transformers import pipeline

  classifier = pipeline(
      task="text-classification",
      model="distilbert-base-uncased-finetuned-sst-2-english",
  )

  result = classifier("The delivery was fast, but the package was damaged.")
  print(result)
  ```
- 예시: 간단한 self-attention score 모양 보기
  - attention score는 각 token이 다른 token을 얼마나 참조하는지 나타낸다.
  - 실제 Transformer에서는 여러 head와 projection layer가 함께 사용된다.
  ```python
  import torch
  import torch.nn.functional as F

  x = torch.randn(1, 4, 8)  # batch=1, tokens=4, hidden=8
  q = x
  k = x
  v = x

  scores = q @ k.transpose(-2, -1) / (x.size(-1) ** 0.5)
  weights = F.softmax(scores, dim=-1)
  context = weights @ v

  print(scores.shape)   # torch.Size([1, 4, 4])
  print(context.shape)  # torch.Size([1, 4, 8])
  ```
- 시각화로 이해한 포인트
  - tokenizer, vocabulary, BERT tokenizer 동작을 시각 자료로 확인했다.
  - embedding vector를 2D로 축소해 단어 간 의미적 거리를 살펴봤다.
  - cosine similarity heatmap으로 임베딩 유사도를 확인했다.

## LLM과 텍스트 파운데이션 모델
- LLM
  - 대규모 텍스트와 큰 모델을 이용해 학습한 언어 모델이다.
  - 다음 token 예측을 기본 학습 목표로 삼는다.
  - 규모가 커지면 in-context learning, 추론, 지시 따르기 같은 능력이 강해진다.
- Foundation Model의 핵심 요소
  - 대규모 데이터
  - self-supervised learning
  - Transformer와 attention
  - 대규모 학습 자원
- Closed Model과 Open Model
  - Closed model
    - 일반적으로 성능과 사용 편의성이 좋지만 내부 구조와 학습 데이터가 공개되지 않는다.
  - Open model
    - 직접 실행, fine-tuning, 구조 분석이 가능하지만 자원과 운영 비용이 필요하다.
- Alignment
  - 기본 language modeling만으로는 사람이 원하는 답변을 안정적으로 따르기 어렵다.
  - SFT, RLHF, preference tuning 등을 통해 지시 따르기와 안전성을 개선한다.
- Prompting
  - Zero-shot
    - 예시 없이 지시만으로 수행한다.
  - Few-shot
    - 몇 개의 예시를 함께 제공한다.
  - Chain-of-Thought
    - 중간 추론 과정을 유도한다.
  - Zero-shot CoT
    - 별도 예시 없이 단계적 사고를 유도한다.
  - Prompting 예시
    - Zero-shot
      ```text
      다음 문장의 감정을 positive / negative / neutral 중 하나로 분류해줘.

      문장: "배송은 빨랐지만 제품 포장이 찢어져 있었다."

      출력 형식:
      {"label": "...", "reason": "..."}
      ```
    - Few-shot
      ```text
      문장의 감정을 분류해줘.

      예시 1
      문장: "가격은 비싸지만 품질이 훌륭했다."
      출력: positive

      예시 2
      문장: "앱이 계속 멈춰서 사용할 수 없었다."
      출력: negative

      문장: "설명은 친절했지만 대기 시간이 길었다."
      출력:
      ```
    - Chain-of-Thought
      - 실제 서비스에서는 장황한 내부 추론을 그대로 요구하기보다 필요한 계산 과정이나 근거만 짧게 요구하는 편이 안전하다.
      ```text
      아래 수학 문제를 풀어줘.

      문제: 사과 3개 묶음이 4상자 있고, 사과 5개가 추가로 있다.
      총 사과는 몇 개인가?

      답을 내기 전에 필요한 계산 단계를 간단히 정리하고,
      마지막 줄에 "정답: 숫자" 형식으로 써줘.
      ```
    - Zero-shot CoT
      ```text
      다음 문제를 단계적으로 생각해서 풀어줘.
      단, 마지막에는 결론만 명확히 적어줘.

      문제: 회의 참석자 12명 중 3명이 먼저 나가고,
      5명이 새로 들어왔다. 현재 참석자는 몇 명인가?
      ```
    - 구조화 출력
      ```text
      너는 데이터 라벨링 도우미야.
      아래 리뷰를 JSON으로 변환해줘.

      리뷰: "화면은 예쁜데 로그인 오류가 자주 발생한다."

      출력 형식:
      {
        "sentiment": "positive | negative | mixed",
        "issue_type": "ui | performance | auth | other",
        "summary": "한 문장 요약"
      }
      ```
  - Prompting을 코드로 관리하는 예시
    ```python
    def build_review_prompt(review: str) -> list[dict[str, str]]:
        return [
            {
                "role": "system",
                "content": "너는 엄격한 리뷰 라벨링 도우미다. JSON만 반환한다.",
            },
            {
                "role": "user",
                "content": (
                    "리뷰를 sentiment, issue_type, summary로 분석해줘.\n"
                    f"리뷰: {review}"
                ),
            },
        ]


    messages = build_review_prompt("화면은 예쁜데 로그인 오류가 자주 발생한다.")
    ```
- LLM 평가
  - MMLU, ARC, GSM8K, HumanEval 같은 벤치마크가 사용된다.
  - LLM-as-a-Judge는 다른 LLM의 출력을 LLM으로 평가하는 방식이다.
  - 평가 모델의 편향과 기준 흔들림을 주의해야 한다.
- 도구 결합형 LLM
  - Tool-Augmented LLM은 모델이 외부 도구를 호출해 계산, 검색, 코드 실행 같은 작업을 수행하게 하는 방식이다.
  - 단순 생성보다 강력하지만 도구 권한, 입력 검증, 실행 결과 검증이 함께 필요하다.
- 안전성과 한계
  - hallucination
    - 사실이 아닌 내용을 그럴듯하게 생성할 수 있다.
  - jailbreaking
    - 안전장치를 우회하려는 입력이 있을 수 있다.
  - AI-generated text detection
    - 탐지기는 보조 도구일 뿐 완전한 판별 기준이 되기 어렵다.

## AI를 이용한 데이터 생성
- 소량 데이터 생성
  - 일반 대화형 LLM으로 빠르게 예시 데이터를 만들 수 있다.
  - 요구 형식, label 기준, 예외 조건을 명확히 적어야 품질이 안정된다.
- 대량 데이터 생성
  - 대화형 UI에 많은 데이터를 한 번에 요청하는 방식은 품질과 재현성이 낮다.
  - API, 소형 생성 모델, batch 처리, 검수 로직을 함께 사용해야 한다.
- OpenAI 호환 API
  - 일부 모델 제공자는 OpenAI와 유사한 API 형식으로 chat completion을 제공한다.
  - 환경 변수로 API key를 관리하고, 코드에 직접 노출하지 않는다.
- Solar / Upstage
  - OpenAI 호환 방식으로 호출할 수 있는 한국어 친화 LLM 실습에 사용되었다.
  - 모델 호출, temperature 조정, JSON 형태 응답 유도, 응답 파싱을 함께 다룬다.
- Prompt Engineering
  - 역할 부여
  - 출력 형식 고정
  - few-shot 예시 제공
  - chain-of-thought 유도
  - 제약 조건 명시
  - 금지 조건 명시
- 합성 데이터 품질 관리
  - 생성된 데이터는 바로 학습에 쓰기 전에 검수해야 한다.
  - label 일관성, 중복, 형식 오류, 사실 오류, 편향을 확인한다.
  - LLM-as-a-Judge로 1차 필터링할 수 있지만 최종 기준은 사람이 설계해야 한다.
- 이미지 데이터 증강
  - 회전, crop, flip, color jitter 같은 transform으로 이미지 다양성을 늘릴 수 있다.
  - 증강은 label을 보존하는 범위 안에서 적용해야 한다.
- 예시: OpenAI 호환 API 호출 패턴
  - API key는 코드에 직접 쓰지 않고 환경 변수로 읽는다.
  - 응답 형식을 JSON으로 요구할 때도 실패 가능성을 고려해 파싱 예외를 처리한다.
  - public README에는 실제 key, endpoint의 민감 정보, 기관 계정 정보를 남기지 않는다.
  ```python
  import json
  import os
  from openai import OpenAI

  client = OpenAI(
      api_key=os.getenv("AI_API_KEY"),
      base_url=os.getenv("AI_BASE_URL"),
  )

  response = client.chat.completions.create(
      model=os.getenv("AI_MODEL", "example-model"),
      messages=[
          {"role": "system", "content": "JSON만 반환하는 데이터 생성 도우미"},
          {"role": "user", "content": "영화 리뷰 예시 3개를 sentiment와 함께 만들어줘."},
      ],
      temperature=0.7,
  )

  content = response.choices[0].message.content

  try:
      data = json.loads(content)
  except json.JSONDecodeError:
      data = {"raw": content}
  ```
- 예시: few-shot 합성 데이터 생성 프롬프트
  - label 기준이 흔들리면 생성 데이터 품질도 흔들린다.
  - 먼저 좋은 예시와 나쁜 예시를 함께 주고, 출력 schema를 고정한다.
  ```python
  topic = "온라인 쇼핑몰 리뷰"

  messages = [
      {
          "role": "system",
          "content": "너는 학습용 데이터를 만드는 보조자다. JSON 배열만 반환한다.",
      },
      {
          "role": "user",
          "content": f"""
  {topic} 문장과 sentiment label을 만들어줘.

  label 기준:
  - positive: 제품, 배송, 서비스에 명확한 만족이 있음
  - negative: 제품, 배송, 서비스에 명확한 불만이 있음
  - mixed: 장점과 단점이 함께 있음

  예시:
  [
    {{"text": "배송이 빠르고 포장도 깔끔했다.", "sentiment": "positive"}},
    {{"text": "가격은 좋지만 제품에 흠집이 있었다.", "sentiment": "mixed"}},
    {{"text": "문의 답변이 늦고 교환도 불편했다.", "sentiment": "negative"}}
  ]

  새 데이터 5개를 만들어줘.
  각 항목은 text, sentiment, reason 필드를 가져야 한다.
  """,
      },
  ]
  ```
- 예시: 생성 데이터 검수 패턴
  - LLM 출력은 형식 오류, label 오류, 중복을 가질 수 있다.
  - 간단한 rule 검수로 1차 필터링한 뒤 사람이 기준을 점검한다.
  ```python
  import pandas as pd

  allowed_labels = {"positive", "negative", "mixed"}

  generated = [
      {"text": "배송이 빨랐다.", "sentiment": "positive", "reason": "배송 만족"},
      {"text": "배송이 빨랐다.", "sentiment": "positive", "reason": "중복 예시"},
      {"text": "", "sentiment": "good", "reason": "잘못된 label"},
  ]

  df = pd.DataFrame(generated)

  valid = df[
      df["text"].str.len().gt(0)
      & df["sentiment"].isin(allowed_labels)
  ].drop_duplicates(subset=["text"])

  invalid = df.drop(valid.index, errors="ignore")
  ```
- 예시: LLM-as-a-Judge 검수 프롬프트
  - 판단 기준을 prompt에 명시하고, 통과 여부와 이유를 분리해서 받는다.
  ```text
  너는 합성 데이터 검수자다.
  아래 항목이 label 기준에 맞는지 평가해줘.

  기준:
  - positive: 명확한 만족
  - negative: 명확한 불만
  - mixed: 만족과 불만이 함께 있음

  데이터:
  text: "색상은 마음에 들지만 하루 만에 고장났다."
  sentiment: mixed

  JSON만 반환해줘:
  {
    "pass": true 또는 false,
    "reason": "짧은 판단 근거"
  }
  ```
- 시각화로 이해한 포인트
  - 소량 데이터 생성, 대량 데이터 생성, LLM-as-a-Judge, API 호출 흐름을 도식으로 확인했다.
  - 이미지 증강 예시를 통해 transform이 데이터 다양성을 늘리는 방식을 확인했다.

## 컴퓨터 비전
- FCN과 CNN
  - FCN
    - 이미지를 1차원으로 펼쳐 처리한다.
    - 공간 구조를 잘 활용하지 못하고 파라미터 수가 커질 수 있다.
  - CNN
    - 이미지의 높이, 너비, 채널 구조를 유지하면서 지역 특징을 추출한다.
    - 필터를 공유하므로 파라미터 효율이 좋다.
- Convolution
  - kernel/filter를 이미지 위로 이동시키며 지역 패턴을 추출한다.
  - filter 하나는 feature map 하나를 만든다.
  - 여러 filter를 사용하면 여러 종류의 특징을 추출할 수 있다.
- Padding / Stride
  - padding은 가장자리 정보 손실을 줄이거나 출력 크기를 조절한다.
  - stride는 filter가 이동하는 간격이다.
  - stride가 커지면 출력 해상도가 줄어든다.
- Receptive Field
  - 한 뉴런이 볼 수 있는 입력 영역이다.
  - 층이 깊어질수록 더 넓은 문맥을 반영한다.
- Pooling
  - 해상도를 줄이고 중요한 특징을 남긴다.
  - max pooling은 영역 안의 최댓값을 선택한다.
- 대표 모델 흐름
  - AlexNet
    - CNN 기반 이미지 인식 성능을 크게 끌어올린 모델이다.
  - VGG
    - 작은 convolution을 깊게 쌓는 구조가 특징이다.
  - ResNet
    - residual connection으로 깊은 네트워크의 degradation 문제를 완화한다.
  - MobileNet
    - 경량화를 위해 depthwise/pointwise convolution을 활용한다.
- Transfer Learning
  - 대규모 데이터로 학습된 모델을 가져와 새 작업에 활용한다.
  - 적은 데이터에서도 좋은 성능을 얻기 쉽다.
- ImageFolder
  - 폴더명을 class label로 보고 이미지 데이터셋을 자동 구성하는 torchvision 도구이다.
  - 합성 이미지로 class별 폴더를 만든 뒤 fine-tuning dataset을 구성할 때 사용할 수 있다.
- Linear Probing
  - backbone은 고정하고 마지막 분류기만 학습한다.
  - 빠르고 안정적이지만 표현 자체는 바꾸지 않는다.
- Fine-tuning
  - backbone 일부 또는 전체를 함께 학습한다.
  - 성능 향상이 가능하지만 데이터와 학습 설정에 민감하다.
- Optimizer / Scheduler 비교
  - SGD + Momentum
    - 기본적이고 안정적인 최적화 방식이지만 learning rate 조정이 중요하다.
  - StepLR
    - 정해진 epoch 간격으로 learning rate를 줄인다.
  - Adam
    - gradient의 1차/2차 모멘트를 활용해 파라미터별 학습률을 조정한다.
  - ReduceLROnPlateau
    - validation loss가 개선되지 않을 때 learning rate를 낮춘다.
- Knowledge Distillation
  - 큰 teacher model의 soft prediction을 작은 student model이 따라 배우게 하는 방식이다.
  - temperature로 soft label을 부드럽게 만들고, KL divergence와 hard label loss를 함께 사용할 수 있다.
  - 모델 경량화나 작은 모델 성능 보강에 활용된다.
- 예시: 이미지 증강 패턴
  - 증강은 데이터 다양성을 늘리지만 label 의미를 깨뜨리면 안 된다.
  - classification에서는 horizontal flip이 안전할 수 있지만, 문자/방향이 중요한 문제에서는 위험할 수 있다.
  ```python
  from torchvision import transforms

  train_transform = transforms.Compose([
      transforms.Resize((224, 224)),
      transforms.RandomHorizontalFlip(p=0.5),
      transforms.ColorJitter(brightness=0.2, contrast=0.2),
      transforms.ToTensor(),
      transforms.Normalize(
          mean=[0.485, 0.456, 0.406],
          std=[0.229, 0.224, 0.225],
      ),
  ])
  ```
- 예시: ImageFolder와 DataLoader 구성
  - `ImageFolder`는 `root/class_name/image.png` 구조를 class label로 해석한다.
  - 합성 이미지나 수집 이미지를 class별 폴더에 넣으면 바로 학습 dataset으로 사용할 수 있다.
  ```text
  dataset/
    cat/
      cat_001.png
      cat_002.png
    dog/
      dog_001.png
      dog_002.png
  ```
  ```python
  from torch.utils.data import DataLoader
  from torchvision.datasets import ImageFolder

  train_dataset = ImageFolder(
      root="dataset",
      transform=train_transform,
  )

  print(train_dataset.class_to_idx)
  # {"cat": 0, "dog": 1}

  train_loader = DataLoader(
      train_dataset,
      batch_size=32,
      shuffle=True,
      num_workers=2,
  )

  images, labels = next(iter(train_loader))
  print(images.shape, labels.shape)
  ```
- 예시: Transfer Learning과 Linear Probing
  - pretrained backbone을 feature extractor로 사용하고 마지막 분류기만 새로 학습한다.
  - 데이터가 적을 때는 전체 fine-tuning보다 linear probing이 안정적일 수 있다.
  ```python
  import torch.nn as nn
  from torchvision import models

  model = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)

  for param in model.parameters():
      param.requires_grad = False

  in_features = model.fc.in_features
  model.fc = nn.Linear(in_features, 3)
  ```
- 예시: Optimizer와 Scheduler 사용
  - `StepLR`은 정해진 주기로 learning rate를 낮춘다.
  - `ReduceLROnPlateau`는 validation loss가 정체될 때 learning rate를 낮춘다.
  ```python
  import torch

  optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
  scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
      optimizer,
      mode="min",
      factor=0.5,
      patience=2,
  )

  for epoch in range(10):
      # train_one_epoch와 evaluate는 학습/검증 로직을 함수로 분리한 helper라고 가정한다.
      train_loss = train_one_epoch(model, train_loader, optimizer)
      valid_loss = evaluate(model, valid_loader)

      scheduler.step(valid_loss)
      print(epoch, train_loss, valid_loss, optimizer.param_groups[0]["lr"])
  ```
- 시각화로 이해한 포인트
  - 영상처리, 패턴인식, AlexNet 등장 배경, CNN 구조를 이미지로 확인했다.
  - convolution, pooling, feature map의 흐름을 도식으로 확인했다.
  - AlexNet, ResNet 추론 결과와 transfer learning 학습 이미지를 확인했다.

## 이미지 파운데이션 모델과 멀티모달
- Vision Foundation Model
  - 이미지, 텍스트, 비디오 등 다양한 입력과 작업에 적응할 수 있는 범용 비전 모델이다.
- CLIP
  - 이미지와 텍스트를 같은 임베딩 공간에 정렬한다.
  - 이미지-텍스트 쌍은 가깝게, 맞지 않는 쌍은 멀게 학습하는 contrastive learning을 사용한다.
  - 직접 문장을 생성하는 모델이 아니라, 이미지와 텍스트 표현을 비교하는 모델이다.
  - zero-shot image classification과 image-text retrieval에 활용된다.
- SigLIP
  - CLIP 계열의 개선형으로, sigmoid 기반 손실을 사용해 학습 효율과 안정성을 높인다.
- ViT
  - 이미지를 patch로 나누고 Transformer 구조로 처리한다.
  - CNN처럼 local inductive bias에 의존하기보다 attention으로 전역 관계를 학습한다.
- LLaVA
  - vision encoder와 LLM을 projection layer로 연결한 multimodal language model이다.
  - 이미지를 보고 질문에 답하거나 설명을 생성할 수 있다.
- Diffusion Model
  - noise에서 시작해 점진적으로 이미지를 복원하며 생성한다.
  - text-to-image 생성 모델의 핵심 방식 중 하나이다.
- Diffusers
  - HuggingFace의 이미지 생성 파이프라인을 다룰 때 사용하는 라이브러리이다.
  - text-to-image 모델을 불러오고 prompt, seed, device 설정을 조정하며 결과 이미지를 생성한다.
- Stable Diffusion 계열
  - 텍스트 조건을 바탕으로 이미지를 생성한다.
  - prompt 품질, negative prompt, seed, sampler, guidance 설정이 결과에 영향을 준다.
- SANA
  - 고해상도 text-to-image 생성을 위한 diffusion 계열 파이프라인으로 실습에 사용되었다.
  - 생성 이미지 품질만 보지 않고 prompt 정합성과 분류 모델 평가 결과를 함께 확인해야 한다.
- Object Detection
  - 이미지 속 객체의 위치와 종류를 함께 예측한다.
  - Transformer 기반 detection 모델도 활용할 수 있다.
- YOLOS
  - Transformer 기반 object detection 모델이다.
  - 이미지에서 객체 위치와 label을 예측하는 실습에 사용되었다.
- CLIP 기반 평가
  - 생성 이미지와 텍스트 prompt의 임베딩 유사도로 alignment를 평가할 수 있다.
  - 단, 시각 품질과 사실성을 완전히 평가하지는 못한다.
- 비디오 / 3D 확장
  - SORA, Veo 계열은 텍스트나 이미지를 기반으로 비디오를 생성하는 모델 흐름과 연결된다.
  - Zero-1-to-3는 2D 이미지에서 다른 시점의 3D view를 생성하는 방향의 모델이다.
  - 이미지 파운데이션 모델은 분류/탐지/생성에서 비디오와 3D로 확장된다.
- PEFT
  - 모든 파라미터를 학습하지 않고 일부 적은 파라미터만 조정하는 방식이다.
  - Prompt Tuning, LoRA 등이 대표적이다.
- 멀티모달 실습에서 확인할 것
  - 모델이 요구하는 입력 형식이 이미지, 텍스트, bounding box 중 무엇인지 확인한다.
  - processor가 이미지 resize, normalize, tokenization을 함께 처리하는 경우가 많다.
  - 생성 모델은 prompt, negative prompt, seed, guidance scale에 따라 결과가 달라진다.
- 예시: ViT 이미지 분류 입력 만들기
  - ViT는 이미지를 patch로 나눠 Transformer 입력처럼 처리한다.
  - 사용자는 직접 patch를 자르기보다 `AutoImageProcessor`로 모델 입력을 만든다.
  ```python
  import torch
  from transformers import AutoImageProcessor, AutoModelForImageClassification

  model_id = "google/vit-base-patch16-224"
  processor = AutoImageProcessor.from_pretrained(model_id)
  model = AutoModelForImageClassification.from_pretrained(model_id)

  # image는 PIL.Image라고 가정
  inputs = processor(images=image, return_tensors="pt")

  with torch.no_grad():
      outputs = model(**inputs)

  pred_id = outputs.logits.argmax(dim=1).item()
  print(model.config.id2label[pred_id])
  ```
- 예시: CLIP으로 이미지-텍스트 정합성 평가하기
  - CLIP은 이미지와 텍스트를 같은 임베딩 공간에 놓고 비교한다.
  - 생성 이미지가 prompt와 얼마나 맞는지 rough한 점검에 사용할 수 있다.
  ```python
  import torch
  from transformers import CLIPModel, CLIPProcessor

  model_id = "openai/clip-vit-base-patch32"
  processor = CLIPProcessor.from_pretrained(model_id)
  model = CLIPModel.from_pretrained(model_id)

  # image는 PIL.Image라고 가정
  labels = ["a photo of a dog", "a photo of a car", "a photo of a tree"]
  inputs = processor(text=labels, images=image, return_tensors="pt", padding=True)

  with torch.no_grad():
      outputs = model(**inputs)
      probs = outputs.logits_per_image.softmax(dim=1)

  print(dict(zip(labels, probs[0].tolist())))
  ```
- 예시: Diffusers text-to-image 호출 패턴
  - text-to-image 모델은 prompt만으로 끝나지 않고 seed, guidance, inference step이 결과에 영향을 준다.
  - 공개 기록에는 생성 결과를 그대로 평가하기보다 어떤 조건으로 생성했는지 함께 남긴다.
  ```python
  import torch
  from diffusers import StableDiffusionPipeline

  device = "cuda" if torch.cuda.is_available() else "cpu"
  dtype = torch.float16 if device == "cuda" else torch.float32

  pipe = StableDiffusionPipeline.from_pretrained(
      "runwayml/stable-diffusion-v1-5",
      torch_dtype=dtype,
  )
  pipe = pipe.to(device)

  generator = torch.Generator(device=device).manual_seed(42)

  image = pipe(
      prompt="a clean product photo of a blue ceramic mug on a white table",
      negative_prompt="blurry, distorted, low quality",
      guidance_scale=7.5,
      num_inference_steps=30,
      generator=generator,
  ).images[0]
  ```
- 예시: Object Detection 결과 후처리 흐름
  - object detection 모델은 class label뿐 아니라 box 좌표와 score를 함께 반환한다.
  - threshold를 정해 낮은 confidence의 예측을 걸러낸다.
  ```python
  import torch
  from transformers import AutoImageProcessor, AutoModelForObjectDetection

  model_id = "hustvl/yolos-tiny"
  processor = AutoImageProcessor.from_pretrained(model_id)
  model = AutoModelForObjectDetection.from_pretrained(model_id)

  # image는 PIL.Image라고 가정
  inputs = processor(images=image, return_tensors="pt")

  with torch.no_grad():
      outputs = model(**inputs)

  target_sizes = torch.tensor([image.size[::-1]])
  results = processor.post_process_object_detection(
      outputs,
      threshold=0.5,
      target_sizes=target_sizes,
  )[0]

  for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
      print(model.config.id2label[label.item()], score.item(), box.tolist())
  ```
- 시각화로 이해한 포인트
  - RNN에서 Transformer로 이어지는 모델 발전 흐름을 도식으로 확인했다.
  - attention과 transformer 구조를 이미지로 확인했다.
  - object detection 결과와 text-to-image 생성 결과를 직접 출력해 확인했다.

## LangChain과 RAG
- AI Workflow
  - 단일 LLM 호출만으로 끝내지 않고, prompt, model, parser, retriever, tool을 연결해 작업 흐름을 만든다.
- LangChain
  - LLM 애플리케이션의 구성 요소를 체인 형태로 연결하기 위한 프레임워크이다.
  - prompt template, model call, output parser, retriever, vector store 등을 조합한다.
- ChatPromptTemplate
  - LLM에 보낼 메시지 형식을 템플릿으로 관리한다.
  - `from_template`
    - 하나의 문자열 템플릿을 만든다.
  - `from_messages`
    - system, user, assistant 같은 역할 메시지를 함께 구성한다.
- OutputParser
  - LLM 응답을 문자열, JSON, 구조화된 객체 등 원하는 형태로 정리한다.
- RunnableLambda
  - Python 함수를 LangChain 체인 안에서 실행 가능한 단계로 감싼다.
- Chain
  - prompt, model, parser 등을 순서대로 연결한 실행 흐름이다.
  - 비동기 실행을 사용하면 여러 요청을 동시에 처리할 수 있다.
- 비동기 실행
  - `asyncio`, `as_completed`, `nest_asyncio`를 사용하면 Jupyter 환경에서도 여러 LLM 요청을 병렬적으로 다룰 수 있다.
  - 오래 걸리는 모델 호출을 순차 처리하지 않고 완료되는 순서대로 모을 수 있다.
- RAG(Retrieval-Augmented Generation)
  - 외부 문서를 검색해 관련 context를 찾고, 그 context를 LLM 입력에 넣어 답변을 생성한다.
  - 모델 파라미터 안에 없는 최신 정보나 사내 문서를 활용할 때 유용하다.
- RAG 기본 파이프라인
  - 문서 로드
    - PDF, 웹페이지, 텍스트 파일 등을 읽는다.
  - 텍스트 분할
    - 긴 문서를 chunk 단위로 나눈다.
  - 임베딩
    - chunk를 벡터로 바꾼다.
  - 벡터 저장소
    - Chroma 같은 vector DB에 벡터를 저장한다.
  - 검색
    - 질문과 가까운 chunk를 찾는다.
  - 생성
    - 검색된 context와 질문을 함께 LLM에 전달한다.
- 문서 로더와 체인 구성 요소
  - `WebBaseLoader`
    - 웹페이지 HTML에서 텍스트를 가져올 때 사용한다.
  - `PyPDFLoader`
    - PDF 문서를 page 단위 document로 불러올 때 사용한다.
  - `RunnablePassthrough`
    - chain 안에서 입력 값을 그대로 다음 단계에 넘길 때 사용한다.
  - `format_docs`
    - 검색된 여러 document의 page content를 하나의 context 문자열로 합치는 helper 함수로 자주 사용한다.
- RAG에서 주의할 점
  - chunk 크기와 overlap 설정이 검색 품질에 영향을 준다.
  - 검색된 context가 틀리면 답변도 흔들린다.
  - prompt에는 “제공된 문맥에 없으면 모른다고 말하기” 같은 제약을 넣는 것이 좋다.
  - 긴 문서 실습에서는 ESG 리포트처럼 페이지와 이미지가 많은 PDF를 대상으로 문서 검색 흐름을 확인할 수 있다.
- 예시: LangChain Chain 기본 구조
  - prompt, model, parser를 연결해 하나의 실행 단위로 만든다.
  - 출력 parser를 붙이면 LLM 응답을 다음 단계에서 다루기 쉬워진다.
  ```python
  from langchain_openai import ChatOpenAI
  from langchain_core.prompts import ChatPromptTemplate
  from langchain_core.output_parsers import StrOutputParser

  prompt = ChatPromptTemplate.from_messages([
      ("system", "너는 친절한 AI 개념 설명자다."),
      ("user", "{topic}을 초보자에게 설명해줘."),
  ])

  model = ChatOpenAI(model="gpt-4o-mini")
  parser = StrOutputParser()

  chain = prompt | model | parser
  print(chain.invoke({"topic": "RAG"}))
  ```
- 예시: RAG 최소 파이프라인
  - 문서를 chunk로 나누고, 임베딩 후 vector store에 저장한다.
  - 질문과 가까운 chunk를 찾아 LLM에게 context로 제공한다.
  ```python
  from langchain_text_splitters import RecursiveCharacterTextSplitter
  from langchain_community.vectorstores import Chroma

  splitter = RecursiveCharacterTextSplitter(
      chunk_size=1000,
      chunk_overlap=200,
  )

  chunks = splitter.split_documents(documents)
  vectorstore = Chroma.from_documents(
      documents=chunks,
      embedding=embeddings,
  )

  retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
  related_docs = retriever.invoke("이 문서의 핵심 전략은 무엇인가?")
  ```
- 예시: PDF / Web 문서 로더
  - PDF는 page 단위 document로 읽히므로 page metadata를 함께 확인할 수 있다.
  - 웹 문서는 HTML에서 텍스트를 가져오되, 페이지 구조에 따라 불필요한 문구가 섞일 수 있다.
  ```python
  from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader

  pdf_loader = PyPDFLoader("report.pdf")
  pdf_docs = pdf_loader.load()
  print(pdf_docs[0].metadata)
  print(pdf_docs[0].page_content[:300])

  web_loader = WebBaseLoader("https://example.com/article")
  web_docs = web_loader.load()
  print(web_docs[0].page_content[:300])
  ```
- 예시: RunnablePassthrough를 이용한 RAG chain
  - 질문은 그대로 prompt에 넘기고, 같은 질문으로 검색한 문서는 context로 변환한다.
  - `format_docs`는 검색된 document를 하나의 문자열 context로 합치는 역할을 한다.
  ```python
  from langchain_core.prompts import ChatPromptTemplate
  from langchain_core.runnables import RunnablePassthrough
  from langchain_core.output_parsers import StrOutputParser

  def format_docs(docs):
      return "\n\n".join(doc.page_content for doc in docs)

  rag_prompt = ChatPromptTemplate.from_template("""
  제공된 문맥만 사용해서 질문에 답해줘.
  문맥에 답이 없으면 "문서에서 확인할 수 없습니다."라고 말해줘.

  문맥:
  {context}

  질문:
  {question}
  """)

  rag_chain = (
      {
          "context": retriever | format_docs,
          "question": RunnablePassthrough(),
      }
      | rag_prompt
      | model
      | StrOutputParser()
  )

  answer = rag_chain.invoke("이 문서의 핵심 전략은 무엇인가?")
  ```
- RAG 흐름 도식
  ```mermaid
  flowchart LR
      A[User Question] --> B[Retriever]
      C[Documents] --> D[Text Splitter]
      D --> E[Embedding]
      E --> F[Vector Store]
      F --> B
      B --> G[Context]
      G --> H[Prompt]
      A --> H
      H --> I[LLM]
      I --> J[Answer]
  ```
- Multi-Agent Orchestration 패턴
  - Orchestrator는 직접 결과를 만들지 않고 요청을 분류한다.
  - Planner는 작업 범위와 인수 조건을 정의한다.
  - Generator는 계획 범위 안에서 결과를 만든다.
  - Reviewer는 결과를 검증하고 위험과 누락을 찾는다.
  ```mermaid
  flowchart TD
      U[User Request] --> O[Orchestrator]
      O -->|요구사항 정리| P[Planner]
      O -->|결과 생성| G[Generator]
      O -->|검토 요청| R[Reviewer]
      P --> G
      G --> R
      R --> O
      O --> A[Final Output]
  ```
- AI Orchestration에서 배운 점
  - Agent를 하나로 크게 만들기보다 역할을 나누면 책임이 명확해진다.
  - Planner, Generator, Reviewer를 분리하면 “계획 없이 생성”하거나 “검토 없이 제출”하는 위험을 줄일 수 있다.
  - Python REPL 같은 도구를 Agent에 연결하면 계산과 검증을 자동화할 수 있지만, 도구 호출 권한과 입력 범위를 통제해야 한다.
- 역할별 프롬프트 설계
  - Planner
    - 요구사항을 정리하고 범위, 제약, 인수 조건을 정의한다.
    - 코드를 직접 작성하지 않는다.
  - Generator
    - Planner가 정한 범위와 기준 안에서 산출물을 만든다.
    - 계획을 임의로 확장하거나 바꾸지 않는다.
  - Reviewer
    - 산출물을 검토하고 동작, 인터페이스, 위험, 테스트 공백을 지적한다.
    - 직접 수정 코드를 작성하지 않는다.
  - 좋은 역할 프롬프트에는 역할, 목표, 금지사항, 입력 맥락, 출력 구조, 예시가 함께 들어간다.
- 도구 결합 Agent 설계
  - Agent가 도구를 사용할 때는 먼저 질문에서 핵심 키워드를 추출한다.
  - Wikipedia API나 Python REPL 같은 도구 결과를 근거로 답변을 만든다.
  - 도구 출처나 링크를 함께 남기면 답변 검증 가능성이 높아진다.
- 시각화로 이해한 포인트
  - AI workflow, chain 구성, RAG 흐름도를 통해 검색과 생성이 결합되는 방식을 확인했다.

## 유의점과 교훈
- 접근성 중심 웹 목업
  - 고령 사용자를 대상으로 한 서비스에서는 큰 글씨, 명확한 버튼, 고대비 모드, 최소 클릭 흐름이 중요하다.
  - 로그인/회원가입 mock을 만들 때도 `aria-live`, `aria-describedby`, focus 이동 같은 접근성 요소를 고려해야 한다.
  - client-side localStorage는 민감한 인증 정보를 보관하기에 안전하지 않다.
  - XSS 방지를 위해 사용자 입력은 출력 전에 sanitize하거나 escape해야 한다.
- 커뮤니티 웹 서비스 실습
  - 로그인, 회원가입, 게시글 CRUD, 댓글, 수정/삭제, 목록 이동 같은 상태 흐름을 localStorage로 구성했다.
  - 동적으로 생성되는 게시글 버튼은 이벤트 위임으로 처리할 수 있다.
  - localStorage 기반 mock은 실습에는 편하지만 실제 서비스 인증/권한/데이터 보관 방식으로는 부족하다.
- AI를 활용한 코드 리뷰
  - 리뷰는 “작동한다/안 한다”보다 위험, 누락, 테스트 공백을 찾는 활동이다.
  - localStorage 보안, 단순한 email regex, alert 사용, focus 관리 누락처럼 UI와 보안의 경계에 있는 문제가 중요했다.
  - 리뷰 결과를 다시 반영한 뒤에도 남은 risk를 문서화해야 한다.
- diff 기반 리뷰 기준
  - 변경사항이 실제 동작에 어떤 영향을 주는지 먼저 본다.
  - 입력/출력 인터페이스가 바뀌었는지 확인한다.
  - 보안 취약점, 성능 저하, 롤백 가능성, 누락된 테스트를 함께 점검한다.
- Kaggle / VQA 전략 메모
  - competition 규칙을 먼저 읽고, 허용되는 데이터/모델/추론 방식을 구분해야 한다.
  - VQA 문제에서는 이미지 인코더와 언어 모델의 연결 방식, prompt, fine-tuning, LoRA, quantization이 주요 선택지가 된다.
  - API 추론이 금지된 대회라면 외부 API 호출 없이 로컬/제출 가능한 모델로 재현성을 확보해야 한다.
  - data leakage 방지를 위해 test 데이터 접근, validation 구성, 제출 파일 생성 흐름을 엄격히 분리해야 한다.
- 학습 기록 기준
  - 개념을 먼저 말로 정의한 뒤 코드로 확인한다.
  - 코드 결과는 숫자만 보지 말고 그래프로 확인한다.
  - 모델 성능은 학습 데이터가 아니라 검증/테스트 데이터 기준으로 판단한다.
  - LLM 출력은 정답처럼 받아들이지 않고 근거, 형식, 재현성을 확인한다.
  - 생성 데이터는 품질 검수 없이 학습에 바로 넣지 않는다.
  - 공개용 기록에는 코드 원본보다 개념, 흐름, 주의점, 직접 이해한 내용을 남긴다.
