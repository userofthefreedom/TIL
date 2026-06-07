# WEB

- WEB이란?

  - 정의
    - 인터넷을 통해 문서(페이지)를 제공하고, 사용자가 브라우저로 접근하여 보는 시스템이다.
    - “웹(Web)”은 흔히 “인터넷(Internet)”과 같이 말하지만 둘은 다르다.
      - 인터넷: 전 세계 컴퓨터가 연결된 네트워크 자체
      - 웹: 인터넷 위에서 동작하는 서비스(문서/페이지 제공 시스템)

  - 왜 웹을 배우나
    - 웹은 대부분의 서비스가 제공되는 플랫폼이다.
    - HTML/CSS/JS를 배우면 “화면(페이지)을 만들고, 꾸미고, 움직이게” 할 수 있다.


- Web Site / Web Page

  - Web Site
    - 정의
      - 여러 Web Page가 모여 하나의 사이트(서비스)를 이룬다.
    - 예시
      - 네이버(사이트) 안에는: 메인 페이지, 로그인 페이지, 검색 결과 페이지 등 여러 페이지가 존재한다.

  - Web Page
    - 정의
      - 브라우저에서 보이는 “한 화면” 단위를 의미한다.
      - 보통 하나의 HTML 문서를 중심으로 구성된다.
    - 특징
      - 페이지는 HTML(구조) + CSS(스타일) + JS(동작)로 완성된다.


- Browser(브라우저)

  - 정의
    - 웹 페이지를 받아서 해석하고, 화면에 렌더링(Rendering)하는 프로그램이다.
  - 예시
    - Chrome, Edge, Safari, Firefox
  - 브라우저가 하는 일(핵심)
    - HTML을 해석하여 구조를 만든다.
    - CSS를 적용하여 모양(색, 크기, 위치)을 결정한다.
    - Javascript를 실행하여 동작을 처리한다.


- WEB의 3대 구성 요소

  - HTML
    - 역할
      - 웹 페이지의 “구조”를 만든다.
    - 예시(무엇을 올릴지)
      - 제목(h1), 문단(p), 이미지(img), 링크(a), 목록(ul/li) 등

  - CSS
    - 역할
      - 웹 페이지의 “스타일(디자인)”을 만든다.
    - 예시(어떻게 보일지)
      - 색상(color), 크기(font-size, width), 간격(margin/padding), 배치(display) 등

  - Javascript
    - 역할
      - 웹 페이지의 “동작”을 만든다.
    - 예시(무엇을 하게 할지)
      - 버튼 클릭 처리, 입력값 검증, 애니메이션, 서버 통신 등

- WEB 동작 과정(요청/응답 흐름)

  - 핵심 개념
    - 사용자가 브라우저로 “요청(Request)”을 보내면
    - 서버가 “응답(Response)”을 반환하고
    - 브라우저가 화면을 만든다(Rendering)

  - 1 단계: 주소 입력(URL)
    - 사용자가 주소를 입력한다.

          https://example.com

    - URL은 “어디에 요청할지”를 나타낸다.

  - 2 단계: 브라우저가 서버에 요청(Request)
    - 브라우저가 서버에게 “페이지 주세요”라고 요청한다.
    - 이 요청을 HTTP Request라고 부른다.

  - 3 단계: 서버가 응답(Response)
    - 서버는 보통 HTML 문서를 응답으로 보낸다.
    - 필요하다면 CSS/JS/이미지 파일도 추가로 받게 된다.
    - 이 응답을 HTTP Response라고 부른다.

  - 4 단계: 브라우저가 화면 생성(Rendering)
    - 브라우저는 보통 다음 순서로 화면을 만든다.
      - HTML 해석 → 구조 생성
      - CSS 적용 → 모양 결정
      - Javascript 실행 → 동작 처리

  - 중요한 포인트
    - “웹은 파일을 열어보는 것”이 아니라, 대부분 “서버와 통신해서 문서를 받는 것”이다.
    - 단, 개발 초반에는 로컬의 html 파일을 브라우저로 열어도 학습이 가능하다.

- (입문 보강) Client / Server

  - Client(클라이언트)
    - 정의
      - 서비스를 요청하는 쪽
    - 예시
      - 브라우저(Chrome)가 대표적인 클라이언트이다.

  - Server(서버)
    - 정의
      - 요청을 받아서 응답을 보내주는 쪽
    - 예시
      - 웹 서버(페이지 제공), API 서버(데이터 제공) 등

  - 요약
    - Client(브라우저) → Request → Server
    - Server → Response(HTML/CSS/JS/데이터) → Client(브라우저)

- Rendering이란?

  - 정의
    - 브라우저가 HTML/CSS/JS를 바탕으로 화면을 만들어 사용자에게 보여주는 과정이다.
  - 초보자가 자주 착각하는 점
    - “HTML을 작성하면 곧바로 화면이 된다”가 아니라
    - 브라우저가 HTML을 해석하고 스타일을 계산해서 “그려주는 과정”이 필요하다.

- 웹 학습 태도
  - 공식 문서 우선
    - 웹에는 유일한 정답보다 표준과 권장 방식이 중요하다.
    - HTML/CSS/JavaScript는 MDN 문서를 기준으로 확인한다.
    - Django, Vue 같은 프레임워크는 공식 문서를 먼저 확인한다.
  - 검색 방법
    - 에러 메시지는 그대로 검색한다.
    - 방법만 찾기보다 왜 그렇게 동작하는지 함께 확인한다.
    - 오래된 글은 현재 표준과 다를 수 있으므로 날짜와 버전을 확인한다.
  - AI 활용
    - 원하는 UI, 동작, 제약을 구체적으로 설명해야 좋은 답을 얻을 수 있다.
    - AI가 만든 코드는 그대로 믿지 않고 공식 문서와 브라우저 결과로 검증한다.
    - 디버깅할 때는 에러 메시지, 현재 코드, 기대 결과를 함께 제공한다.

## HTML

- HTML이란

  - 정의
    - 웹 페이지의 구조를 만드는 언어이다.
    - 웹 페이지에 어떤 요소가 있는지를 정의한다.
    - 제목, 문단, 이미지, 링크 등을 표현할 수 있다.

  - 특징
    - 프로그래밍 언어가 아니라 문서 구조 언어이다.
    - 태그(Tag)를 사용하여 문서를 구성한다.
    - 브라우저가 해석하여 화면으로 보여준다.

  - HTML과 CSS의 차이

    - HTML
      - 구조를 만든다.
      - 무엇이 있는지 정의한다.

    - CSS
      - 디자인을 만든다.
      - 어떻게 보일지 정의한다.

    - 예시

          <h1>Hello</h1>

      - HTML은 "제목이다" 라는 의미를 만든다.
      - 크기나 색상은 CSS가 담당한다.


- HyperText

  - 정의
    - 문서와 문서를 연결하는 기능이다.
    - 링크(Link)를 통해 다른 페이지로 이동할 수 있다.

  - 예시

        <a href="https://google.com">
        Google
        </a>

    - 클릭하면 다른 페이지로 이동한다.

- Markup Language

  - 정의
    - 태그(Tag)를 이용하여 문서 구조를 표현하는 언어이다.

  - 특징
    - 꺾쇠괄호 < > 를 사용한다.

          <p>Hello</p>

    - 태그를 이용해 의미를 표현한다.

  - 예시

        <h1>Title</h1>
        <p>Hello</p>

    - h1은 제목을 의미한다.
    - p는 문단을 의미한다.

