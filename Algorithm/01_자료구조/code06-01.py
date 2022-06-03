## ch06 - 7/37

## 함수

## 전역
#stack = [None, None, None, None, None]
SIZE = 5 # 스텍의 크기
stack = [None for _ in range(SIZE)]
top = -1 # 초기값

### 메인 ###
## Push()
#top += 1 # top 한칸 위로 증가
#stack[top] = '커피'

## 내가 만들어본 코드 ㅎㅎㅎ
veb = ['커피', '녹차', '꿀물']
for v in veb:
    top += 1
    stack[top] = v
print(stack)
#=> ['커피', '녹차', '꿀물', None, None]

## Pop()
data = stack[top]
stack[top] = None
top -= 1
print('pop-->', data )
print('bottom-->', stack )
#=> pop--> 꿀물
#   bottom--> ['커피', '녹차', None, None, None]

