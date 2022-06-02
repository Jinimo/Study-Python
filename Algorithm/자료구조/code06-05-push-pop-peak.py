
### 함수 ###
# 스텍이 꽉 차면 더이상 데이터 추가하면 안됨
def isStackFull():
    global SIZE, stack, top
    if (top >= SIZE -1): # 스택이 꽉 찼다면
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if (isStackFull()):
        print("스택이 꽉 찼음!")
        return # 아무것도 하지말고 그냥 return
    top += 1
    stack[top] = data

def isStackEmpty():
    global SIZE, stack, top
    if (top <= -1):
        return True
    else:
        return False

def pop():
    global SIZE, stack, top
    if (isStackEmpty()):
        print("스택 텅 비었다!")
        return None
    data=stack[top]
    stack[top] = None
    top -= 1
    return data

def peak():
    global SIZE, stack, top
    if (isStackEmpty()):
        print("스택 텅~")
        return None
    return stack[top]



### 전역 ###
SIZE = 5 # 스텍의 크기
stack = [None for _ in range(SIZE)]
top = -1 # 초기값

### 메인 ###
push('커피')
push('녹차')
push('꿀물')
push('콜라')
push('환타')
print(stack)
#=> ['커피', '녹차', '꿀물', '콜라', '환타']

push('사이다')
print(stack)
#=> 스택이 꽉 찼음!
#   ['커피', '녹차', '꿀물', '콜라', '환타']

retData = pop()
print('추출-->', retData)
retData = pop()
print('추출-->', retData)
retData = pop()
print('추출-->', retData)
print(stack)
#=> ['커피', '녹차', None, None, None]

print("다음 나올 데이터-->", peak())