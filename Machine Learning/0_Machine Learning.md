# Machine Learning

> - **Supervised Learning** (지도학습): 예측, 분류
>
> - **Un-supervised Learning**  (비지도학습): 연관 규칙, 군집 
>
> - **Reinforcement Learning** (강화학습): 보상 

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
-  `Test datadset` : 머신러닝의 모델 예측 성능을 평가하기 위해 별도로 주어진 데이터 세트



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



 ### - 교차 검증 

> - K 폴드 교차 검증
>
> - Stratified K 폴드



### - RridSearchCV 

> 교차검증 + 최적 하이퍼 파라미터 튜닝 => 한번에 수행
