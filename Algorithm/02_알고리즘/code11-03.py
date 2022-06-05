import random
### 함수 ###
def selectionSort(ary):
    n = len(ary)
    for i in range(0, n-1): # cycle
        minIndex = 0
        for k in range(i+1, n):
            if (ary[minIndex] > ary[k]):
                minIndex = k                          # 업데이트
        ary[i], ary[minIndex] = ary[minIndex], ary[i] # 값 교환

    return ary

### 변수 ###
dataAry = [random.randint(1, 100) for _ in range(8)]


### 메인 ###
print('정렬 전 -->', dataAry)
dataAry = selectionSort(dataAry) # 파이썬 'sorted(배열)'과 동일
print('정렬 후 -->', dataAry)