- HTML 기본 구조

  - 기본 구조

        <!DOCTYPE html>
        <html>

        <head>
            <title>Page Title</title>
        </head>

        <body>

        </body>

        </html>

  - DOCTYPE

        <!DOCTYPE html>

    - HTML 문서라는 것을 브라우저에 알려준다.
    - HTML5 문서라는 것을 의미한다.
    - 표준 모드(Standard Mode)로 동작하도록 한다.
    - 없으면 브라우저가 비표준 모드로 동작할 수 있다.

  - html 태그

        <html>
        </html>

    - HTML 문서 전체를 감싸는 태그이다.
    - HTML 문서의 루트(root) 요소이다.
    - 모든 HTML 요소는 html 태그 안에 들어간다.

  - head 태그

        <head>
        </head>

    - 문서 설정 정보를 넣는 영역이다.
    - 화면에는 표시되지 않는다.

    - 예시 내용
      - title
      - CSS 연결
      - 문자 인코딩 설정

  - title 태그

        <title>Page Title</title>

    - 브라우저 탭 이름이 된다.

    - 예시

      - Chrome 탭에 표시된다.

  - body 태그

        <body>
        </body>

    - 실제 화면에 표시되는 내용을 넣는다.
    - 대부분의 HTML 코드는 body 안에 작성한다.

- HTML 태그(Tag)

  - 정의
    - 꺾쇠괄호 < > 로 이루어진 명령어이다.

  - 시작 태그

        <p>

  - 종료 태그

        </p>

  - 특징
    - 대부분 시작 태그와 종료 태그가 존재한다.

        <p>Hello</p>

  - 규칙
    - 먼저 열린 태그는 나중에 닫혀야 한다.

          <div>
              <p>Hello</p>
          </div>

    - 잘못된 예

          <div>
              <p>Hello
          </div>
          </p>

- HTML 요소(Element)

  - 정의
    - 시작 태그 + 내용 + 종료 태그 전체를 요소(Element)라고 한다.

          <p>Hello</p>

  - 구성

        <p> + Hello + </p>

  - Tag와 Element 차이

    - Tag

          <p>

    - Element

          <p>Hello</p>

    - 태그는 요소의 일부이다.

- HTML 구조 (중첩 구조)

  - 정의
    - 요소는 다른 요소 안에 들어갈 수 있다.

  - 예시

        <div>

            <p>Hello</p>

        </div>

  - 구조

        div
         └ p

    - div는 부모 요소이다.
    - p는 자식 요소이다.

  - 특징
    - HTML은 트리 구조(Tree Structure)를 가진다.

- HTML 속성(Attribute)

  - 정의
    - 태그에 추가 정보를 제공한다.

  - 구조

        name="value"

  - 위치
    - 시작 태그 안에 작성한다.

      ```html
      <a href="google.com">
      ```

  - 여러 속성 사용

        <a href="google.com" target="_blank">

  - 주요 속성

    - href

          <a href="google.com">

      - 링크 주소를 지정한다.

    - src

          <img src="image.png">

      - 이미지 파일 위치를 지정한다.

    - class

          <p class="menu">

      - CSS 적용 대상을 지정한다.
      - 여러 요소에 사용할 수 있다.

    - id

          <div id="header">

      - 특정 요소 하나를 지정한다.
      - 보통 하나만 사용한다.

- HTML 텍스트 구조

  - Heading

        <h1>Title</h1>

    - 제목을 나타낸다.
    - h1 ~ h6까지 존재한다.
    - h1이 가장 중요하다.

    - 구조 예시

          <h1>Book</h1>
          <h2>Chapter</h2>
          <h3>Section</h3>

  - Paragraph

        <p>Hello world</p>

    - 문단을 나타낸다.
    - 자동으로 줄바꿈이 된다.

    - 예시

          <p>Hello</p>
          <p>World</p>

  - Lists

        <ul>
            <li>Apple</li>
            <li>Banana</li>
        </ul>

    - 순서 없는 목록이다.

  - Ordered Lists

        <ol>
            <li>One</li>
            <li>Two</li>
        </ol>

    - 순서가 있는 목록이다.

  - li 태그

        <li>Apple</li>

    - 목록 항목을 나타낸다.
    - ul 또는 ol 안에 들어간다.

  - Emphasis

        <em>important</em>

    - 강조를 나타낸다.
    - 보통 기울임꼴로 표시된다.
    - 의미적으로 강조를 표현한다.

  - Strong

        <strong>important</strong>

    - 중요한 내용을 나타낸다.
    - 보통 굵게 표시된다.
    - 의미적으로 중요함을 나타낸다.

- div 태그

  - 정의
    - 영역을 나누는 태그이다.
    - 여러 요소를 묶는 역할을 한다.

  - 특징
    - 의미가 없는 일반적인 태그이다.
    - Layout 구성에 자주 사용된다.

  - 예시

        <div class="menu">
            <p>Home</p>
            <p>About</p>
        </div>

- span 태그

  - 정의
    - 텍스트 일부를 묶는 태그이다.

  - 특징
    - 문장 안에서 특정 부분만 선택할 때 사용한다.

  - 예시

        Price : <span>$10</span>

- Block 요소

  - 특징
    - 줄 전체를 차지한다.
    - 자동 줄바꿈이 된다.

  - 대표 요소

        div
        p
        h1
        ul

  - 예시

        <p>Hello</p>
        <p>World</p>

- Inline 요소

  - 특징
    - 줄 안에 표시된다.
    - 자동 줄바꿈이 없다.

  - 대표 요소

        span
        a
        em
        strong

  - 예시

        Hello <span>world</span>

- Semantic HTML

  - 정의
    - 의미가 있는 태그를 사용하여 문서 구조를 표현하는 방식이다.
    - 단순히 화면에 보이는 모양이 아니라, 해당 영역이 어떤 역할을 하는지 드러낸다.

  - 대표 태그

        header
        nav
        main
        section
        article
        aside
        footer

  - 사용 이유
    - 코드 구조를 읽기 쉬워진다.
    - 검색 엔진과 보조 기술이 페이지 구조를 이해하기 쉬워진다.
    - 유지보수할 때 영역의 역할을 빠르게 파악할 수 있다.

  - 예시

        <header>
            <h1>Book Service</h1>
        </header>

        <main>
            <section>
                <h2>Best Seller</h2>
            </section>
        </main>

- div / span 선택 기준

  - div
    - 여러 요소를 묶어 하나의 영역으로 다룰 때 사용한다.
    - Layout, card, section, container처럼 덩어리를 만들 때 적합하다.

  - span
    - 문장 안의 일부 텍스트만 따로 다룰 때 사용한다.
    - 특정 단어에 색상, 크기, 강조 스타일을 적용할 때 적합하다.

  - 핵심

        div  -> 영역을 묶는다.
        span -> 텍스트 일부를 묶는다.

- img 태그와 background-image

  - img 태그
    - 이미지 자체가 문서의 중요한 콘텐츠일 때 사용한다.
    - alt 속성을 통해 이미지의 의미를 설명할 수 있다.

        <img src="book.jpg" alt="책 표지">

  - background-image
    - 장식용 배경이나 레이아웃을 채우는 시각 요소에 사용한다.
    - CSS에서 크기, 반복, 위치를 함께 제어한다.

        .hero {
            background-image: url("hero.jpg");
            background-size: cover;
            background-position: center;
        }

  - 선택 기준
    - 사용자가 이미지 내용을 알아야 하면 img
    - 없어도 정보 전달에 문제가 없는 장식이면 background-image

