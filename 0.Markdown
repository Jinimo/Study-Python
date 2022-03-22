

# Markdown

> - 일반 텍스트 형식 구문 사용 마크업 언어의 일종
> - 텍스트 -> HTML로 변환
> - 쉽고 간결한 사용법 -> 빠른 문서 정리 가능 
> - 단, 모든 HTML 마크업 대체 X



### 1 문장 & 문단 

1. 문장 줄바꿈 = 문장 끝 공백 2칸 / `<br>`

- 공백 X 

```HTML
<!-- Markdown -->
Hello World(띄어쓰기 없음)
Hi MD
<!-- HTML -->
<p>Hello World Hi MD</p>
```

Hello World Hi md

- 공백 O - 문장 줄 바꿈

```html
<!-- Markdown -->
Hello World(공백)(공백)
Hi MD
<!-- HTML -->
<p>Hello World<br>Hi MD</p>
```

Hello World
Hi MD



2. 문단 구분 -> 한 줄 공백 / `<p></p>`

-  한 줄 공백 X 

```html
<!-- Markdown -->
Hello World
Hi MD
<!-- HTML -->
<p>Hello World Hi MD</p>
```

Hello World Hi md

- 한 줄 공백 O

```html
<!-- Markdown -->
Hello World
    
Hi MD
<!-- HTML -->
<p>Hello World</p><p>Hi MD</p>
```

Hello World
    
Hi MD



### 2 Header

> - 제목 표현시 사용
> - 단순한 글자 크기 표현 X -> 논리적 구조! 



1. `#` 개수 표현 /  `<h1></h1>` 의 형태 표현 방법 

```
<!-- Markdown -->
# H1
## H2
### H3
#### H4
##### H5
###### H6

<!-- HTML -->
<h1>H1</h1>
<h2>H2</h2>
<h3>H3</h3>
<h4>H4</h4>
<h5>H5</h5>
<h6>H6</h6>
```

# H1

## H2

### H3

#### H4

##### H5

###### H6



2. `-` / `=`  이용 방법

```
<!-- Markdown -->
H1
=======
H2
-------
<!-- HTML -->
<h1>H1</h1>
<h1>H2</h1>
```

H1
=======

H2
-------



### 3 List

> - 목록 나열
> - 순서 O/X 목록으로 구분 
> - 순서 O 목록 아래 순서 X 목록 지정 가능 (반대도 가능)



**순서 O 목록** :  `1.`, `2.`, `3.`  -> `space bar` 눌러 생성 

**순서 X 목록** :  `-`, `* `, `+` -> `space bar` 눌러 생성 

`tab` 키 : 하위 목록 생성 / `shift + tab` 키 : 상위 목록 이동 



1. **순서 O 목록**

```
<!-- Markdown -->
1. ORDER 1
2. ORDER 2
3. ORDER 3
  * ORDER 3-A
  * ORDER 3-B

<!-- HTML -->
<ol>
    <li><p>ORDER 1</p></li>
    <li><p>ORDER 2</p></li>
    <li><p>ORDER 3</p></li>
    <ul>
        <li><p>ORDER 3-A</p></li>
        <li><p>ORDER 3-B</p></li>
    </ul>
</ol>
```

1. ORDER 1
2. ORDER 2
3. ORDER 3
   - ORDER 3-A
   - ORDER 3-B



2. **순서 X 목록**

```
<!-- Markdown -->
* ORDER 1
  + ORDER 1-1
  + ORDER 1-2
  + ORDER 1-3
    - ORDER 1-3-1
	- ORDER 1-3-2

<!-- HTML -->
* ORDER 2
<ul>
    <li><p>ORDER 1</p></li>
    <ul>
        <li><p>ORDER 1-1</p></li>
        <li><p>ORDER 1-2</p></li>
        <li><p>ORDER 1-3</p></li>
        <ul>
            <li><p>ORDER 1-3-1</p></li>
            <li><p>ORDER 1-3-2</p></li>
        </ul>
    </ul>
    <li><p>ORDER 2</p></li>
</ul>e
```



