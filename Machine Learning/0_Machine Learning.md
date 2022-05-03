

# Machine Learning

> - **Supervised Learning** (지도학습): 예측, 분류 => 문제와 정답을 모두 알려주고 학습
>
> - **Un-supervised Learning**  (비지도학습): 연관 규칙, 군집  => 답 가르쳐주지 않고 학습
>
> - **Reinforcement Learning** (강화학습): 보상 => 보상을 통해 상은 최대화, 벌은 최소화하는 방향으로 강화학습

| Supervised Learning (지도학습) | Un-supervised Learning  (비지도학습) |
| :----------------------------: | :----------------------------------: |
|     Classification (분류)      |         Clustering (군집화)          |
|       Regression (회귀)        |           PCA (차원 축소)            |
|          추천 시스템           |    Feature Extraction (피처 추출)    |
|    시각 / 음성 감지 / 인지     |              강화 학습               |
|        텍스트 분석, NLP        |                                      |



## **Supervised Learning (지도학습)**


- 학습을 위한 다양한 `feature`와 분류 결정값인 `Label`(레이블) 데이터로 모델 학습 -> 별도의 `test datadset` 에서 미지의 레이블 값 예측
- 명확한 정답이 주어진 데이터 먼저 학습 -> 미지의 정답 예측 방식
- `Train dataset` : 학습을 위해 주어진 데이터 세트
- `Test datadset` : 머신러닝의 모델 예측 성능을 평가하기 위해 별도로 주어진 데이터 세트



### - **Estimator**

> 지도학습의 모든 알고리즘 구현 클래스 통칭 (학습: `.fit()`, 예측: `predict()`)

- **Classifier** (분류)
  - DecisionTreeClassifier
  - RandomForestClassifier
  - GadientBoostingClassifier
  - SVC (Support vector Meachine)
- **Regressor** (회귀)
  - LinearRegressor
  - Ridge
  - Lasso
  - RandomForestRegressor
  - GadientBoostingRegressor





## Un - supervised Learning (비지도학습)

`fit()`, `transform()` 적용

비지도학습, 피처 추출의 `fit()` 

- 지도학습의 `fit()`과 다름 - > 학습 의미X, 입력 데이터의 형태에 맞춰 데이터의 변환 위한 사전 구조 맞춤 작업
- 사전 구조 맞춤`fit()`  => 데이터 차원 변환, 클러스팅, 피처 추출등의 실제 작업 `transform()`
- `fit_tarnsfrom()`
  -  `fit()`  + `transform()`
  -  개별 사용과 한번에 적용하는 것의 차이점 주의! 



​	



##  module

- `sklearn.dataset` 내 모듈: 사이킷런에서 자체적으로 제공하는 데이터 세트 생성 모듈

- `sklearn.tree` 내 모듈: 트리기반 ML 알고리즘 구현 class 모임  

- `sklearn.model_selection` 내 모듈: train/test dataset 데이터 분리, 최적의 파라미터로 평가하기 위한 다양한 모듈 모임











## Classification (분류)

- 데이터 로딩, 데이터 프레임 구조 변환(피처, 데이터 값 구성 확인) 

- Train/test dataset 분리: `train_test_split()`

- 모델 학습 후 예측 수행: 의사 결정 트리 클래스 DecisionTreeClassifier 객체 생성 

  - Classifier class 객체 생성 -> 학습: `.fit()` -> 예측: `.predict(X_train, y_train)`

- 예측 성능 평가 : 실제 테스트 데이터 값과 예측 데이터 값 비교해 ML 모델 성능 평가 

  - 정확도(  `accuracy_score(y_test, pred)` ): 예측 결과가 실제 레이블 값과 얼마나 정확하게 일치하는지의 지표 (y_test: 실제 레이블 데이터 세트, pred: 학습하여 예측한 데이터 세트 )



## Model Selection module 소개



### - train_test_split()

> train/test dataset 분리

```py
X_train, X_test, y_train, t_test = train_test_split(피터 데이터 세트, label 데이터 세트, test_size=0.2, random_state=11 )

# train_test_split() => 반환값: 튜플 형식 (feature data set, label data set)
# test_size: train/test dataset 분활 비율 (default=0.25) (train_size 파라미터도 존재하지만 이게 더 통상적으로 쓰임)
# random_state: 수행할 때마다 동일한 데이터 세트로 분리하기 위해 임의의 값 지정 (숫자 아무거나 상관 X)
# -> 미지정시 수행할 때마다 무작위로 데이터 분리
# shuffle: 데이터 분리 전 데이터 미리 섞을지 결정 (default=True) -> 데이터 분산시켜 효율적인 train/test dataset 만드는데 사용
# 
```



 ### -  Cross Validation (교차 검증)

