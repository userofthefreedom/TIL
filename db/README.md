# DB Study Notes

## 핵심 흐름
- DB 학습은 데이터를 저장하는 방법에서 시작해, 관계를 맺고, 조회하고, 웹 애플리케이션의 모델로 연결하는 흐름으로 이어진다.
- 이 폴더의 학습 내용은 크게 SQL 기본 문법, JOIN, Django ORM과 CRUD, M:N 관계 구현, fixtures, hashtag 기능으로 정리할 수 있다.
- PDF의 표와 관계도에서는 테이블 사이의 연결을 눈으로 확인했고, zip 예시 코드에서는 그 관계가 Django 모델, view, template으로 어떻게 구현되는지 확인했다.

## 관계형 데이터베이스 기초
- Database
  - 데이터를 구조화해서 저장하고 관리하는 공간이다.
  - 웹 애플리케이션에서는 사용자, 게시글, 댓글, 좋아요 같은 데이터를 테이블 단위로 관리한다.
- DBMS
  - 데이터베이스를 관리하는 소프트웨어이다.
  - SQLite, MySQL, MariaDB, Oracle, PostgreSQL 등이 관계형 DBMS에 속한다.
- RDB(Relational Database)
  - 데이터를 table, row, column 구조로 저장한다.
  - table 사이의 관계를 key로 연결한다.
- NoSQL
  - 문서, key-value, graph 등 다양한 형태로 데이터를 저장한다.
  - 관계형 구조보다 유연하지만, 명확한 관계와 정합성이 중요한 경우 RDB가 더 적합할 수 있다.
- SQL
  - 관계형 데이터베이스에 명령을 내리는 언어이다.
  - 데이터 정의, 조회, 삽입, 수정, 삭제에 사용된다.

## SQL 기본 문법
- DDL(Data Definition Language)
  - table 구조를 만들거나 바꾼다.
  - `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE` 등이 있다.
- DML(Data Manipulation Language)
  - table 안의 데이터를 다룬다.
  - `INSERT`, `SELECT`, `UPDATE`, `DELETE` 등이 있다.
- SQLite Data Types
  - `NULL`
  - `INTEGER`
  - `REAL`
  - `TEXT`
  - `BLOB`
- Constraints
  - column에 저장될 수 있는 값의 규칙을 정한다.
  - `PRIMARY KEY`, `NOT NULL`, `UNIQUE`, `DEFAULT`, `CHECK`, `FOREIGN KEY` 등이 있다.
- SQL 문법을 볼 때 구분할 것
  - table 구조를 바꾸는 명령인지
  - table 안의 데이터를 바꾸는 명령인지
  - 데이터를 조회만 하는 명령인지
  - 조건, 정렬, 그룹화처럼 조회 결과를 다듬는 절인지

## SQL 테이블과 데이터 변경
- `CREATE TABLE`
  - 새 table을 만든다.
  - column 이름, data type, constraint를 함께 정의한다.
- `ALTER TABLE`
  - 기존 table의 이름, column 이름, column 구성을 변경한다.
  - 실습에서는 table 이름 변경, column 이름 변경, column 추가, column 삭제 흐름을 확인했다.
- `DROP TABLE`
  - table 자체를 삭제한다.
  - 복구가 어렵기 때문에 실제 데이터베이스에서는 특히 조심해야 한다.
- `INSERT`
  - 새 row를 추가한다.
- `UPDATE`
  - 기존 row의 값을 수정한다.
  - `WHERE` 없이 실행하면 모든 row가 수정될 수 있다.
- `DELETE`
  - row를 삭제한다.
  - `WHERE` 없이 실행하면 table의 모든 row가 삭제될 수 있다.
- 예시: table 생성
  ```sql
  CREATE TABLE contacts (
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      email TEXT UNIQUE,
      age INTEGER CHECK (age >= 0)
  );
  ```

  - `PRIMARY KEY`는 row를 구분하는 대표 key이다.
  - `NOT NULL`은 값이 비어 있으면 안 된다는 뜻이다.
  - `UNIQUE`는 중복 값을 허용하지 않는다.
  - `CHECK`는 값이 만족해야 하는 조건을 둔다.
- 예시: table 구조 변경
  ```sql
  ALTER TABLE contacts RENAME TO new_contacts;
  ALTER TABLE new_contacts RENAME COLUMN name TO last_name;
  ALTER TABLE new_contacts ADD COLUMN address TEXT;
  ALTER TABLE new_contacts DROP COLUMN address;
  ```

  - `ADD COLUMN`으로 `NOT NULL` column을 추가할 때는 기존 row에 들어갈 기본값 문제를 함께 생각해야 한다.
  - `DROP COLUMN`은 constraint나 DBMS 버전에 따라 제한될 수 있다.
- 예시: 데이터 추가, 수정, 삭제
  ```sql
  INSERT INTO contacts (last_name, email, age)
  VALUES ('Kim', 'kim@example.com', 30);

  UPDATE contacts
  SET age = 31
  WHERE email = 'kim@example.com';

  DELETE FROM contacts
  WHERE email = 'kim@example.com';
  ```

  - `UPDATE`와 `DELETE`는 `WHERE` 조건을 먼저 확인하고 실행한다.
  - 실습에서는 `rowid`를 함께 조회해 특정 row를 정확히 지정하는 흐름을 확인했다.

