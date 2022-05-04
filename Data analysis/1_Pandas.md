# Pandas

> 테이블 형태의 데이터를 쉽게 다룰 수 있는 파이썬 라이브러리









```py
### 모듈 연결
import pandas as pd
```

### 데이터 불러오기

```py
### 데이터 불러오기
df_read = pd.read_csv('./파일경로', encoding='cp949')   # csv
df_read = pd.read_excel('./파일경로', encoding='utf-8') # excel 
df_read = pd.read_table('./파일경로.txt')  # 테이블 형식으로 

pd1 = pd.read_excel('파일 경로')
pd1 = pd.read_excel('파일 경로',      # ./ : 상대경로 
              header = 1,		  # 원하는 컬럼명 위치 (두번째)
             skipfooter = 2 ,	# 마지막 행에서 2줄 생략
             usecols = )		  # A:C : A ~ C 컬럼까지 불러오기
```

### 데이터 확인 
```py
### 데이터 확인 ###

display()                # pandas에서만 가능
display(df_read.head(3)) # 상위 3개
display(df_read.tail(3)) # 하위 3개

# 행/열 갯수 확인 
df_read.shape            

# 고윳값 
df_b.운동량.unique() 
df_b['운동량'].unique()

# 데이터 타입 확인
df_l.dtype         # (단수)  
df_l.dtypes        # (복수)

# 숫자형 데이터 기초통계 개요(대표값)
df_m.describe()    

# 데이터 고유값 갯수 확인 
df.필드명.value_counts()
# 넘파이 배열 데이터
np.unique(y, return_counts=True)
```

### 데이터 선택
````py
### 데이터 선택 ###
# 불러온 데이터를 원하는 부분만 선택해서 보기

## 1. 컬럼(Column) 기준

# 컬럼(Column) 데이터 선택
 `pd1[ '컬럼명' ]` # 1개 선택 
`pd1[ [ '컬럼명1', '컬럼명2'  ] ]` # 여러개 선택

# 컬럼(Column) 생성
`pd1['생성 컬럼명'] = 값` 

## 1. 로우(row) 기준
# 특정 조건에 맞는 데이터 필터링(filtering)한 결과를 찾고자 하는 경우 선택 기준
row1 = pd1['로우1'] == '값1'  # True/False 출력 
pd1[row1]									  # True 해당값 출력
````

### 데이터 필터링
```py
### 필터링(filtering) ### 

# 2개 컬럼에 대해
row1 = (pd1['로우1'] == '값1') & (pd1['로우2'] >= '값2')
# 가독성 좋게 표현 
row1 = (pd1['로우1'] == '값1')\
			& (pd1['로우2'] >= '값2')

# 1개 컬럼에 대해 - 여러 조건 1
row1 = (pd1['로우1'] == '값1')  (pd1['로우2'] >= '값2')
```


### 데이터 변경
```py
### 데이터 변경 ###

## 열 이름 정의
df_l.columns = ['대여소번호', '대여소명', '소재지(자치구)','상세주소']

## 열 이름 변경 

# '성별' -> '대여자성별' (하나만 변경하는 경우)
# 컬럼명 이용 (특정 컬럼명 일치하지않거나 없을 경우 사용 X )
df_b.rename(columns = {'성별':'대여자성별'}) 
#  위치값 이용 (추천 방법)
df_b.rename(columns = {df_b.columns[5]:'대여자성별'}, inplace=True)


## index 재설정 
df_l.reset_index(drop=True, inplace = True)
            
### 데이터형 변경하기
# 비트 지정 -> "int64" / "float64"
df_l = df_l.astype({'대여소번호':int, '설치형태(LCD)':int, '설치형태(QR)':int, '위도':float, '경도':float })

### 특정 데이터 변경
# 'y'필드의  yes를 1、no를 0으로 치환
bank_df_tmp['y'] = bank_df_tmp['y'].replace('yes', 1)
bank_df_tmp['y'] = bank_df_tmp['y'].replace('no', 0)

### 
df['날짜'] = pd.to_datetime(df['날짜']) # to_datetime

```


### 데이터 삭제
```py
### 데이터 삭제

# del 명령 -> 즉시 삭제 (즉시적용, 복구 X)
del df_l['설치형태(LCD)']

# drop 함수
df_l.drop('설치형태(QR)', axis=1, inplace=True)   # 하나의 특정 열 삭제
df_l.drop(['설치형태(QR)','설치형태(LCD)'], axis=1) # 다수의 특정 열 삭제
#  inplace=True : 즉시 적용 


```


