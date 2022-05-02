# Numpy



공학용 계산기와 같음 

숫자 자료만 계산

헹/열 계산을 해줌 

array 구조의 원소들 리스트형태와 달라 -> 쉼표 구분 X

<class 'numpy.ndarray'>  => [20 10 15  8  9 10]

<class 'list'> =>  [20, 10, 15, 8, 9, 10]

```py
# 모듈 연결
import numpy as np 

###############################
list1 = [[10,20,30],[12,25,35]]
arr = np.array(list1)

# 구조 확인 
print(arr.shape) 
# 1차원: (1차 원소수, ) / 2차원: (1차 , 2차 원소수) / 3차원: (1차, 2차, 3차 원소수) ?

# 차원 확인 (.ndim)
print(arr.ndim)

# 전체 데이터 갯수 (.size)
print(len(list1))                    # 차원 갯수
print(len(list1[0]) + len(list1[1])) # 2차원 원소 갯수  
print(arr.size)                      # 전체 갯수

# 데이터 타입 확인 (.dtype)
print(arr.dtype)

# 원소 크기 확인 (.itemsize)
# 결과: 8비트 (64비트) / 4비트 (32비트) -> 사용하는 컴퓨터의 사황에 따라 다르게 나옴 
print(arr.itemsize) 

# 원소와 하나의 행의 크기 (.strides) -> 등간격
# numpy에서는, 각 dimensions를 건너가는데 몇 bytes나 뛰어넘어야 하는지에 대한 정보
# 예시 결과) (24, 8) 24=원소수(3)*원소크기(8비트) , 원소크기(8)
print(arr.strides) 


```

#### - `ndarray` 생성

- 기본적으로 `vectorization`과 `broadcasting`을 지원 
- `list`, `tuple` 등의 시퀀스 자료형으로 구성할 수 있으며 내부 요소의 자료형은 모두 동일한 타입으로만 가질 수 있음 (딕셔너리 X)
- 자료의 크기도 고정되어 있음 



#### - 변형

```py
### 데이터 형 변형 ### 
# 'dtype=' 옵션으로 데이터형 변경 가능 
arr = np.array((1, 2, 3.), dtype='float64') 
# 뒤에 '.' 붙여주면 모든 숫자 소수로 바뀜
arr = np.array((1, 2, 3.)) 
# 데이터 중 하나라도 실수형이 있다면 모두 실수형으로 바뀜 
arr = np.array(((1, 2, 3.), (10, 20, "30")))  
# 문자형이 가장 큰 데이터형-> 모든 원소 문자형으로 바뀜  
arr = np.array(([(1, 2, 3.), (10, 20, "30")], 
                [(1, 33, 25), (15, 20.0, 35)]
                ))  

### 새로운 데이터 받아와 순차적으로 array 만들기 ## 
arr = np.array([])
for i in range(3):
  arr = np.append(arr, [10, 20, 30]) # arr에 값을 주어 반복 / 데이터형은 실수형으로 생성됨! 
print(arr)

## np.arange(): 정수형 데이터를 이용한 배열값 만들기
arr = np.arange(15) # 'range'와 같음 / 데이터 순차적으로 만들어짐 

## reshape(): 차원변경 
# reshape(3, 5)의 숫자의 곱은 array(15)의 숫자와 일치해야 함 
# 즉, 데이터 수가 같아야 함 !
arr = np.arange(15).reshape(3, 5) 
arr = np.arange(18).reshape(3, 6)  # 18 = 3*6
arr = arr.reshape(2, 9)            # 18 = 2*9
arr = arr.reshape(2, -1)           # -1: 행 기준으로 열 원소 자동으로 계산 
arr = arr.reshape(-1, 9)           # -1: 원소의 갯수을 기준으로 행 원소 자동으로 계산 

## 1차원으로 변경 
arr = arr.reshape(18,) 
arr = arr.reshape(-1)              # -1: 1차원 구조로 변경  


## 구조 확인
arr = arr.reshape(2, -1)  # 2차원 변경
print(arr)         
print(arr[0])       # 0번째 행
print(arr[0, 1:4])  # 0번째 행의 1~3까지 원소들 출력
print(arr[:, 1:4])  # 모든 행의 1~3까지 원소들 출력
print(arr[0][2])    # 0번째 행의 2번째 원소


## array 합치기 (np.concatenate()) -> 차원 같아야함!
arr1 = np.arange(1, 5).reshape(2,-1) # 2차원
arr2 = np.array([5,6]).reshape(-1,2) # 2차원
#arr2 = np.array([5,6]).reshape(1,2) # 2차원
#arr2 = np.array([[5,6]])            # 2차원

print(arr1, '\n', arr2)
print(np.concatenate((arr1,arr2), axis=0)) # 행 방향
print(np.concatenate((arr1,arr2), axis=1)) # 열 방향 -> 오류!(차원 다름)
print(np.concatenate((arr1,arr2.T), axis=1)) # 열 방향 
```