> - KFold 교차 검증
>
> - Stratified KFold

- Overfitting(과적합): 모델의 과도한 학습 데이터에 최적화 -> 실제 테스트 데이터의 예측 성능 저하

- 교차검증 -> 데이터 편중 막기 위해 별도의 여러 세트로 구성된 학습+검증 데이터 세트에서 학습, 평가 수행

- ML 모델 성능 평가 
  - 1차: 교차 검증 기반 평가
  - 최종: test datase 적용 -> 평가 

| Train dataset ( train + Validation ) | Test dataset |
| :----------------------------------: | :----------: |



#### - KFold

가장 보편적인 교차 검증 기법 

K개 데이터 폴드 세트 생성 -> 폴드 세트의 학습+검증 평가 K번 반복 수행 

`kfold = Kfold(n_split = 5)` -> 5개의 검증 폴더 생성 

`kfold.split(features)` -> kfold.split()->학습,검증 인덱스 array로 나눠줌 

```py
from sklearn.datasets import load_iris
from sklearn import DecisionTreeClassifier # 분류 (DecisionTree)
from sklearn.model_selection import Kfold  # 교차검증 (Kfold) 
from sklearn.metrics import accuracy_score # 정확도
import numpy as np

# 1) 데이터 불러오기 및 분류
iris = load_iris()
feature = iris.data
label = iris.target
dt_clf = DecisionTreeClassifier(random_state=156)

# 2) KFold 객체, 정확도 담을 리스트 생성 
kfold = Kfold(n_split = 5) # 5개의 폴더로 나눔 
cv_accuracy = []
# 여기서 붓꽃 데이터 세트 크기 ->  feature.shape[0] = 150
# 학습:120(4/5) , 검증: 30(1/5)
n_iter = 0
for train_index, test_index in kfold.split(features): # kfold.split()->학습,검증 인덱스 array
  X_train, X_test = features[train_index], features[test_index]
  y_train, y_test = label[train_index], label[test_index]
  
  dt_clf.fit(X_train, y_train)  # 학습 
  pred = dt_clf.predict(X_test) # 예측
  
  accuracy = np.round(accuracy_score(y_test, pred), 4) # 정확도 / np.round():반올림 
  #train_size = X_train.shape[0] # 학습 데이터 크기
  #test_size = X_test.shape[0]   # 테스트 데이터 크기
  cv_accuracy.append(accuracy)
  
# 개별 iteration 별 정확도 합 -> 평균 정확도 계산
print('\n##평균 검증 정확도:', np.mean(cv_accuracy))

##===> 5번 반복수행하면서 각각 30개씩 검증 인덱스 생성
## 학습|학습|학습|학습|(검증)
## 학습|학습|학습|(검증)|학습
## 학습|학습|(검증)|학습|학습
## 학습|(검증)|학습|학습|학습
## (검증)|학습|학습|학습|학습
```



#### - Stratified KFold

- Imbalanced(불균형)한 분포도 가진 label(레이블) 데이터 집합위한 KFold 방식

​		-> 특정 레이블 값이 특이하게 많거나 매우 적어서 값의 분포가 한쪽으로 치우치는 것 

- KFold가 레이블 데이터 집합이 원본 데이터 집합의 laebel 분포를 trian/test dataset에 제대로 분배하지 못하는 경우의 문제 해결
- 원본 데이터의 laebel 분포 먼저 고려 -> 분포와 동일하게 trian/test dataset 분배
- 일반적인 `Classification(분류)`에서 교차검증 -> `Stratified KFold`
- `Regression(회귀)` -> `Stratified KFold` 지원 X (회귀의 결정값->연속된 숫자값이기 때문)

`kfold = StratifiedKfold(n_split = 3)` 

`kfold.split(features, laebel)`