## SQL 조회 흐름
- `SELECT`
  - table에서 원하는 column을 조회한다.
- `WHERE`
  - row를 조건으로 필터링한다.
- `LIKE`
  - 문자열 패턴으로 검색한다.
  - `%`는 길이 제한 없는 여러 글자, `_`는 한 글자를 의미한다.
- `IN`
  - 여러 후보 값 중 하나와 일치하는지 확인한다.
- `BETWEEN`
  - 특정 범위 안에 있는지 확인한다.
- `ORDER BY`
  - 결과를 정렬한다.
- `DISTINCT`
  - 중복 값을 제거한다.
- `LIMIT`
  - 조회 개수를 제한한다.
- `OFFSET`
  - 앞의 일부 row를 건너뛴다.
- `GROUP BY`
  - 같은 값을 가진 row를 그룹으로 묶는다.
- Aggregate Function
  - `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`처럼 여러 row를 하나의 결과로 집계한다.
- `HAVING`
  - `GROUP BY`로 묶은 결과에 조건을 걸 때 사용한다.
  - `WHERE`가 그룹화 전 row를 거른다면, `HAVING`은 그룹화 후 결과를 거른다.

- 예시: SELECT, WHERE, ORDER BY
  ```sql
  SELECT first_name, last_name, age, balance
  FROM users
  WHERE age >= 30
  ORDER BY balance DESC
  LIMIT 5;
  ```

  - `WHERE`가 먼저 row를 고른다.
  - `ORDER BY`가 남은 row를 정렬한다.
  - `LIMIT`이 최종 출력 개수를 제한한다.
  - SQL을 읽을 때는 작성 순서와 실제 처리 흐름이 다를 수 있다는 점을 의식해야 한다.
- 예시: LIKE, IN, BETWEEN
  ```sql
  SELECT first_name, phone
  FROM users
  WHERE phone LIKE '02-%';

  SELECT first_name, country
  FROM users
  WHERE country IN ('경기도', '강원도');

  SELECT first_name, age
  FROM users
  WHERE age BETWEEN 20 AND 30;
  ```

  - `LIKE '02-%'`는 `02-`로 시작하는 전화번호를 찾는다.
  - `IN`은 여러 `OR` 조건을 더 읽기 쉽게 만든다.
  - `BETWEEN`은 시작과 끝 값을 포함하는 범위 조건으로 이해한다.
- 예시: DISTINCT, LIMIT, OFFSET
  ```sql
  SELECT DISTINCT country
  FROM users
  ORDER BY country;

  SELECT rowid, first_name
  FROM users
  LIMIT 10 OFFSET 10;
  ```

  - `DISTINCT`는 중복 값을 제거해 고유한 목록을 확인할 때 사용한다.
  - `LIMIT 10 OFFSET 10`은 앞의 10개 row를 건너뛰고 다음 10개를 조회한다.
  - pagination을 구현할 때 `LIMIT`과 `OFFSET`을 함께 사용할 수 있다.

- 예시: GROUP BY와 집계
  ```sql
  SELECT country, COUNT(*) AS user_count, AVG(balance) AS avg_balance
  FROM users
  GROUP BY country
  ORDER BY user_count DESC;
  ```

  - `country`가 같은 row를 하나의 그룹으로 묶는다.
  - `COUNT(*)`는 그룹별 row 수를 계산한다.
  - `AVG(balance)`는 그룹별 평균 잔액을 계산한다.
  - 집계 결과를 다시 정렬하면 지역별 규모나 평균 차이를 비교하기 쉽다.
- 예시: HAVING
  ```sql
  SELECT country, COUNT(*) AS user_count
  FROM users
  GROUP BY country
  HAVING COUNT(*) >= 10
  ORDER BY user_count DESC;
  ```

  - `WHERE`에서는 `COUNT(*)` 같은 집계 결과에 조건을 걸 수 없다.
  - 그룹별 집계 결과를 필터링하려면 `HAVING`을 사용한다.

