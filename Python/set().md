# set(집합)

> - 수학의 **집합**과 비슷 
> - 순서 X
> - 집합 내에서 Unique한 값 가짐 -> 중복 X
> - Mutable 객체 -> 변하기 쉬움  



### 1. set(집합)

- `{ }` 사용 
  - dictionary와 비슷하지만, `key` X => 값만 존재 
- 내부 원소 다양한 값 함께 가질 수 있음. But mutable한 값은 X



### 2. `set()` 선언

- 중괄호 `{ }` 만으로 사용 X => dict 타입과 동일한 괄호 사용하기 때문 
- Set 생성자 사용 

```python
s = set()
s = {1, 5, 1, 1, 1, 3, 7}
>>> s
{1, 3, 5, 7}

>>> s = set([1,3,5,7])
>>> s
{1, 3, 5, 7}
```



### 3. in

- 다른 collection 타입과 동일하게 동작 



### 4. 원소 추가

- `.add()` 매소드 사용 

```python
>>> k = {100, 105}
>>> k.add(50)
>>> k
{105, 50, 100}
```



### 5. update

- 중복 자동 제거, 여러 데이터 한번에 추가시 사용 
  - dict type - update: 여러 값 수정 or 추가 할 경우 사용 

```py
>>> k = {1, 2, 3}
>>> k.update([3, 4, 5])
>>> k
{1, 2, 3, 4, 5}
```



### 6. 원소 제거 

- `.remove(item)` -> item 해당 원소 제거, 존재 하지 않으면 KeyErrror 발생 
- `.discard(item)` -> item 해당 원소 제거, 존재 하지 않아도 KeyErrror 발생 X

```python
>>> k = {1, 2, 3}
>>> k.remove(3)
>>> k
{1, 2}
>>> k.remove(3)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
KeyError: 3

>>> k = {1, 2, 3}
>>> k.discard(3)
>>> k
{1, 2}
>>> k.discard(3)
>>> k
{1, 2}
```



### 7. 복사 

- `.copy()` -> 얕은 복사 해당 
  - set 내부 값 -> 불변의 값만 들어옴. 
- 생성자로 복사 가능 

```py
>>> s = {1, 3, 5}
>>> t = s.copy()
>>> s
{1, 3, 5}
>>> t
{1, 3, 5}

# 생성자 복사
>>> s = {1, 3, 5}
>>> t = set(s)
>>> s
{1, 3, 5}
>>> t
{1, 3, 5}
```



### 8. 연산자

`|` : 합집합 / `&` : 교집합 / `-` : 차집합  / `^`: 대칭 차집합 (합집합-교집합) / `|=`, `&=`, `-=`, `^=`: `=`과 조합하여 연산 동시에 할당 



### 9. 연산 메소드

- `.union()`: 합집합
- `.intersection()`: 교집합
- `.difference()`: 차집합
- `symmetric_difference()`: 대칭차집합 연산자 (합집합-교집합)



### 10. 기타 메소드

- `.issubest()`: 부분집합 여부 확인 
- `.issuperset()`: issubset과 반대 superset인지 확인 
- `.isdisjoint()`: 교집합이 없으면 True, 있으면 False



-----

[참고]

- https://wikidocs.net/16044