```py
######## 획인) 학습 레이블/ 검증 레이블 데이터 값 분포 비슷하게 할당하기 
from sklearn.model_selection import StratifiedKFold

skf = kfold = StratifiedKfold(n_split = 3)
n_iter = 0
for train_index, test_index in skf.split(iris_df, iris_df['label']):
  n_iter+=1
  label_train = irid_df['label'].iloc[train_index]
  label_test = irid_df['label'].iloc[test_index]
  
######## 적용)   
dt_clf = DecisionTreeClassifier(random_state=156)

# 2) KFold 객체, 정확도 담을 리스트 생성 
skf = StratifiedKfold(n_split = 3) # laebel 고유값 3개라서
cv_accuracy = []
n_iter = 0
for train_index, test_index in skfold.split(features, label): # kfold.split()->학습,검증 인덱스 array
  X_train, X_test = features[train_index], features[test_index]
  y_train, y_test = label[train_index], label[test_index]
  
  dt_clf.fit(X_train, y_train)  # 학습 
  pred = dt_clf.predict(X_test) # 예측
  
  
## =====> 왜곡된 데이터는 반드시 Stratified KFold 사용하기
```



#### - `cross_val_score()`

- 아래의 교차검증의 일련의 과정 한번에 수행해주는 API

- 내부에서  `estimator` -> fit(학습), predict(평가), evaluation(평가) 시켜줌 (Stratified KFold 사용)

 	1. 폴드 세트 설정
 	2. for loop -> train/test dataset 추출
 	3. 반복적인 fit, predict 수행 -> 예측 성능 반환 

`cross_val_score(estimator, X, y=None, cv=None, n_jobs, verbose=0, fit_params=None, pre_dispatch='2*n_gobs')`



- 비슷한 API : `cross_val_validate()`: 여러개의 평가지표 반환 

  (`cross_val_score()`: 단 하나의 평가 지표만 가능 -> 대부분 이거 사용 !)

```py
from sklearn.datasets import load_iris
from sklearn import DecisionTreeClassifier # 분류 (DecisionTree)
from sklearn.model_selection import cross_val_score, cross_validate

# 1) 데이터 불러오기 및 분류
iris = load_iris()
data = iris.data
label = iris.target
dt_clf = DecisionTreeClassifier(random_state=156)

# 2) 성능 지표: 정확도(accuracy), 교차 검증 세트: 3개
score = cross_val_score(dt_clf, data, label, scoring='accuracy', cv=3)
# cv로 저장된 횟수만큼 -> scoring 파라미터로 지정된 평가 지표로 평가 결과값 -> array 배열로 반환 
# cv=3 이면 -> 3개 정확도 결과값  
```



### - GridSearchCV 

> 교차검증 + 최적 하이퍼 파라미터 튜닝 => 한번에 수행

- `Classfier`, `Regressor`과 같은 알고리즘에 사용되는 하이퍼 파라미터 순차적 입력 -> 최적의 파라미터 도출 

- 교차검증 기반: 데이터 세트를 `cross-valiadtion`위한 train/test adtaset로 자동 분할 -> 파라미터 그리드에 기술된 모든 파라미터 순차적으로 적용 -> 최적의 파라미터 찾음 

- 튜닝 하고자하는 여러 종류의 하이퍼파라미터의 다양한 테스트 -> 편리하게 최적의 파라미터 찾아줌 
- 하지만, 동시에 순차적으로 파라미터 테스트 -> 수행시간 상당히 오래 걸림 

Ex) cv=3, parameter=3 => 3*3=9회의 fit/predict

- GridSearchCV class 생성자 parameter 

| Parameter      |                                                              |
| -------------- | ------------------------------------------------------------ |
| **estimator**  | classifier, regressor, pipeline 사용 가능                    |
| **param_grid** | {"key 값" : [리스트 값]} => estimator의 튜닝위해 파라미터명, 값 지정 |
| **scoring**    | 예측 성능 평가 방법 지정 => 사이킷런의 성능 평가 지표 지정 문자열, 함수 지정 가능 |
| **cv**         | 교차 검증 위해 분할되는 train/test dataset 개수 지정         |
| **refit**      | default=True => 최적의  하이퍼 파라미터 찾고 입력된 estimator 객체를 해당 파라미터도 재학습 |



1. `train_test_split()` -> train/test dataset 분리 
2. Train data -> GridSearchCV 최적 하이퍼 파라미터 찾기

```py
from sklearn.datasets import load_iris
from sklearn import DecisionTreeClassifier # 분류 (DecisionTree)
from sklearn.model_selection import GridSearchCV

# 1) 데이터 불러오기 및 분류
iris = load_iris()
data = iris.data
label = iris.target
dt_clf = DecisionTreeClassifier(random_state=156)
```