- OOCSS

  - 정의
    - Object Oriented CSS의 약자이다.
    - CSS를 재사용 가능한 객체 단위로 나누어 작성하는 방식이다.

  - 핵심
    - 구조와 스킨을 분리한다.
    - 컨테이너와 콘텐츠를 분리한다.
    - 같은 스타일을 반복해서 새로 만들기보다 공통 클래스를 재사용한다.

  - 예시

        .card {
            padding: 16px;
            border-radius: 8px;
        }

        .card-primary {
            background: #0d6efd;
            color: white;
        }

## CSS

- CSS란

  - 정의
    - HTML 요소의 스타일을 지정하는 언어이다.
    - 웹 페이지의 디자인을 담당한다.
    - 색상, 크기, 위치 등을 지정할 수 있다.

  - 역할

    - HTML
      - 구조를 만든다.
      - 무엇이 있는지 정의한다.

    - CSS
      - 디자인을 만든다.
      - 어떻게 보일지 정의한다.

  - 예시

        <p>Hello</p>

        p {
            color:red;
        }

    - p 태그 글자가 빨간색이 된다.

- CSS 적용 방법

  - Inline 방식

        <p style="color:red;">
        Hello
        </p>

    - HTML 태그 안에 CSS를 작성하는 방식이다.
    - 특정 요소 하나에 스타일을 적용할 때 사용한다.
    - 관리가 어렵기 때문에 많이 사용하지 않는다.

  - Internal 방식

        <style>

        p {
            color:red;
        }

        </style>

    - HTML 파일 안에 CSS를 작성하는 방식이다.
    - head 태그 안에 작성한다.
    - 작은 프로젝트에서 사용한다.

  - External 방식

        <link rel="stylesheet" href="style.css">

    - CSS 파일을 따로 만들어 연결하는 방식이다.
    - 가장 많이 사용하는 방식이다.
    - 여러 HTML 파일에서 사용할 수 있다.

  - 파일 구조 예시

        index.html
        style.css

- CSS 구문(Syntax)

        p {

            color:red;

        }

  - Selector

        p

    - 스타일을 적용할 HTML 요소를 선택한다.

  - Property

        color

    - 변경할 속성을 의미한다.

  - Value

        red

    - 속성 값을 의미한다.

- CSS 선택자(Selector)

  - Tag 선택자

        p {
            color:red;
        }

    - 특정 태그 전체에 스타일을 적용한다.
    - 예시에서는 모든 p 태그 글자를 빨간색으로 만든다.
    - 가장 기본적인 선택자이다.

    - 적용 예시

          <p>A</p>
          <p>B</p>
          <p>C</p>

    - 결과
      - A B C 모두 빨간색이 된다.

  - Class 선택자

        .menu {
            color:red;
        }

    - class 속성을 가진 요소를 선택한다.
    - 가장 많이 사용하는 선택자이다.
    - 여러 요소에 적용할 수 있다.

    - HTML 예시

          <p class="menu">A</p>
          <p class="menu">B</p>

    - 결과
      - A B가 빨간색이 된다.

  - ID 선택자

        #header {
            color:red;
        }

    - id 속성을 가진 요소를 선택한다.
    - 보통 하나의 요소에만 사용한다.

    - HTML 예시

          <div id="header">
          </div>

  - Tag + Class 선택자

        p.menu {
            color:red;
        }

    - p 태그 중 class가 menu인 요소를 선택한다.

    - HTML 예시

          <p class="menu">A</p>
          <div class="menu">B</div>

    - 결과
      - A만 적용된다.

  - Attribute 선택자

        input[type="text"] {

        }

    - 특정 속성을 가진 요소를 선택한다.

    - HTML 예시

          <input type="text">
          <input type="password">

    - Attribute 값 선택

          [type="text"] {

          }

      - type이 text인 요소 선택한다.

    - 시작 선택

          [href^="https"]

      - https로 시작하는 요소 선택한다.

    - 끝 선택

          [src$=".png"]

      - png로 끝나는 요소 선택한다.

    - 포함 선택

          [class*="menu"]

      - menu를 포함하는 요소 선택한다.

- Cascade

  - 정의
    - 여러 CSS 규칙 중 어떤 스타일이 적용될지 결정하는 규칙이다.

  - 특징
    - 같은 선택자라면 아래쪽 CSS가 적용된다.

  - 예시

        p {
            color:blue;
        }

        p {
            color:red;
        }

    - 결과
      - 빨간색 적용된다.

- Specificity

  - 정의
    - 선택자 우선순위를 결정하는 규칙이다.

  - 우선순위

        Inline > ID > Class > Tag

  - 설명
    - Inline style이 가장 강하다.
    - ID 선택자가 Class보다 강하다.
    - Class 선택자가 Tag보다 강하다.

  - 예시

        p {
            color:blue;
        }

        .menu {
            color:red;
        }

    - 결과
      - 빨간색 적용된다.

  - !important

          color:red !important;

    - 우선순위를 강제로 높인다.

    - 특징
      - 다른 CSS보다 우선 적용된다.
      - 남용하면 관리가 어려워진다.

- CSS 단위(Unit)

  - px

        width:200px;

    - 고정 크기 단위이다.
    - 가장 많이 사용하는 단위이다.

  - %

        width:50%;

    - 부모 요소 기준 단위이다.

  - em

        font-size:2em;

    - 부모 font-size 기준 단위이다.
    - 중첩되면 계산이 어려워질 수 있다.

  - rem

        font-size:2rem;

    - html font-size 기준 단위이다.
    - 실무에서 많이 사용한다.

  - vw

        width:50vw;

    - 화면 너비 기준 단위이다.
    - 1vw는 화면 너비의 1%이다.

  - vh

        height:100vh;

    - 화면 높이 기준 단위이다.
    - 1vh는 화면 높이의 1%이다.