## JOIN
- JOIN은 두 개 이상의 table을 관계 조건으로 연결해 하나의 결과처럼 조회하는 방식이다.
- PDF의 관계도에서는 `articles`와 `users`가 user id를 기준으로 연결되는 구조를 확인했다.
- JOIN을 이해할 때는 “어느 table의 row를 기준으로 남길 것인가”가 중요하다.
- JOIN은 보통 `FROM` 단계에서 table을 합친 뒤 `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, `LIMIT` 흐름으로 결과를 다듬는다고 생각하면 이해하기 쉽다.
- column 이름이 여러 table에 함께 있을 때는 `articles.id`, `users.id`처럼 table 이름을 붙여 모호함을 줄인다.

- JOIN 종류
  - `INNER JOIN`
    - 양쪽 table에 모두 매칭되는 row만 남긴다.
    - 게시글 작성자처럼 반드시 연결된 대상이 있는 row를 조회할 때 사용한다.
  - `LEFT JOIN`
    - 왼쪽 table의 row는 모두 남기고, 오른쪽 table의 매칭 결과를 붙인다.
    - 댓글이 없는 게시글도 목록에 남기고 싶을 때 유용하다.
  - `RIGHT JOIN`
    - 오른쪽 table을 기준으로 row를 남긴다.
    - SQLite에서는 직접 지원이 제한적일 수 있어 table 순서를 바꾸는 방식으로 생각할 수 있다.
  - `CROSS JOIN`
    - 양쪽 table의 모든 조합을 만든다.
    - 명확한 목적 없이 사용하면 결과 row 수가 급격히 커진다.
  - comma join
    - `FROM articles, users WHERE articles.user_id = users.id`처럼 쓰는 방식도 있다.
    - 명시적인 `INNER JOIN ... ON ...`이 관계 조건을 더 분명하게 보여준다.

- 예시: INNER JOIN
  ```sql
  SELECT
      articles.id,
      articles.title,
      users.username
  FROM articles
  INNER JOIN users
      ON articles.user_id = users.id;
  ```

  - `articles.user_id`와 `users.id`가 같은 row를 연결한다.
  - 게시글 목록에 작성자 이름을 함께 보여줄 때 이런 형태를 사용한다.
  - 연결 기준 column을 명확히 쓰지 않으면 의도하지 않은 결과가 나올 수 있다.

- 예시: LEFT JOIN
  ```sql
  SELECT
      articles.id,
      articles.title,
      COUNT(comments.id) AS comment_count
  FROM articles
  LEFT JOIN comments
      ON articles.id = comments.article_id
  GROUP BY articles.id
  ORDER BY articles.id;
  ```

  - 댓글이 없는 게시글도 `articles` 기준으로 결과에 남는다.
  - `COUNT(comments.id)`는 연결된 댓글 수를 센다.
  - 목록 화면에서 게시글별 댓글 수를 보여줄 때 사용할 수 있는 패턴이다.
- 예시: CROSS JOIN
  ```sql
  SELECT products.name, colors.name
  FROM products
  CROSS JOIN colors;
  ```

  - 상품과 색상처럼 모든 조합을 만들어야 할 때 사용할 수 있다.
  - 두 table row 수를 곱한 만큼 결과가 생기므로 큰 table에서는 주의해야 한다.

## Django와 DB
- Django는 Python class로 DB table을 표현한다.
- 모델 class는 migration을 거쳐 실제 DB schema가 된다.
- view에서는 ORM을 통해 SQL을 직접 작성하지 않고 데이터를 조회하거나 저장할 수 있다.
- template에서는 view가 넘긴 context를 화면에 표시한다.

## Django 프로젝트 기본 흐름
- 프로젝트 생성
  - `django-admin startproject`
- 앱 생성
  - `python manage.py startapp`
- 앱 등록
  - `INSTALLED_APPS`
- 모델 정의
  - `models.py`
- migration 생성과 적용
  - `makemigrations`
  - `migrate`
- URL 연결
  - project URL에서 app URL을 include한다.
- view와 template 작성
  - 요청을 처리하고 HTML을 응답한다.
- 전역 template 설정
  - `settings.py`의 `TEMPLATES["DIRS"]`에 `BASE_DIR / "templates"`를 등록하면 프로젝트 공통 template을 둘 수 있다.
- URL namespace
  - app별 `urls.py`에 `app_name`을 지정하면 `{% url 'movies:detail' movie.pk %}`처럼 명확하게 URL을 역참조할 수 있다.
- URL parameter
  - detail, update, delete처럼 특정 객체를 다루는 URL에는 pk를 포함한다.
  - 댓글 삭제처럼 게시글과 댓글을 함께 알아야 하는 경우 `movie_pk`, `comment_pk`를 분리해서 받는다.
- custom user model
  - 프로젝트 초기에 `AUTH_USER_MODEL`을 설정해야 이후 관계 모델에서 일관되게 사용자 모델을 참조할 수 있다.
- 예시: settings와 URL 연결
  ```python
  # settings.py
  AUTH_USER_MODEL = "accounts.User"

  TEMPLATES = [
      {
          "DIRS": [BASE_DIR / "templates"],
          # ...
      },
  ]

  # project/urls.py
  urlpatterns = [
      path("accounts/", include("accounts.urls")),
      path("movies/", include("movies.urls")),
  ]
  ```

  - `AUTH_USER_MODEL`은 migration 전에 정하는 것이 안전하다.
  - `include`는 app별 URL을 프로젝트 URL에 연결한다.
- 예시: 객체 pk를 받는 URL 설계
  ```python
  app_name = "movies"

  urlpatterns = [
      path("", views.index, name="index"),
      path("create/", views.create, name="create"),
      path("<int:pk>/", views.detail, name="detail"),
      path("<int:pk>/update/", views.update, name="update"),
      path("<int:pk>/delete/", views.delete, name="delete"),
      path("<int:pk>/comments/", views.comments_create, name="comments_create"),
      path(
          "<int:movie_pk>/comments/<int:comment_pk>/delete/",
          views.comments_delete,
          name="comments_delete",
      ),
  ]
  ```

  - `pk`는 단일 게시글을 찾는 데 사용한다.
  - 댓글 삭제는 어느 게시글로 돌아갈지와 어떤 댓글을 지울지 모두 알아야 하므로 `movie_pk`, `comment_pk`를 함께 받는다.

## Django 인증과 커스텀 유저
- `AbstractUser`
  - Django 기본 User 구조를 유지하면서 필요한 field나 관계를 추가할 때 상속한다.
- `get_user_model`
  - 현재 프로젝트에서 사용 중인 User model을 가져온다.
  - custom user model을 직접 import하기보다 이 함수를 사용하면 설정 변경에 더 안전하다.
- `UserCreationForm`
  - 회원가입 form을 만들 때 기반으로 사용할 수 있다.
- `UserChangeForm`
  - 회원정보 수정 form을 만들 때 기반으로 사용할 수 있다.
- `AuthenticationForm`
  - 로그인 검증에 사용하는 Django 기본 form이다.
- `PasswordChangeForm`
  - 비밀번호 변경에 사용하는 Django 기본 form이다.
- `update_session_auth_hash`
  - 비밀번호 변경 후 기존 로그인 세션이 끊기지 않도록 갱신한다.
- 예시: custom user form
  ```python
  from django.contrib.auth import get_user_model
  from django.contrib.auth.forms import UserChangeForm, UserCreationForm


  class CustomUserCreationForm(UserCreationForm):
      class Meta(UserCreationForm.Meta):
          model = get_user_model()


  class CustomUserChangeForm(UserChangeForm):
      class Meta(UserChangeForm.Meta):
          model = get_user_model()
          fields = ("email", "first_name", "last_name")
  ```

  - form의 `Meta.model`을 `get_user_model()`로 지정하면 custom user model을 기준으로 form이 동작한다.
  - 수정 form에서는 사용자가 바꿀 수 있는 field만 노출하는 것이 좋다.
- 예시: login 흐름
  ```python
  from django.contrib.auth import login as auth_login
  from django.contrib.auth.forms import AuthenticationForm


  def login(request):
      if request.user.is_authenticated:
          return redirect("movies:index")

      if request.method == "POST":
          form = AuthenticationForm(request, request.POST)
          if form.is_valid():
              auth_login(request, form.get_user())
              return redirect("movies:index")
      else:
          form = AuthenticationForm()

      return render(request, "accounts/login.html", {"form": form})
  ```

  - 이미 로그인한 사용자는 로그인 페이지에 다시 접근하지 않게 redirect할 수 있다.
  - `AuthenticationForm`은 request와 POST 데이터를 함께 받는다.
- 예시: logout과 회원탈퇴는 POST로 처리
  ```python
  @require_POST
  def logout(request):
      if request.user.is_authenticated:
          auth_logout(request)
      return redirect("movies:index")


  @require_POST
  def delete(request):
      if request.user.is_authenticated:
          request.user.delete()
          auth_logout(request)
      return redirect("movies:index")
  ```

  - 로그아웃과 회원탈퇴는 세션이나 DB 상태를 바꾸므로 POST 요청으로 처리한다.
  - 회원탈퇴 후에는 세션도 함께 정리한다.
- 예시: 비밀번호 변경 후 세션 유지
  ```python
  from django.contrib.auth import update_session_auth_hash
  from django.contrib.auth.forms import PasswordChangeForm


  @login_required
  def change_password(request):
      if request.method == "POST":
          form = PasswordChangeForm(request.user, request.POST)
          if form.is_valid():
              form.save()
              update_session_auth_hash(request, form.user)
              return redirect("movies:index")
      else:
          form = PasswordChangeForm(request.user)

      return render(request, "accounts/change_password.html", {"form": form})
  ```

  - 비밀번호가 바뀌면 인증 hash가 달라진다.
  - `update_session_auth_hash`를 호출하지 않으면 사용자가 로그아웃될 수 있다.

## Django 모델 관계
- `ForeignKey`
  - 1:N 관계를 표현한다.
  - 한 명의 사용자가 여러 게시글을 작성하거나, 하나의 게시글에 여러 댓글이 달리는 구조에 사용한다.
- `ManyToManyField`
  - M:N 관계를 표현한다.
  - 좋아요, 팔로우, 해시태그처럼 양쪽 모두 여러 대상을 가질 수 있을 때 사용한다.
- `related_name`
  - 역참조 이름을 직접 지정한다.
  - 예를 들어 사용자가 좋아요한 게시글을 `user.like_movies.all()`처럼 조회할 수 있게 만든다.

- 예시: 1:N 모델 관계
  ```python
  from django.conf import settings
  from django.db import models


  class Movie(models.Model):
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      title = models.CharField(max_length=100)
      description = models.TextField()


  class Comment(models.Model):
      movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      content = models.CharField(max_length=200)
  ```

  - `Movie.user`
    - 게시글 작성자를 나타낸다.
  - `Comment.movie`
    - 댓글이 어느 게시글에 속하는지 나타낸다.
  - `Comment.user`
    - 댓글 작성자를 나타낸다.
  - `on_delete=models.CASCADE`
    - 연결된 대상이 삭제될 때 함께 삭제되도록 한다.

## Django CRUD
- Create
  - form 입력을 검증하고 새 객체를 저장한다.
- Read
  - index/detail 화면에서 객체 목록과 상세 정보를 조회한다.
- Update
  - 기존 객체를 form instance로 불러와 수정한다.
- Delete
  - 권한을 확인한 뒤 객체를 삭제한다.
- `ModelForm`
  - 모델 기반 form을 만들어 입력 검증과 객체 저장을 연결한다.
- 댓글 처리
  - 댓글 form에는 사용자가 입력할 `content`만 노출하고, `movie`와 `user`는 view에서 직접 연결한다.
- 역참조
  - `movie.comment_set.all()`처럼 특정 게시글에 연결된 댓글 목록을 가져올 수 있다.
- 소유자 기반 UI
  - template에서는 현재 사용자가 작성자인 경우에만 수정/삭제 버튼을 보여줄 수 있다.
- 예시: MovieForm과 CommentForm
  ```python
  from django import forms
  from .models import Comment, Movie


  class MovieForm(forms.ModelForm):
      class Meta:
          model = Movie
          fields = ("title", "description")


  class CommentForm(forms.ModelForm):
      class Meta:
          model = Comment
          fields = ("content",)
  ```

  - 작성자나 연결된 게시글은 사용자가 form에서 고르는 값이 아니라 view에서 정해야 한다.
  - form에 노출할 field를 제한하면 의도하지 않은 데이터 수정 가능성을 줄일 수 있다.

- 예시: ModelForm 저장 흐름
  ```python
  @login_required
  def create(request):
      if request.method == "POST":
          form = MovieForm(request.POST)
          if form.is_valid():
              movie = form.save(commit=False)
              movie.user = request.user
              movie.save()
              return redirect("movies:detail", movie.pk)
      else:
          form = MovieForm()

      return render(request, "movies/create.html", {"form": form})
  ```

  - `commit=False`
    - DB에 바로 저장하지 않고 객체만 만든다.
    - 작성자처럼 form에 없는 값을 추가한 뒤 저장할 수 있다.
  - `request.user`
    - 현재 로그인한 사용자를 작성자로 연결한다.
  - `redirect`
    - 저장 후 detail 화면으로 이동한다.
- 예시: detail에서 댓글 form과 댓글 목록 전달
  ```python
  def detail(request, pk):
      movie = get_object_or_404(Movie, pk=pk)
      comment_form = CommentForm()
      comments = movie.comment_set.all()

      context = {
          "movie": movie,
          "comment_form": comment_form,
          "comments": comments,
      }
      return render(request, "movies/detail.html", context)
  ```

  - `comment_set`은 `Comment.movie`의 역참조 manager이다.
  - detail 화면은 게시글 자체뿐 아니라 댓글 작성 form과 기존 댓글 목록도 함께 필요하다.
- 예시: 댓글 생성
  ```python
  @require_POST
  def comments_create(request, pk):
      if not request.user.is_authenticated:
          return redirect("accounts:login")

      movie = get_object_or_404(Movie, pk=pk)
      form = CommentForm(request.POST)

      if form.is_valid():
          comment = form.save(commit=False)
          comment.movie = movie
          comment.user = request.user
          comment.save()

      return redirect("movies:detail", movie.pk)
  ```

  - 댓글은 특정 movie와 현재 user에 연결된 뒤 저장되어야 한다.
  - 게시글 생성과 마찬가지로 `commit=False`가 관계 field를 채울 시간을 준다.
- 예시: 댓글 삭제
  ```python
  @require_POST
  def comments_delete(request, movie_pk, comment_pk):
      comment = get_object_or_404(Comment, pk=comment_pk)

      if request.user == comment.user:
          comment.delete()

      return redirect("movies:detail", movie_pk)
  ```

  - 댓글 삭제 URL에는 게시글 pk와 댓글 pk가 모두 필요하다.
  - 댓글 작성자만 삭제할 수 있게 확인한다.
- 예시: 게시글 수정
  ```python
  @login_required
  def update(request, pk):
      movie = get_object_or_404(Movie, pk=pk)

      if request.user != movie.user:
          return redirect("movies:index")

      if request.method == "POST":
          form = MovieForm(request.POST, instance=movie)
          if form.is_valid():
              form.save()
              return redirect("movies:detail", movie.pk)
      else:
          form = MovieForm(instance=movie)

      return render(request, "movies/update.html", {"movie": movie, "form": form})
  ```

  - `instance=movie`를 넘기면 기존 데이터를 채운 form을 만들 수 있다.
  - POST에서도 같은 instance를 넘겨야 새 객체 생성이 아니라 기존 객체 수정이 된다.
  - 작성자가 아니면 수정 화면에 접근하지 못하게 한다.
- 예시: 게시글 삭제
  ```python
  @require_POST
  def delete(request, pk):
      movie = get_object_or_404(Movie, pk=pk)

      if request.user.is_authenticated and request.user == movie.user:
          movie.delete()

      return redirect("movies:index")
  ```

  - 삭제는 반드시 POST 요청으로 처리한다.
  - 작성자 확인 없이 삭제하면 다른 사용자의 데이터를 지울 수 있다.
- 예시: 작성자에게만 수정/삭제 UI 보여주기
  ```django
  {% if user == movie.user %}
    <a href="{% url 'movies:update' movie.pk %}">UPDATE</a>

    <form action="{% url 'movies:delete' movie.pk %}" method="POST">
      {% csrf_token %}
      <button type="submit">DELETE</button>
    </form>
  {% endif %}
  ```

  - template에서 버튼을 숨기는 것은 사용자 경험을 위한 처리이다.
  - 실제 권한 검사는 view에서도 반드시 다시 해야 한다.

## HTTP Method와 권한
- 조회 화면
  - `GET` 요청으로 처리한다.
- 생성, 수정, 삭제
  - 데이터가 바뀌므로 `POST` 요청을 사용한다.
- `@login_required`
  - 로그인한 사용자만 접근하게 한다.
- `@require_POST`
  - POST 요청만 허용한다.
- 소유자 확인
  - 작성자만 수정/삭제할 수 있게 한다.

## M:N 관계
- M:N 관계는 한 row가 여러 row와 연결되고, 반대쪽도 여러 row와 연결되는 구조이다.
- Django는 `ManyToManyField`로 중개 테이블을 자동 생성할 수 있다.
- PDF의 좋아요/팔로우/해시태그 시각 자료는 모두 “중복 저장을 피하고 관계만 별도 테이블에 저장한다”는 관점으로 이해할 수 있다.
- 중개 테이블
  - M:N 관계의 양쪽 pk를 저장하는 table이다.
  - 예를 들어 게시글 좋아요는 `movie_id`와 `user_id`를 저장하는 중개 테이블로 표현된다.
- 역참조 이름 충돌
  - 같은 User 모델을 `ForeignKey`와 `ManyToManyField`가 동시에 참조하면 역참조 이름이 헷갈릴 수 있다.
  - 이때 `related_name`으로 “작성한 글”과 “좋아요한 글”을 구분한다.

## 좋아요 구현
- 한 사용자는 여러 게시글에 좋아요를 누를 수 있다.
- 한 게시글은 여러 사용자에게 좋아요를 받을 수 있다.
- 따라서 `Movie`와 `User`는 M:N 관계이다.

- 예시: 좋아요 모델
  ```python
  class Movie(models.Model):
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      like_users = models.ManyToManyField(
          settings.AUTH_USER_MODEL,
          related_name="like_movies",
          blank=True,
      )
      title = models.CharField(max_length=100)
      description = models.TextField()
  ```

  - `like_users`
    - 해당 게시글을 좋아요한 사용자 목록이다.
  - `related_name="like_movies"`
    - 사용자 기준에서 좋아요한 게시글 목록을 조회할 때 사용한다.
  - `blank=True`
    - 좋아요가 하나도 없어도 게시글을 만들 수 있게 한다.
- 예시: 좋아요 관계 조회
  ```python
  movie.like_users.all()      # 이 게시글을 좋아요한 사용자들
  user.like_movies.all()      # 이 사용자가 좋아요한 게시글들
  movie.like_users.count()    # 이 게시글의 좋아요 수
  ```

  - `movie.user`는 게시글 작성자이다.
  - `movie.like_users`는 게시글을 좋아요한 사용자 목록이다.
  - 둘 다 User와 연결되지만 의미가 다르므로 이름을 분명히 나누어야 한다.

- 예시: 좋아요 토글 view
  ```python
  @require_POST
  def likes(request, movie_pk):
      if not request.user.is_authenticated:
          return redirect("accounts:login")

      movie = get_object_or_404(Movie, pk=movie_pk)

      if movie.like_users.filter(pk=request.user.pk).exists():
          movie.like_users.remove(request.user)
      else:
          movie.like_users.add(request.user)

      return redirect("movies:detail", movie.pk)
  ```

  - 이미 좋아요한 사용자라면 `remove`로 취소한다.
  - 아직 좋아요하지 않았다면 `add`로 추가한다.
  - 같은 URL이 좋아요와 좋아요 취소를 모두 처리한다.

- 예시: 좋아요 template
  ```django
  <form action="{% url 'movies:likes' movie.pk %}" method="POST">
    {% csrf_token %}
    {% if request.user in movie.like_users.all %}
      <input type="submit" value="좋아요 취소">
    {% else %}
      <input type="submit" value="좋아요">
    {% endif %}
  </form>

  <p>좋아요: {{ movie.like_users.count }}개</p>
  ```

  - template에서는 현재 사용자가 좋아요 목록에 있는지 확인한다.
  - `count`로 좋아요 수를 표시할 수 있다.

## 팔로우 구현
- 팔로우는 User와 User 사이의 M:N 관계이다.
- 사용자가 자기 자신을 팔로우하면 안 된다.
- 방향성이 있는 관계이므로 `symmetrical=False`가 중요하다.

- 예시: 팔로우 모델
  ```python
  from django.contrib.auth.models import AbstractUser
  from django.db import models


  class User(AbstractUser):
      followings = models.ManyToManyField(
          "self",
          symmetrical=False,
          related_name="followers",
          blank=True,
      )
  ```

  - `followings`
    - 내가 팔로우하는 사용자 목록이다.
  - `followers`
    - 나를 팔로우하는 사용자 목록이다.
  - `symmetrical=False`
    - A가 B를 팔로우한다고 해서 B가 A를 자동으로 팔로우하지 않게 한다.

- 예시: 팔로우 토글 view
  ```python
  @require_POST
  def follow(request, user_pk):
      if not request.user.is_authenticated:
          return redirect("accounts:login")

      person = get_object_or_404(get_user_model(), pk=user_pk)

      if person == request.user:
          return redirect("accounts:profile", person.username)

      if person.followers.filter(pk=request.user.pk).exists():
          person.followers.remove(request.user)
      else:
          person.followers.add(request.user)

      return redirect("accounts:profile", person.username)
  ```

  - 팔로우 대상과 현재 사용자가 같은지 먼저 확인한다.
  - `person.followers`를 기준으로 현재 사용자가 이미 팔로우 중인지 검사한다.
  - 좋아요와 마찬가지로 add/remove toggle 구조이다.
- 예시: 팔로우 template
  ```django
  {% if request.user != person %}
    <form action="{% url 'accounts:follow' person.pk %}" method="POST">
      {% csrf_token %}
      {% if request.user in person.followers.all %}
        <input type="submit" value="Unfollow">
      {% else %}
        <input type="submit" value="Follow">
      {% endif %}
    </form>
  {% endif %}
  ```

  - 자기 자신의 profile에서는 follow 버튼을 보여주지 않는다.
  - 현재 사용자가 이미 follower 목록에 있으면 `Unfollow`, 없으면 `Follow`를 보여준다.

## Profile 화면에서 확인할 관계
- 사용자가 작성한 게시글
  - `person.movie_set.all`
- 사용자가 작성한 댓글
  - `person.comment_set.all`
- 사용자가 좋아요한 게시글
  - `person.like_movies.all`
- 팔로잉 수
  - `person.followings.count`
- 팔로워 수
  - `person.followers.count`

## Fixtures
- Fixtures는 DB 초기 데이터나 예시 데이터를 JSON 같은 파일로 저장해 두는 방식이다.
- 실습에서는 사용자, 영화, 댓글, 좋아요, 팔로우 관계가 fixture에 포함될 수 있음을 확인했다.
- M:N 관계는 fixture에서 pk 목록으로 표현된다.
- fixture 파일 위치
  - app 안에 `fixtures/` 폴더를 만들고 JSON 파일을 넣으면 `loaddata`로 불러오기 쉽다.
  - 예를 들어 `accounts/fixtures/users.json`, `movies/fixtures/movie.json`처럼 나눌 수 있다.
- 인코딩
  - 한글 데이터가 포함된 fixture를 만들 때는 UTF-8 출력이 깨지지 않도록 주의한다.
  - 실습에서는 `python -Xutf8 manage.py dumpdata ...` 형태로 UTF-8 출력을 강제하는 흐름을 확인했다.

- 예시: fixture 데이터 형태
  ```json
  [
    {
      "model": "movies.movie",
      "pk": 1,
      "fields": {
        "user": 1,
        "title": "Example Movie",
        "description": "sample description",
        "like_users": [2, 3]
      }
    }
  ]
  ```

  - `model`
    - 어떤 app의 어떤 model인지 나타낸다.
  - `pk`
    - 객체의 primary key이다.
  - `fields`
    - 실제 column 값이다.
  - M:N field
    - 연결된 객체의 pk 목록으로 표현된다.

- 예시: dumpdata와 loaddata
  ```bash
  python -Xutf8 manage.py dumpdata movies.movie --indent 2 > movies.json
  python manage.py loaddata movies.json
  ```

  - `dumpdata`
    - 현재 DB 데이터를 fixture 파일로 내보낸다.
  - `loaddata`
    - fixture 파일을 읽어 DB에 넣는다.
  - 여러 fixture load
    ```bash
    python manage.py loaddata users.json movie.json comment.json
    ```

  - 관계가 있는 데이터는 참조 대상이 먼저 준비되어 있어야 한다.
  - 사용자, 게시글, 댓글처럼 연결된 fixture는 load 순서와 pk 일관성을 확인한다.
  - 공개 저장소에서는 실사용자의 개인정보나 계정 정보가 들어간 fixture를 남기면 안 된다.

## Hashtag 구현
- Hashtag는 게시글 내용에 포함된 `#word`를 별도 모델로 저장하고, 게시글과 M:N 관계로 연결하는 방식이다.
- 같은 hashtag가 중복으로 만들어지지 않도록 `unique=True`를 사용할 수 있다.
- 게시글 생성/수정 시 description을 단어 단위로 훑어 `#`로 시작하는 단어를 찾아 연결한다.