### 결측지(NaN) 확인
```py
# 파이썬에서는 결측지(NaN) = Null값(결손값)

### 결측지(NaN) 확인 ###

# 필드(열)별 NaN 갯수 확인 
print(df_l.isna().sum())

# 모든 NaN값 0으로 변경하기
df_l.fillna(0)
df_l.fillna(0, inplace = True) # 적용
df_l=df_l.fillna(0)            # 적용

# 특정 필드의 모든 NaN값 원하는 데이터로 변경하기
df.age.fillna(df.age.mean(), inplace=True)

### Null값(결손값) 확인 (T/F) ###
bank_df.isnull()
bank_df.isnull().any(axis=1) # 행 단위 결과 확인
bank_df.isnull().any(axis=0) # 열 단위 결과 확인

# 결손값의 갯수 확인 
df_l.isnull().sum(axis=1) # 행에 대한
df_l.isna().sum(axis=1)

df_l.isnull().sum(axis=0) # 열에 대한
df_l.isna().sum(axis=0)


# 결측지 값 출력 
dfNa = df_b.isna().sum()
print(dfNa)                # 전체
print(dfNa.loc["대여자성별"]) # 특정 값에 대한 출력(index값 이용)

# 결측지 비율 계산
print(dfNa[5]/len(df_b)) # 결측지수/전체데이터수



## Pandas DataFrame에서 빈 셀을 포함하는 행 삭제
# isnull 옵션이 누락 된 값을 인식하지 못할경우
# 빈 셀 -> NaN값으로 변경 -> NaN값 제거 
# 1)  Tenants열의 빈 문자열을 다음 과 np.nan같이 객체로 바꿈
df['Tenant'].replace('', np.nan, inplace=True)
# 2) null 값을 삭제
 df.dropna(subset=['Tenant'], inplace=True)



## '이동거리'이 가장 큰 데이터
display(df_m[df_m['이동거리'] == df_m['이동거리'].max()])





## 비율 계산 
# 해당 데이터 갯수/ 전제 데이터 갯수
job_u = bank_df['job'].unique() # 유니크값 확인 

# 방법 1 (.groupby() 사용)
# 'job' 기준 - 'age' 값들에 대한 합계 / 전체 갯수
print(bank_df.groupby('job')[['age']].count() / len(bank_df)
)

# 방법 2 (이게 더 쉬워)
# .value_counts(ascending=False, normalize=True) : 각 항목의 건수 계산
# 뒤에 추가적인 옵션 주면 자동으로 비율 계산 (normalize=True)
print(bank_df['job'].value_counts(ascending=False, normalize=True)



```



### 결측지(NaN) 처리

파이썬에서는 NaN = Null 



#### NaN 값 삭제

- DataFrame.dropna( axis=0, how='any', thresh=None, subset=None, inplace=False )
- axis = 0 (row) 혹은 1 (column)
- how = 'any' 일 경우, label 중 하나만 NaN이어도 해당 label을 삭제함.
- how = 'all' 일 경우, label 의 모든 데이터가 NaN이어야 해당 label을 삭제함.
- subset 다른 축(axis)의 어떤 label를 고려해야 하는지 list형태로 지정

```py
# df.drop() : NaN 데이터가 포함되어 있는 행 전체 삭제

# df.drop()                  # 특정 조건 만족하지 않는 데이터 모두 삭제
df.dropna()                  # NaN이 1개라도 존재하면 삭제  
df.dropna(subset=['answer']) # 'answer'에 NaN이 있으면 행 전체 삭제 

bank_df.dropna(how='any')    # 하나만 NaN이어도 해당 label을 삭제
bank_df.dropna(how='all')    # 모든 데이터가 NaN이어야 해당 label을 삭제

df.dropna(axis=1)            # NaN이 포함된 열 전체 삭제   

# 조건 주기
bank_df(thresh=2400, axis=1) # 결손값이 2400개 이상인 열을 제외


# -> 실제로 적용된 것은 아님!! 
# -> 적용: df=drop()/df.drop(inplace=True)
```



#### NaN을 다른 데이터로 대체

- `DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)`

- `value` = 스칼라, dic, Series, DataFrame 만 넣을 수 있음 

- 결손값 대체하기 전에 `df.dtypes` 확인하고 처리!! 

```py
# 특정 열['answer']의 NaN값을 입력값('내용없음')으로  대체
df['answer'].fillna('내용없음')
df.fillna({'contact':'unknown'}) # 딕셔너리 구조로

# 변경 적용 
df = df['answer'].fillna('내용없음')
df['answer'].fillna('내용없음', inplace=True)

# 특정 필드의 조건을 주어 NaN값 변경

### 예: 남자(1)/여자(2)에 따라 평균 나이 입력 ###
# '성별'-'남자(1)'인 데이터의 '나이'의 NaN값 
# -> 성별'-'남자(1)'의 '나이' 평균값으로 채우기 
df[df['성별']==1]['나이'].fillna(df[df['성별']==1]['나이'].mean())
```














###  병합