- CSS 상속과 값 제어 (Inheritance / inherit / initial / unset)

  - CSS 상속(Inheritance)이란

    - 정의
      - 부모 요소에 적용된 스타일이 자식 요소에 전달되는 현상이다.
      - HTML 요소는 부모-자식 구조를 가지므로 스타일이 전달될 수 있다.

    - 구조 예시

          <div>

              Hello
              <p>World</p>

          </div>

      - div는 부모 요소이다.
      - p는 자식 요소이다.

    - 상속 예시

          div {

              color:red;

          }

      - 결과
        - div 안의 모든 글자가 빨간색이 된다.
        - p 태그도 빨간색이 된다.

    - 특징
      - 모든 속성이 상속되는 것은 아니다.
      - 일부 속성만 상속된다.

  - 상속이 일어나는 이유

    - 목적
      - 문서 전체 스타일을 쉽게 적용하기 위해서이다.

    - 예시

          body {

              font-family:Arial;
              color:black;

          }

      - 결과
        - 페이지 전체 글자가 Arial 글꼴이 된다.
        - 대부분의 텍스트가 검은색이 된다.

    - 특징
      - 보통 body나 html에 기본 스타일을 설정한다.

  - 대표적으로 상속되는 속성

    - 특징
      - 텍스트 관련 속성은 대부분 상속된다.

    - color

          div {
              color:red;
          }

      - 자식 요소 글자도 빨간색이 된다.

    - font-size

          div {
              font-size:20px;
          }

      - 자식 요소도 20px이 된다.

    - font-family

          body {
              font-family:Arial;
          }

      - 전체 글꼴이 Arial이 된다.

    - font-weight

          div {
              font-weight:bold;
          }

      - 자식 글자도 굵어진다.

    - line-height

          div {
              line-height:2;
          }

      - 자식 요소도 적용된다.

    - text-align

          div {
              text-align:center;
          }

      - 자식 텍스트도 가운데 정렬된다.

    - visibility

          div {
              visibility:hidden;
          }

      - 자식 요소도 보이지 않는다.

    - 대표 속성 정리

          color
          font-size
          font-family
          font-weight
          line-height
          text-align
          visibility

  - 대표적으로 상속되지 않는 속성

    - 특징
      - Layout과 크기 관련 속성은 대부분 상속되지 않는다.

    - margin

          div {
              margin:20px;
          }

      - 자식 margin은 적용되지 않는다.

    - padding

          div {
              padding:20px;
          }

      - 자식 padding은 적용되지 않는다.

    - border

          div {
              border:1px solid black;
          }

      - 자식 border는 없다.

    - width

          div {
              width:200px;
          }

      - 자식 width는 자동이다.

    - height

          div {
              height:200px;
          }

      - 자식 height는 자동이다.

    - background

          div {
              background:red;
          }

      - 자식 background는 없다.
      - 부모 배경이 보일 뿐이다.

    - display

          div {
              display:flex;
          }

      - 자식 요소는 flex가 아니다.

    - position

          div {
              position:relative;
          }

      - 자식 요소는 relative가 아니다.

    - 대표 속성 정리

          margin
          padding
          border
          width
          height
          background
          display
          position

  - inherit

    - 정의
      - 부모 요소의 값을 그대로 사용한다.
      - 부모 값이 바뀌면 자식 값도 함께 바뀐다.
      - 자동 상속이 아닌 속성도 상속할 수 있다.

    - 예시 (color)

          .parent {
              color:red;
          }

          .child {
              color:inherit;
          }

      - 결과
        - child도 빨간색이 된다.

    - 예시 (border)

          .parent {
              border:1px solid black;
          }

          .child {
              border:inherit;
          }

      - 결과
        - child에도 border가 생긴다.

    - 특징
      - 부모 값을 그대로 따라간다.
      - 강제 상속을 만들 수 있다.

  - initial

    - 정의
      - 브라우저 기본값으로 되돌린다.
      - 부모 값과 관계없이 기본값을 사용한다.

    - 예시

          div {
              color:red;
          }

          p {
              color:initial;
          }

      - 결과
        - p는 기본 글자색이 된다.

    - 특징
      - 상속을 끊고 기본값으로 돌아간다.

  - unset

    - 정의
      - 상황에 따라 inherit 또는 initial처럼 동작한다.

    - 동작 규칙

          상속 속성 → inherit

          비상속 속성 → initial

    - 예시 (상속 속성)

          div {
              color:red;
          }

          p {
              color:unset;
          }

      - 결과
        - p는 빨간색이 유지된다.

    - 예시 (비상속 속성)

          div {
              margin:20px;
          }

          p {
              margin:unset;
          }

      - 결과
        - p margin은 기본값이 된다.

  - inherit vs initial vs unset 비교

        inherit → 부모값 사용

        initial → 기본값 사용

        unset → 자동 판단

  - 실무 예시

    - 링크 색상 부모와 동일하게 만들기

          a {
              color:inherit;
          }

      - 링크 색상이 부모와 같아진다.

    - 버튼 기본 스타일 제거

          button {
              all:unset;
          }

      - 모든 스타일이 제거된다.

- em / rem 선택 기준

  - em
    - 현재 요소 또는 부모 요소의 글자 크기를 기준으로 계산된다.
    - 컴포넌트 내부에서 글자 크기에 맞춰 여백과 크기가 함께 변해야 할 때 사용할 수 있다.

  - rem
    - html 요소의 글자 크기를 기준으로 계산된다.
    - 전체 페이지에서 일관된 크기 체계를 만들 때 많이 사용한다.

  - 주의
    - em은 중첩될수록 계산 기준이 달라질 수 있다.
    - 전체 spacing이나 font-size scale은 rem이 관리하기 쉽다.

  - 예시

        html {
            font-size: 16px;
        }

        .title {
            font-size: 2rem;
            margin-bottom: 1rem;
        }

        .button {
            padding: 0.5em 1em;
        }

## Layout

- Layout이란

  - 정의
    - 웹 페이지에서 요소들의 위치와 크기를 결정하는 것이다.
    - 요소를 어디에 배치할지 결정하는 작업이다.

  - 예시
    - 메뉴 영역
    - 본문 영역
    - 사이드바 영역

  - 특징
    - HTML은 구조를 만든다.
    - CSS Layout은 위치를 만든다.

- Block vs Inline

  - Block 요소

    - 특징
      - 줄 전체를 차지한다.
      - 자동으로 줄바꿈이 된다.
      - width 설정 가능하다.
      - height 설정 가능하다.
      - margin 설정 가능하다.
      - padding 설정 가능하다.

    - 대표 요소

          div
          p
          h1
          ul
          li

    - 예시

          <div>A</div>
          <div>B</div>

    - 결과

          A
          B

    - 세로로 배치된다.

  - Inline 요소

    - 특징
      - 줄 안에 표시된다.
      - 자동 줄바꿈이 없다.
      - 내용(content) 크기만큼만 공간을 차지한다.
      - width 설정이 제한된다.
      - height 설정이 제한된다.

    - 대표 요소

          span
          a
          em
          strong

    - 예시

          Hello <span>world</span>

    - 결과

          Hello world

    - 한 줄에 표시된다.

- Box Model

  - 정의
    - 모든 HTML 요소는 사각형(Box) 형태를 가진다.
    - 요소의 크기는 Box Model로 계산된다.

  - 구조

        Margin
        Border
        Padding
        Content

  - 설명

    - Content
      - 실제 내용이 들어가는 영역이다.

    - Padding
      - Content와 Border 사이의 공간이다.
      - 내부 여백이다.

    - Border
      - 요소의 테두리이다.

    - Margin
      - 요소 바깥 공간이다.
      - 다른 요소와의 거리를 만든다.

  - width

        width:200px;

    - Content 영역 크기이다.
    - 전체 크기가 아니다.

  - 예시

        div {

            width:200px;
            padding:20px;
            border:5px solid black;

        }

    - 전체 크기 계산

          200 + 20 + 20 + 5 + 5

    - 결과

          250px

  - padding

        padding:20px;

    - 내부 여백이다.

  - margin

        margin:20px;

    - 외부 여백이다.

  - border

        border:1px solid black;

    - 테두리이다.

  - box-sizing

        box-sizing:border-box;

    - width에 padding과 border를 포함한다.

    - 예시

          div {

              width:200px;
              padding:20px;
              box-sizing:border-box;

          }

    - 전체 크기가 200px로 유지된다.

- Display

  - 정의
    - 요소가 화면에 표시되는 방식을 결정하는 속성이다.
    - 요소의 배치 방법을 변경할 수 있다.
    - 태그의 기본 동작을 변경할 수 있다.

    - 예시

          div {
              display:inline;
          }

    - div를 inline처럼 사용할 수 있다.

  - block

        display:block;

    - 특징
      - 줄 전체를 차지한다.
      - 자동 줄바꿈이 된다.
      - width 설정 가능하다.
      - height 설정 가능하다.

    - 예시

          div {
              display:block;
          }

  - inline

        display:inline;

    - 특징
      - 줄 안에 표시된다.
      - 자동 줄바꿈이 없다.
      - width 설정이 제한된다.
      - height 설정이 제한된다.

    - 예시

          span {
              display:inline;
          }

  - inline-block

        display:inline-block;

    - 특징
      - 줄 안에 표시된다.
      - width 설정 가능하다.
      - height 설정 가능하다.
      - block과 inline의 특징을 함께 가진다.

    - 예시

          div {
              display:inline-block;
              width:100px;
              height:50px;
          }

    - 결과
      - 가로로 배치되면서 크기를 지정할 수 있다.

  - none

        display:none;

    - 특징
      - 요소가 화면에서 사라진다.
      - 공간도 함께 사라진다.

    - 예시

          .menu {
              display:none;
          }