* ORDER 1
  + ORDER 1-1
  + ORDER 1-2
  + ORDER 1-3
    - ORDER 1-3-1
	
	- ORDER 1-3-2



### 4 Code Block

> - 코드 정리, 강조하고 싶은 부분 나타내는 경우 사용 
> - Inline과 Block 단위로 구분



1. **Inline**

인라인 블럭으로 처리하고 싶은 부분 `` `(백틱)으로  감싸줌



2. **Block** 

- 언어지정 코드 블럭 : ```` `(백틱) 3번 입력 / `~~~` 로 감싸기 
  - 하이라이트 기능 off : {.no-hightlight} 
- 스페이스 코드 블럭 : 문장 앞 (공백) 4개 / `tab`키 1번 

~~~html
<!-- Markdown -->
```javascript
console.log("Hello World");
```
  
```{.no-hightlight}
console.log("Hello World");
```
<!-- Html -->
<pre>
	<code>
		console.log("Hello World");
	</code>
</pre>
~~~

```javascript
console.log("Hello World");
```


```{.no-hightlight}
console.log("Hello World");
```



언어 선택 가능 

```
block
```



### 5 Image

> 로컬에 위치한 이미지 삽입 / 이미지 링크 활용 

- 이미지 링크 앞에 `!` 붙여 사용 
- 인라인 / 참조 링크 / URI 링크 모두 사용 가능 

```
![git-github-image](https://miro.medium.com/max/3586/1*mtsk3fQ_BRemFidhkel3dA.png)
```