- 예시: Hashtag 모델
  ```python
  class Hashtag(models.Model):
      content = models.TextField(unique=True)

      def __str__(self):
          return self.content


  class Movie(models.Model):
      hashtags = models.ManyToManyField(Hashtag, blank=True)
      description = models.TextField()
  ```

  - `Hashtag.content`
    - `#django` 같은 태그 문자열이다.
  - `unique=True`
    - 같은 태그가 여러 row로 저장되는 것을 막는다.
  - `Movie.hashtags`
    - 한 게시글이 여러 태그를 가질 수 있고, 한 태그가 여러 게시글에 연결될 수 있다.

- 예시: 생성 시 hashtag 연결
  ```python
  movie = form.save(commit=False)
  movie.user = request.user
  movie.save()

  for word in movie.description.split():
      if word.startswith("#"):
          hashtag, created = Hashtag.objects.get_or_create(content=word)
          movie.hashtags.add(hashtag)
  ```

  - `get_or_create`
    - 이미 있는 hashtag는 가져오고, 없으면 새로 만든다.
    - 반환값은 `(객체, 생성 여부)` 형태이다.
  - `movie.save()`
    - M:N 관계를 추가하려면 먼저 movie가 DB에 저장되어 pk를 가져야 한다.
  - `movie.hashtags.add`
    - 게시글과 hashtag 사이의 관계를 추가한다.