- Position

  - 정의
    - 요소의 “위치 배치 방식”을 결정하는 속성이다.
    - display가 “줄 배치 방식(block/inline)”을 정한다면,
      - position은 “특정 좌표(top/left 등)로 옮길 수 있는지 / 무엇을 기준으로 옮기는지”를 정한다.
    - position은 보통 top / left / right / bottom 과 함께 사용된다.

  - position 종류
    - static
    - relative
    - absolute
    - fixed
    - sticky

  - top / left / right / bottom 기본 개념
    - 숫자를 주면 “이동”하는 게 아니라 “해당 방향에서 떨어진 거리”를 의미한다.
    - 그래서 헷갈릴 수 있다.

    - top: 20px
      - “위에서 20px 떨어져라” 라는 뜻
      - 결과적으로 아래로 내려간 것처럼 보인다.

    - left: 20px
      - “왼쪽에서 20px 떨어져라”
      - 결과적으로 오른쪽으로 이동한 것처럼 보인다.

  - position: static (기본값)

    - 특징
      - 모든 요소의 기본값이다.
      - 문서의 기본 흐름(위에서 아래, 왼쪽에서 오른쪽)에 따라 배치된다.
      - top/left/right/bottom이 적용되지 않는다.

    - 예시

          .box {
              position:static;
              top:50px;      /* 적용되지 않음 */
              left:50px;     /* 적용되지 않음 */
          }

    - 결과
      - 화면 변화가 없다.

  - position: relative

    - 정의
      - “원래 있어야 할 위치(기본 흐름에서의 위치)”를 기준으로 이동한다.

    - 특징
      - top/left/right/bottom이 적용된다.
      - 이동해도 “원래 자리(공간)”가 유지된다.
        - 겉으로는 이동하지만, 주변 요소는 원래 자리 기준으로 배치된 것처럼 남아있다.

    - 예시

          <div>A</div>
          <div class="box">B</div>
          <div>C</div>

          .box {
              position:relative;
              left:40px;
              top:10px;
          }

    - 결과
      - B가 오른쪽/아래로 이동한다.
      - 하지만 B의 원래 공간은 유지되어 A와 C의 위치는 크게 바뀌지 않는다.

    - 매우 중요한 용도(실무 핵심)
      - absolute의 기준점(부모)을 만들기 위해 사용한다.
      - 즉, “부모를 relative로 만든다”는 패턴이 매우 흔하다.

  - position: absolute (가장 중요)

    - 정의
      - “문서 흐름에서 빠져나와서” 특정 기준점에 붙어서 배치된다.

    - 특징 1 : 공간을 차지하지 않는다
      - absolute를 주면 요소가 흐름에서 빠져나간다.
      - 즉, 주변 요소는 그 요소가 없는 것처럼 배치된다.
      - 그래서 요소가 겹쳐 보일 수 있다.

    - 특징 2 : 기준점이 필요하다
      - absolute는 “가장 가까운 position이 설정된 조상 요소”를 기준으로 한다.
      - 여기서 position이 설정된 조상 요소란 보통 relative인 부모를 말한다.

    - 기준점 규칙(초보 핵심)
      - 가까운 조상 중에서 position이 static이 아닌 요소를 기준으로 한다.
      - 대부분 이렇게 만든다.

            .parent {
                position:relative;
            }

            .child {
                position:absolute;
            }

      - 만약 기준점이 없으면(조상에 position 설정이 없으면)
        - 브라우저 화면(문서 전체)을 기준으로 배치되는 것처럼 보인다.

    - 예시 1 : 부모 기준으로 배치하기 (정석)

          <div class="parent">
              <div class="child">BOX</div>
          </div>

          .parent {
              position:relative;
              width:300px;
              height:200px;
              border:1px solid black;
          }

          .child {
              position:absolute;
              top:20px;
              left:30px;
              width:80px;
              height:40px;
              border:1px solid black;
          }

    - 결과
      - child는 parent 내부의 (top:20, left:30) 위치에 배치된다.

    - 예시 2 : absolute는 공간이 사라진다 (겹침)

          <div>A</div>
          <div class="box">B</div>
          <div>C</div>

          .box {
              position:absolute;
              top:0;
              left:0;
          }

    - 결과
      - B는 문서 흐름에서 빠져나가며 A, C는 “B가 없는 것처럼” 배치된다.
      - B는 화면 좌상단 근처로 이동하며 다른 요소와 겹칠 수 있다.

    - 언제 쓰나(대표 예시)
      - 뱃지(badge) 붙이기: “NEW”, “HOT”
      - 카드 이미지 위 텍스트 올리기
      - 모달, 드롭다운 같은 떠있는 UI
      - 특정 영역의 한쪽 모서리에 요소 고정(부모 기준)

  - position: fixed

    - 정의
      - 브라우저 화면(Viewport)을 기준으로 고정된다.

    - 특징
      - 스크롤을 내려도 같은 위치에 유지된다.
      - absolute처럼 흐름에서 빠져나와 공간을 차지하지 않는다.

    - 예시

          .chat {
              position:fixed;
              right:20px;
              bottom:20px;
              width:60px;
              height:60px;
              border:1px solid black;
          }

    - 결과
      - 화면 오른쪽 아래에 고정된 버튼처럼 보인다.
      - 스크롤해도 위치가 유지된다.

    - 언제 쓰나(대표 예시)
      - “맨 위로” 버튼
      - 채팅 버튼
      - 고정 상단/하단 바(단, 요즘은 sticky도 자주 사용)

  - position: sticky

    - 정의
      - 기본은 문서 흐름에 따라 움직이지만,
      - 특정 위치(top 등)에 도달하면 그 자리에서 고정된다.

    - 필수 조건(중요)
      - 보통 top 값을 같이 써야 동작한다.

            position:sticky;
            top:0;

    - 예시

          .menu {
              position:sticky;
              top:0;
              border:1px solid black;
          }

    - 결과
      - 스크롤 전에는 일반 요소처럼 있다가,
      - 스크롤로 top:0 위치에 닿으면 상단에 붙어서 고정된다.

    - fixed와 차이
      - fixed는 항상 고정
      - sticky는 “닿을 때만” 고정

  - z-index (겹침 순서)

    - 정의
      - 요소가 겹칠 때 “누가 위에 보일지”를 결정한다.
      - position이 static이 아닌 요소(또는 특정 상황)에서 의미가 커진다.

    - 예시

          .a {
              position:absolute;
              z-index:1;
          }

          .b {
              position:absolute;
              z-index:2;
          }

    - 결과
      - z-index가 큰 요소가 위에 보인다.

    - 주의
      - z-index는 “같은 기준(같은 stacking context)”에서 비교된다.
      - 초보 단계에서는 “숫자가 크면 위”라고 이해해도 충분하다.

