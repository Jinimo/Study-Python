### Hyperparameter 설명 



#### 1) Booster Method

> 부스팅 방법 결정 파라미터. 모형, 성능, 학습 시간, 램 사용량이 영향 줌. 
>
> 사용에 어려움이 있다면, 디폴트 설정 그대로 놓는것이 좋음.  



▶️ 사용법

- Default - `GBDT` 사용하는 것이 좋음 
- `DART`는 과적합을 제어할 수 있는 방법. 한 번쯤 테스트 해볼만 함.
- lightgbm을 사용한다면 -> `GOSS`도 함께 테스트 해볼만 함.



✅ 비교 및 설명 

|         | Xgboost                                        | lightgbm                                   |
| ------- | ---------------------------------------------- | ------------------------------------------ |
| Method  | booster                                        | boosting                                   |
| Default | `gbtree` (Gradient boosting tree)              | `gbt` (Gradient boosting tree)             |
| Option  | `DART` (Dropout Additive Regression Trees)     | `DART` (Dropout Additive Regression Trees) |
|         | `gblinear` (Generalized Linear Model boosting) | `rf`, `goss`                               |



- Gradient boosting tree

  - Decision tree와  Stochastic Grasient Descent( `SGD` ) 이용하여 boosting 수행 

    - `SGD` : 학습데이터의 일부(mini-batch)만 사용하여 loss function 계산 

      

- `DART` (Dropout Additive Regression Trees)

  - 신경망의 dropout을 적용시킨 방법 
  - Rashmi and Gilad-Barchrach(2015)이 과도한 특수화(over-specialization) 문제를 해결고자 `DART` 제안
  - tree 수준에서 작동하며, 개별 특성이 아니라 tree를 완전히 누락시킴 



- `gblinear` (Generalized Linear Model boosting)
  - xgboost에만 있는 옵션. 경험상 거의 사용 X 
  -  `GLM`에 부스팅을 적용한 것
  - [ref] [Model-based Boosting in R](https://cran.r-project.org/web/packages/mboost/vignettes/mboost_tutorial.pdf)



- `rf` , `goss`
  - xgboost기반 ` rf`: [XGBRFClassifier](https://xgboost.readthedocs.io/en/latest/python/python_api.html)로 구현되어 있어  `goss`를 제외한 나머지 옵션은 xgboost와 lightgbm 모두에서 사용 가능. 
  - `rf`  : boosting X -> randomforest 모형(배깅) 만드는 방법 
  - `goss` (Gradient-based One-side Sampling) : `SGD`를 더 빠르고 더 잘 수렴시키기 위해 subsampling을 이용하는 방법





----

[참조] 

[XGBoost와 LightGBM 하이퍼파라미터 튜닝 가이드 by psystat]( https://psystat.tistory.com/131#head2 )

