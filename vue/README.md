# Vue

Vue는 사용자 인터페이스를 컴포넌트 단위로 만들고, 상태 변화에 따라 화면을 자동으로 다시 그려주는 프론트엔드 프레임워크다.

이 폴더에서는 Vue 프로젝트 생성, Single File Component, 반응형 state, directive, computed/watch/lifecycle, component 분리, props/emit, Vue Router와 navigation guard를 정리한다.

## Quick Navigation

- [Vue 프로젝트 시작](#vue-프로젝트-시작)
- [Vue 앱의 실행 흐름](#vue-앱의-실행-흐름)
- [Single File Component](#single-file-component)
- [반응형 state와 `ref`](#반응형-state와-ref)
- [Mustache와 `v-model`](#mustache와-v-model)
- [Event와 `v-on`](#event와-v-on)
- [Directive](#directive)
- [Computed, Method, Watch](#computed-method-watch)
- [Lifecycle Hooks](#lifecycle-hooks)
- [Components](#components)
- [Props](#props)
- [Emit](#emit)
- [Vue Router](#vue-router)
- [Dynamic Routes](#dynamic-routes)
- [Nested Routes](#nested-routes)
- [Navigation Guard](#navigation-guard)
- [정리하며 남긴 기준](#정리하며-남긴-기준)

## Vue 프로젝트 시작

Vue 프로젝트는 Vite 기반으로 생성할 수 있다.

```bash
npm create vue@latest
cd vue-project
npm install
npm run dev
```

`npm create vue@latest`는 Vue 프로젝트 틀을 만들고, `npm install`은 `package.json`에 기록된 패키지를 설치한다. 설치가 끝나면 `node_modules`가 생긴다. `node_modules`는 패키지 설치 결과물이므로 직접 수정하지 않는다.

`package.json`에서 주로 확인할 부분:

```json
{
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "vue": "^3",
    "vue-router": "^4",
    "pinia": "^3"
  }
}
```

- `dev`: 개발 서버 실행
- `build`: 배포용 파일 생성
- `preview`: build 결과 미리보기
- `vue`: Vue 본체
- `vue-router`: SPA에서 URL 기반 화면 전환 담당
- `pinia`: Vue 상태 관리 라이브러리

Vue를 쓰는 방식은 크게 CDN 방식과 npm 방식으로 나눌 수 있다.

- CDN 방식: HTML 파일에 `<script>`로 Vue를 불러온다. 간단한 실습에 좋다.
- npm 방식: 프로젝트 단위로 패키지를 설치하고 Vite로 실행한다. 실제 앱 개발에 적합하다.

CDN 방식 예시:

```html
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
```

npm 방식은 패키지 버전 관리, 라우터, 빌드, 컴포넌트 분리까지 함께 다루기 좋다. 실습 초반에는 CDN 방식으로 문법을 확인하고, 프로젝트에서는 npm 방식으로 넘어가는 흐름이 자연스럽다.

Vite 개발 서버는 저장한 변경사항을 브라우저에 빠르게 반영한다. 이를 HMR(Hot Module Replacement)이라고 한다. 개발 중에는 화면을 새로고침하지 않아도 변경된 컴포넌트나 스타일이 바로 반영되는 경우가 많다.

## Vue 앱의 실행 흐름

Vue 앱은 하나의 HTML 문서를 기준으로 시작한다.

```text
index.html
-> src/main.js
-> createApp(App)
-> app.use(router)
-> app.use(createPinia())
-> app.mount("#app")
-> App.vue 렌더링
```

`index.html`에는 Vue 앱이 붙을 자리만 있다.

```html
<div id="app"></div>
<script type="module" src="/src/main.js"></script>
```

`main.js`는 Vue 앱의 시작점이다.

```javascript
import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";
import router from "./router";

const app = createApp(App);

app.use(createPinia());
app.use(router);

app.mount("#app");
```

`createApp(App)`은 최상위 컴포넌트인 `App.vue`를 기준으로 Vue 앱을 만든다. `app.mount("#app")`은 만들어진 앱을 `index.html`의 `id="app"` 요소에 붙인다.

Vue는 SPA(Single Page Application) 구조로 동작한다. 페이지는 하나지만, 라우터와 컴포넌트 렌더링을 통해 여러 페이지처럼 보이게 만든다.

## Single File Component

`.vue` 파일은 하나의 컴포넌트다. Vue에서는 HTML, JavaScript, CSS를 하나의 파일 안에 함께 작성할 수 있다.

```vue
<script setup>
import { ref } from "vue";

const message = ref("Hello Vue");
</script>

<template>
  <h1>{{ message }}</h1>
</template>

<style scoped>
h1 {
  color: royalblue;
}
</style>
```

- `<script setup>`: state, 함수, import 같은 JavaScript 로직을 작성한다.
- `<template>`: 화면에 렌더링될 HTML 구조를 작성한다.
- `<style scoped>`: 해당 컴포넌트에만 적용할 CSS를 작성한다.

`<script setup>`은 Vue 3의 Composition API를 간결하게 쓰는 방식이다. 전통적인 Options API에서는 `data`, `methods`, `computed` 옵션을 나누어 작성했지만, 현재 학습 흐름에서는 `<script setup>`을 중심으로 정리한다.

컴포넌트 이름은 보통 PascalCase를 사용한다.

```text
HomeView.vue
HomeHeader.vue
UserCard.vue
BoardDetailView.vue
```

## 반응형 state와 `ref`

Vue에서 화면과 연결되는 값은 일반 변수와 다르게 다룬다. 값이 바뀌었을 때 화면도 다시 그려져야 하기 때문이다.

```vue
<script setup>
import { ref } from "vue";

const count = ref(0);

function increase() {
  count.value += 1;
}
</script>

<template>
  <p>{{ count }}</p>
  <button @click="increase">증가</button>
</template>
```

`ref(0)`은 반응형 state를 만든다. `<script setup>` 안에서 값을 읽거나 바꿀 때는 `.value`가 필요하다.

```javascript
const count = ref(0);

console.log(count.value);
count.value += 1;
```

하지만 `<template>`에서는 `.value`를 붙이지 않는다.

```vue
<template>
  <p>{{ count }}</p>
</template>
```

정리하면:

- script 안: `count.value`
- template 안: `count`

## Mustache와 `v-model`

`{{ }}`는 mustache 문법이라고 부르며, template에서 state 값을 출력할 때 사용한다.

```vue
<script setup>
import { ref } from "vue";

const message = ref("Hello Vue");
</script>

<template>
  <p>message: {{ message }}</p>
</template>
```

`v-model`은 입력 요소와 state를 양방향으로 연결한다.

```vue
<script setup>
import { ref } from "vue";

const message = ref("");
const checked = ref(false);
</script>

<template>
  <input type="text" v-model="message">
  <p>{{ message }}</p>

  <input id="agree" type="checkbox" v-model="checked">
  <label for="agree">{{ checked }}</label>
</template>
```

사용자가 input에 값을 입력하면 state가 바뀌고, state가 바뀌면 화면도 다시 렌더링된다.

`v-model`은 사용자 입력값을 state에 실시간 저장할 때 사용한다. 태그의 일반 속성과 state를 연결할 때는 `v-bind`를 사용한다.

숫자 input은 기본적으로 문자열로 들어올 수 있다. 숫자로 다루고 싶다면 `v-model.number`를 사용한다.

```vue
<script setup>
import { ref } from "vue";

const count = ref(0);
</script>

<template>
  <input type="number" v-model.number="count">
  <p>{{ count + 10 }}</p>
</template>
```

바인딩 방향도 구분해 둔다.

- 단방향 바인딩: state가 DOM에 반영된다. 예: `v-bind`, `:style`
- 양방향 바인딩: state와 사용자 입력 DOM이 서로 동기화된다. 예: `v-model`

## Event와 `v-on`

Vue에서 이벤트를 연결할 때는 `v-on`을 사용한다. 축약형은 `@`다.

```vue
<script setup>
import { ref } from "vue";

const text = ref("처음 값");

function changeText() {
  text.value = "짜잔";
}
</script>

<template>
  <p>{{ text }}</p>
  <button @click="changeText">클릭하면 글자가 변해</button>
</template>
```

이벤트 객체가 필요하면 함수의 인자로 받을 수 있다.

```vue
<script setup>
function logValue(event) {
  console.log(event.target.value);
}
</script>

<template>
  <input type="text" @keyup="logValue">
</template>
```

`@click`, `@keyup`, `@change`처럼 DOM 이벤트 이름을 그대로 사용할 수 있다.

## Directive

Directive는 template에서 Vue의 반응형 state와 DOM을 연결하는 문법이다.

### `v-bind`

`v-bind`는 HTML 속성을 state와 연결한다. 축약형은 `:`다.

```vue
<script setup>
import { ref } from "vue";

const url = ref("https://www.naver.com");
const isActive = ref(false);
const largeText = ref(true);
</script>

<template>
  <a :href="url">링크</a>

  <button @click="isActive = !isActive">토글</button>
  <p :class="{ active: isActive }">class binding</p>

  <button @click="largeText = !largeText">크기 변경</button>
  <p :style="{ fontSize: largeText ? '24px' : '14px', color: 'blue' }">
    style binding
  </p>
</template>
```

`v-bind`와 `v-model`은 구분해서 사용한다.

- `v-bind`: 속성을 state와 연결한다.
- `v-model`: 입력값을 state와 양방향으로 연결한다.

### `v-if`

`v-if`, `v-else-if`, `v-else`는 조건에 따라 DOM에 요소를 만들거나 제거한다.

```vue
<script setup>
import { ref } from "vue";

const isActive = ref(false);
</script>

<template>
  <button @click="isActive = !isActive">토글</button>

  <div v-if="isActive">보임</div>
  <div v-else>안 보임</div>
</template>
```

조건이 거짓이면 해당 요소는 DOM에 존재하지 않는다.

### `v-for`

`v-for`는 배열을 순회해 반복 렌더링할 때 사용한다.

```vue
<script setup>
import { ref } from "vue";

const menus = ref([
  { id: 1, name: "짜장면" },
  { id: 2, name: "짬뽕" },
  { id: 3, name: "탕수육" },
]);
</script>

<template>
  <ul>
    <li v-for="menu in menus" :key="menu.id">
      {{ menu.name }}
    </li>
  </ul>
</template>
```

index도 함께 받을 수 있다.

```vue
<li v-for="(menu, index) in menus" :key="menu.id">
  {{ index }} : {{ menu.name }}
</li>
```

`v-for`에서는 `key`를 반드시 안정적인 고유값으로 지정한다. 단순히 배열 index를 key로 쓰면 항목이 추가되거나 삭제될 때 DOM 재사용이 꼬일 수 있다.

```vue
<script setup>
import { ref } from "vue";

const menus = ref([
  { id: 1, name: "짜장면" },
  { id: 2, name: "짬뽕" },
]);

function addMenuAtTop() {
  menus.value.unshift({
    id: Date.now(),
    name: "볶음밥",
  });
}
</script>

<template>
  <button @click="addMenuAtTop">맨 앞에 추가</button>

  <ul>
    <li v-for="menu in menus" :key="menu.id">
      {{ menu.name }}
      <input placeholder="메모">
    </li>
  </ul>
</template>
```

입력값이 있는 리스트에서는 key가 더 중요하다. Vue가 어떤 DOM을 재사용해야 하는지 key를 기준으로 판단하기 때문이다.

### `v-html`과 `v-text`

`v-html`은 HTML 문자열을 실제 HTML로 렌더링한다.

```vue
<script setup>
import { ref } from "vue";

const htmlContent = ref("<strong>강조된 텍스트</strong>");
</script>

<template>
  <div v-html="htmlContent"></div>
</template>
```

외부 입력값을 `v-html`로 넣으면 XSS 위험이 생길 수 있다. 사용자가 입력한 문자열이나 신뢰할 수 없는 데이터를 HTML로 렌더링하지 않는다.

`v-text`는 HTML 태그를 해석하지 않고 텍스트로 출력한다.

```vue
<script setup>
import { ref } from "vue";

const textContent = ref("<strong>그냥 문자열</strong>");
</script>

<template>
  <div v-text="textContent"></div>
</template>
```

단순 텍스트 출력은 mustache나 `v-text`를 사용하고, HTML 렌더링이 꼭 필요한 경우에만 `v-html`을 생각한다.

### `v-show`

`v-show`는 조건에 따라 화면 표시 여부를 바꾼다.

```vue
<script setup>
import { ref } from "vue";

const isVisible = ref(false);
</script>

<template>
  <button @click="isVisible = !isVisible">토글</button>
  <div v-show="isVisible">자주 보였다 숨겨질 내용</div>
</template>
```

`v-if`와 `v-show`의 차이:

- `v-if`: 조건이 거짓이면 DOM에서 요소를 생성하지 않는다.
- `v-show`: DOM에는 남겨두고 `display: none`으로 숨긴다.

자주 보였다가 사라지는 요소는 `v-show`, 조건이 드물게 바뀌거나 처음부터 렌더링하지 않아도 되는 요소는 `v-if`가 어울린다.

## Computed, Method, Watch

### `computed`

`computed`는 state를 기반으로 계산된 값을 만들 때 사용한다.

```vue
<script setup>
import { computed, ref } from "vue";

const message = ref("");

const upperMessage = computed(() => {
  return message.value.toUpperCase();
});
</script>

<template>
  <input v-model="message" placeholder="영어 소문자 입력">
  <p>{{ upperMessage }}</p>
</template>
```

배열을 필터링해서 화면에 보여줄 때도 유용하다.

```vue
<script setup>
import { computed, ref } from "vue";

const items = ref([
  { id: 1, text: "small" },
  { id: 2, text: "small" },
  { id: 3, text: "big" },
  { id: 4, text: "big" },
]);

const smallItems = computed(() => {
  return items.value.filter((item) => item.id < 3);
});

const bigItems = computed(() => {
  return items.value.filter((item) => item.id >= 3);
});
</script>

<template>
  <p v-for="item in smallItems" :key="item.id">{{ item.text }}</p>
  <p v-for="item in bigItems" :key="item.id">{{ item.text }}</p>
</template>
```

`computed`의 특징:

- 의존하는 반응형 값이 바뀔 때만 다시 계산한다.
- 계산 결과를 캐싱한다.
- 화면에 표시할 계산된 값을 만들 때 적합하다.
- 읽기 전용 값으로 생각한다.

### Method

method는 상태를 바꾸거나 이벤트에 반응하는 동작을 처리할 때 사용한다.

```vue
<script setup>
import { computed, ref } from "vue";

const items = ref([
  { id: 1, text: "Item 1" },
  { id: 2, text: "Item 2" },
]);

const itemCount = computed(() => items.value.length);

function addItem() {
  const newId = Date.now();
  items.value.push({ id: newId, text: `Item ${newId}` });
}

function removeItem() {
  items.value.pop();
}
</script>

<template>
  <p>개수: {{ itemCount }}</p>
  <button @click="addItem">추가</button>
  <button @click="removeItem">제거</button>
</template>
```

구분 기준:

- 계산된 값을 화면에 보여주기: `computed`
- 클릭, 추가, 삭제처럼 동작을 실행하기: method

### `watch`

`watch`는 state의 변화를 감시하고, 변화가 생겼을 때 특정 작업을 실행한다.

```vue
<script setup>
import axios from "axios";
import { ref, watch } from "vue";

const userName = ref("");
const userAge = ref(null);

watch(userName, (newName) => {
  if (!newName) {
    userAge.value = null;
    return;
  }

  axios.get(`https://api.agify.io?name=${newName}`)
    .then((response) => {
      userAge.value = response.data.age;
    });
});
</script>

<template>
  <input v-model="userName" placeholder="이름 입력">
  <p>예상 나이: {{ userAge }}</p>
</template>
```

`computed`와 `watch`의 차이:

- `computed`: state를 기반으로 화면에 표시할 값을 계산한다.
- `watch`: state 변화에 반응해 API 요청, 로그 출력, 다른 state 업데이트 같은 side effect를 실행한다.

## Lifecycle Hooks

Vue 컴포넌트는 생성되고, DOM에 붙고, state 변화로 다시 렌더링되고, 화면에서 사라지는 생명주기를 가진다.

주요 단계:

- `created`: 데이터와 이벤트가 준비되었지만 아직 화면에는 붙지 않은 상태
- `setup`: 컴포넌트 로직 준비
- `onBeforeMount`: DOM에 붙기 직전
- `onMounted`: DOM에 붙은 직후
- `onUpdated`: 반응형 값 변경으로 다시 렌더링된 뒤
- `onBeforeUnmount`: 컴포넌트가 사라지기 직전
- `onUnmounted`: 컴포넌트가 사라진 뒤

크게 보면 create, mount, update, destroy 흐름으로 이해할 수 있다. Vue 3의 `<script setup>`에서는 생성 단계의 많은 준비가 setup 안에서 이루어진다고 보면 된다.

DOM 접근은 `onMounted` 이후가 안전하다.

```vue
<script setup>
import { onBeforeMount, onMounted, onUpdated, ref } from "vue";

const count = ref(0);

function countUp() {
  count.value += 1;
}

onBeforeMount(() => {
  console.log("mount 전:", document.querySelector("h1"));
});

onMounted(() => {
  console.log("mount 후:", document.querySelector("h1"));
});

onUpdated(() => {
  console.log("화면이 다시 렌더링됨");
});
</script>

<template>
  <h1>Lifecycle</h1>
  <p>{{ count }}</p>
  <button @click="countUp">증가</button>
</template>
```

`onBeforeMount`에서는 아직 실제 DOM에 붙지 않았으므로 DOM 선택 결과가 없을 수 있다. `onMounted`는 실제 화면에 컴포넌트가 나타난 뒤 실행되므로 DOM 접근, 초기 API 요청, 외부 라이브러리 초기화에 자주 사용한다.

## Components

컴포넌트는 화면을 작은 부품으로 나누는 단위다. 큰 HTML 파일 하나에서 모든 UI를 관리하면 유지보수가 어려워진다. Vue에서는 각 UI 조각을 `.vue` 파일로 분리해 조립한다.

예시 구조:

```text
src/
  views/
    HomeView.vue
  components/
    HomeHeader.vue
    HomeMain.vue
    HomeFooter.vue
```

`views/`에는 라우터가 직접 연결하는 화면 단위 컴포넌트를 둔다. `components/`에는 여러 곳에서 재사용할 수 있는 일반 컴포넌트를 둔다.

부모 컴포넌트에서 자식 컴포넌트를 사용하는 흐름:

```vue
<!-- src/views/HomeView.vue -->
<script setup>
import HomeHeader from "@/components/HomeHeader.vue";
import HomeMain from "@/components/HomeMain.vue";
import HomeFooter from "@/components/HomeFooter.vue";
</script>

<template>
  <h1>Home</h1>
  <HomeHeader />
  <HomeMain />
  <HomeFooter />
</template>
```

`@`는 `src/` 디렉터리를 의미하는 alias다.

```javascript
import HomeHeader from "@/components/HomeHeader.vue";
```

컴포넌트를 template에서 사용할 때는 일반 HTML 태그와 구분하기 위해 PascalCase를 사용한다.

### `scoped`

Vue 프로젝트는 결국 하나의 HTML 문서에 컴포넌트들이 렌더링된다. 그래서 style에 `scoped`를 붙이지 않으면 다른 컴포넌트에도 스타일이 영향을 줄 수 있다.

```vue
<style>
h2 {
  color: red;
}
</style>
```

위처럼 작성하면 현재 컴포넌트 밖의 `h2`에도 영향을 줄 수 있다.

```vue
<style scoped>
h2 {
  color: blue;
}
</style>
```

`scoped`를 붙이면 해당 컴포넌트 내부에만 스타일이 적용된다.

정리:

- 전역 스타일: `src/assets/main.css` 또는 루트 레벨에서 관리
- 컴포넌트별 스타일: `<style scoped>`

## Props

Props는 부모 컴포넌트가 자식 컴포넌트에 내려주는 값이다.

부모:

```vue
<!-- HomeView.vue -->
<script setup>
import { ref } from "vue";
import HomeChild from "@/components/HomeChild.vue";

const name = ref("ssafy");
const age = ref(10);
</script>

<template>
  <HomeChild
    :name-prop="name"
    :age-prop="age"
  />
</template>
```

자식:

```vue
<!-- HomeChild.vue -->
<script setup>
const props = defineProps({
  nameProp: String,
  ageProp: Number,
});
</script>

<template>
  <h2>Child</h2>
  <p>{{ nameProp }}</p>
  <p>{{ ageProp }}</p>
</template>
```

`defineProps`는 `<script setup>`에서 import 없이 사용할 수 있는 compiler macro다.

props 이름 컨벤션:

- template 속성: kebab-case
- script 변수: camelCase

```vue
<HomeChild :name-prop="name" />
```

```javascript
const props = defineProps({
  nameProp: String,
});
```

Props는 읽기 전용이다. 자식이 직접 props를 바꾸려고 하면 Vue의 데이터 흐름을 깨게 된다.

```vue
<!-- 피해야 할 흐름 -->
<button @click="ageProp = 9">나이 변경</button>
```

부모의 state는 부모가 바꾸고, 자식은 변경 요청을 emit으로 올린다.

## Emit

Emit은 자식 컴포넌트가 부모 컴포넌트에게 이벤트를 올리는 방식이다. Vue의 기본 흐름은 props down, emits up이다.

```text
부모 state
-> props로 자식에게 전달
-> 자식은 직접 수정하지 않음
-> emit으로 부모에게 변경 요청
-> 부모가 state 수정
```

자식:

```vue
<!-- HomeChild.vue -->
<script setup>
const props = defineProps({
  nameProp: String,
  ageProp: Number,
});

const emit = defineEmits(["changeName"]);

function requestChangeName() {
  emit("changeName", "싸피");
}
</script>

<template>
  <p>{{ nameProp }}</p>
  <p>{{ ageProp }}</p>
  <button @click="requestChangeName">부모에게 이름 변경 요청</button>
</template>
```

부모:

```vue
<!-- HomeView.vue -->
<script setup>
import { ref } from "vue";
import HomeChild from "@/components/HomeChild.vue";

const name = ref("ssafy");
const age = ref(10);

function changeName(newName) {
  name.value = newName;
}
</script>

<template>
  <HomeChild
    :name-prop="name"
    :age-prop="age"
    @change-name="changeName"
  />
</template>
```

`defineEmits`도 import 없이 사용할 수 있다. 이벤트 이름 역시 template에서는 kebab-case, script에서는 camelCase로 이어지는 경우가 많다.

### 하위 컴포넌트의 emit을 다시 올리기

깊은 자식 컴포넌트가 최상위 부모 state를 바꾸고 싶다면 중간 컴포넌트가 이벤트를 다시 올려야 한다.

GrandChild:

```vue
<script setup>
const emit = defineEmits(["changeAge"]);

function changeAge(newAge) {
  emit("changeAge", newAge);
}
</script>

<template>
  <button @click="changeAge(1)">한 살로 돌아가기</button>
</template>
```

HomeChild:

```vue
<script setup>
import GrandChild from "@/components/GrandChild.vue";

const emit = defineEmits(["changeAge"]);
</script>

<template>
  <GrandChild @change-age="emit('changeAge', $event)" />
</template>
```

HomeView:

```vue
<script setup>
import { ref } from "vue";
import HomeChild from "@/components/HomeChild.vue";

const age = ref(10);

function changeAge(newAge) {
  age.value = newAge;
}
</script>

<template>
  <p>{{ age }}</p>
  <HomeChild @change-age="changeAge" />
</template>
```

`$event`는 자식 emit이 함께 보낸 값을 의미한다.

## Vue Router

Vue Router는 URL에 따라 어떤 컴포넌트를 보여줄지 정하는 라이브러리다. SPA 구조를 유지하면서도 URL 기반 화면 전환을 가능하게 한다.

기본 라우터 설정:

```javascript
// src/router/index.js
import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/about",
      name: "about",
      component: () => import("@/views/AboutView.vue"),
    },
  ],
});

export default router;
```

라우트 객체의 주요 속성:

- `path`: URL 경로
- `name`: 라우트 이름
- `component`: 해당 URL에서 렌더링할 컴포넌트

`component: () => import(...)` 방식은 lazy loading이다. 해당 라우트에 접근할 때 필요한 컴포넌트 코드를 나중에 불러온다.

Vue는 기본적으로 CSR(Client Side Rendering) 방식으로 동작한다. 서버가 완성된 HTML을 매번 보내기보다, 브라우저가 JavaScript 번들을 실행해서 화면을 구성한다. 그래서 초기 로딩 때 불러올 코드가 많아질 수 있고, 라우트 단위 lazy loading으로 처음에 필요한 코드만 먼저 불러오는 전략이 중요해진다.

SSR(Server Side Rendering)이 필요한 경우 Vue 생태계에서는 Nuxt를 함께 고려할 수 있다. 이 문서에서는 Vue 기본 CSR 흐름과 Router 중심으로 정리한다.

`App.vue`에서는 `RouterLink`와 `RouterView`를 사용한다.

```vue
<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <nav>
    <RouterLink :to="{ name: 'home' }">Home</RouterLink>
    <RouterLink :to="{ name: 'about' }">About</RouterLink>
  </nav>

  <RouterView />
</template>
```

- `RouterLink`: 라우터 이동 링크
- `RouterView`: 현재 URL에 맞는 컴포넌트가 렌더링되는 자리

`path`를 직접 쓰는 것보다 `name`을 사용하는 방식이 권장된다.

```vue
<RouterLink :to="{ name: 'about' }">About</RouterLink>
```

named route를 쓰면 URL 문자열 하드코딩을 줄이고, params 처리도 더 안정적으로 할 수 있다.

### `useRouter`

링크 클릭이 아니라 함수 안에서 페이지를 이동하려면 `useRouter`를 사용한다.

```vue
<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

function goToBoard() {
  router.push({ name: "board" });
}
</script>

<template>
  <button @click="goToBoard">게시판으로 이동</button>
</template>
```

`router`는 페이지 이동, URL 변경 같은 동작을 수행하는 객체다.

```javascript
router.push({ name: "board" });
router.replace({ name: "home" });
```

## Dynamic Routes

동적 라우트는 URL 일부를 변수처럼 받는 방식이다.

```javascript
{
  path: "/board/:id",
  name: "detail",
  component: () => import("@/views/BoardDetailView.vue"),
}
```

`/board/1`, `/board/2`처럼 접근하면 `id` 값이 달라진다.

현재 라우트 정보를 읽으려면 `useRoute`를 사용한다.

```vue
<script setup>
import { useRoute } from "vue-router";

const route = useRoute();
</script>

<template>
  <h1>{{ route.params.id }}번 글 상세 페이지</h1>
</template>
```

`route`와 `router`는 다르다.

- `route`: 현재 URL 정보 읽기, `useRoute()`
- `router`: 페이지 이동 실행, `useRouter()`

```javascript
const route = useRoute();
console.log(route.params.id);

const router = useRouter();
router.push({ name: "home" });
```

상세 페이지에서 params로 API 요청을 보내는 패턴:

```vue
<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const article = ref(null);

onMounted(() => {
  axios.get(`/api/articles/${route.params.id}/`)
    .then((response) => {
      article.value = response.data;
    });
});
</script>
```

### 같은 컴포넌트에서 params만 바뀌는 경우

`/board/1`에서 `/board/2`로 이동할 때 같은 `BoardDetailView` 컴포넌트가 재사용될 수 있다. 이때 초기화 코드가 다시 실행되지 않아 화면이 갱신되지 않는 문제가 생길 수 있다.

```javascript
const num = ref(route.params.id);
```

위 코드는 처음 한 번만 params 값을 복사한다. 이후 params가 바뀌어도 `num`이 자동으로 바뀌지 않는다.

해결 방법 1: `watch`

```vue
<script setup>
import { ref, watch } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const num = ref(route.params.id);

watch(
  () => route.params.id,
  (newId) => {
    num.value = newId;
  }
);
</script>

<template>
  <h1>{{ num }}번 글 상세 페이지</h1>
</template>
```

해결 방법 2: `onBeforeRouteUpdate`

```vue
<script setup>
import { ref } from "vue";
import { onBeforeRouteUpdate, useRoute } from "vue-router";

const route = useRoute();
const num = ref(route.params.id);

onBeforeRouteUpdate((to, from, next) => {
  num.value = to.params.id;
  next();
});
</script>
```

`watch`는 일반 state 변화에도 쓸 수 있고, `onBeforeRouteUpdate`는 라우트 변경 시점에 맞춰 처리할 때 적합하다.

## Nested Routes

Nested routes는 URL 구조를 계층적으로 나누는 방식이다. 컴포넌트의 부모-자식 관계와 라우트의 부모-자식 관계는 별개의 개념이다.

예를 들어:

```text
/board/:id/over
/board/:id/under
```

라우터 설정:

```javascript
{
  path: "/board/:id",
  name: "detail",
  component: () => import("@/views/BoardDetailView.vue"),
  children: [
    {
      path: "over",
      name: "over-thirty",
      component: () => import("@/components/OverThirty.vue"),
    },
    {
      path: "under",
      name: "under-thirty",
      component: () => import("@/components/UnderThirty.vue"),
    },
  ],
}
```

부모 라우트 컴포넌트에는 자식 라우트가 렌더링될 `RouterView`가 필요하다.

```vue
<script setup>
import { RouterLink, RouterView, useRoute } from "vue-router";

const route = useRoute();
</script>

<template>
  <h1>{{ route.params.id }}번 글 상세</h1>

  <RouterLink :to="{ name: 'over-thirty' }">30세 이상</RouterLink>
  <RouterLink :to="{ name: 'under-thirty' }">30세 미만</RouterLink>

  <RouterView />
</template>
```

Nested routes는 자식 컴포넌트를 직접 import해서 template에 붙이는 것과 다르다. URL의 하위 경로에 따라 `RouterView` 자리에 다른 컴포넌트를 보여주는 방식이다.

## Navigation Guard

Navigation guard는 라우터 이동을 허용, 차단, redirect하는 기능이다.

종류:

- 전역 가드: 모든 라우터 이동에 적용
- 라우트 가드: 특정 route에만 적용
- 컴포넌트 가드: 특정 컴포넌트 안에서 적용

### 전역 가드 `beforeEach`

`beforeEach`는 모든 페이지 이동 직전에 실행된다.

```javascript
// router/index.js
router.beforeEach((to, from) => {
  const isAuthenticated = false;

  if (!isAuthenticated && to.name !== "login") {
    return { name: "login" };
  }

  if (isAuthenticated && to.name === "login") {
    return { name: "home" };
  }
});

export default router;
```

`to`는 이동하려는 route, `from`은 이동 전 route다. `beforeEach`에서는 `return { name: "login" }`처럼 redirect할 수 있다.

로그인 여부, 전체 서비스 접근 제어처럼 앱 전체에 걸리는 규칙은 전역 가드가 어울린다.

### 라우트 가드 `beforeEnter`

`beforeEnter`는 특정 route에 진입하기 전에 실행된다.

```javascript
{
  path: "/about",
  name: "about",
  component: () => import("@/views/AboutView.vue"),
  beforeEnter: (to, from, next) => {
    const userRole = "user";

    if (userRole !== "admin") {
      next("/");
    } else {
      next();
    }
  },
}
```

`beforeEnter`는 route 단위로 접근 권한을 제한할 때 사용한다. 이 실습 흐름에서는 `return`보다 `next()`를 이용해 이동을 제어했다.

주의할 점:

- `beforeEnter`는 특정 route 설정 안에 작성한다.
- 이 실습 기준으로 `beforeEach`는 `return { name: "login" }`처럼 redirect할 수 있지만, `beforeEnter`는 `next()`로 이동을 제어한다고 구분해 둔다.
- params만 바뀌고 같은 컴포넌트를 재사용하는 경우에는 원하는 시점에 실행되지 않을 수 있다.

### 컴포넌트 가드

컴포넌트 안에서 라우터 이동을 제어할 때 사용한다.

`onBeforeRouteLeave`는 현재 페이지를 떠나기 전에 실행된다.

```vue
<script setup>
import { onBeforeRouteLeave } from "vue-router";

onBeforeRouteLeave((to, from, next) => {
  const ok = window.confirm("정말 떠나시겠습니까?");

  if (ok) {
    next();
  } else {
    next(false);
  }
});
</script>

<template>
  <h1>Board</h1>
</template>
```

작성 중인 form이 있거나, 저장하지 않은 데이터가 있을 때 이동을 막는 데 사용할 수 있다.

`onBeforeRouteUpdate`는 같은 컴포넌트 안에서 라우트 params가 바뀔 때 데이터를 갱신하는 데 사용할 수 있다.

```vue
<script setup>
import { ref } from "vue";
import { onBeforeRouteUpdate, useRoute } from "vue-router";

const route = useRoute();
const id = ref(route.params.id);

onBeforeRouteUpdate((to, from, next) => {
  id.value = to.params.id;
  next();
});
</script>
```

정리:

- `beforeEach`: 앱 전체 이동 제어
- `beforeEnter`: 특정 route 진입 제어
- `onBeforeRouteLeave`: 컴포넌트를 떠나는 이동 제어
- `onBeforeRouteUpdate`: 같은 컴포넌트에서 route 정보가 바뀔 때 갱신

## 정리하며 남긴 기준

Vue는 상태와 화면의 연결을 중심으로 이해해야 한다.

- 화면에 연결되는 값은 `ref`로 만들고, script에서는 `.value`로 접근한다.
- template에서는 `.value`를 생략한다.
- 입력값은 `v-model`, 속성 연결은 `v-bind`, 이벤트 연결은 `v-on`으로 생각한다.
- `v-for`에는 안정적인 `key`를 붙인다.
- 사용자가 만든 HTML 문자열은 `v-html`로 바로 렌더링하지 않는다.
- 화면에 보여줄 계산값은 `computed`, 상태 변경에 따른 작업은 `watch`를 사용한다.
- DOM 접근이나 초기 외부 작업은 `onMounted` 이후를 생각한다.
- 컴포넌트는 작게 나누고, 일반 컴포넌트 스타일에는 `scoped`를 붙인다.
- 부모 state는 부모가 관리하고, 자식은 props로 받고 emit으로 요청한다.
- route 정보 읽기는 `useRoute`, 페이지 이동은 `useRouter`를 사용한다.
- params만 바뀌는 동적 라우트에서는 컴포넌트 재사용을 고려해 `watch`나 `onBeforeRouteUpdate`를 사용한다.
- 라우터 접근 제어는 범위에 따라 `beforeEach`, `beforeEnter`, 컴포넌트 가드를 나누어 쓴다.
