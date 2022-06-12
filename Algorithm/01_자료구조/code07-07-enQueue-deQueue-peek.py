## ch07 - 12/50

### 함수 ###
# 큐 꽉 찼는지 확인하는 함수
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear == SIZE -1): # 꽉 찼다면
        return True
    else:
        return False
# 데이터 삽입 함수
def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print('큐 꽉 찼음!')
        return
    rear += 1
    queue[rear] = data

# 큐 비어있는지 확인하는 함수
def isQueueEmpty():
    global SIZE, queue, front, rear
    if (rear == SIZE): # 비어있다면
        return True
    else:
        return False

# 데이터 추출 함수
def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('큐가 비어있습니다.')
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

# 다음 추출할 데이터 확인 함수
def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('큐가 비어있습니다.')
        return None
    return queue[front +1]


### 전역 ###
SIZE = 5
queue =[None for _ in range(SIZE)]
front = rear = -1

### 메인 ###
# 데이터 삽입
print('----- enQueue -----')
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('현아')
enQueue('선미')
enQueue('재남') #=> 큐 꽉 찼음!
print('출구<--', queue, '<--입구') #=> 출구<-- ['화사', '솔라', '문별', '현아', '선미'] <--입구

# 데이터 추출
print('----- deQueue -----')
retData = deQueue()
print('deQueue-->', retData)
retData = deQueue()
print('deQueue-->', retData)
retData = deQueue()
print('deQueue-->', retData)
print('출구<--', queue, '<--입구')

# 다음 데이터 확인
print('----- peek -----')
retData = peek()
print('다음에 추출할 데이터 확인 -->', retData)
print(queue)