- 예시: `created` 값 활용
  ```python
  hashtag, created = Hashtag.objects.get_or_create(content=word)

  if created:
      print("새 hashtag가 만들어졌다.")
  else:
      print("이미 있던 hashtag를 재사용한다.")
  ```

  - 당장 `created`를 사용하지 않아도 `get_or_create`의 동작을 이해하는 데 도움이 된다.
  - 중복 생성을 피해야 하는 tag, category, keyword 류의 데이터에서 자주 쓰는 패턴이다.

- 예시: 수정 시 hashtag 갱신
  ```python
  movie = form.save()
  movie.hashtags.clear()

  for word in movie.description.split():
      if word.startswith("#"):
          hashtag, created = Hashtag.objects.get_or_create(content=word)
          movie.hashtags.add(hashtag)
  ```

  - 수정 전 연결된 hashtag를 먼저 비운다.
  - 새 description을 기준으로 hashtag 관계를 다시 만든다.
  - `clear`를 하지 않으면 삭제된 hashtag 관계가 남을 수 있다.
  - `clear`는 관계만 삭제한다.
    - `Hashtag` table의 row 자체를 삭제하는 것은 아니다.
    - 다른 게시글이 같은 hashtag를 쓰고 있을 수 있기 때문이다.

- 예시: hashtag별 게시글 조회
  ```python
  @login_required
  def hashtag(request, hash_pk):
      hashtag = get_object_or_404(Hashtag, pk=hash_pk)
      movies = hashtag.movie_set.order_by("-pk")

      return render(
          request,
          "movies/hashtag.html",
          {"hashtag": hashtag, "movies": movies},
      )
  ```

  - `hashtag.movie_set`
    - 특정 hashtag에 연결된 게시글 목록을 역참조한다.
  - `order_by("-pk")`
    - 최신 게시글이 먼저 보이도록 정렬한다.