![git-github-image](https://miro.medium.com/max/3586/1*mtsk3fQ_BRemFidhkel3dA.png)



### 6 Link

> 특정 주소로 링크 걸 때 사용



1. 인 라인 링크

- `[화면 표시 글자](URI)`  
-  `[화면 표시 글자](URI "툴팁")`  툴팁에 텍스트 넣으면 html title 속성 들어감

```html
<!-- Markdown -->
[naver](https://www.naver.com)
[naver2](https://www.naver.com "네이버")
<!-- Html -->
<a href="https://www.naver.com" target="_blank">naver</a>
<a href="https://www.naver.com" target="_blank" title="네이버">naver</a>
```

[naver](https://www.naver.com/) 

[naver2](https://www.naver.com/)



2. 참조 링크

- `[화면 표시 글자][1]` , `[1]: URI "툴팁"`

```html
<!-- Markdown -->
[daum][1]
[1]:https://daum.net "다음"   # [daum][1] 정의 해줌 
<!-- Html -->
<a href="https://daum.com" target="_blank" title="다음">daum</a>
```

[daum][1]

[1]:https://daum.net "다음"

[daum](https://daum.net/)



3. URI 링크 `<주소>`

```html
<!-- Markdown -->
<https://github.com>
<!-- Html -->
<a href="https://github.com" target="_blank">https://github.com</a>
```



### 7. 인용문

- `>` 입력 -> `enter` 키
- 중첩 사용 가능 (인용문 안 인용문)
- 인용문 입력 후 `enter` 키 누르면 빠져나옴 

```html
<!-- Markdown -->
> 인용구 입니다.
> # H1
> * a
> * b
>> 이중 인용구

<!-- Html -->
<blockquote>
    <P>인용구 입니다.</P>
    <h1>H1</h1>
    <ul>
        <li>ORDER1</li>
        <li>ORDER2</li>
    </ul>
    <blockquote>이중인용구</blockquote>
</blockquote>
```

> 인용구 입니다.
> # H1
> * a
> * b
>
> > 이중 인용구



### 8. 수평선

`---`,  `*** `,  `___`  입력

수평선 1  `---`

---

수평선 2  `*** `

***

수평선 3  `___`

___

 

### 9.  강조

- 이텔릭체  `*`/  `_` (언더바)로 강조하고 싶은 부분을 감싸서 사용
- 보드체:  `**` / `__` (언더바 2개)로 감싸줍니다.
- 취소선:  `~~` 표시를 사용합니다.

|||||
|--|--|--|--|
| 이텔릭체 | `*`/  `_` (언더바)로 감싸줌 | `*이텔릭체*` / `_이텔릭체_` | *이텔릭체* |
| 보드체 | `**` / `__` (언더바 2개)로 감싸줌 | `**보드체**`/ `__보드체__` | **보드체** |
| 취소선 | `~~`로 감싸줌 | `~~취소선~~` | ~~취소선~~ |



## Markdown Extension

> - 마크 다운 추가 기능
> - 몇몇 에디터에서 동작하지 않을 수 있음



### 10. Table

> 표 작성하여 요소 구분 

- `|` (파이프) 사이 컬럼 작성 후  `enter` 키
- 마지막 컬럼 뒤 `|`

1. **일반**

문자-문자로 표 만들기 

```
|제목|내용|설명|
|------|---|---|
|제목 1|내용 1|설명 1|
|제목 2|내용 2|설명 2|
|제목 3|내용 3|설명 3|
```

| 제목   | 내용   | 설명   |
| ------ | ------ | ------ |
| 제목 1 | 내용 1 | 설명 1 |
| 제목 2 | 내용 2 | 설명 2 |
| 제목 3 | 내용 3 | 설명 3 |

2. **정렬**

`:---` : 왼쪽 정렬 / `:---:` : 중앙 정렬/ `:---` : 오른쪽 정렬 

```
|제목|내용|설명|
|:---|---:|:---:|
|왼쪽정렬|오른쪽정렬|중앙정렬|
|왼쪽정렬|오른쪽정렬|중앙정렬|
|왼쪽정렬|오른쪽정렬|중앙정렬|
```

| 제목     |       내용 |   설명   |
| :------- | ---------: | :------: |
| 왼쪽정렬 | 오른쪽정렬 | 중앙정렬 |
| 왼쪽정렬 | 오른쪽정렬 | 중앙정렬 |
| 왼쪽정렬 | 오른쪽정렬 | 중앙정렬 |



3. **셀 확장**

`| |`  파이프 사이 비어있으면 자동 확장 

```
|제목|내용|설명|
|:---|:---:|---:|
||중앙에서확장||
|||오른쪽에서 확장|
|왼쪽에서확장||
```

| 제목         |     내용     |            설명 |
| :----------- | :----------: | --------------: |
|              | 중앙에서확장 |                 |
|              |              | 오른쪽에서 확장 |
| 왼쪽에서확장 |              |                 |



4. **셀 강조**

일반적인 text 강조와 동일 

```
|제목|내용|설명|
|---|---|---|
|테스트1|*강조1*|테스트3|
|테스트1|**강조2**|테스트3|
|테스트1|<span style="color:red">강조3</span>|테스트3|
```

| 제목    | 내용                                 | 설명    |
| ------- | ------------------------------------ | ------- |
| 테스트1 | *강조1*                              | 테스트3 |
| 테스트1 | **강조2**                            | 테스트3 |
| 테스트1 | <span style="color:red">강조3</span> | 테스트3 |



### 11. 각주

```markdown
<!-- Markdown -->
Markdown[^1] 정리 거의 다 끝나가니 포기하지 마세요.
[^1]: 마크업 언어의 일종으로 일반 텍스트 문서의 양식을 편집하는 문법입니다.
```

Markdown[^1] 정리 거의 다 끝나가니 포기하지 마세요.
[^1]: 마크업 언어의 일종으로 일반 텍스트 문서의 양식을 편집하는 문법입니다.



### 12. 목차 

- ​	`TOC` 입력 -> 문서 내 헤딩 태그들 이용하여 목차 자동 생성  

```markdown
<!-- Markdown -->
[TOC]
```

[TOC]

----



[참조]

[Peotic Code]( https://inchijeong.github.io/markdown/2019/03/20/markdown.html)

[손 끝으로 만드는 세상](https://inasie.github.io/it%EC%9D%BC%EB%B0%98/%EB%A7%88%ED%81%AC%EB%8B%A4%EC%9A%B4-%ED%91%9C-%EB%A7%8C%EB%93%A4%EA%B8%B0/)