- Flexbox

  - 정의
    - 요소들을 가로나 세로 방향으로 정렬하는 Layout 방식이다.
    - 부모 요소(Container)에 display:flex를 적용하면 자식 요소(Item)들이 flex 방식으로 배치된다.
    - 요소 정렬(Layout)을 만들 때 가장 많이 사용하는 방법이다.

  - 기본 사용 방법

        .container {
            display:flex;
        }

    - 부모 요소가 Flex Container가 된다.
    - 자식 요소들이 Flex Item이 된다.

  - 기본 예시

        <div class="container">

            <div>A</div>
            <div>B</div>
            <div>C</div>

        </div>


        .container {
            display:flex;
        }

    - 결과
      - A B C 가 가로로 배치된다.
      - 기본 block 요소는 세로로 배치되지만 flex에서는 가로 배치된다.

  - Container와 Item

    - Container
      - display:flex가 적용된 부모 요소이다.

            .container {
                display:flex;
            }

    - Item
      - Container 안에 들어있는 자식 요소이다.

            <div class="container">

                <div>A</div>
                <div>B</div>

            </div>

    - 구조

            Container
              ├ Item
              ├ Item
              └ Item

  - Flex 축 개념 (매우 중요)

    - Main Axis
      - 아이템이 배치되는 기본 방향이다.

    - Cross Axis
      - Main Axis와 수직 방향이다.

    - 기본 상태

            display:flex;

    - 구조

            Main Axis → 가로 방향

            Cross Axis ↓ 세로 방향


    - 결과

            A B C

  - flex-direction

    - 정의
      - Main Axis 방향을 결정한다.

    - row (기본값)

            .container {
                display:flex;
                flex-direction:row;
            }

      - Main Axis = 가로
      - Cross Axis = 세로

      - 결과

            A B C

    - column

            .container {
                display:flex;
                flex-direction:column;
            }

      - Main Axis = 세로
      - Cross Axis = 가로

      - 결과

            A
            B
            C


    - 매우 중요한 특징
      - column이 되면 justify-content와 align-items 방향이 바뀐다.

  - justify-content

    - 정의
      - Main Axis 방향 정렬을 결정한다.

    - center

            justify-content:center;

      - 가운데 정렬

            A B C

    - flex-start

            justify-content:flex-start;

      - 시작 위치 정렬

    - flex-end

            justify-content:flex-end;

      - 끝 위치 정렬

    - space-between

            justify-content:space-between;

      - 양 끝 정렬 + 사이 공간 동일

            A     B     C

    - space-around

            justify-content:space-around;

      - 양쪽 공간 포함 균등 분배

  - align-items

    - 정의
      - Cross Axis 방향 정렬을 결정한다.

    - center

            align-items:center;

      - 세로 가운데 정렬

    - flex-start

            align-items:flex-start;

      - 위쪽 정렬

    - flex-end

            align-items:flex-end;

      - 아래쪽 정렬

  - justify-content vs align-items (핵심)

    - row일 때

      - justify-content
        - 가로 정렬

      - align-items
        - 세로 정렬

    - column일 때

      - justify-content
        - 세로 정렬

      - align-items
        - 가로 정렬

  - gap

    - 정의
      - Flex Item 사이 간격을 만든다.

    - 예시

            .container {

                display:flex;
                gap:20px;

            }

      - 결과

            A   B   C


    - 특징
      - Item 사이 간격만 생긴다.
      - 가장자리에는 간격이 생기지 않는다.
      - margin보다 관리가 쉽다.

  - flex-wrap

    - 정의
      - 줄바꿈 허용 여부를 결정한다.

    - nowrap (기본값)

            flex-wrap:nowrap;

      - 줄바꿈이 발생하지 않는다.

    - wrap

            flex-wrap:wrap;

      - 줄바꿈이 발생한다.

      - 결과

            A B C
            D E F


    - 대표 사용 예
      - 카드 Layout
      - 상품 목록

  - align-content

    - 정의
      - 여러 줄이 있을 때 줄 전체 정렬을 결정한다.

    - 특징
      - flex-wrap:wrap 상태에서만 동작한다.

    - 예시

            .container {

                display:flex;
                flex-wrap:wrap;
                height:300px;

                align-content:center;

            }

      - 결과
        - 여러 줄이 가운데 정렬된다.

  - flex-grow

    - 정의
      - 남는 공간을 얼마나 차지할지 결정한다.

    - 예시

            .container {
                display:flex;
                width:400px;
            }

            .a {
                flex-grow:1;
            }

            .b {
                flex-grow:1;
            }

      - 결과
        - 같은 크기로 확장된다.

    - 비율 예시

            .a {
                flex-grow:1;
            }

            .b {
                flex-grow:2;
            }

      - 결과
        - b가 a보다 2배 넓어진다.

  - flex-shrink

    - 정의
      - 공간이 부족할 때 얼마나 줄어들지 결정한다.

    - 기본값

            flex-shrink:1;

      - 줄어든다.

    - 줄어들지 않게

            flex-shrink:0;

      - 크기가 유지된다.

  - flex-basis

    - 정의
      - Flex Item의 기본 크기를 결정한다.

    - 예시

            flex-basis:200px;

      - 기본 크기가 200px이 된다.

  - flex (축약형)

    - 정의
      - flex-grow, flex-shrink, flex-basis를 한번에 설정한다.

    - 예시

            flex:1;

      - 의미

            flex-grow:1
            flex-shrink:1
            flex-basis:0

    - 대표 사용 방법

            .box {

                flex:1;

            }

      - 모든 아이템이 같은 크기가 된다.