​	

#### - 배열 연산 

```py
# 합계
np.sum(arr)         # 전체 데이터의 합계
np.sum(arr, axis=0) # 열 기준 데이터의 합계 (axis=0)
np.sum(arr, axis=1) # 행 기준 데이터의 합계 (axis=1)

# pandas 데이터 numpy 모듈을 이용한 합계 
colSum = np.sum(df[tmp], axis=0) # 열 
rowSum = np.sum(df[tmp], axis=1) # 행


# array간 사칙연산 
arr1 = np.array([1,2,3,4]).reshape(2,-1)
arr2 = np.array([5,6,7,8]).reshape(2,-1)
print("더하기:", arr1+arr2) # 더하기
print("빼기:", arr1-arr2) # 빼기
print("곱하기:", arr1*arr2) # 곱하기 
print("나누기:", arr1/arr2) # 나누기 

# array간 사칙연산 
arr1 = np.array([1,2,3,4]).reshape(2,-1) # 2차원
arr2 = np.array([5,6]) # 1차원
# [1,2] 연산 [5,6]
# [3,4]     [5,6]
# 차원 달라도 연산가능! 
# 원소의 갯수는 맞춰야함! 
```

```python

np.round(수, 자리수)  # 반올림
np.ceil(수)         # 올림  (입력값과 같거나 큰 정수 중 가장 가까운 값 반환 )
np.trunc(수)        # 버림  (소수점 버리기)
np.floor(수)        # 내림  (입력값과 같거나 작은 정수 중 가장 가까운 값 반환 )
 

np.max(배열)        # 최대
np.min(배열)        # 최소
np.mean(배열)       # 평균
n차원배열.mean(axis=0)   # 행방향 평균(열별 평균)
n차원배열.mean(axis=1)   # 열방향 평균(행별 평균)
```






#### -입출력

- `np.save(file명, arr)`: array 1개 파일 저장할 경우 사용 (바이너리 형식)
- `np.savez(file명, arr1, arr2)`: 복수 배열을 파일로 저장 (바이너리 형식)
- `np.load(file명)`: 배열 형삭으로 저장된 데이터 불러오기 
- `np.savetxt()`: 텍스트 형식으로 배열값 저장
- `np.loadtxt()`: 텍스트 형식으로 배열값 저장된 배열값 불러오기



```py
# 정보 보기 편하게 함수 만들기
def pprint(arr):
  print(f'type:{type(arr)}')
  print(f'shape:{arr.shape}, ndim:{arr.ndim}, dtype:{arr.dtype}')
  print(f'array data: \n {arr}')
  
# np.random.randint(시작값, 종료값, 갯수)
x = np.random.randint(0, 10, (2, 3)) # 0~10 범위의 랜덤한 수 -> 2행 3열의 데이터 
y = np.random.randint(0, 10, (2, 3))

# 1개의 배열 저장 
np.save('./data/arr1', x) # x 값을 'arr1' 이름으로 저장 -> .npy 형태로 저장 
# x, y 두개의 배열 저장 
np.savez('./data/arr_all', x, y) # x,y 값을 'arr1_all' 이름으로 저장 -> .npz 형태로 저장 
# .npy 파일 읽어오기
np_file = np.load('./data/arr1.npy')
pprint(np_file)
# .npz 파일 읽어오기
npz_file = np.load('./data/arr_all.npz') # 배열이 두개로 분리된 파일 
print(npz_file.files) # 배열 갯수 확인 (.files) / pprint(npz_file) 요고 안됨 
pprint(npz_file['arr_0'])
pprint(npz_file[1]) # 오류) 위치값 X, 파일명으로만 가능 !

## 저장 
# 확장자명(.csv, .txt 등) 적어야함
# fmt='%.18e: 지수형 / fmt='%d': 정수형
# 위에서 정의한 'x'배열 -> 텍스트형으로 저장하기
np.savetxt('./data/x_arr.csv', x, delimiter=',', fmt='%.18e') 
np.savetxt('./data/x_arr.csv', x, delimiter=',', fmt='%d') 
# 텍스트 배열값 읽어오기
txt_arr = np.loadtxt('./data/x_arr.csv',delimiter=',' )ㄴ

```



