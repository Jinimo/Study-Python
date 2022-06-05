## ch13 - 11/29
## 이진 탐색 (binary search)

### 함수 ###
def binarySearch(ary, fData):
    pos = -1

    start = 0
    end = len(ary) -1

    while (start<= end):          # 몇번 돌려야 하는지 모르니까 while
        mid = (start + end) // 2  # 중앙 찾기
        if ary[mid] == fData:     # 중앙 값이 찾는 값과 같다면
            return mid            # 중앙 값 리턴
        elif fData > ary[mid]:    # 중앙 값이 찾는 값보다 작다면
            start = mid + 1       # 중앙 값 -> 오른쪽으로 한칸 이동하여 start로
        else:                     # 중앙 값이 찾는 값보다 크다면
            end = mid -1          # 중앙 값 -> 왼쪽으로 한칸 이동하여 end로
    return pos

### 전역 ###
dataAry = [50, 60, 105, 120, 150, 160, 162, 168, 177, 188]
findData = 162 # 할머니 키

### 메인 ###
print('배열 --> ', dataAry)
position = binarySearch(dataAry, findData)
if position == -1:
    print(findData, '가 없음....')
else:
    print(findData, '가', position, ' 위치에 있음.')