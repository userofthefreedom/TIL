# JavaScript

JavaScript는 웹 브라우저에서 동적인 동작을 만들기 위해 사용하는 프로그래밍 언어다.  
이 폴더에서는 JavaScript 기초 문법, 함수와 객체, `this`, 배열 helper method, DOM 조작, Event, 비동기 처리, Axios를 이용한 Ajax 요청까지 정리한다.

## JavaScript Quick Navigation

- [JavaScript](#javascript)
  - [JavaScript Quick Navigation](#javascript-quick-navigation)
  - [JavaScript의 큰 흐름](#javascript의-큰-흐름)
  - [변수 선언과 기본 자료형](#변수-선언과-기본-자료형)
  - [연산자, 조건문, 반복문](#연산자-조건문-반복문)
  - [Array와 Object 기초](#array와-object-기초)
  - [객체 문법 확장](#객체-문법-확장)
  - [함수](#함수)
  - [Callback 함수](#callback-함수)
  - [`this`](#this)
  - [Array Helper Method](#array-helper-method)
  - [DOM과 BOM](#dom과-bom)
  - [DOM 요소 선택과 조작](#dom-요소-선택과-조작)
  - [Event](#event)
  - [비동기 처리](#비동기-처리)
  - [Promise, then/catch, async/await](#promise-thencatch-asyncawait)
  - [Axios와 Ajax](#axios와-ajax)
  - [Ajax 좋아요와 팔로우 실습 흐름](#ajax-좋아요와-팔로우-실습-흐름)
  - [정리하며 남긴 기준](#정리하며-남긴-기준)

## JavaScript의 큰 흐름

브라우저 환경에서 JavaScript는 단순히 문법만 있는 언어가 아니라, 브라우저가 제공하는 기능과 함께 동작한다.

```text
JavaScript
-> ECMAScript 문법
-> DOM
-> BOM
-> Web API
```

- `ECMAScript`: 변수, 함수, 객체, 배열 같은 JavaScript의 표준 문법이다.
- `DOM`: HTML 문서를 객체처럼 다룰 수 있게 만든 구조다.
- `BOM`: 브라우저 창, 주소, history 같은 브라우저 기능을 다루는 객체 모델이다.
- `Web API`: 브라우저가 제공하는 비동기, 이벤트, 요청 처리 기능이다.

JavaScript를 공부할 때는 다음 연결을 계속 확인해야 한다.

- 문법으로 값을 만들고 가공한다.
- DOM에서 원하는 HTML 요소를 선택한다.
- Event로 사용자 동작을 감지한다.
- 비동기 요청으로 서버와 통신한다.
- 응답 데이터를 이용해 DOM을 다시 갱신한다.

## 변수 선언과 기본 자료형

JavaScript의 변수 선언 키워드는 `const`, `let`, `var`가 있다.

- `const`: 재할당하지 않을 값을 선언한다.
- `let`: 재할당이 필요한 값을 선언한다.
- `var`: 오래된 문법이며 재선언 문제가 있어 사용을 피한다.

대부분의 경우 `const`를 먼저 생각하고, 값이 바뀌어야 할 때만 `let`을 사용한다.

```javascript
const name = "minho";
let count = 0;

count += 1;
console.log(name, count);
```

`var`는 같은 이름으로 다시 선언해도 에러가 나지 않아 큰 코드에서 실수를 숨길 수 있다.

```javascript
var greeting = "안녕";
var greeting = "하이";

console.log(greeting); // "하이"
```

변수 선언 키워드 없이 값을 대입하는 방식도 피한다. 브라우저 환경에서는 전역 객체인 `window`에 값이 붙을 수 있어, 작은 실수가 전역 상태를 오염시킬 수 있다.

```javascript
// greeting = "hello"; // 선언자 없이 쓰지 않는다.
const greeting = "hello";
```

`const`는 변수 재할당을 막지만, 배열 요소나 객체 속성의 변경까지 막지는 않는다.

```javascript
const numbers = [1, 2, 3];
numbers.push(4);
console.log(numbers); // [1, 2, 3, 4]

const user = {
  name: "kim",
};
user.name = "lee";
console.log(user.name); // "lee"
```

자료형은 크게 원시 타입과 참조 타입으로 볼 수 있다.

- 원시 타입: `number`, `string`, `boolean`, `undefined`, `null`, `symbol`, `bigint`
- 참조 타입: `object`, `array`, `function`

`typeof`로 값의 타입을 확인할 수 있다.

```javascript
console.log(typeof 1); // "number"
console.log(typeof "hello"); // "string"
console.log(typeof true); // "boolean"
console.log(typeof undefined); // "undefined"
console.log(typeof null); // "object"
```

`null`의 `typeof` 결과가 `"object"`인 것은 JavaScript의 오래된 동작이다. 값이 없음을 직접 표현하려면 `null`, 아직 값이 할당되지 않았음을 표현하려면 `undefined`로 이해하면 된다.

조건문에서는 boolean이 아닌 값도 참/거짓처럼 평가된다.

- falsy: `false`, `0`, `""`, `undefined`, `null`, `NaN`
- truthy: falsy를 제외한 대부분의 값

빈 배열 `[]`과 빈 객체 `{}`는 값이 비어 있어도 truthy다. 그래서 배열이 비었는지 확인하려면 배열 자체를 조건에 넣기보다 `length`를 확인한다.

```javascript
const numbers = [];

if (numbers.length === 0) {
  console.log("비어 있음");
}
```

문자열을 만들 때 backtick을 사용하면 template literal을 쓸 수 있다.

```javascript
const username = "minho";
const age = 20;

console.log(`${username}의 나이는 ${age}살입니다.`);
```

## 연산자, 조건문, 반복문

비교할 때는 `==`보다 `===`를 사용한다.

- `==`: 타입 변환 후 비교한다.
- `===`: 타입까지 엄격하게 비교한다.

```javascript
console.log(1 == "1"); // true
console.log(1 === "1"); // false
```

조건문:

```javascript
const score = 85;

if (score >= 90) {
  console.log("A");
} else if (score >= 80) {
  console.log("B");
} else {
  console.log("C");
}
```

논리 연산자:

```javascript
const isLoggedIn = true;
const isOwner = false;

if (isLoggedIn && isOwner) {
  console.log("수정 가능");
}

if (isLoggedIn || isOwner) {
  console.log("접근 가능");
}
```

반복문:

```javascript
for (let i = 0; i < 5; i += 1) {
  console.log(i);
}
```

반복문의 index처럼 값이 계속 바뀌어야 하는 변수에는 `let`을 사용한다.

배열을 값 중심으로 순회할 때는 `for...of`, 객체의 key를 순회할 때는 `for...in`을 사용할 수 있다.

```javascript
const names = ["kim", "lee", "park"];

for (const name of names) {
  console.log(name);
}
```

```javascript
const user = {
  name: "kim",
  age: 20,
};

for (const key in user) {
  console.log(key, user[key]);
}
```

`for...of`와 `for...in`에서 선언한 변수는 반복이 돌 때마다 블록 안에서 새로 만들어진다. 배열은 값이 중요하므로 `for...of`, 객체는 속성 이름이 중요하므로 `for...in`으로 구분해 두면 읽기 쉽다.

## Array와 Object 기초

Array는 순서가 있는 값의 묶음이다.

```javascript
const fruits = ["apple", "banana", "orange"];

console.log(fruits[0]); // "apple"
console.log(fruits.length); // 3

fruits.push("mango");
console.log(fruits);
```

배열 기본 메서드는 위치 기준으로 생각하면 정리하기 쉽다.

```javascript
const numbers = [1, 2, 3, 4];

numbers.push(5);       // 뒤에 추가
numbers.pop();         // 뒤에서 제거
numbers.unshift(0);    // 앞에 추가
numbers.shift();       // 앞에서 제거

console.log(numbers.indexOf(3));   // 3의 index, 없으면 -1
console.log(numbers.includes(3));  // 포함 여부
console.log(numbers.join("/"));    // "1/2/3/4"
```

문자열도 자주 쓰는 메서드가 있다.

```javascript
const message = "hello javascript";

console.log(message.length);
console.log(message.includes("java")); // true
console.log(message.split(" "));       // ["hello", "javascript"]
```

문자열을 바꾸거나 공백을 정리할 때도 전용 메서드를 사용한다.

```javascript
const rawText = "  hello javascript  ";

console.log(rawText.trim());                 // "hello javascript"
console.log(rawText.trimStart());            // "hello javascript  "
console.log(rawText.trimEnd());              // "  hello javascript"
console.log(rawText.replace("a", "A"));      // 첫 번째 a만 변경
console.log(rawText.replaceAll("a", "A"));   // 모든 a 변경
```

Object는 key와 value로 이루어진 property의 묶음이다.

```javascript
const person = {
  name: "kevin",
  age: 42,
  greeting: function () {
    console.log(`안녕하세요 저는 ${this.name}입니다.`);
  },
};

console.log(person.name);
person.greeting();
```

객체의 value에는 문자열, 숫자, 배열, 객체, 함수 등 거의 모든 값이 들어갈 수 있다. 객체 안에 있는 함수를 method라고 부른다.

없는 index나 없는 property에 접근하면 `undefined`가 나온다. 이것은 값이 없다는 결과이지, 접근 자체가 항상 에러라는 뜻은 아니다.

```javascript
const numbers = [1, 2, 3];
const user = {
  name: "kim",
};

console.log(numbers[10]); // undefined
console.log(user.email);  // undefined
```

## 객체 문법 확장

객체 key를 동적으로 만들 수 있다.

```javascript
const key = "name";

const user = {
  [key]: "kim",
};

console.log(user.name); // "kim"
```

변수명과 property명이 같으면 속성명 축약을 사용할 수 있다.

```javascript
const name = "kim";
const age = 20;

const user = {
  name,
  age,
};
```

객체 method도 짧게 쓸 수 있다.

```javascript
const calculator = {
  add(a, b) {
    return a + b;
  },
};

console.log(calculator.add(1, 2));
```

Destructuring은 객체나 배열에서 값을 꺼내 변수에 담는 문법이다.

```javascript
const user = {
  username: "kim",
  email: "kim@example.com",
};

const { username, email } = user;
console.log(username, email);
```

배열 destructuring:

```javascript
const numbers = [10, 20, 30];
const [first, second] = numbers;

console.log(first, second);
```

Spread는 배열이나 객체를 펼쳐서 복사하거나 합칠 때 사용한다.

```javascript
const a = [1, 2];
const b = [3, 4];
const merged = [...a, ...b];

console.log(merged); // [1, 2, 3, 4]
```

```javascript
const baseUser = {
  name: "kim",
};

const detailUser = {
  ...baseUser,
  age: 20,
};

console.log(detailUser);
```

Spread로 배열이나 객체를 복사하면 가장 바깥쪽만 새로 만들어진다. 안쪽에 중첩 객체가 있으면 같은 참조를 공유할 수 있으므로 깊은 복사가 필요한지 확인해야 한다.

```javascript
const original = {
  name: "kim",
  profile: {
    city: "seoul",
  },
};

const copied = { ...original };
copied.profile.city = "busan";

console.log(original.profile.city); // "busan"
```

중첩된 데이터를 완전히 분리해야 한다면 `structuredClone()`이나 lodash의 `_.cloneDeep()` 같은 깊은 복사 도구를 고려한다.

```javascript
const copied = structuredClone(original);
copied.profile.city = "busan";

console.log(original.profile.city); // "seoul"
```

JSON은 JavaScript 객체 표기법을 기반으로 한 데이터 교환 형식이다.

```javascript
const user = {
  name: "kim",
  age: 20,
};

const jsonText = JSON.stringify(user);
const parsedUser = JSON.parse(jsonText);

console.log(jsonText);
console.log(parsedUser.name);
```

JavaScript 객체는 key에 따옴표가 없어도 동작할 수 있지만, JSON 문자열에서는 key를 반드시 큰따옴표로 감싸야 한다. 서버와 통신할 때는 `JSON.stringify()`로 객체를 JSON 문자열로 바꾸고, 문자열 응답을 객체로 다룰 때는 `JSON.parse()`를 사용한다.

```javascript
const validJson = '{"name":"kim","age":20}';
const parsed = JSON.parse(validJson);

console.log(parsed.name);
```

## 함수

JavaScript에서 함수를 만드는 대표적인 방식은 함수 선언식과 함수 표현식이다.

함수 선언식:

```javascript
function add(a, b) {
  return a + b;
}

console.log(add(1, 2));
```

함수 표현식:

```javascript
const add = function (a, b) {
  return a + b;
};

console.log(add(1, 2));
```

둘의 중요한 차이는 hoisting이다.

- 함수 선언식은 선언 전 호출이 가능하다.
- 함수 표현식은 변수에 함수가 할당된 뒤 호출해야 한다.

```javascript
console.log(hello());

function hello() {
  return "hello";
}
```

```javascript
// console.log(hello()); // 오류

const hello = function () {
  return "hello";
};
```

Arrow Function은 함수 표현식을 더 짧게 쓰는 방식이다.

```javascript
const add = (a, b) => {
  return a + b;
};

const multiply = (a, b) => a * b;

console.log(add(1, 2));
console.log(multiply(2, 3));
```

매개변수가 하나면 괄호를 생략할 수 있다.

```javascript
const square = number => number * number;
console.log(square(3));
```

하지만 프로젝트에서는 일관성을 위해 매개변수가 하나여도 괄호를 유지하는 스타일도 자주 쓴다.

화살표 함수에서 객체 하나를 바로 반환하려면 객체 literal을 소괄호로 감싼다. 소괄호가 없으면 `{}`를 함수 본문으로 해석할 수 있다.

```javascript
const makeUser = (name) => ({ name });

console.log(makeUser("kim")); // { name: "kim" }
```

## Callback 함수

JavaScript에서 함수는 값처럼 사용할 수 있다.  
함수를 다른 함수의 인자로 넘기면 callback 함수가 된다.

```javascript
function run(callback) {
  callback();
}

run(function () {
  console.log("실행됨");
});
```

`setTimeout`은 callback을 일정 시간 뒤 실행한다.

```javascript
const sayHello = () => {
  console.log("hello");
};

setTimeout(sayHello, 1000);
```

배열 helper method도 callback을 자주 사용한다.

```javascript
const numbers = [1, 2, 3];

numbers.forEach((number) => {
  console.log(number);
});
```

## `this`

`this`는 호출 상황에 따라 가리키는 대상이 달라진다.

객체 method 안에서 일반 함수를 사용하면 `this`는 method를 호출한 객체를 가리킨다.

```javascript
const person = {
  name: "kim",
  greeting: function () {
    console.log(this.name);
  },
};

person.greeting(); // "kim"
```

하지만 method를 변수에 따로 담아 호출하면 호출 주체가 사라진다.

```javascript
const person = {
  name: "kim",
  greeting: function () {
    console.log(this);
  },
};

const greeting = person.greeting;
greeting(); // 브라우저에서는 window를 가리킬 수 있음
```

화살표 함수는 자기만의 `this`를 만들지 않고, 선언된 위치 바깥쪽의 `this`를 사용한다. 이를 lexical this라고 한다.

객체 method로 화살표 함수를 쓰면 기대한 객체를 가리키지 않을 수 있다.

```javascript
const person = {
  name: "kim",
  greeting: () => {
    console.log(this.name);
  },
};

person.greeting(); // 기대와 다를 수 있음
```

따라서 객체 method에서 객체 자신을 `this`로 사용해야 한다면 일반 함수 표현식을 사용하는 편이 안전하다.

반대로 method 안쪽의 중첩 함수에서 바깥 method의 `this`를 그대로 쓰고 싶다면 화살표 함수가 도움이 된다.

```javascript
const person = {
  name: "kim",
  greeting: function () {
    const inner = () => {
      console.log(this.name);
    };

    inner();
  },
};

person.greeting(); // "kim"
```

생성자 함수에서는 `new`로 만들어지는 새 객체가 `this`가 된다.

```javascript
function User(name) {
  this.name = name;
}

const user = new User("kim");
console.log(user.name);
```

`this`를 볼 때의 기준:

- 전역에서 호출했는가
- 객체의 method로 호출했는가
- 생성자 함수로 호출했는가
- 일반 함수인가 화살표 함수인가
- 함수가 어디서 선언되었고, 어떻게 호출되었는가

## Array Helper Method

Array helper method는 배열을 순회하거나 변환할 때 자주 사용한다.

`forEach`는 배열을 순회한다. 반환값을 모아 새 배열을 만들지는 않는다.

```javascript
const menus = ["짜장면", "짬뽕", "탕수육"];

menus.forEach((menu, index) => {
  console.log(`${index}: ${menu}`);
});
```

`forEach`에서는 `break`, `continue`를 사용할 수 없다. 중간에 멈춰야 하는 로직이라면 일반 `for`문이 더 맞을 수 있다.

`map`은 callback의 반환값을 모아 새 배열을 만든다.

```javascript
const numbers = [8, 5, 2, 1];
const doubled = numbers.map((number) => number * 2);

console.log(doubled); // [16, 10, 4, 2]
```

`filter`는 조건이 `true`인 값만 모아 새 배열을 만든다.

```javascript
const numbers = [8, 5, 2, 1];
const evenNumbers = numbers.filter((number) => number % 2 === 0);

console.log(evenNumbers); // [8, 2]
```

`map`과 `filter`를 연결해서 쓸 수 있다.

```javascript
const products = [
  { name: "apple", type: "fruit" },
  { name: "carrot", type: "vegetable" },
  { name: "banana", type: "fruit" },
];

const fruitNames = products
  .filter((product) => product.type === "fruit")
  .map((product) => product.name);

console.log(fruitNames); // ["apple", "banana"]
```

`find`는 조건을 만족하는 첫 번째 값을 반환하고, 없으면 `undefined`를 반환한다.

```javascript
const numbers = [8, 9, 5, 2, 1, 9];
const found = numbers.find((number) => number === 9);

console.log(found); // 9
```

`every`는 모든 값이 조건을 만족해야 `true`다.

```javascript
const numbers = [8, 5, 2, 1];
console.log(numbers.every((number) => number > 0)); // true
console.log(numbers.every((number) => number > 3)); // false
```

`some`은 하나라도 조건을 만족하면 `true`다.

```javascript
const numbers = [8, 5, 2, 1];
console.log(numbers.some((number) => number > 5)); // true
```

`reduce`는 배열을 하나의 값으로 누적한다.

```javascript
const numbers = [8, 5, 2, 1];

const sum = numbers.reduce((acc, cur) => {
  return acc + cur;
}, 0);

console.log(sum); // 16
```

구분 기준:

- 단순 순회: `forEach`
- 새 배열로 변환: `map`
- 일부만 남기기: `filter`
- 첫 번째 값 찾기: `find`
- 모두 만족하는지 확인: `every`
- 하나라도 만족하는지 확인: `some`
- 하나의 값으로 누적: `reduce`

## DOM과 BOM

DOM은 HTML 문서를 객체로 표현한 구조다.

```text
HTML 문서
-> 브라우저가 해석
-> DOM tree 생성
-> JavaScript가 document 객체를 통해 접근
```

DOM tree는 부모-자식 관계로 이루어진다.

- Document Node: 문서 전체
- Element Node: HTML 태그
- Attribute Node: 태그의 속성
- Text Node: 태그 안의 텍스트

BOM은 브라우저 창과 관련된 기능을 다룬다.

```javascript
console.log(window.location.href);
history.back();
```

브라우저 환경의 최상위 객체는 `window`이고, HTML 문서 전체를 대표하는 객체는 `document`다.

## DOM 요소 선택과 조작

DOM 조작은 크게 두 단계로 생각한다.

```text
1. 원하는 요소를 선택한다.
2. 선택한 요소의 내용, 속성, class, 위치를 바꾼다.
```

요소 선택:

```javascript
const title = document.getElementById("title");
const fruitCollection = document.getElementsByClassName("fruit");
const container = document.querySelector("#container");
const firstFruit = document.querySelector(".fruit");
const fruits = document.querySelectorAll(".fruit");
```

처음 학습할 때는 `querySelector`, `querySelectorAll`을 중심으로 잡으면 좋다.

- `querySelector`: CSS 선택자에 맞는 첫 번째 요소
- `querySelectorAll`: CSS 선택자에 맞는 모든 요소를 NodeList로 반환

`getElementsByClassName`은 `HTMLCollection`을 반환하고, `querySelectorAll`은 `NodeList`를 반환한다. 처음 학습할 때는 CSS 선택자를 그대로 사용할 수 있는 `querySelector`, `querySelectorAll`을 중심으로 잡아도 충분하다.

`NodeList`는 배열처럼 보이지만 배열은 아니다. `forEach`는 사용할 수 있지만 `map`, `filter`, `reduce`를 쓰려면 배열로 바꾸는 편이 안전하다.

```javascript
const pTags = document.querySelectorAll("p");

pTags.forEach((pTag) => {
  console.log(pTag.textContent);
});

const pArray = Array.from(pTags);
const texts = pArray.map((pTag) => pTag.textContent);
console.log(texts);
```

요소 생성과 추가:

```javascript
const newFruit = document.createElement("li");
newFruit.textContent = "mango";

const fruitsList = document.querySelector("#fruits-list");
fruitsList.appendChild(newFruit);
```

`appendChild`는 마지막 자식으로 붙인다. 앞쪽에 붙이거나 특정 요소 앞에 넣어야 할 때는 `prepend`, `insertBefore`를 사용한다.

```javascript
const firstFruit = document.createElement("li");
firstFruit.textContent = "apple";

const fruitsList = document.querySelector("#fruits-list");
const banana = document.querySelector(".banana");

fruitsList.prepend(firstFruit);
fruitsList.insertBefore(firstFruit, banana);
```

요소 삭제:

```javascript
const banana = document.querySelector(".banana");
banana.remove();
```

```javascript
const fruitsList = document.querySelector("#fruits-list");
const apple = document.querySelector(".apple");
fruitsList.removeChild(apple);
```

내용 변경:

```javascript
const title = document.querySelector("#title");
title.textContent = "새 제목";
```

`innerHTML`, `innerText`, `textContent`는 비슷해 보이지만 차이가 있다.

- `innerHTML`: HTML 태그를 포함해 읽고 쓸 수 있다.
- `innerText`: 화면에 실제로 보이는 텍스트를 기준으로 한다.
- `textContent`: DOM에 있는 텍스트 내용을 그대로 다룬다.

```javascript
const box = document.querySelector("#box");

box.innerHTML = "<strong>강조</strong>";
box.textContent = "<strong>강조</strong>";
```

사용자 입력값을 그대로 넣을 때 `innerHTML`을 사용하면 XSS 위험이 생길 수 있다. 단순 텍스트를 넣을 때는 `textContent`를 우선 생각한다.

속성 조작:

```javascript
const orange = document.querySelector(".orange");

orange.setAttribute("data-origin", "jeju");
console.log(orange.getAttribute("data-origin"));
orange.removeAttribute("data-origin");
```

class 조작:

```javascript
const button = document.querySelector("#submit-button");

button.classList.add("active");
button.classList.remove("disabled");
button.classList.toggle("selected");

if (button.classList.contains("selected")) {
  console.log("선택됨");
}
```

`dataset`은 `data-*` 속성을 JavaScript에서 다룰 때 사용한다.

```html
<button id="like-button" data-movie-id="10">좋아요</button>
```

```javascript
const button = document.querySelector("#like-button");
console.log(button.dataset.movieId); // "10"
```

`data-*` 속성은 JavaScript에서 camelCase로 바뀐다. 예를 들어 `data-user-id`는 `dataset.userId`, `data-test-value`는 `dataset.testValue`로 접근한다.

## Event

Event는 브라우저나 사용자의 동작으로 발생하는 사건이다.

- click
- input
- submit
- copy
- keydown
- mouseover

이벤트를 다룰 때는 `addEventListener`를 사용한다.

```javascript
const button = document.querySelector("#btn");
const counter = document.querySelector("#counter");

let count = 0;

button.addEventListener("click", function () {
  count += 1;
  counter.textContent = count;
});
```

기본 형태:

```javascript
target.addEventListener("event-name", function (event) {
  // event가 발생했을 때 실행할 코드
});
```

input 이벤트:

```html
<input id="message-input" type="text">
<p id="preview"></p>
```

```javascript
const input = document.querySelector("#message-input");
const preview = document.querySelector("#preview");

input.addEventListener("input", function (event) {
  preview.textContent = event.target.value;
});
```

`event.target`은 실제 이벤트가 발생한 요소를 가리킨다.

```javascript
input.addEventListener("input", function (event) {
  console.log(event.target);
  console.log(event.target.value);
});
```

`event.currentTarget`은 event listener가 붙어 있는 요소를 가리킨다. 이벤트 버블링이 있는 구조에서는 `target`과 `currentTarget`이 다를 수 있다.

이벤트 버블링은 자식 요소에서 발생한 이벤트가 부모 요소 방향으로 전파되는 현상이다. 버블링 덕분에 여러 자식 요소에 각각 listener를 붙이지 않고 부모 하나에 listener를 붙이는 이벤트 위임을 사용할 수 있다.

```html
<ul id="todo-list">
  <li>DOM 정리</li>
  <li>Event 복습</li>
  <li>Ajax 실습</li>
</ul>
```

```javascript
const todoList = document.querySelector("#todo-list");

todoList.addEventListener("click", function (event) {
  if (event.target.tagName === "LI") {
    console.log("클릭된 항목:", event.target.innerText);
    console.log("listener가 붙은 요소:", event.currentTarget);
  }
});
```

`event.target.tagName`은 대문자 문자열을 반환하므로 `"li"`가 아니라 `"LI"`와 비교한다. 버블링을 의도적으로 막아야 하는 경우에는 `event.stopPropagation()`을 사용할 수 있지만, 이벤트 위임이 필요한 구조에서는 버블링을 활용하는 편이 좋다.

```javascript
const childButton = document.querySelector("#child-button");

childButton.addEventListener("click", function (event) {
  event.stopPropagation();
  console.log("부모로 이벤트 전파를 막음");
});
```

form submit의 기본 동작은 페이지 이동 또는 새로고침이다. 이를 막고 JavaScript로 직접 처리하려면 `preventDefault()`를 사용한다.

```html
<form id="search-form">
  <input name="keyword" type="text">
  <button type="submit">검색</button>
</form>
```

```javascript
const form = document.querySelector("#search-form");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  const keyword = event.target.keyword.value;
  console.log(keyword);

  event.target.reset();
});
```

`preventDefault()`는 Ajax 요청에서 특히 중요하다. form이 기본 submit을 해버리면 페이지가 새로고침되어 JavaScript로 DOM을 갱신하는 흐름이 끊길 수 있다.

`copy` 같은 이벤트도 기본 동작을 막을 수 있다.

```javascript
const title = document.querySelector("#title");

title.addEventListener("copy", function (event) {
  event.preventDefault();
  console.log("복사를 막음");
});
```

`addEventListener` callback에서 `this`를 써야 한다면 화살표 함수보다 일반 함수를 사용한다. 일반 함수의 `this`는 listener가 붙은 요소를 가리키지만, 화살표 함수는 바깥 scope의 `this`를 그대로 가져온다.

```javascript
const button = document.querySelector("#btn");

button.addEventListener("click", function () {
  console.log(this); // button
});

button.addEventListener("click", () => {
  console.log(this); // browser 환경에서는 보통 window
});
```

간단한 DOM 생성 실습 흐름:

```javascript
const button = document.querySelector("#lotto-btn");
const result = document.querySelector("#result");

button.addEventListener("click", function () {
  const numbers = [3, 11, 18, 24, 32, 41];
  const container = document.createElement("div");

  numbers.forEach((number) => {
    const ball = document.createElement("div");
    ball.textContent = number;
    ball.classList.add("ball");
    container.appendChild(ball);
  });

  result.appendChild(container);
});
```

## 비동기 처리

동기 처리는 코드가 작성된 순서대로 하나씩 끝난 뒤 다음 코드가 실행되는 방식이다.  
비동기 처리는 시간이 오래 걸리는 작업을 기다리는 동안 다음 코드를 먼저 실행할 수 있는 방식이다.

JavaScript는 single thread 언어다. 한 번에 하나의 call stack만 실행하지만, 브라우저가 제공하는 Web API와 event loop 덕분에 비동기 처리가 가능하다.

```text
Call Stack
-> Web API
-> Task Queue / Microtask Queue
-> Event Loop
-> Call Stack으로 callback 이동
```

`setTimeout` 예시:

```javascript
console.log("start");

setTimeout(() => {
  console.log("timeout");
}, 1000);

console.log("end");
```

실행 순서:

```text
start
end
timeout
```

Ajax 요청, timer, event handler는 브라우저 Web API와 event loop의 도움을 받아 비동기적으로 처리된다.

비동기 코드는 시작한 순서와 끝나는 순서가 다를 수 있다. 그래서 요청을 보낸 직후의 코드에서 응답값을 바로 사용하려고 하면 아직 데이터가 없을 수 있다.

```javascript
console.log("요청 시작");

setTimeout(() => {
  console.log("응답 도착");
}, 1000);

console.log("응답을 기다리지 않고 먼저 실행");
```

callback을 계속 중첩하면 코드가 안쪽으로 깊어지는 callback hell이 생긴다. Promise와 `async`/`await`는 이런 비동기 흐름을 더 읽기 쉽게 정리하기 위해 사용한다.

```javascript
firstTask(function (firstResult) {
  secondTask(firstResult, function (secondResult) {
    thirdTask(secondResult, function (thirdResult) {
      console.log(thirdResult);
    });
  });
});
```

## Promise, then/catch, async/await

Promise는 비동기 작업의 성공 또는 실패 결과를 나중에 처리하기 위한 객체다.

```javascript
const promise = new Promise((resolve, reject) => {
  const success = true;

  if (success) {
    resolve("성공");
  } else {
    reject("실패");
  }
});

promise
  .then((result) => {
    console.log(result);
  })
  .catch((error) => {
    console.log(error);
  });
```

`.then()`은 성공 결과를 처리하고, `.catch()`는 실패 결과를 처리한다.

`async/await`는 Promise 기반 코드를 더 동기 코드처럼 읽히게 만든다.

`async`가 붙은 함수는 항상 Promise를 반환하고, `await`는 `async` 함수 안에서만 사용할 수 있다. `await`는 Promise가 끝날 때까지 다음 줄로 넘어가지 않게 해 주지만, 브라우저 전체를 멈추는 것은 아니다.

```javascript
async function fetchData() {
  try {
    const response = await fetch("/api/movies/");
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.log(error);
  }
}

fetchData();
```

기준:

- Promise 결과를 chain으로 이어가면 `.then()`/`.catch()`
- 비동기 흐름을 위에서 아래로 읽고 싶으면 `async`/`await`
- 실패 가능성이 있으면 `catch` 또는 `try/catch`

## Axios와 Ajax

Ajax는 페이지 전체를 새로고침하지 않고 서버와 데이터를 주고받아 DOM을 갱신하는 방식이다.  
Axios는 Ajax 요청을 쉽게 보내기 위한 JavaScript 라이브러리다.

Ajax는 특정 언어나 프레임워크 이름이 아니라 비동기 HTTP 통신을 이용하는 방식이다. 예전에는 `XMLHttpRequest(XHR)` 객체를 직접 다뤘고, 실습에서는 이를 더 편하게 쓰기 위해 Promise 기반의 Axios를 사용했다.

Axios와 Fetch는 모두 비동기 HTTP 요청에 사용할 수 있다.

- Axios는 외부 라이브러리라 CDN 또는 설치가 필요하지만, 응답 데이터를 다루기 쉽고 timeout 같은 옵션을 제공한다.
- Fetch는 JavaScript 내장 API라 별도 설치가 필요 없지만, JSON 응답을 쓰려면 `response.json()`으로 한 번 더 파싱해야 한다.

```javascript
async function getMovies() {
  const response = await fetch("/api/movies/");
  const data = await response.json();

  console.log(data);
}
```

흐름:

```text
사용자 이벤트 발생
-> event listener 실행
-> preventDefault로 기본 submit 방지
-> axios 요청 전송
-> 서버가 JSON 응답
-> response.data를 이용해 DOM 갱신
```

Axios CDN:

```html
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
```

GET 요청:

```javascript
axios({
  method: "get",
  url: "/api/movies/",
})
  .then((response) => {
    console.log(response.data);
  })
  .catch((error) => {
    console.log(error.response);
  });
```

POST 요청:

```javascript
axios({
  method: "post",
  url: "/movies/1/likes/",
})
  .then((response) => {
    console.log(response.data);
  })
  .catch((error) => {
    console.log(error.response);
  });
```

Django에서 POST 요청을 보낼 때는 CSRF token을 header에 넣어야 한다.

```html
<form id="like-form">
  {% csrf_token %}
  <button type="submit">좋아요</button>
</form>
```

```javascript
const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

axios({
  method: "post",
  url: "/movies/1/likes/",
  headers: {
    "X-CSRFToken": csrftoken,
  },
});
```

## Ajax 좋아요와 팔로우 실습 흐름

좋아요와 팔로우 실습은 Django view와 JavaScript DOM 조작이 연결되는 구조였다.

핵심은 form submit을 서버의 일반 redirect 흐름이 아니라 axios 요청으로 바꾸는 것이다.

```text
기존 form submit
-> Django view 처리
-> redirect
-> 페이지 새로고침

Ajax submit
-> JavaScript가 submit 이벤트 가로챔
-> axios POST
-> Django view가 JsonResponse 반환
-> JavaScript가 현재 페이지 DOM만 갱신
```

템플릿에서는 JavaScript를 페이지 하단에서 실행할 수 있도록 `base.html`에 script block을 열어 두고, 각 페이지에서 Axios CDN과 script를 넣었다.

```html
<!-- base.html -->
<body>
  {% block content %}
  {% endblock content %}

  {% block script %}
  {% endblock script %}
</body>
```

```html
<!-- profile.html 또는 index.html -->
{% block script %}
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    // page-specific JavaScript
  </script>
{% endblock script %}
```

팔로우 form:

```html
<form id="follow-form" data-user-id="{{ person.pk }}">
  {% csrf_token %}
  <button type="submit" class="btn btn-primary">팔로우</button>
</form>

<span id="followers-count">{{ person.followers.all|length }}</span>
<span id="followings-count">{{ person.followings.all|length }}</span>
```

팔로우 JavaScript:

```javascript
const form = document.querySelector("#follow-form");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  const userId = event.target.dataset.userId;
  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

  axios({
    method: "post",
    url: `/accounts/${userId}/follow/`,
    headers: {
      "X-CSRFToken": csrftoken,
    },
  })
    .then((response) => {
      const isFollowed = response.data.is_followed;
      const followersCount = response.data.followers_count;
      const followingsCount = response.data.followings_count;

      const followButton = document.querySelector("#follow-form > button[type=submit]");
      const followersCountTag = document.querySelector("#followers-count");
      const followingsCountTag = document.querySelector("#followings-count");

      followersCountTag.textContent = followersCount;
      followingsCountTag.textContent = followingsCount;

      if (isFollowed) {
        followButton.textContent = "언팔로우";
      } else {
        followButton.textContent = "팔로우";
      }

      followButton.classList.toggle("btn-primary", !isFollowed);
      followButton.classList.toggle("btn-secondary", isFollowed);
    })
    .catch((error) => {
      console.log(error.response);
    });
});
```

`classList.toggle(className, condition)`처럼 두 번째 인자를 넣으면 조건이 참일 때 class를 추가하고, 거짓일 때 제거한다. 팔로우 여부에 따라 버튼 색상까지 바꾸고 싶을 때 유용하다.

Django view는 JSON으로 현재 상태를 반환한다.

```python
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_POST


@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        User = get_user_model()
        me = request.user
        you = User.objects.get(pk=user_pk)

        if me != you:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
                is_followed = False
            else:
                you.followers.add(me)
                is_followed = True

            context = {
                "is_followed": is_followed,
                "followers_count": you.followers.count(),
                "followings_count": you.followings.count(),
            }
            return JsonResponse(context)

        return redirect("accounts:profile", you.username)

    return redirect("accounts:login")
```

좋아요는 여러 게시글에 같은 이벤트를 붙여야 하므로 `querySelectorAll`과 `forEach`를 사용한다.

```html
{% for movie in movies %}
  <form class="like-forms" data-movie-id="{{ movie.pk }}">
    {% csrf_token %}
    <input type="submit" value="좋아요" id="like-{{ movie.pk }}">
  </form>
  <span id="like-count-{{ movie.pk }}">{{ movie.like_users.count }}</span>
{% endfor %}
```

```javascript
const forms = document.querySelectorAll(".like-forms");
const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

forms.forEach((form) => {
  form.addEventListener("submit", function (event) {
    event.preventDefault();

    const movieId = event.target.dataset.movieId;

    axios({
      method: "post",
      url: `/movies/${movieId}/likes/`,
      headers: {
        "X-CSRFToken": csrftoken,
      },
    })
      .then((response) => {
        const isLiked = response.data.is_liked;
        const likedCount = response.data.liked_count;

        const likeButton = document.querySelector(`#like-${movieId}`);
        const likeCountTag = document.querySelector(`#like-count-${movieId}`);

        likeButton.value = isLiked ? "좋아요 취소" : "좋아요";
        likeCountTag.textContent = likedCount;
      })
      .catch((error) => {
        console.log(error.response);
      });
  });
});
```

Django view:

```python
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from .models import Movie


@require_POST
def likes(request, movie_pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=movie_pk)

        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
            is_liked = False
        else:
            movie.like_users.add(request.user)
            is_liked = True

        context = {
            "is_liked": is_liked,
            "liked_count": movie.like_users.count(),
        }
        return JsonResponse(context)

    return redirect("accounts:login")
```

실습에서 조심할 점:

- HTML의 `id`와 JavaScript selector가 정확히 일치해야 한다.
- `data-movie-id`는 JavaScript에서 `dataset.movieId`로 접근한다.
- `data-user-id`는 JavaScript에서 `dataset.userId`로 접근한다.
- form submit 기본 동작을 막지 않으면 페이지가 새로고침된다.
- Django POST 요청에는 CSRF token header가 필요하다.
- 서버는 redirect가 아니라 현재 상태와 count를 JSON으로 돌려줘야 DOM 갱신이 쉽다.
- 여러 form에 이벤트를 붙일 때는 `querySelectorAll` 결과를 순회해야 한다.

실습 코드에서 확인한 주의 사례:

```html
<span id="liked-count-1"></span>
```

```javascript
document.querySelector("#like-count-1");
```

위처럼 HTML은 `liked-count`인데 JavaScript는 `like-count`를 찾으면 선택 결과가 `null`이 된다. 버튼 값은 바뀌어도 count 갱신은 실패할 수 있으므로, DOM id와 selector 이름을 끝까지 맞춰야 한다.

## 정리하며 남긴 기준

JavaScript는 문법만 따로 공부하면 실제 웹 화면과 연결되지 않는다.  
기초 문법을 배운 뒤에는 DOM 선택, Event 감지, 비동기 요청, DOM 갱신이 하나의 흐름으로 이어지는지 확인해야 한다.

- 변수는 `const`를 기본으로 두고, 재할당이 필요할 때 `let`을 쓴다.
- 비교는 `===`를 기본으로 사용한다.
- 함수는 값처럼 전달될 수 있고 callback이 될 수 있다.
- 객체 method에서 `this`가 필요하면 화살표 함수보다 일반 함수를 우선 생각한다.
- 배열 변환은 `map`, 필터링은 `filter`, 누적은 `reduce`를 떠올린다.
- DOM 조작은 선택 후 변경이라는 순서로 생각한다.
- 사용자 입력을 화면에 넣을 때는 `innerHTML`보다 `textContent`가 안전한 경우가 많다.
- form submit을 JavaScript로 처리하려면 `preventDefault()`가 필요하다.
- 비동기 요청은 성공/실패를 모두 처리한다.
- Ajax 실습에서는 HTML의 `data-*`, JavaScript의 `dataset`, Django의 `JsonResponse`가 연결되는 구조를 확인한다.