```py
### 데이터 병합 ###

# 행/열 인덱스 기준으로 병합
pd.concat() 
#  두 데이터프레임의 고유값(key)를 기준으로 병합
pd.merge()   
pd.merge(df_left, df_right, how='inner', on=None) # 두 데이터 관계설정 후 뽑아냄 
# how='inner': 교집합 (기본값, 생략 가능 )


## groupby ##
df_m.이용건수.groupby(df_m.대여일자)['이용건수'].sum()
# '요일'에 대한 '이용건수','대여시간'의 합계 표시 (요일별 각각의 합계 )
chrt_df = df_m.groupby('요일')[['이용건수','대여시간']].sum() 
# 요일별 대여시간에따른 '이용건수'의 합 표시 
chrt_df = df_m.groupby(['요일', '대여시간'])['이용건수'].sum() 


## concat ##
# pd.concat([, , , ... ])
# axis=0 : 열 방향(옆으로) / axis=1 : 행 방향(밑으로)

# 원하는 데이터 병합 (pd.concat())
df_gu = pd.DataFrame()

df_gu1 = df_l.groupby('소재지(자치구)')[['대여소번호']].count() 
df_gu = pd.concat([df_gu, df_gu1], ignore_index=True, axis=1)

df_gu1 = df_m.groupby('소재지(자치구)')[['이용건수']].mean() 
df_gu = pd.concat([df_gu, df_gu1], ignore_index=True, axis=1)

df_gu1 = df_m.groupby('소재지(자치구)')[['이동거리']].mean() 
df_gu = pd.concat([df_gu, df_gu1], ignore_index=True, axis=1)

df_gu1 = df_m.groupby('소재지(자치구)')[['사용시간']].max() 
df_gu = pd.concat([df_gu, df_gu1], ignore_index=True, axis=1)

# 열 이름 지정 
df_gu.columns = ['설치건수', '평균이용건수', '평균이동거리', '최대이동거리']
display(df_gu)


```



Concat: 단순히 행/열 방향으로 병합 (axis=0/1)

merge: 키를 이용해서 키 기준으로 병합 

**pandas merge, concat**

[참고1_블로그](https://kimdingko-world.tistory.com/207)

[pandas.merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html)

**how**: {‘left’, ‘right’, ‘outer’, ‘inner’, ‘cross’} / default `inner`

Type of merge to be performed.

- `inner`: use intersection of keys from both frames, similar to a SQL inner join; preserve the order of the left keys.
- `left`: use only keys from left frame, similar to a SQL left outer join; preserve key order.
- `right`: use only keys from right frame, similar to a SQL right outer join; preserve key order.
- `outer`: use union of keys from both frames, similar to a SQL full outer join; sort keys lexicographically.
- `cross`: creates the cartesian product from both frames, preserves the order of the left keys.



[pandas.concat](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html)

- Series - DataFrame 병합 
- Series - Series 병합 

### 정렬

```py
.sort()

# 탄소량을 기준으로 오름차순 정렬 
#display(df_m.sort_values('탄소량', ascending=True).head())
display(df_m.sort_values('탄소량').head())

# 탄소량을 기준으로 내림차순 정렬 
display(df_m.sort_values('탄소량', ascending=False).head())


.groupby()
# 
df_m['이용건수'].groupby(df_m['대여일자'])['이용건수'].sum()
df_m.groupby('대여일자')['이용건수'].sum()
chrt_df = df_m.groupby('요일')[['이용건수','대여시간']].sum()
```



### 조건

```py
# columns에서 데이터형이 숫자인 컬럼만 모으기
# (int32, int64, float32, float64)

colList = df_b.columns
findList = ['int32', 'int64', 'float32', 'float64']
tmp = [col for col in colList if df_b[col].dtypes in findList]

# 각 열 합계 계산 (소수점 둘째자리)
for col in tmp:
    print("%s: %.2f"%(col, df_b[col].sum()))

# 행 합계 (10개)

for i in df_b.index[:10]:
    print(i, df_b.loc[i, tmp].sum())
    

### 대상 : 최소값, 최대값, 평균값, 표준편차
colList = df_m[['운동량','탄소량','사용시간', '이동거리']]
for col in colList:
    print(f'{col}:{df_m[col].min()} / {df_m[col].max()} / {df_m[col].mean()} / {df_m[col].std()}')

```



### 더미변수

```py
### 더미변수 ###
pd.get_dummies()

# job을 더미 변수로 변경 
bank_df_job = pd.get_dummies(bank_df_tmp['job'])
      
# 데이터 복사 변수 만들기     
df_c = df_a.copy()
```



### 피벗 테이블

```py
### 피벗 테이블 ###
# 집계함수 2개
pdf2 = pd.pivot_table(df,                # 피벗할 데이터프레임
                     index = 'class',    # 행 위치에 들어갈 열
                     columns = 'sex',    # 열 위치에 들어갈 열
                     values = 'survived',     # 데이터로 사용할 열
                     aggfunc = ['mean', 'sum'])   # 데이터 집계함수
pdf2

# 
pdf3 = pd.pivot_table(df,
                     index = ['class','sex'],
                     columns = 'survived',
                     values = ['age','fare'],
                     aggfunc = ['mean','max'])
pdf3
```

[참조_피벗테이블 & 멀티인덱스](https://yganalyst.github.io/data_handling/Pd_14/)

[참조_더미변수](https://mizykk.tistory.com/13)

[basic](https://pandas.pydata.org/docs/user_guide/basics.html)

[.describe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)

[판다스 문자열 처리법](https://blog.naver.com/wideeyed/221603778414)

count : 컬럼별 총 데이터 수

Mean / std : 컬럼별 평균/ 표준편차

min / max : 컬럼별 최소 / 최대

25%/50%/75% : 백분위수의 각 지점으로 분포를 반영해 평균을 보완하는 목적으로 사용  