- Grid

  - 정의
    - 행(Row)과 열(Column)을 이용해 요소를 배치하는 Layout 방식이다.
    - Flexbox와 달리 2차원 Layout을 만들 수 있다.
    - 페이지 전체 구조를 만들 때 많이 사용된다.

  - Flexbox와 Grid 차이

    - Flexbox
      - 한 방향 Layout이다.
      - 가로나 세로 중 한 방향 정렬에 사용한다.

            A B C

      - 메뉴 정렬이나 버튼 정렬에 적합하다.

    - Grid
      - 두 방향 Layout이다.
      - 행과 열을 동시에 제어할 수 있다.

            A B C
            D E F

      - 페이지 Layout에 적합하다.

  - 기본 사용 방법

        .container {

            display:grid;

        }

    - 부모 요소가 Grid Container가 된다.
    - 자식 요소가 Grid Item이 된다.

  - 기본 예시

        <div class="container">

            <div>A</div>
            <div>B</div>
            <div>C</div>

        </div>


        .container {

            display:grid;

        }


    - 결과

            A
            B
            C

    - 기본 배치는 세로 방향이다.

  - grid-template-columns

    - 정의
      - 열(Column)의 개수와 크기를 결정한다.

    - 예시

        grid-template-columns:100px 100px 100px;


    - 결과

            A B C


    - 특징
      - 값의 개수만큼 열이 생성된다.

    - 예시

        grid-template-columns:200px 100px;


    - 결과

            A B
            C D
            E F

    - 열은 2개가 된다.

  - grid-template-rows

    - 정의
      - 행(Row)의 높이를 결정한다.


    - 예시

        grid-template-rows:100px 200px;


    - 결과
      - 첫 번째 행 높이는 100px
      - 두 번째 행 높이는 200px

    - 예시

        .container {

            display:grid;

            grid-template-columns:1fr 1fr;
            grid-template-rows:100px 200px;

        }

  - fr 단위

    - 정의
      - 남은 공간을 비율로 나누는 단위이다.

    - 예시

        grid-template-columns:1fr 1fr;


    - 결과
      - 두 열이 같은 크기가 된다.

    - 예시

        grid-template-columns:1fr 2fr;


    - 결과
      - 두 번째 열이 두 배 넓어진다.

  - px와 fr 차이

    - px

        grid-template-columns:200px 200px;

      - 고정 크기이다.

    - fr

        grid-template-columns:1fr 1fr;

      - 화면 크기에 따라 변한다.

  - gap

    - 정의
      - Grid Item 사이 간격을 만든다.

    - 예시

        .container {

            display:grid;

            grid-template-columns:1fr 1fr;

            gap:20px;

        }


    - 결과

            A   B
            C   D


    - 특징
      - 요소 사이 간격만 생긴다.
      - 가장자리에는 간격이 생기지 않는다.

  - Grid 자동 배치

    - 정의
      - Grid는 자동으로 요소를 배치한다.

    - 예시

        grid-template-columns:1fr 1fr;


        A B C D E F


    - 결과

            A B
            C D
            E F

  - Grid 선(Line) 개념

    - 특징
      - Grid는 칸이 아니라 선 번호 기준으로 동작한다.


    - 예시

        grid-template-columns:1fr 1fr 1fr;


    - 구조

            1   2   3   4
            | A | B | C |


    - 열이 3개이면 선은 4개이다.

  - grid-column

    - 정의
      - 요소가 차지하는 열 범위를 지정한다.


    - 예시

        .box {

            grid-column:1 / 3;

        }


    - 결과

            A A B
            C D E


    - 설명
      - 1번 선부터 3번 선까지 사용한다.
      - 두 칸을 차지한다.

  - grid-row

    - 정의
      - 요소가 차지하는 행 범위를 지정한다.


    - 예시

        .box {

            grid-row:1 / 3;

        }


    - 결과

            A B
            A C


    - 설명
      - 세로 방향으로 확장된다.

  - span

    - 정의
      - 몇 칸을 차지할지 지정한다.

    - 예시

        .box {

            grid-column:span 2;

        }


    - 결과

            A A B
            C D E


    - 특징
      - 현재 위치 기준으로 확장된다.

  - grid-column과 span 차이

    - grid-column:1 / 3

      - 1번 선에서 3번 선까지 이동한다.

    - grid-column:span 2

      - 현재 위치에서 2칸 차지한다.

  - grid-column + grid-row

    - 예시

        .box {

            grid-column:1 / 3;
            grid-row:1 / 3;

        }


    - 결과

            A A B
            A A C
            D E F

    - 특징
      - 2 x 2 영역을 차지한다.

  - 실전 Layout 예시

    - 구조

            Header Header
            Menu   Content
            Footer Footer

    - CSS

        .container {

            display:grid;

            grid-template-columns:200px 1fr;

            grid-template-rows:80px 1fr 80px;

            gap:10px;

        }


        .header {

            grid-column:1 / 3;

        }


        .menu {

            grid-column:1;

        }


        .content {

            grid-column:2;

        }


        .footer {

            grid-column:1 / 3;

        }

    - 결과

            Header Header
            Menu   Content
            Footer Footer

  - grid-template-areas

    - 정의
      - Grid 영역에 이름을 붙여 Layout 구조를 문자열로 표현하는 방식이다.
      - 복잡한 페이지 구조를 눈으로 읽기 쉽게 만들 수 있다.

    - 예시

        .container {
            display: grid;
            grid-template-columns: 200px 1fr;
            grid-template-rows: 80px 1fr 80px;
            grid-template-areas:
                "header header"
                "menu   content"
                "footer footer";
            gap: 10px;
        }

        .header {
            grid-area: header;
        }

        .menu {
            grid-area: menu;
        }

        .content {
            grid-area: content;
        }

        .footer {
            grid-area: footer;
        }

    - 장점
      - Layout 구조를 CSS만 보고도 파악하기 쉽다.
      - 반응형에서 영역 배치를 바꿀 때 유용하다.

    - 주의
      - 같은 행 안의 영역 문자열 개수는 column 개수와 맞아야 한다.
      - 직사각형이 아닌 형태의 영역은 만들 수 없다.

- overflow

  - 개념
    - 요소(box)의 크기보다 내용이 더 클 때 **넘친 부분을 어떻게 처리할지 결정하는 CSS 속성**
    - 박스보다 내용이 크면 overflow가 발생함
    - 레이아웃 제어에서 매우 자주 사용되는 속성

  - 기본 구조

    overflow: 값;

    대표 값:

    overflow: visible;
    overflow: hidden;
    overflow: scroll;
    overflow: auto;


  - 동작 원리

    box 크기 > 내용 크기
    → 정상 표시

    box 크기 < 내용 크기
    → overflow 발생

    overflow는 반드시 **크기(width 또는 height)가 있어야 작동함**

    예시:

    height: 200px;
    overflow: auto;


  - overflow: visible

    - 기본값 (default)
    - 내용이 넘쳐도 그대로 표시됨
    - 박스 밖으로 내용이 튀어나옴

    예시:

    div {
        width: 200px;
        height: 100px;
        overflow: visible;
    }


  - overflow: hidden

    - 넘친 부분을 잘라서 숨김
    - 박스 영역 밖의 내용은 보이지 않음
    - 레이아웃 정리에 자주 사용됨

    예시:

    div {
        width: 200px;
        height: 100px;
        overflow: hidden;
    }

    사용 예:

    - 이미지 자르기
    - 둥근 모서리 처리

    예:

    border-radius: 20px;
    overflow: hidden;


  - overflow: scroll

    - 항상 스크롤바가 생성됨
    - 내용이 넘치지 않아도 스크롤 표시됨
    - 실무에서는 거의 사용하지 않음

    예시:

    div {
        width: 200px;
        height: 100px;
        overflow: scroll;
    }


  - overflow: auto

    - 내용이 넘칠 때만 스크롤 생성
    - 넘치지 않으면 스크롤 없음
    - 실무에서 가장 많이 사용됨

    예시:

    div {
        width: 200px;
        height: 100px;
        overflow: auto;
    }


  - 방향별 overflow

    가로 스크롤

    overflow-x: auto;

    - 가로 방향만 스크롤 생성

    세로 스크롤

    overflow-y: auto;

    - 세로 방향만 스크롤 생성


  - overflow가 작동하는 조건 (중요 ⭐)

    overflow는 반드시 크기가 있어야 동작함

    예:

    overflow: auto;

    → 아무 일도 안 일어남

    반드시:

    height: 200px;
    overflow: auto;

    또는:

    width: 300px;
    overflow: auto;


  - 실무 사용 패턴

    1) 스크롤 박스

    height: 300px;
    overflow: auto;

    사용 예:

    - 채팅창
    - 리스트
    - 메뉴


    2) 이미지 자르기

    overflow: hidden;

    사용 예:

    - 카드 UI
    - 프로필 이미지


    3) 가로 스크롤

    overflow-x: auto;

    사용 예:

    - 테이블
    - 코드 영역

- Responsive Web / Breakpoint

  - Responsive Web
    - 화면 크기에 따라 Layout과 요소 크기가 자연스럽게 바뀌는 웹 페이지를 말한다.
    - 모바일, 태블릿, 데스크톱처럼 다양한 화면에서 같은 콘텐츠를 보기 좋게 제공하는 것이 목적이다.

  - Breakpoint
    - Layout이 바뀌는 기준 화면 너비이다.
    - CSS에서는 주로 media query로 지정하고, Bootstrap에서는 정해진 breakpoint class를 사용한다.

  - Media Query 기본 형태

        @media (min-width: 768px) {
            .container {
                display: grid;
                grid-template-columns: 240px 1fr;
            }
        }

  - 설계 순서
    - 작은 화면에서 먼저 세로 흐름을 만든다.
    - 화면이 넓어질 때 column, grid, card 개수를 늘린다.
    - 이미지와 텍스트가 부모 영역을 넘치지 않는지 확인한다.

  - Bootstrap breakpoint 예시

        col-12      -> 모든 화면에서 12칸
        col-md-6    -> md 이상에서 6칸
        col-lg-4    -> lg 이상에서 4칸

  - 주의
    - 반응형은 단순히 작아지는 것이 아니라 배치가 다시 구성되는 것이다.
    - 고정 width를 많이 쓰면 작은 화면에서 overflow가 생기기 쉽다.

