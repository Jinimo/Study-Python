# Open CV



```python
### install 
pip install opencv-python

### 모듈 import 
import cv2

### 이미지 불러오기
img = cv2.imread("lenna.png")




```



### cvtcolor

```python
### convert color
dst = cv2.cvtcolor(src, code, dstCn)

# dst : 입력 이미지와 동일한 크기의 출력 이미지
# src : 입력 이미지
# code : 컬러 공간 변환 코드
# dstCn :출력 채널, 기본값을 사용하면 자동으로 계산

# BGR -> GRAY
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```






### 이진화 (Binarization, threshholding)



```python
# BGR -> GRAY
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 이진화
# cv2.threshold(대상, 임계값, 최댓값, 이진화 방법)

# 임계값: 이진화 할 기준 값
# 최대값: 이진화 방법에 따라 변경시 필요한 값

# cv2.THRESH_BINARY : 임계값 이상 = 최댓값, 임계값 이하 = 0
# cv2.THRESH_BINARY_INV : THRESH_BINARY inverse, 임계값 이상 = 0, 임계값 이하 = 최댓값
# cv2.THRESH_TOZERO : 임계값 이상 = 원본값, 임계값 이하 = 0
# cv2.THRESH_TOZERO_INV : 위의 반전, 임계값 이상 = 0, 임계값 이하 = 원본값
# cv2.THRESH_TRUNC : 임계값 이상 = 임계값 임계값 이하 = 원본값
# cv2.THRESH_MASK : 흑색 이미지로
# cv2.THRESH_OTSU : otsu 알고리즘
# cv2.THRESH_TRIANGLE : triangle 알고리즘

ret, dst = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
```



### 윤곽선 (Contours)

```py
### 윤곽선 검출
images, contours, hierachy = cv2.findContours(image, mode, method)

# image: 흑백 or 이진화 된 이미지
# mode: 컨투어 찾는 방법 
#		- cv2.RETR_EXTERNAL: 가장 바깥 라인만
#		- cv2.RETR_LIST: 모든 라인 찾음. but 상하구조(hierachy) 관계 구성X
#		- cv2.RETR_CCOMP: 모든 라인 찾음. 상하구조(hierachy) 2단계 구성
#		- cv2.RETR_TREE: 모든 라인 찾음. 모든 상하구조 구성 
# method
#		- cv2.CHAIN_APPROX_NONE: 모든 컨투어 포인트 반환 
#		- cv2.CHAIN_APPROX_SIMPLE: 라인 그릴 수 있는 포인트만 반환 
#		- cv2.CHAIN_APPROX_TC89_L1: 연결 근사 알고리즘(L1 버전) 적용 -> 컨투어 포인트 줄임
#		- cv2.CHAIN_APPROX_TC89_KCOS: 연결 근사 알고리즘(KCOS 버전) 적용 -> 컨투어 포인트 줄임


### 윤곽선 그리기
# cv2.drawContours(이미지, [윤곽선], 윤곽선 인덱스, (B, G, R), 두께, 선형 타입)
cv2.drawContours(src, [contours[0]], 0, (0, 0, 255), 2)
```

`contours` ->  3차원의 리스트



첫번째 차원 -> 윤곽선 인덱스

두번째 차원 -> 외곽선의 x,y좌표

```py
contours[0][0] =  [[116  11]]
contours[0][1] =  [[115  12]]

contours[0][0][0][0] =  116 # 첫번째 윤곽선 좌표의 x값
contours[0][0][0][1] =  11  # 첫번째 윤곽선 좌표의 y값
contours[0][1][0][0] =  115 # 두번째 윤곽선 좌표의 x값
contours[0][1][0][1] =  12  # 두번째 윤곽선 좌표의 y값
```



#### 윤곽선 최대 최소값

```py
src = cv2.imread("contours.jpg", cv2.IMREAD_COLOR)

gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
binary = cv2.bitwise_not(binary)

contours, hierachy = cv2.findContours(binary, cv2.RETR_TREE , cv2.CHAIN_APPROX_NONE)

contours_min = np.argmin(contours[0], axis = 0) # [[119   0]]
contours_max = np.argmax(contours[0], axis = 0) # [[488 245]]


print("x-Min =", contours[0][contours_min[0][0]][0][0])
print("y-Min =", contours[0][contours_min[0][1]][0][1])
print("x-Max =", contours[0][contours_max[0][0]][0][0])
print("y-Max =", contours[0][contours_max[0][1]][0][1])

x-Min = 30
y-Min = 11
x-Max = 326
y-Max = 189
```



### 이미지 회전

1. 좌푯값을 회전시키는 회전 행렬 - 원점을 중심으로 좌푯값을 회전시켜 매핑
2.  좌표 축을 회전시키는 회전 행렬 - 원점을 중심으로 행렬 자체를 회전시켜 새로운 행렬의 값을 구성

```py
src = cv2.imread("Image/ara.jpg", cv2.IMREAD_COLOR) # 이미지 읽어오기

height, width, channel = src.shape

# 2×3 회전 행렬 생성 함수 (matrix = cv2.getRotationMatrix2D(center, angle, scale))
# 중심점(center): 튜플(Tuple) 형태로 사용하며 회전의 기준점을 설정
# 각도(angle): 중심점을 기준으로 회전할 각도를 설정
# 비율(scale): 이미지의 확대 및 축소 비율을 설정
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)  

# 아핀 변환 함수(cv2.warpAffine) (dst = cv2.warpAffine(src, M, dsize))
# 아핀 맵 행렬(M): 회전 행렬 생성 함수에서 반환된 매핑 변환 행렬을 사용
# 출력 이미지 크기(dsize): 튜플(Tuple) 형태로 사용하며 출력 이미지의 너비와 높이를 의미
dst = cv2.warpAffine(src, matrix, (width, height))

```







```

```





### 이미지 출력

```python
cv2.imshow("binary", dst)   # 이진화 
cv2.imshow("original", img) # 원본
```



### etc

```python
### 대기 명령 (다른 키 입력될때까지 대기)
cv2.waitKey(0)
```





----

[참조]

 -https://jung-max.github.io/2020/04/08/opencv%20%EC%9C%A4%EA%B3%BD%EC%84%A0(Contours)%EA%B0%92%EC%9D%98%20%EC%9D%98%EB%AF%B8(%EB%82%B4%EC%9A%A9)%20%EC%B5%9C%EB%8C%80%EA%B0%92%20%EC%B5%9C%EC%86%8C%EA%B0%92%20%EA%B5%AC%ED%95%98%EA%B8%B0/

- https://076923.github.io/posts/Python-opencv-6/