- 예시: template filter로 hashtag 링크 만들기
  ```python
  from django import template

  register = template.Library()


  @register.filter
  def hashtag_link(movie):
      content = movie.description + " "

      for hashtag in movie.hashtags.all():
          url = f"/movies/{hashtag.pk}/hashtag/"
          content = content.replace(
              hashtag.content + " ",
              f'<a href="{url}">{hashtag.content}</a> ',
          )

      return content
  ```

  ```django
  {% load make_link %}

  {{ movie|hashtag_link|safe }}
  ```

  - custom template filter를 사용하면 description 안의 hashtag를 링크로 바꿀 수 있다.
  - HTML 문자열을 출력하므로 template에서 `safe`를 사용할 수 있지만, 사용자 입력을 HTML로 바꾸는 작업은 XSS 위험을 항상 고려해야 한다.

## CSV와 데이터 가져오기
- `users.csv`는 이름, 나이, 지역, 전화번호, 금액처럼 보이는 사용자 데이터를 담고 있다.
- SQL 실습에서는 CSV를 SQLite table로 가져온 뒤 조회, 정렬, 필터링, 그룹화를 연습할 수 있다.
- CSV를 다룰 때는 header 유무, encoding, delimiter, column type을 먼저 확인해야 한다.

- 예시: CSV import 후 확인할 쿼리
  ```sql
  SELECT COUNT(*) FROM users;

  SELECT age, COUNT(*) AS user_count
  FROM users
  GROUP BY age
  ORDER BY age;

  SELECT country, AVG(balance) AS avg_balance
  FROM users
  GROUP BY country
  ORDER BY avg_balance DESC;
  ```

  - 데이터가 제대로 들어왔는지 row 수를 먼저 확인한다.
  - 숫자 column은 집계로 분포를 확인한다.
  - 범주 column은 group by로 묶어 비교한다.

## 정리하며 남긴 기준
- 관계를 먼저 그린 뒤 모델을 작성한다.
  - 1:N인지 M:N인지 판단하면 `ForeignKey`와 `ManyToManyField` 선택이 쉬워진다.
- M:N은 중복 데이터를 저장하는 방식으로 해결하지 않는다.
  - 관계 자체를 별도 중개 테이블로 관리한다.
- POST 요청으로 상태 변경을 처리한다.
  - 좋아요, 팔로우, 삭제처럼 DB를 바꾸는 동작은 GET으로 만들지 않는다.
- 로그인 여부와 소유자 권한을 함께 확인한다.
  - 인증과 인가를 분리해서 생각해야 한다.
- fixture는 편리하지만 공개 저장소에서는 조심한다.
  - 사용자 계정, 비밀번호 hash, 개인정보, 기관 제공 데이터가 들어갈 수 있다.
- 공개용 기록에는 원본 코드보다 개념, 관계 구조, 구현 패턴, 주의점을 남긴다.