## Bootstrap

- Bootstrap

  - 정의
    - 웹사이트 디자인을 빠르게 만들기 위한 CSS + JavaScript 라이브러리이다.
    - 버튼, 메뉴, 카드, 팝업창 같은 UI를 class만으로 만들 수 있다.
    - CSS를 직접 작성하지 않아도 기본 디자인이 적용된다.
    - 실무에서 매우 많이 사용되는 프레임워크이다.

  - CDN

    - 정의
      - Bootstrap 파일을 인터넷에서 바로 가져오는 방식이다.
      - Bootstrap을 설치하지 않고 사용할 수 있다.

    - Bootstrap CSS 연결

          <link href="https://cdn.jsdelivr.net/npm/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">

      - Bootstrap 디자인을 적용하기 위해 필요하다.

    - Bootstrap JavaScript 연결

          <script src="https://cdn.jsdelivr.net/npm/bootstrap/dist/js/bootstrap.bundle.min.js"></script>

      - Bootstrap 기능을 사용하기 위해 필요하다.

    - JavaScript가 필요한 기능

      - Navbar 버튼
      - Dropdown
      - Carousel
      - Modal

  - 기본 사용 방법

    - Bootstrap은 class 중심 구조이다.

          태그 class="bootstrap-class"

    - class를 추가하면 디자인이 적용된다.

    - 예시

          <button class="btn btn-primary">버튼</button>

    - Bootstrap 사용 순서

      1 Bootstrap 연결
      2 HTML 작성
      3 class 추가

  - Reset CSS

    - 정의
      - 브라우저 기본 스타일을 초기화하는 것이다.

    - 브라우저 기본 스타일 예

      - h1 → 큰 글자
      - p → margin 존재
      - ul → 들여쓰기 존재

    - Bootstrap 특징

      - 폰트 통일
      - margin 정리
      - 줄 간격 통일

    - Bootstrap은 Reset CSS가 포함되어 있다.

  - 활용 영역

    - Typography
      - 글자 스타일을 설정하는 기능이다.

    - Colors
      - 글자색과 배경색을 설정하는 기능이다.

    - Component
      - 완성된 UI 부품이다.

  - Typography

    - 정의
      - 글자의 크기와 스타일을 설정하는 기능이다.

    - Display 글자 크기

          <h1 class="display-1">Display 1</h1>

      - display-1 → 가장 큰 글자
      - display-6 → 작은 글자

      - 사이트 제목에 많이 사용된다.

    - 글자 스타일 태그

      - 형광펜

            <mark>text</mark>

      - 취소선

            <del>text</del>

      - 밑줄

            <ins>text</ins>

      - 굵은 글씨

            <strong>text</strong>

      - 기울임

            <em>text</em>

  - Colors

    - 정의
      - Bootstrap에서 제공하는 색상 시스템이다.

    - 글자 색상

          class="text-primary"

      - primary → 파랑
      - success → 초록
      - danger → 빨강
      - warning → 노랑
      - info → 하늘색
      - dark → 검정
      - light → 밝은색

    - 배경 색상

          class="bg-dark"

    - 사용 예

          class="text-warning bg-dark"

      - 글자색 노랑
      - 배경색 검정

    - 특징

      - 색상 이름만 기억하면 사용할 수 있다.

  - Component

    - 정의
      - Bootstrap에서 제공하는 완성된 UI 부품이다.

    - Navbar

      - 정의
        - 웹사이트 상단 메뉴이다.

      - 구성 요소

        - 로고
        - 메뉴
        - 검색창

    - Alert

      - 정의
        - 알림 메시지를 표시하는 Component이다.

      - 종류

        - alert-success
        - alert-danger
        - alert-warning
        - alert-info

    - Badge

      - 정의
        - 작은 표시를 나타내는 Component이다.

      - 사용 예

        - NEW 표시
        - 공지 표시

    - Card

      - 정의
        - 정보를 박스 형태로 표시하는 Component이다.

      - 사용 예

        - 상품 표시
        - 게시글 표시

      - 구성 요소

        - 이미지
        - 제목
        - 설명
        - 버튼

    - Carousel

      - 정의
        - 이미지를 슬라이드 형태로 표시하는 Component이다.

      - 사용 예

        - 쇼핑몰 배너
        - 메인 화면 이미지

    - Modal

      - 정의
        - 팝업창을 표시하는 Component이다.

    - 사용 예

      - 로그인 창
      - 회원가입 창

- Bootstrap 프로젝트 구성 패턴

  - 개념
    - Bootstrap 프로젝트는 보통 재사용 가능한 Component와 Grid Layout을 조합하여 페이지를 만든다.
    - 먼저 큰 영역을 나누고, 각 영역 안에 Navbar, Card, Carousel, Modal 같은 컴포넌트를 배치한다.

  - 기본 구성 순서

        1. 페이지 영역 나누기
        2. Bootstrap CSS / JS 연결
        3. Navbar 작성
        4. Grid system으로 section 배치
        5. Card, Carousel, Modal 등 Component 적용
        6. 이미지와 폰트 assets 연결
        7. breakpoint별 화면 확인

  - 자주 쓰는 조합

    - Navbar
      - 페이지 상단 메뉴와 브랜드 영역을 만든다.

    - Card
      - 도서, 상품, 게시글처럼 반복되는 정보를 한 덩어리로 표현한다.

    - Carousel
      - 주요 이미지나 추천 콘텐츠를 슬라이드로 보여준다.

    - Modal
      - 로그인, 상세 보기, 확인 창처럼 현재 화면 위에 임시 UI를 띄운다.

    - Grid system
      - 모바일에서는 `col-12`, 넓은 화면에서는 `col-md-6`, `col-lg-4`처럼 카드 개수를 조절한다.

  - assets 관리

        assets/
          images/
          fonts/
          css/

    - 이미지와 폰트는 경로가 틀리면 화면에 보이지 않는다.
    - 상대 경로 기준이 현재 HTML 파일 위치인지 먼저 확인한다.

  - 주의
    - Bootstrap class가 길어지면 영역별로 주석이나 구조를 정리해두는 것이 좋다.
    - Component는 그대로 복사하기보다 프로젝트 목적에 맞게 텍스트, 이미지, 간격을 조정한다.
    - 반응형 화면은 넓은 화면과 좁은 화면을 모두 확인해야 한다.

- Bootstrap Layout

  - 정의
    - 웹페이지 요소를 화면에 배치하는 방법이다.

  - 기본 구조

        container
          row
            col

    - Bootstrap Layout의 기본 구조이다.

  - Container

    - 정의
      - 내용을 가운데 정렬하고 폭을 제한하는 영역이다.

    - 형식

          <div class="container">

    - 특징

      - 가운데 정렬
      - 좌우 여백 생성
      - 최대 폭 제한

    - container-fluid

          <div class="container-fluid">

      - 화면 전체 폭 사용

  - Row

    - 정의
      - 가로 한 줄을 만드는 요소이다.

    - 형식

          <div class="row">

  - Column

    - 정의
      - 한 줄 안에서 칸을 나누는 요소이다.

    - 형식

          <div class="col">

  - Grid 시스템

    - 정의
      - Bootstrap은 화면을 12칸으로 나누어 Layout을 만든다.

    - 특징

      - 한 줄 = 12칸

    - col-6

          <div class="col-6">

      - 화면 반반 분할

    - col-4

          <div class="col-4">

      - 화면 3칸 분할

  - 핵심 구조

        container → 영역
        row → 줄
        col → 칸
