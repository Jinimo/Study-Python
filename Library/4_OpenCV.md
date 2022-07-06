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
# dst = cv2.cvtcolor(src, code, dstCn)

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



