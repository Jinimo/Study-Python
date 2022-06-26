

`index.html` :	사용자가 보는 화면. 실제 랜더링 

`index.js` -> `App.js` 파일 안에 있는 작은 html ->`public `폴더 -  `index.html` 에 모두 넣어주는 명령어 있음 

```
## index.js
document.getElementById('root')
# 아이디가 root인 태그에 index.js에 있는것을 다 가져다 넣어달라는 의미 

## App.js
function App() {
  return (                # 여기까지 그냥 js 문법 
    <div className="App"> # 안에 그냥 html 작성??
      <div className='black-nav'> # <div class=''> 불가능! -> <div className=''>
      </div>
    </div>
  );
}

export default App;

```



2. 리액트에서 데이터 바인딩 쉽게하는 법 (Angular, Vue도 가능)

=> `{ 변수명, 함수 등 }`

```
# ex 1 

# 기존 방식 
function App() {

  let posts = '강남 고기 맛집'; # 예를 든 서버에서 가져온 데이터 
  document.getElementById().innerHTML='' #(전통적인 자바스크립트 데이터 바인딩 방식) => 리액트에서는 필요 없음!!
  return (
    <div className="App">
      <div className='black-nav'>    
        <div> 현진 개발 Blog </div> 
      </div>
      
      <h4> 블로그 글  </h4> # 가져온 데이터를 여기서 보여줘야 함 

    </div>
  );
}

```



```js
# 리액트 방식 
import logo from './logo.svg';
import './App.css';

function App() {

  let posts = '강남 고기 맛집'; 
  function 함수(){
    return 100
  }

  return (
    <div className="App">
      <div className='black-nav'>    
        <div> 현진 개발 Blog </div> 
      </div>
      <img sr={logo}/>      ##  import한 logo 이미지 불러오기  
      <h3> { 함수() }  </h3> ## 동적인 함수 
      <h4> { posts }  </h4> ## 변수 

    </div>
  );
}
```



3. JSX에서 style 속성 집어넣을 때 

=> `style={object 자료형으로 만든 스타일}` --> 중괄호 필수!!

```
function App() {

  let posts = '강남 고기 맛집'; 
  function 함수(){
    return 100
  }

  return (
    <div className="App">
      <div className='black-nav'>    
        <div style={ {color: 'green', fontSize: '30px'}}> 현진 개발 Blog </div> 
      </div>
      <img src = {logo}/>
      <h3> { 함수() }  </h3>
      <h4> { posts }  </h4>

    </div>
  );
}
 
export default App;


## style 변수로 지정하여 사용 가능 


function App() {

 let posts = {color: 'green', fontSize: '30px'}; 
  function 함수(){
    return 100
  }

  return (
    <div className="App">
      <div className='black-nav'>    
        <div style={ posts }> 현진 개발 Blog </div> 
      </div>
    </div>
  );
}
```