#### - 표준편차 

```py
# var: 분산 / std: 표준편차
# pandas / numpy 계산 결과값 다름!
print(df_m['대여시간'].std())   # pandas
print(np.std(df_m['대여시간'])) # numpy

#############################
numData = [1, 3, 4, 5, 8, 10, 12]
# 평균 계산 = 전체통계 / 전체 데이터 갯수
dara_m = np.sum(numData) / len(numData)

## 모집단에 대한(n) 분산 계산 (pandas) 
# 분산 = ((numData[0]-평균)^2 + (numData[2]-평균)^2 + ...) / 전체데이터갯수(n)  
# 실제 제곱근 계산 : **2
vsum = 0
for v in numData:
    vsum += (v - dara_m)**2
var = vsum / len(numData)

# 비교 확인
print("분산 (일반 계산):", var)               # pandas
print("분산 (numpy 계산):", np.var(numData)) # numpy
#-> 분산으로 계산한 결과값은 같음!

## 표본에 대한(n-1) 분산 계산 
# 분산 = ((numData[0]-평균)^2 + (numData[2]-평균)^2 + ...) / 전체데이터갯수(n-1)  
vsum = 0
for v in numData:
    vsum += (v - dara_m)**2
var1 = vsum / (len(numData)-1)

# 비교 확인
print("분산 (일반 계산):", var1)
print("분산 (numpy 계산):", np.var(numData))

print("표준편차 (일반 계산 2):", math.sqrt(var1))
print("표준편차 (numpy 계산):", np.std(numData))

# '대여시간'에 대한 표준편차 계산 
print(df_m['대여시간'].std())   # pandas => 표본에 대한 표준편차
print(np.std(df_m['대여시간'])) # numpy  => 모집단에 대한 표준편차 
```



요구상황에따라 둘중 하나 쓰기 !

Pandas (일반 공식으로 계산/ 표본에 대한(n-1))

Numpy (구하는 함수 존재/  모집단에 대한(n))

분산 



[Python 기초 통계](https://mindscale.kr/course/basic-stat-python/)

[표준편차 계산 참조 1](https://ourcalc.com/%ED%91%9C%EC%A4%80%ED%8E%B8%EC%B0%A8-%EA%B3%84%EC%82%B0%EA%B8%B0/)

[중앙값 계산](https://lsh-story.tistory.com/90)



#### - 문자열 전처리 

- https://hleecaster.com/pandas-data-cleaning-2/







#### - pandas와 numpy

``` py
# 판다스에 .values 붙이면 numpy 배열(array)로 바뀜
print(type(df_m.탄소량))
print(type(df_m.탄소량.values)) 

#-> 결과값
<class 'pandas.core.series.Series'>
<class 'numpy.ndarray'>

# numpy의 브로드 캐스트 개념 이용(모든 열 한꺼번에 사칙연산 가능)
# 분양가격/3.3 결과 다시 분양가격에 업데이트
print(files['분양가격'].head(3))
print((files['분양가격']/3.3).head(3))

a = np.array(files['분양가격'])
b = np.array([3.3])
c = a/b

files['평당분양가격'] = c # '평당분양가격' 열 추가 
files.head(3)
```