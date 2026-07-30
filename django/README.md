# Django

Django는 Python으로 웹 애플리케이션을 만들기 위한 웹 프레임워크다.  
이 폴더에서는 Django 프로젝트 구조, MTV 패턴, URL/View/Template 흐름, Model과 ORM, Form과 인증, Static/Media 파일, 그리고 DRF 기반 REST API 흐름을 정리한다.

## Quick Navigation

- [Django의 큰 흐름](#django의-큰-흐름)
- [개발 환경과 프로젝트 시작](#개발-환경과-프로젝트-시작)
- [URL, View, Template](#url-view-template)
- [Template와 DTL](#template와-dtl)
- [URL namespace와 variable routing](#url-namespace와-variable-routing)
- [GET, POST, CSRF](#get-post-csrf)
- [Model, Migration, Admin](#model-migration-admin)
- [ORM과 QuerySet](#orm과-queryset)
- [View 기반 CRUD](#view-기반-crud)
- [Django Form과 ModelForm](#django-form과-modelform)
- [Static File과 Media File](#static-file과-media-file)
- [Auth 1: 로그인과 로그아웃](#auth-1-로그인과-로그아웃)
- [Auth 2: 회원가입, 탈퇴, 정보수정, 비밀번호 변경](#auth-2-회원가입-탈퇴-정보수정-비밀번호-변경)
- [Django 웹페이지 구현 실습에서 정리한 흐름](#django-웹페이지-구현-실습에서-정리한-흐름)
- [REST API와 DRF](#rest-api와-drf)
- [DRF 예시 프로젝트 흐름](#drf-예시-프로젝트-흐름)
- [정리하며 남긴 기준](#정리하며-남긴-기준)

## Django의 큰 흐름

Django 학습에서 가장 먼저 잡아야 하는 것은 요청이 들어와 응답이 나가기까지의 길이다.

```text
client request
-> project urls.py
-> app urls.py
-> view function
-> model / form / serializer / template
-> response
```

Django는 흔히 MTV 패턴으로 설명한다.

- `Model`: 데이터 구조와 DB 접근 로직을 담당한다.
- `Template`: 사용자에게 보여 줄 HTML 화면을 담당한다.
- `View`: 요청을 받아 필요한 데이터를 만들고 응답을 반환한다.

MVC와 비교하면 Django의 `View`는 일반적인 MVC의 Controller에 가까운 역할을 하고, `Template`이 화면 표현을 담당한다.

Django를 공부할 때는 파일을 따로따로 외우기보다 다음 연결을 계속 확인해야 한다.

- `urls.py`에 등록된 경로가 어떤 view를 호출하는가
- view가 어떤 model, form, serializer를 사용하는가
- view가 어떤 template에 어떤 context를 넘기는가
- template에서 어떤 URL name, context variable, static/media file을 참조하는가
- DB 구조가 바뀌면 migration이 만들어지고 적용되었는가

## 개발 환경과 프로젝트 시작

Django 프로젝트는 보통 가상환경을 만들고, Django를 설치한 뒤, 프로젝트와 앱을 생성하면서 시작한다.

- `venv`: 프로젝트별 Python 패키지 환경을 분리한다.
- `django-admin startproject`: 프로젝트 설정 폴더를 만든다.
- `python manage.py startapp`: 기능 단위 앱을 만든다.
- `settings.py`: 설치 앱, 템플릿 경로, DB, static/media 설정 등을 관리한다.
- `manage.py`: 서버 실행, migration, admin 계정 생성 등 Django 명령의 진입점이다.

예시:

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install django

django-admin startproject config .
python manage.py startapp articles
python manage.py runserver
```

앱을 만들었다면 `settings.py`의 `INSTALLED_APPS`에 등록해야 Django가 해당 앱을 인식한다.

```python
# config/settings.py

INSTALLED_APPS = [
    "articles",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

프로젝트 URL은 앱 URL로 위임하면 구조가 깔끔해진다.

```python
# config/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("articles/", include("articles.urls")),
]
```

## URL, View, Template

Django의 기본 요청 처리 흐름은 `URL -> View -> Template`이다.

- URLconf는 요청 경로와 view 함수를 연결한다.
- view는 요청 객체를 받고 필요한 데이터를 준비한다.
- template은 view에서 받은 context를 사용해 HTML을 만든다.
- `render()`는 template과 context를 합쳐 HTML 응답을 반환한다.
- `redirect()`는 다른 URL로 이동시키는 응답을 반환한다.

예시:

```python
# articles/urls.py

from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("hello/<str:name>/", views.hello, name="hello"),
]
```

```python
# articles/views.py

from django.shortcuts import render


def index(request):
    return render(request, "articles/index.html")


def hello(request, name):
    context = {
        "name": name,
    }
    return render(request, "articles/hello.html", context)
```

```html
<!-- articles/templates/articles/hello.html -->

<h1>Hello, {{ name }}</h1>
```

view에서 template으로 넘기는 데이터는 보통 `context`라는 딕셔너리로 관리한다. template에서는 key 이름을 변수처럼 사용할 수 있다.

간단한 문자열만 바로 응답할 때는 `HttpResponse`를 사용할 수도 있지만, HTML 화면을 구성할 때는 보통 `render()`를 사용한다.

```python
from django.http import HttpResponse


def ping(request):
    return HttpResponse("pong")
```

## Template와 DTL

Django Template Language, 즉 DTL은 HTML 안에서 Python 데이터를 표현하기 위한 문법이다. Python 코드를 그대로 실행하는 문법이 아니라, template에서 필요한 표현만 제한적으로 제공하는 문법이다.

DTL에서 자주 쓰는 요소는 다음과 같다.

- `{{ variable }}`: context variable 출력
- `{{ value|filter }}`: filter 적용
- `{% tag %}`: 조건, 반복, URL 생성, template 상속 등
- `{# comment #}`: template 주석

예시:

```html
<h1>{{ article.title }}</h1>
<p>{{ article.content|truncatewords:30 }}</p>

{% if article.is_public %}
  <p>공개된 글입니다.</p>
{% else %}
  <p>비공개 글입니다.</p>
{% endif %}

<ul>
  {% for comment in comments %}
    <li>{{ comment.content }}</li>
  {% empty %}
    <li>댓글이 없습니다.</li>
  {% endfor %}
</ul>
```

Template 상속은 여러 페이지에서 공통 레이아웃을 재사용하기 위한 핵심 기능이다.

```html
<!-- templates/base.html -->

<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Django Study</title>
</head>
<body>
  <nav>
    <a href="{% url 'articles:index' %}">Home</a>
  </nav>

  {% block content %}
  {% endblock content %}
</body>
</html>
```

```html
<!-- articles/templates/articles/index.html -->

{% extends "base.html" %}

{% block content %}
  <h1>Articles</h1>
{% endblock content %}
```

`base.html`처럼 프로젝트 전체에서 공유하는 template은 root templates 폴더에 두고, 앱별 template은 `app_name/templates/app_name/` 구조로 두면 이름 충돌을 줄일 수 있다.

root templates 폴더를 사용하려면 `settings.py`의 `TEMPLATES` 설정에 경로를 등록한다.

```python
# settings.py

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

## URL namespace와 variable routing

URL name을 쓰면 template이나 view에서 경로 문자열을 직접 하드코딩하지 않아도 된다.  
앱이 많아지면 같은 이름의 URL이 생길 수 있으므로 `app_name`을 사용해 namespace를 나누는 것이 좋다.

```python
# articles/urls.py

from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:article_pk>/", views.detail, name="detail"),
    path("<int:article_pk>/edit/", views.update, name="update"),
]
```

template에서는 `{% url %}` 태그로 URL을 만든다.

```html
<a href="{% url 'articles:detail' article.pk %}">
  {{ article.title }}
</a>
```

view에서도 `redirect()`에 URL name을 사용할 수 있다.

```python
from django.shortcuts import redirect


def go_detail(request, article_pk):
    return redirect("articles:detail", article_pk)
```

Variable routing은 URL 일부를 변수로 받아 view에 넘기는 방식이다.

- `<int:pk>`: 정수 값
- `<str:name>`: 문자열 값
- `<slug:slug>`: slug 형식 문자열

라우팅 변수 이름과 view 함수의 매개변수 이름은 맞춰야 한다.

## GET, POST, CSRF

HTTP method는 요청의 의도를 구분한다.

- `GET`: 데이터를 조회하거나 검색할 때 사용한다.
- `POST`: 데이터를 생성, 수정, 삭제하는 요청에 사용한다.

GET 요청은 query string으로 데이터를 전달할 수 있다.

```html
<form action="{% url 'articles:search' %}" method="GET">
  <input type="text" name="keyword">
  <button type="submit">검색</button>
</form>
```

```python
def search(request):
    keyword = request.GET.get("keyword", "")
    articles = Article.objects.filter(title__contains=keyword)
    context = {
        "keyword": keyword,
        "articles": articles,
    }
    return render(request, "articles/search.html", context)
```

POST 요청은 서버의 데이터를 바꾸는 요청에 사용한다. Django에서는 POST form에 `{% csrf_token %}`을 넣어야 한다.

```html
<form action="{% url 'articles:create' %}" method="POST">
  {% csrf_token %}
  <input type="text" name="title">
  <textarea name="content"></textarea>
  <button type="submit">저장</button>
</form>
```

CSRF는 사용자가 의도하지 않은 요청을 다른 사이트가 대신 보내도록 만드는 공격이다. Django의 CSRF token은 요청이 정상적인 form에서 온 것인지 확인하는 방어 장치다.

CSRF token 흐름은 다음처럼 이해할 수 있다.

```text
서버가 form을 응답할 때 CSRF token을 함께 내려줌
-> template의 {% csrf_token %}이 hidden input으로 렌더링됨
-> 사용자가 POST 요청을 보낼 때 form data와 token이 함께 전송됨
-> 서버가 발급한 token과 요청 token을 비교함
```

요청 method를 제한하고 싶을 때는 decorator를 사용할 수 있다.

```python
from django.views.decorators.http import require_http_methods, require_POST


@require_http_methods(["GET", "POST"])
def create(request):
    ...


@require_POST
def delete(request, article_pk):
    ...
```

`require_POST`는 `require_http_methods(["POST"])`의 짧은 형태로 볼 수 있다.

## Model, Migration, Admin

Model은 Django에서 DB table을 Python class로 표현하는 방식이다.

- class 이름은 table의 개념을 나타낸다.
- field는 column을 나타낸다.
- field option은 column 제약 조건이나 입력 옵션을 나타낸다.
- model을 바꾼 뒤에는 migration 파일을 만들고 DB에 적용해야 한다.

예시:

```python
# articles/models.py

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

자주 쓰는 field:

- `CharField`: 길이 제한이 있는 문자열
- `TextField`: 긴 문자열
- `IntegerField`: 정수
- `BooleanField`: 참/거짓
- `DateTimeField`: 날짜와 시간
- `ForeignKey`: 1:N 관계
- `ManyToManyField`: M:N 관계
- `ImageField`: 이미지 업로드

Field에서 기억할 점:

- `CharField`는 `max_length`가 필요하다.
- `TextField`는 긴 본문에 적합하고, DB 저장 길이 제한 용도로 `max_length`를 쓰기에는 적합하지 않다.
- `DateTimeField(auto_now_add=True)`는 최초 생성 시간을 자동 저장한다.
- `DateTimeField(auto_now=True)`는 객체가 저장될 때마다 수정 시간을 갱신한다.
- 기존 model에 NOT NULL field를 새로 추가하면 기존 row에 들어갈 기본값 문제가 생길 수 있다.

Migration 흐름:

```powershell
python manage.py makemigrations
python manage.py migrate
```

Admin 사이트에서 model을 관리하려면 등록이 필요하다.

```python
# articles/admin.py

from django.contrib import admin
from .models import Article

admin.site.register(Article)
```

관리자 계정은 다음 명령으로 만든다.

```powershell
python manage.py createsuperuser
```

## ORM과 QuerySet

ORM은 SQL을 직접 많이 작성하지 않고 Python 코드로 DB를 다루게 해주는 도구다. Django ORM의 조회 결과는 보통 QuerySet이다.

자주 쓰는 QuerySet 메서드:

- `all()`: 전체 조회
- `get()`: 단일 객체 조회
- `filter()`: 조건에 맞는 여러 객체 조회
- `exclude()`: 조건을 제외한 객체 조회
- `order_by()`: 정렬
- `create()`: 생성 후 저장
- `save()`: 변경사항 저장
- `delete()`: 삭제

예시:

```python
# create
article = Article.objects.create(
    title="Django ORM",
    content="QuerySet으로 데이터를 다룬다.",
)

# read
articles = Article.objects.all()
article = Article.objects.get(pk=1)
filtered = Article.objects.filter(title__contains="Django")

# update
article.title = "Django ORM 정리"
article.save()

# delete
article.delete()
```

조회 조건에는 field lookup을 사용할 수 있다.

```python
Article.objects.filter(title__contains="Django")
Article.objects.filter(created_at__year=2026)
Article.objects.filter(pk__in=[1, 2, 3])
Article.objects.order_by("-created_at")
```

`get()`은 결과가 반드시 하나일 때만 안전하다. 결과가 없거나 여러 개면 예외가 발생한다. 목록 페이지에서는 `filter()`나 `all()`을 쓰고, 상세 페이지에서는 `get_object_or_404()`를 많이 사용한다.

`get_object_or_404()`와 `get_list_or_404()`는 조회 실패 시 직접 예외 처리를 길게 쓰는 대신 404 응답으로 연결해준다.

```python
from django.shortcuts import get_list_or_404, get_object_or_404

article = get_object_or_404(Article, pk=article_pk)
articles = get_list_or_404(Article)
```

## View 기반 CRUD

CRUD는 데이터 생성, 조회, 수정, 삭제 흐름이다.

- Create: 새 객체 생성
- Read: 목록과 상세 조회
- Update: 기존 객체 수정
- Delete: 기존 객체 삭제

목록과 상세:

```python
from django.shortcuts import get_object_or_404, render
from .models import Article


def index(request):
    articles = Article.objects.order_by("-pk")
    context = {
        "articles": articles,
    }
    return render(request, "articles/index.html", context)


def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        "article": article,
    }
    return render(request, "articles/detail.html", context)
```

생성:

```python
from django.shortcuts import redirect, render
from .models import Article


def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        article = Article.objects.create(title=title, content=content)
        return redirect("articles:detail", article.pk)

    return render(request, "articles/create.html")
```

수정:

```python
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == "POST":
        article.title = request.POST.get("title")
        article.content = request.POST.get("content")
        article.save()
        return redirect("articles:detail", article.pk)

    context = {
        "article": article,
    }
    return render(request, "articles/update.html", context)
```

삭제:

```python
from django.views.decorators.http import require_POST


@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect("articles:index")
```

삭제 요청은 단순 링크보다 POST form으로 처리하는 편이 안전하다. `require_POST`를 붙이면 GET 요청으로 삭제 view가 실행되는 일을 막을 수 있다.

```html
<form action="{% url 'articles:delete' article.pk %}" method="POST">
  {% csrf_token %}
  <button type="submit">삭제</button>
</form>
```

## Django Form과 ModelForm

Django Form은 입력을 검증하고 form HTML을 만드는 데 도움을 준다.

- `Form`: model과 직접 연결되지 않은 일반 form
- `ModelForm`: model을 기반으로 form field를 자동 생성하는 form

Form을 쓰면 view에서 직접 `request.POST` 값을 하나씩 꺼내 검증하는 부담이 줄어든다.

일반 Form 예시:

```python
# accounts/forms.py

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
```

```python
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            # 검증된 데이터를 사용해 로그인 로직 처리
    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})
```

ModelForm 예시:

```python
# articles/forms.py

from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("title", "content")
```

생성과 수정을 같은 form으로 처리할 수 있다.

```python
# articles/views.py

from django.shortcuts import get_object_or_404, redirect, render
from .forms import ArticleForm
from .models import Article


def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect("articles:detail", article.pk)
    else:
        form = ArticleForm()

    context = {
        "form": form,
    }
    return render(request, "articles/form.html", context)


def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect("articles:detail", article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {
        "form": form,
        "article": article,
    }
    return render(request, "articles/form.html", context)
```

template에서는 form을 간단히 출력할 수 있다.

```html
<form method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">저장</button>
</form>
```

Form에서 기억할 점:

- `is_valid()`를 통과한 데이터는 `cleaned_data`에 들어간다.
- `ModelForm.save()`는 model instance를 만들고 저장한다.
- 수정할 때는 `instance=기존객체`를 넘긴다.
- file upload가 있으면 `request.FILES`도 함께 넘긴다.
- `fields`는 포함할 field를 지정하고, `exclude`는 제외할 field를 지정한다.

`fields`와 `exclude` 예시:

```python
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ("movie", "user")
```

`form.as_p`는 form field들을 `<p>` 태그로 감싸 기본 HTML을 만들어준다.

## Static File과 Media File

Static file과 media file은 목적이 다르다.

- Static file: 개발자가 프로젝트에 넣어둔 CSS, JS, 이미지 파일
- Media file: 사용자가 업로드한 파일

Static file 사용 흐름:

```python
# settings.py

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

```text
articles/
  static/
    articles/
      style.css
      logo.png
```

```html
{% load static %}

<link rel="stylesheet" href="{% static 'articles/style.css' %}">
<img src="{% static 'articles/logo.png' %}" alt="logo">
```

Media file을 사용하려면 upload field와 media 설정이 필요하다.

`ImageField`는 이미지 파일 검증을 위해 Pillow가 필요하다.

```powershell
pip install pillow
```

```python
# articles/models.py

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="articles/", blank=True)
```

```python
# settings.py

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"
```

개발 서버에서 media file을 제공하려면 프로젝트 URL에 설정을 추가한다.

```python
# config/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("articles/", include("articles.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

업로드 form에는 `enctype="multipart/form-data"`가 필요하다.

```html
<form method="POST" enctype="multipart/form-data">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">저장</button>
</form>
```

view에서는 `request.FILES`를 같이 넘긴다.

```python
form = ArticleForm(request.POST, request.FILES)
```

수정 view에서는 기존 객체와 파일 데이터를 함께 넘긴다.

```python
form = ArticleForm(request.POST, request.FILES, instance=article)
```

이미지가 있을 때만 출력하려면 조건을 둔다.

```html
{% if article.image %}
  <img src="{{ article.image.url }}" alt="{{ article.title }}">
{% endif %}
```

Static과 Media에서 기억할 점:

- 앱별 static은 `app/static/app/` 구조로 두면 이름 충돌을 줄일 수 있다.
- 전역 static 폴더를 따로 쓸 때는 `STATICFILES_DIRS`에 등록한다.
- `MEDIA_ROOT`와 `STATIC_ROOT`는 같은 경로로 두면 안 된다.
- `MEDIA_URL`과 `STATIC_URL`도 서로 다른 URL prefix로 관리한다.

## Auth 1: 로그인과 로그아웃

Auth는 인증과 권한을 다룬다.

- Authentication: 사용자가 누구인지 확인하는 것
- Authorization: 확인된 사용자가 무엇을 할 수 있는지 판단하는 것

Django는 기본 User model, session, password hashing, login/logout helper, auth form을 제공한다.

로그인 상태가 유지되는 흐름:

```text
사용자가 로그인 요청
-> 서버가 session 데이터를 만들고 session id 발급
-> 브라우저가 session id를 cookie에 저장
-> 이후 요청마다 cookie를 함께 보냄
-> 서버가 session id로 사용자를 확인
```

쿠키는 브라우저 쪽에 저장되는 작은 데이터이고, 세션은 서버가 로그인 상태 같은 정보를 일정하게 유지하기 위해 사용하는 구조다.

로그인 흐름:

```python
# accounts/views.py

from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render


def login(request):
    if request.user.is_authenticated:
        return redirect("articles:index")

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("articles:index")
    else:
        form = AuthenticationForm()

    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)
```

로그아웃 흐름:

```python
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect


def logout(request):
    if request.method == "POST":
        auth_logout(request)
    return redirect("articles:index")
```

template에서는 로그인 상태에 따라 다른 UI를 보여줄 수 있다.

```html
{% if request.user.is_authenticated %}
  <p>{{ request.user.username }}님</p>
  <form action="{% url 'accounts:logout' %}" method="POST">
    {% csrf_token %}
    <button type="submit">로그아웃</button>
  </form>
{% else %}
  <a href="{% url 'accounts:login' %}">로그인</a>
{% endif %}
```

로그인이 필요한 view에는 `login_required`를 붙인다.

```python
from django.contrib.auth.decorators import login_required


@login_required
def create(request):
    ...
```

`login_required`로 막힌 페이지에 접근하면 로그인 페이지로 이동하고, 로그인 후 원래 가려던 주소는 `next` parameter로 전달될 수 있다.

```python
next_url = request.GET.get("next") or "articles:index"
return redirect(next_url)
```

## Auth 2: 회원가입, 탈퇴, 정보수정, 비밀번호 변경

회원가입에는 `UserCreationForm` 계열 form을 사용한다. Custom User model을 쓰는 프로젝트에서는 `get_user_model()`을 사용해 현재 활성화된 User model을 참조하는 것이 안전하다.

User model을 참조하는 방식은 상황에 따라 다르다.

- `settings.AUTH_USER_MODEL`: model field에서 문자열로 User model을 참조할 때 사용한다.
- `get_user_model()`: view, form, serializer처럼 실제 User model class가 필요할 때 사용한다.
- `User`를 직접 import하면 custom user model을 사용하는 프로젝트에서 어긋날 수 있다.

Custom User model을 사용할 때의 기본 형태:

```python
# accounts/models.py

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
```

```python
# settings.py

AUTH_USER_MODEL = "accounts.User"
```

```python
# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

Custom User model은 프로젝트 초기에 설정하는 편이 안전하다. 이미 migration과 DB가 많이 진행된 뒤 바꾸면 관계 설정과 migration 정리가 복잡해질 수 있다.

회원가입 form 예시:

```python
# accounts/forms.py

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ("email", "first_name", "last_name")
```

회원가입 후 바로 로그인시키는 흐름:

```python
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm


def signup(request):
    if request.user.is_authenticated:
        return redirect("articles:index")

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("articles:index")
    else:
        form = CustomUserCreationForm()

    return render(request, "accounts/signup.html", {"form": form})
```

회원 탈퇴는 로그인한 사용자를 삭제하는 흐름이다.

```python
def delete(request):
    if request.method == "POST":
        request.user.delete()
    return redirect("articles:index")
```

회원정보 수정은 기존 user instance를 form에 연결한다.

```python
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm


@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("articles:index")
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, "accounts/update.html", {"form": form})
```

비밀번호 변경 후에는 세션 인증 정보가 바뀌기 때문에 `update_session_auth_hash()`로 로그인 상태를 유지할 수 있다.

```python
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("articles:index")
    else:
        form = PasswordChangeForm(request.user)

    return render(request, "accounts/change_password.html", {"form": form})
```

Auth에서 특히 조심할 점:

- 비밀번호는 직접 저장하지 않고 Django form과 helper를 사용한다.
- 로그아웃, 회원탈퇴, 삭제 요청은 POST로 처리한다.
- 로그인 사용자에게만 허용할 기능은 view와 template 양쪽에서 흐름을 맞춘다.
- 사용자의 소유권이 필요한 기능은 단순 로그인 여부뿐 아니라 작성자 일치 여부도 확인한다.

## Django 웹페이지 구현 실습에서 정리한 흐름

Django 웹페이지 구현 실습은 여러 개념이 한 프로젝트 안에서 연결되는 연습이었다.

전형적인 앱 구성:

```text
project/
  accounts/
    forms.py
    urls.py
    views.py
  movies/
    forms.py
    models.py
    urls.py
    views.py
    templates/
```

영화와 댓글 구조 예시:

```python
from django.conf import settings
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    poster = models.ImageField(upload_to="movies/", blank=True)


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
```

`on_delete=models.CASCADE`는 참조 대상이 삭제될 때 연결된 객체도 함께 삭제한다. 예를 들어 영화가 삭제되면 해당 영화의 댓글도 함께 삭제되어야 하는 경우에 사용한다.

댓글 form은 사용자가 직접 고르면 안 되는 field를 제외한다.

```python
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ("movie", "user")
```

`movie`와 `user`를 form에서 제외하는 이유는 명확하다.

- 댓글의 작성자는 현재 로그인한 사용자여야 한다.
- 댓글이 달릴 대상은 현재 보고 있는 게시글이어야 한다.
- 사용자가 form에서 작성자나 대상 게시글을 임의로 바꿀 수 있으면 안 된다.

댓글 생성은 부모 객체인 movie를 먼저 찾고, form으로 댓글을 만든 뒤, `commit=False`로 관계를 채워 저장할 수 있다.

```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .forms import CommentForm
from .models import Movie


@login_required
def comments_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.movie = movie
        comment.user = request.user
        comment.save()

    return redirect("movies:detail", movie.pk)
```

상세 페이지에서는 부모 객체와 form, 역참조 객체를 함께 다룬다.

```python
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment_form = CommentForm()
    comments = movie.comment_set.order_by("-pk")
    context = {
        "movie": movie,
        "comment_form": comment_form,
        "comments": comments,
    }
    return render(request, "movies/detail.html", context)
```

template에서는 form과 목록을 같은 화면에 배치할 수 있다.

```html
<form action="{% url 'movies:comments_create' movie.pk %}" method="POST">
  {% csrf_token %}
  {{ comment_form.as_p }}
  <button type="submit">댓글 작성</button>
</form>

<ul>
  {% for comment in comments %}
    <li>{{ comment.user }} - {{ comment.content }}</li>
  {% empty %}
    <li>아직 댓글이 없습니다.</li>
  {% endfor %}
</ul>
```

작성자에게만 수정/삭제 UI를 보여주는 패턴:

```html
{% if request.user == movie.user %}
  <a href="{% url 'movies:update' movie.pk %}">수정</a>
  <form action="{% url 'movies:delete' movie.pk %}" method="POST">
    {% csrf_token %}
    <button type="submit">삭제</button>
  </form>
{% endif %}

{% for comment in comments %}
  <p>{{ comment.content }}</p>
  {% if request.user == comment.user %}
    <form action="{% url 'movies:comments_delete' movie.pk comment.pk %}" method="POST">
      {% csrf_token %}
      <button type="submit">댓글 삭제</button>
    </form>
  {% endif %}
{% endfor %}
```

댓글 삭제 URL에는 부모 게시글 pk와 댓글 pk가 함께 들어갈 수 있다.

```python
path(
    "<int:movie_pk>/comments/<int:comment_pk>/delete/",
    views.comments_delete,
    name="comments_delete",
)
```

이런 실습에서 중요한 것은 개별 문법보다 데이터의 방향이다.

- URL의 `movie_pk`가 view로 들어온다.
- view가 `Movie`를 찾는다.
- 댓글 form은 `content`만 받고, `movie`와 `user`는 view에서 채운다.
- `movie.comment_set.all()`은 1:N 관계에서 부모 객체가 자식 객체들을 역참조하는 방식이다.
- `comment.movie`는 댓글이 참조하는 부모 게시글을 확인하는 방식이다.
- 저장 후 상세 페이지로 redirect한다.
- 상세 페이지는 movie, comment form, comments를 함께 보여준다.

## REST API와 DRF

REST API는 자원을 URI로 표현하고 HTTP method로 행위를 표현하는 방식이다.

- `GET`: 조회
- `POST`: 생성
- `PUT` / `PATCH`: 수정
- `DELETE`: 삭제

RESTful하게 설계할 때는 URL에 동사보다 명사를 두고, 행위는 method로 구분한다.

REST URL을 작성할 때의 기본 기준:

- URL은 동사보다 명사를 사용한다.
- 행위는 URL에 넣지 않고 HTTP method로 표현한다.
- 단어를 구분할 때는 underscore보다 hyphen을 사용하는 편이 일반적이다.
- 파일 확장자처럼 표현 형식을 URL 자원 이름에 섞지 않는다.
- URL만 보고 어떤 자원을 다루는지 어느 정도 추측할 수 있어야 한다.

```text
GET    /movies/
GET    /movies/1/
POST   /movies/1/reviews/
PUT    /reviews/3/
DELETE /reviews/3/
```

일반적인 REST 설계 원칙에서는 URL 끝의 trailing slash를 쓰지 않는 스타일도 자주 언급된다. Django와 DRF 예제에서는 `/movies/`처럼 trailing slash를 쓰는 관례도 흔하므로, 프로젝트 안에서 일관성을 유지하는 것이 중요하다.

DRF, Django REST Framework는 Django에서 API를 쉽게 만들기 위한 도구다.

- `Serializer`: model instance나 QuerySet을 JSON으로 변환하고, 요청 데이터를 검증한다.
- `ModelSerializer`: model 기반 serializer를 빠르게 만든다.
- `@api_view`: function based API view에서 허용 method를 지정한다.
- `Response`: DRF 응답 객체다.
- `status`: HTTP status code를 명확히 표현한다.

Serializer는 두 방향으로 이해하면 쉽다.

- 직렬화: Python 객체나 QuerySet을 JSON으로 응답하기 좋은 데이터로 바꾼다.
- 역직렬화: 클라이언트가 보낸 JSON 데이터를 검증하고 model instance로 저장할 수 있게 바꾼다.

```python
# 직렬화
serializer = MovieSerializer(movie)
return Response(serializer.data)

# 역직렬화
serializer = ReviewSerializer(data=request.data)
if serializer.is_valid(raise_exception=True):
    serializer.save(movie=movie)
```

자주 쓰는 status code:

- `200 OK`: 조회나 수정 요청이 정상 처리됨
- `201 Created`: 생성 요청이 성공해 새 자원이 만들어짐
- `204 No Content`: 삭제처럼 응답 body가 없어도 되는 요청이 성공함
- `400 Bad Request`: 요청 데이터가 유효하지 않음
- `404 Not Found`: 요청한 자원을 찾을 수 없음
- `405 Method Not Allowed`: 허용되지 않은 HTTP method로 요청함

DRF 설치와 등록:

```powershell
pip install djangorestframework
```

```python
# settings.py

INSTALLED_APPS = [
    "rest_framework",
    "movies",
    # ...
]
```

Serializer 기본 예시:

```python
from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
```

목록용 serializer와 상세용 serializer를 나누면 응답 크기와 정보량을 조절할 수 있다.

```python
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("title", "overview")


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
```

Nested serializer는 관계 데이터를 함께 보여줄 때 사용한다.

```python
class ActorSerializer(serializers.ModelSerializer):
    class MovieTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ("title",)

    movies = MovieTitleSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = "__all__"
```

`many=True`는 여러 객체를 직렬화할 때 사용하고, `read_only=True`는 응답에는 포함하되 입력으로 직접 받지 않겠다는 의미다.

## DRF 예시 프로젝트 흐름

DRF 예시 프로젝트는 영화, 배우, 리뷰 데이터를 API로 제공하는 구조였다.

Model 관계:

```python
from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    actors = models.ManyToManyField(Actor, related_name="movies")
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    poster_path = models.TextField()


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
```

관계 정리:

- Actor와 Movie는 M:N 관계다.
- Movie와 Review는 1:N 관계다.
- `related_name="movies"`를 사용하면 actor에서 관련 movie를 `actor.movies`로 접근할 수 있다.
- `ForeignKey`에 `related_name`을 지정하지 않으면 기본 역참조 이름은 `review_set` 형태가 된다.

URL 구조:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("actors/", views.actor_list),
    path("actors/<int:actor_pk>/", views.actor_detail),
    path("movies/", views.movie_list),
    path("movies/<int:movie_pk>/", views.movie_detail),
    path("reviews/", views.review_list),
    path("movies/<int:movie_pk>/reviews/", views.create_review),
    path("reviews/<int:review_pk>/", views.review_detail),
]
```

API를 Postman 같은 도구로 테스트할 때는 프로젝트 URL 규칙을 정확히 맞춰야 한다. Django/DRF 예시처럼 trailing slash가 있는 URL을 쓰는 경우에는 `/api/v1/movies/`와 `/api/v1/movies`가 다르게 처리될 수 있다.

목록 API:

```python
from django.shortcuts import get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieListSerializer


@api_view(["GET"])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
```

상세 API:

```python
from django.shortcuts import get_object_or_404
from .serializers import MovieSerializer


@api_view(["GET"])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
```

리뷰 생성 API:

```python
from rest_framework import status
from .models import Movie
from .serializers import ReviewSerializer


@api_view(["POST"])
def create_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

리뷰 상세, 수정, 삭제 API:

```python
from .models import Review


@api_view(["GET", "PUT", "DELETE"])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == "GET":
        serializer = ReviewSerializer(review)
        review_count = Review.objects.filter(movie=review.movie).count()
        return Response({
            "review": serializer.data,
            "review_count": review_count,
        })

    if request.method == "PUT":
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    review.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
```

여기서 확인한 DRF 패턴:

- 목록 응답과 상세 응답은 serializer를 다르게 가져갈 수 있다.
- 생성 시 URL에서 부모 객체의 pk를 받고, view에서 실제 부모 객체를 찾아 `serializer.save(movie=movie)`처럼 주입한다.
- 수정 시 `partial=True`를 쓰면 일부 field만 보내도 수정할 수 있다.
- 삭제 응답은 `HTTP_204_NO_CONTENT`를 사용할 수 있다.
- 응답에 추가 계산값이 필요하면 serializer 결과와 별도 값을 묶어서 반환할 수 있다.

fixture 데이터는 JSON 파일로 준비해 DB에 넣을 수 있다.

```powershell
python manage.py loaddata movies/actors.json movies/movies.json movies/reviews.json
```

fixture를 사용할 때는 model 구조와 JSON의 app/model/field 구조가 맞아야 한다. 앱 안에서는 보통 `fixtures/app_name/` 경로에 JSON을 두고 `loaddata`로 불러온다.

## 정리하며 남긴 기준

Django는 기능별 문법을 각각 외우는 것보다 연결을 따라가는 공부가 더 효과적이었다.

- URL을 보면 어떤 view가 실행되는지 확인한다.
- view를 보면 어떤 model/form/template/serializer가 연결되는지 확인한다.
- model을 바꾸면 migration이 필요한지 확인한다.
- form은 입력 검증과 HTML 생성을 함께 담당한다.
- auth는 로그인 여부와 소유권 확인을 나눠 생각한다.
- static과 media는 파일의 주체가 개발자인지 사용자인지로 구분한다.
- DRF는 serializer가 응답 모양과 요청 검증의 중심이 된다.

공개용 기록으로 정리할 때는 실습 파일의 원본 코드나 제공받은 자료를 그대로 남기기보다, 내가 이해한 흐름과 재작성한 예시를 중심으로 남기는 것이 좋다.
