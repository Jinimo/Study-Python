# React

- 사용 언어: HTML, CSS, JavaScript

- 사용 문법: JSX(JavaScript와 XML)라는 HTML-in-JavaScript 문법



JSX -> JavaScript의 구문을 확장하여 HTML과 유사한 코드를 함께 사용

```jsx
const heading = <h1>Mozilla Developer Network</h1>;

// 다른 요소 안에 요소 중첩 가능 
const header = (
  <header>
    <h1>Mozilla Developer Network</h1>
  </header>
);

// Babel or Parcel 같은 툴 사용하여 컴파일 한 결과 
// React.createElement() -> UI 직접 작성하여 컴파일 단계 생략 가능 but 가독성 저하 
const header = React.createElement("header", null,
  React.createElement("h1", null, "Mozilla Developer Network")
);

```



### 1. React 앱 준비 

create-react-app 사용 -> `Node.js` 설치 필요

저장장소 이동 -> 터미널에 명령어 추가 -> `moz-todo-react` directory 생성 

```
npx create-react-app moz-todo-react
```



#### 앱 구성 

```
moz-todo-react
├── README.md
├── node_modules
├── package.json
├── package-lock.json
├── .gitignore
├── public
│   ├── favicon.ico
│   ├── index.html
│   └── manifest.json
└── src                  
    ├── App.css
    ├── App.js
    ├── App.test.js
    ├── index.css
    ├── index.js
    ├── logo.svg
    └── serviceWorker.js
```

- `src`: 애플리케이션 소스 코드 있는곳. 리액트 개발 메인폴더
- `Public`: 앱 개발하는동안 브라우저가 읽을 파일 보유. 가장 중요한 것은 `index.html`
  -  html 파일에 코드 주입 -> 브라우저 코드 실행 가능하도록 해줌.
  - create-react-app function에 중요한 마크업 존재 -> 함부러 편집 X 
- `package.json`: Node.js/npm가 프로젝트를 조직하기 위해 사용하는, 프로젝트에 관련한 정보를 포함



#### `CRA` 폴더 구성

`Public`

가상 DOM이 들어갈 빈 html 존재 

	- `favicon.ico` 페이지 아이콘 이미지 파일 
	- `index.html` 가상 DOM이 들어갈 빈 html 
	- `manifest.json` 사용자가 보는 영역에 웹앱 또는 사이트 나타내는 방식 -> 개발자가 ㅔ제어, 사용자에게 시작 가능 항목 지시, 시작 시 모습 정의 

`src`

리액트 개발 메인폴더

 - `index.js` : `index.js`에서  `App.js`에서 생성된 리액트 코드 불러온 후 -> `public`-`index.html` 의 id가 root인 곳에 넣는 코드 

 - `App.js`: 리액트 코드 생성 부분 

   1. React, React component 불러옴
   2. App class 생성 -> React component 상속 받음 => React component method 사용 가능 

   3. 상속 받은 React component 중  `render()` method (화면에 html view 생성 역할) 활용-> html 코드를 작성해 `return` 

   4. 생성된 App class `export` 문법 사용해 내보냄 



=> html 코드 여러개의 React 파일로 분할해 작업 가능. 부분 코드 수정, 협업에 용이.



#### `Props` & `State`



##### 1) `State`

 하나의 component가 가질 수 있는 변경 가능한 데이터

- Component rendering 할 때 새로운 데이터 생성시 사용 사능 
- 기존 데이터 참고 -> 새로운 데이터 생성시 사용 가능 