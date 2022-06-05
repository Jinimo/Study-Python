## ch11 - 5/42
## 선택 정렬

import random
### 함수 ###
def findMinIndex(ary) : # ary에서 제일 작은 위치를 찾기 (값 찾기 X)
    minIndex = 0
    for i in range(1, len(ary)) :
        # 이건 값으로 비교해야해
        if ( ary[minIndex] > ary[i]) : # 가장 작은 값보다 작다면
            minIndex = i               # 최소값의 위치 업데이트
    return minIndex

### 전역 ###
before = [random.randint(1, 100) for _ in range(8)]
after = []

### 메인 ###
print('정렬 전 -->', before)
for i in range(len(before)) :
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del(before[minPos])  # 빠지면 지워야해
print('정렬 후 -->', after)