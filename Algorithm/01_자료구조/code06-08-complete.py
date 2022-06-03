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
SIZE = int(input("스택 크기를 입력하세요: ")) # 스텍의 크기
stack = [None for _ in range(SIZE)]
top = -1 # 초기값

###################################################
##### 메인 코드 부분 #####
###################################################

if __name__ == '__main__':
    select = input('삽입(I), 추출(E), 확인(V), 종료(X) 중 하나 선택 ==>')

    while (select != 'X' and select != 'x'):
        if select == 'I' or select == 'i':   # 삽입(I)
            data = input("입력할 데이터: ")
            push(data)
            print("스택 상태: ", stack)

        elif select == 'E' or select == 'e':  # 추출(E)
            data = pop()
            print("추출된 데이터: ", data)
            print("스택 상태: ", stack)

        elif select == 'V' or select == 'v':  # 확인(V)
            data = peak()
            print("확인된 데이터: ", data)
            print("스택 상태: ", stack)
        else:
            print("입력이 잘못됨")

        select = input('삽입(I), 추출(E), 확인(V), 종료(X) 중 하나 선택 ==>')

    print('프로그램 종료!')
