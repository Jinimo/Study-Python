# matplotlib



### 0. 한글 문제 해결 
```py
# 그래프 출력 시 이상한 에러들 무시
import warnings
warnings.filterwarnings("ignore")

## 방법 1) os 
# 그래프 그릴 때 한글 깨짐 방지 설정
import os

# Mac OS의 경우와 그 외 OS의 경우로 나누어 설정
if os.name == 'posix':
    plt.rc("font", family="AppleGothic")
else:
    plt.rc("font", family="Malgun Gothic")

## 방법 2) plt,platform
import matplotlib.pyplot as plt
import platform

# 시스템별 폰트 적용
if platform.system() == "Drawin":          # Mac 시스템
    plt.rc("font", family = "AppleGothic")
elif platform.system() == "Windows":       # Windows 시스템
    plt.rc("font", family = "Malgun Gothic")
elif platform.system() == "Linux":         # Linux 시스템 (코랩)
    plt.rc("font", family = "Malgun Gothic")
```



정렬

```
.sort() # 정렬
.sort_valuse(by="기준", ascending=True)  # 오름차순 
.sort_valuse(by="기준", ascending=False) # 내림차순
```



사이즈 지정

```
plt.figure(figsize=(가로값, 세로값) )

```



차트 모양

```
plt.모양(, labels= , autopct='%2f%%')

plt.plot() # 점 
plt.pie()  # 원
plt.bar()  # 세로 막대
plt.hbar() # 가로 막대
plt.scatter()  # 산점도
df.hist()  # 히스토그램 
 

```



```
plt.imshow(wc) # 이미지
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
```


```py
# 데이터 시각화 
import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt
# 선 깨짐 방지
%matplotlib inline 

## 차트 가로/세로 크기 지정
# 앞으로의 모든 차트 크기 지정 / 한번만 써주면 다 적용
plt.rcParams['figure.figsize']=(10, 5) 
# 일반적인 크기 지정
plt.figure(figsize=(5,5)) 
# 차트 제목
plt.title('차트 제목')

# 그래프들 사이 간격 설정 (그래프들 떨어져서 출력)
plt.tight_layout() 

# 레이블(범례)
plt.xlabel('연도')
plt.ylabel('평당분양가격')
plt.legend() # 범례 표시 



## 차트 모양 
#(labels: 레이블 여러개일 경우)
plt.plot()
plt.plot(df_m.대여일자, df_m.이용건수, marker='o' ) 
plt.pie(job_nor.values, labels=job_nor.index)  # 원 
plt.bar()  # 막대(가로)
plt.hbar() # 막대(세로)

#산점도 차트 
plt.scatter(df_m.대여소번호, df_m.대여시간)  


# 히스토그램 
df.hist(figsize=(10,10)) # df의 모든 데이터 그래프들 표시 
plt.hist(df['']) # df 중 하나 정해서 



### 차트 한번에 그리기
plt.subplot(row, column, index)


plt.show()

```

[참조_Matplotlib 범례 표시](https://codetorial.net/matplotlib/set_legend.html)



### 박스플롯 만들기

```py
## 데이터 추출 
# 'y'가 yes나 no일때의 'age'데이터를 추출
y_yes = bank_df[bank_df['y'] == 'yes'] 
y_no  = bank_df[bank_df['y'] == 'no'] 

## 데이터 정리
# yes와 no의 데이터를 정리
y_bal = [y_yes['balance'], y_no['balance']] 
#print(y_age)

# 박스수염 플롯의 작성
plt.boxplot(y_bal)

# x축(횡축)）의 레이블을 추가
plt.xlabel('y')
# y축 （종축）의 레이블을 추가
plt.ylabel('balance')

ax = plt.gca() # 객체들을 쪼개서 만들어줌 , 각각의 위치값 
plt.setp(ax, xticklabels=['yes', 'no'])

plt.show()
```


[참고1_블로그/plt.gca()](https://engineer-mole.tistory.com/215)

