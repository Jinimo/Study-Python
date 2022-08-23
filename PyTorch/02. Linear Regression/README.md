### 2. Linear Regression

#### 01) Linear Regression

1. 변수 선언
2. 가중치(`W`)와 편향(`b`) 초기화
3. 가설(`H`) 세우기
4. 비용 함수(cost function) 선언
5. 경사 하강법 구현
6. `optimizer.zero_grad()`의 필요 이유
7. `torch.manual_seed()` 사용 이유


#### 02) Multivariable Linear Regression

1. 벡터와 행렬 연산으로 바꾸기 (Dot Product)

#### 03) nn_Module로 Linear Regression 구현 

1. 단순 선형 회귀(`nn.Linear(input_dim, output_dim)`)
- 예시) `input_dim = 1`, `output_dim = 1`

#### 04) nn_Module로 Multivariable Linear Regression 구현 

1. 다중 선형 회귀(`nn.Linear(input_dim, output_dim)`
- 예시) `input_dim = 3`, `output_dim = 1`

1. 타입 캐스팅 (Type Casting)
2. 연결하기 (Concatenate)
3. 스텍킹 (Stacking)
4. 채우기
5. 덮어쓰기 연산 (In-place Operation)

#### 05) Class로 PyTorch 구현하기

1. model - Class로 구현하기
2. 단순 선형 회귀(Linear Regression) - Class로 구현하기
3. 다중 선형 회귀 (Multivariable Linear Regression) - Class로 구현하기

#### 06) Mini Batch and Data Load

1. 미니 배치와 배치 크기 (Mini Batch and Batch Size)
2. 이터레이션 (Iteration)
3. 데이터 로드 (Data Load)
 






-----
[참조]
- [위키독스, PyTorch로 시작하는 딥 러닝 입문](https://wikidocs.net/book/2788)
